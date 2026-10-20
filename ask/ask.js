/*
 * HorseVeterinarian.AI — /ask/ question interface (private beta, not yet connected).
 *
 * Execution modes
 *   disabled (default) : form stays disabled, nothing is sent anywhere.
 *   live               : only if CONFIG.liveEnabled is changed to true in a reviewed commit.
 *                        Sends same-origin requests to CONFIG.endpoints. Requires the
 *                        private same-origin routing to exist first (see release notes).
 *   demo               : only on a local development host (localhost / 127.0.0.1 / [::1])
 *                        AND only when the local dev server injects
 *                        <meta name="hvai-ask-demo" content="mock">. Requests go to the
 *                        local mock server. Every answer is labelled as a mock fixture.
 *
 * Request contract: POST {question, requestId}. No conversationId is ever generated or sent.
 * Answers are rendered with textContent only (never parsed as HTML). No automatic retry.
 */
(function () {
  'use strict';

  var CONFIG = Object.freeze({
    liveEnabled: false,      // keep false until the protected same-origin route is verified
    unlockEnabled: false,    // beta-code unlock; only valid once /beta/unlock is same-origin
    endpoints: Object.freeze({ ask: '/api/vet-assistant', unlock: '/beta/unlock' }),
    timeoutMs: 90000,
    maxChars: 4000
  });

  var LOCAL_HOSTS = ['localhost', '127.0.0.1', '[::1]'];

  function $(id) { return document.getElementById(id); }

  var els = {
    demoBanner: $('ask-demo-banner'),
    unavailable: $('ask-unavailable'),
    form: $('ask-form'),
    fieldset: $('ask-fieldset'),
    q: $('ask-q'),
    count: $('ask-count'),
    submit: $('ask-submit'),
    submitLabel: $('ask-submit-label'),
    status: $('ask-status'),
    error: $('ask-error'),
    unlockForm: $('unlock-form'),
    unlockCode: $('unlock-code'),
    unlockSubmit: $('unlock-submit'),
    answer: $('ask-answer'),
    answerText: $('ask-answer-text'),
    mockTag: $('ask-mocktag')
  };
  if (!els.form) return;

  function resolveMode() {
    var meta = document.querySelector('meta[name="hvai-ask-demo"]');
    var isLocal = LOCAL_HOSTS.indexOf(location.hostname) !== -1;
    if (meta && meta.getAttribute('content') === 'mock' && isLocal) return 'demo';
    if (CONFIG.liveEnabled === true) return 'live';
    return 'disabled';
  }

  var MODE = resolveMode();
  var UNLOCK_ALLOWED = MODE === 'demo' || (MODE === 'live' && CONFIG.unlockEnabled === true);
  var TIMEOUT_MS = CONFIG.timeoutMs;
  if (MODE === 'demo') {
    // Local test harness may shorten the timeout; never lengthen it.
    var t = parseInt(document.querySelector('meta[name="hvai-ask-demo"]').getAttribute('data-timeout-ms'), 10);
    if (t > 0 && t <= CONFIG.timeoutMs) TIMEOUT_MS = t;
  }

  var MSG = {
    empty: 'Type a question before sending.',
    tooLong: 'Your question is over 4,000 characters. Shorten it and try again.',
    unsupported: 'This browser can’t send questions securely. Please update your browser.',
    sending: 'Sending your question. This can take a little while…',
    received: 'Answer received.',
    400: 'The question couldn’t be accepted. Check that it isn’t empty and is under 4,000 characters, then try again.',
    401: 'Beta access is required on this device. Enter your access code below, then send your question again.',
    '401-nounlock': 'Beta access is required. Access can’t be unlocked from this page yet.',
    403: 'This page isn’t permitted to send questions right now. Reload the page and try again. If it continues, your access may have expired.',
    409: 'This request ID has already been used, so the service did not accept it as a new request. Its earlier outcome is not known here, and sending your question again will create a separate request.',
    429: 'The question limit has been reached for now. Please try again later.',
    502: 'The answer service couldn’t complete this request. Please try again later.',
    503: 'The question service is temporarily unavailable. Please try again later.',
    timeout: 'No answer arrived in time. The outcome is unknown: the service may have received your question, and sending it again may create another request.',
    invalid: 'The answer service sent a reply this page couldn’t read. The outcome is unknown, and sending your question again may create another request.',
    network: 'The connection failed before an answer arrived. The outcome is unknown: your question may have reached the service, and sending it again may create another request.',
    generic: 'Something went wrong. Please try again later.',
    unexpected: 'Something went wrong on this page. The outcome is unknown, and sending your question again may create another request.',
    kept: 'Your question has been kept in the box above.',
    emergency: 'If your horse may be having an emergency, contact your veterinarian or an equine emergency clinic now.',
    unlocking: 'Checking your access code…',
    unlocked: 'Access unlocked on this device. Send your question again.',
    unlockEmpty: 'Enter your access code.',
    unlockBad: 'That access code wasn’t accepted.',
    unlockLimit: 'Too many attempts. Please wait and try again later.',
    unlockInvalid: 'The access check returned a reply this page couldn’t confirm. Access was not unlocked.',
    unlockTimeout: 'The access check did not finish in time. Access was not unlocked.',
    unlockNetwork: 'The connection failed during the access check. Access was not unlocked.',
    unlockUnexpected: 'Something went wrong on this page during the access check. Access was not confirmed.'
  };

  // ---------- UI helpers ----------
  function setStatus(text) { els.status.textContent = text || ''; }
  // Error text is built from fixed strings with textContent only. `questionFailed` adds the
  // kept-question note and the emergency-contact line.
  function setError(text, questionFailed) {
    els.error.textContent = '';
    if (text) {
      var m = document.createElement('p');
      m.textContent = text;
      els.error.appendChild(m);
      if (questionFailed) {
        var k = document.createElement('p');
        k.textContent = MSG.kept;
        els.error.appendChild(k);
        var e = document.createElement('p');
        e.className = 'err-emg';
        e.textContent = MSG.emergency;
        els.error.appendChild(e);
      }
    }
    els.error.classList.toggle('show', !!text);
  }
  function updateCount() {
    var n = els.q.value.length;
    els.count.textContent = n.toLocaleString('en-US') + ' / 4,000';
    els.count.classList.toggle('over', n > CONFIG.maxChars);
  }
  function setAskBusy(on) {
    els.submit.disabled = on;
    els.submit.classList.toggle('busy', on);
    els.submit.setAttribute('aria-disabled', on ? 'true' : 'false');
    els.submitLabel.textContent = on ? 'Waiting for answer…' : 'Ask';
    els.q.readOnly = on;              // keep the question visible and readable while waiting
    els.answer.setAttribute('aria-busy', on ? 'true' : 'false');
    els.form.setAttribute('aria-busy', on ? 'true' : 'false');
  }
  function setUnlockBusy(on) {
    els.unlockSubmit.disabled = on;
    els.unlockSubmit.classList.toggle('busy', on);
    els.unlockCode.readOnly = on;
  }
  function showUnlock(on) { els.unlockForm.classList.toggle('show', !!on); }
  function hideAnswer() {
    els.answer.classList.remove('show');
    els.answerText.textContent = '';
  }
  function showAnswer(text) {
    els.answerText.textContent = text; // text only; line breaks preserved by CSS pre-wrap
    els.mockTag.hidden = MODE !== 'demo';
    els.answer.classList.add('show');
    try { els.answer.focus({ preventScroll: false }); } catch (e) { els.answer.focus(); }
  }

  // ---------- transport (same-origin only) ----------
  function postJson(path, payload, timeoutMs) {
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, timeoutMs);
    return fetch(path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload),
      credentials: 'same-origin',
      cache: 'no-store',
      redirect: 'manual',
      signal: controller.signal
    }).then(function (res) {
      // An Access login redirect comes back as an opaque redirect; never follow it from fetch.
      if (res.type === 'opaqueredirect' || (res.status >= 300 && res.status < 400)) {
        clearTimeout(timer);
        return { kind: 'status', status: 403 };
      }
      return res.text().then(function (body) {
        clearTimeout(timer);
        var data = null;
        try { data = body ? JSON.parse(body) : null; } catch (e) { data = undefined; }
        return { kind: 'http', status: res.status, ok: res.ok, data: data };
      });
    }).catch(function (err) {
      clearTimeout(timer);
      // AbortError = our timeout (also during body read); anything else = transport failure.
      return { kind: err && err.name === 'AbortError' ? 'timeout' : 'network' };
    });
  }

  function messageForStatus(status) {
    if (status === 401) return UNLOCK_ALLOWED ? MSG[401] : MSG['401-nounlock'];
    if (MSG[status]) return MSG[status];
    return MSG.generic;
  }

  // ---------- ask flow ----------
  var inFlight = false;

  function onAskSubmit(ev) {
    ev.preventDefault();
    if (inFlight || unlockInFlight) return;   // explicit guard, checked before any await
    if (MODE === 'disabled') return;

    var question = els.q.value.trim();
    if (!question) { setError(MSG.empty); els.q.focus(); return; }
    if (question.length > CONFIG.maxChars) { setError(MSG.tooLong); els.q.focus(); return; }
    if (!window.crypto || typeof window.crypto.randomUUID !== 'function') { setError(MSG.unsupported, true); return; }

    inFlight = true;                          // set synchronously, before the request starts
    var pending;
    try {
      var requestId = window.crypto.randomUUID(); // one id per intentional submission
      setError('');
      hideAnswer();
      setAskBusy(true);
      setStatus(MSG.sending);
      pending = postJson(CONFIG.endpoints.ask, { question: question, requestId: requestId }, TIMEOUT_MS);
    } catch (err) {
      pending = Promise.reject(err);
    }

    pending
      .then(handleAskResult)
      .catch(function () {
        try { hideAnswer(); setStatus(''); setError(MSG.unexpected, true); } catch (e) { /* never surface */ }
      })
      .finally(function () {
        inFlight = false;                     // always released first
        try { setAskBusy(false); } catch (e) { /* best-effort */ }
      })
      .catch(function () { /* no unhandled rejection */ });
  }

  function handleAskResult(r) {
    if (r.kind === 'timeout') { setStatus(''); setError(MSG.timeout, true); return; }
    if (r.kind === 'network') { setStatus(''); setError(MSG.network, true); return; }
    if (r.kind === 'status') { setStatus(''); setError(messageForStatus(r.status), true); return; }
    if (r.ok && r.status === 200) {
      if (r.data && typeof r.data === 'object' && r.data.ok === true &&
          typeof r.data.response === 'string' && r.data.response.length > 0) {
        setStatus(MSG.received);
        showAnswer(r.data.response);          // text unchanged; nothing appended
        return;
      }
      setStatus(''); setError(MSG.invalid, true); return;
    }
    setStatus('');
    setError(messageForStatus(r.status), true);
    if (r.status === 401 && UNLOCK_ALLOWED) { showUnlock(true); }
  }

  // ---------- unlock flow (only when routing supports it) ----------
  var unlockInFlight = false;

  function onUnlockSubmit(ev) {
    ev.preventDefault();
    if (unlockInFlight || inFlight || !UNLOCK_ALLOWED) return;
    var code = els.unlockCode.value.trim();
    if (!code) { setError(MSG.unlockEmpty); els.unlockCode.focus(); return; }

    unlockInFlight = true;
    var pending;
    try {
      setError('');
      setUnlockBusy(true);
      els.submit.disabled = true;
      setStatus(MSG.unlocking);
      pending = postJson(CONFIG.endpoints.unlock, { code: code }, 20000);
    } catch (err) {
      pending = Promise.reject(err);
    }

    pending
      .then(handleUnlockResult)
      .catch(function () {
        try { setStatus(''); setError(MSG.unlockUnexpected); showUnlock(true); } catch (e) { /* never surface */ }
      })
      .finally(function () {
        unlockInFlight = false;               // always released first
        try { setUnlockBusy(false); } catch (e) { /* best-effort */ }
        try { els.submit.disabled = false; } catch (e) { /* best-effort */ }
      })
      .catch(function () { /* no unhandled rejection */ });
  }

  function handleUnlockResult(r) {
    // Success only on HTTP 200 with a JSON object whose ok === true.
    if (r.kind === 'http' && r.status === 200 && r.data && typeof r.data === 'object' && r.data.ok === true) {
      els.unlockCode.value = '';
      showUnlock(false);
      setStatus(MSG.unlocked);
      els.q.focus();
      return;
    }
    setStatus('');
    if (r.kind === 'timeout') return setError(MSG.unlockTimeout);
    if (r.kind === 'network') return setError(MSG.unlockNetwork);
    if (r.kind === 'http' && r.status === 200) return setError(MSG.unlockInvalid);
    if (r.status === 401 || r.status === 400) return setError(MSG.unlockBad);
    if (r.status === 429) return setError(MSG.unlockLimit);
    setError(messageForStatus(r.status));
  }

  // ---------- init ----------
  if (MODE === 'disabled') {
    els.form.addEventListener('submit', function (e) { e.preventDefault(); });
    els.unlockForm.parentNode.removeChild(els.unlockForm);
    els.unavailable.classList.add('show');
    els.fieldset.disabled = true;
    els.submitLabel.textContent = 'Not available yet';
    return;
  }

  if (MODE === 'demo') {
    els.demoBanner.hidden = false;
    document.title = '[DEMO] ' + document.title;
  }

  els.fieldset.disabled = false;
  updateCount();
  els.q.addEventListener('input', updateCount);
  els.q.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      if (typeof els.form.requestSubmit === 'function') els.form.requestSubmit();
      else els.submit.click();
    }
  });
  els.form.addEventListener('submit', onAskSubmit);
  if (UNLOCK_ALLOWED) els.unlockForm.addEventListener('submit', onUnlockSubmit);
  else els.unlockForm.parentNode.removeChild(els.unlockForm);
})();
