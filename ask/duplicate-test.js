(function () {
  'use strict';
  var preview = /^(?:ask-interface-local|[a-f0-9]{8})\.horseveterinarian-ai\.pages\.dev$/;
  var form = document.getElementById('unlock-form');
  var code = document.getElementById('unlock-code');
  var unlock = document.getElementById('unlock-submit');
  var session = document.getElementById('session-status');
  var button = document.getElementById('run-test');
  var result = document.getElementById('test-result');
  var ready = false, busy = false, attempted = false;
  var storageKey = 'horsevet-duplicate-test-v1';
  var record = {};
  function show() { result.textContent = JSON.stringify(record, null, 2); }
  function save() { sessionStorage.setItem(storageKey, JSON.stringify(record)); show(); }
  if (location.protocol !== 'https:' || !preview.test(location.hostname)) {
    form.hidden = true;
    result.textContent = 'This test is disabled outside the protected preview.';
    return;
  }
  try {
    var saved = sessionStorage.getItem(storageKey);
    if (saved) { record = JSON.parse(saved); attempted = true; show(); }
  } catch (e) {
    form.hidden = true;
    result.textContent = 'Session storage is unavailable. No requests will be sent.';
    return;
  }
  async function request(path, method, payload) {
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, 70000);
    try {
      var response = await fetch(path, {
        method: method, credentials: 'same-origin', redirect: 'manual', cache: 'no-store',
        headers: payload ? {'Content-Type':'application/json'} : {'Accept':'application/json'},
        body: payload ? JSON.stringify(payload) : undefined, signal: controller.signal
      });
      var data;
      try { data = await response.json(); } catch (e) { data = null; }
      return {status:response.status, data:data};
    } finally { clearTimeout(timer); }
  }
  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    if (busy || attempted || !code.value.trim()) return;
    busy = true; unlock.disabled = true;
    session.textContent = 'Verifying beta session…';
    try {
      var reply = await request('/beta/unlock', 'POST', {code:code.value.trim()});
      code.value = '';
      ready = reply.status === 200 && reply.data && reply.data.ok === true;
      if (ready) {
        form.hidden = true;
        session.textContent = 'Beta session confirmed. Test has not run.';
      } else {
        session.textContent = 'Beta session not confirmed. HTTP ' + reply.status + '. No test requests sent.';
      }
    } catch (e) {
      code.value = '';
      session.textContent = 'Beta session check failed. No test requests sent.';
    } finally { busy = false; unlock.disabled = false; button.disabled = !ready || attempted; }
  });
  button.addEventListener('click', async function () {
    if (busy || attempted || !ready) return;
    busy = true; button.disabled = true;
    try {
      var health = await request('/api/horsevet-health', 'GET');
      if (health.status !== 200 || !health.data || health.data.revision !== '2026-10-20-dedupe-v2' || health.data.enabled !== true) {
        result.textContent = 'Test not started. Expected dedupe-v2 with enabled:true. No question requests sent.';
        return;
      }
      record = {startedUTC:new Date().toISOString(), requestId:crypto.randomUUID(), question:'My horse cannot get up.', requestsSent:0};
      attempted = true;
      save(); // Reserve locally before any question request; a reload cannot repeat the test.
      var payload = {question:record.question, requestId:record.requestId};
      record.requestsSent = 1; save();
      var first = await request('/api/vet-assistant', 'POST', payload);
      record.firstHTTP = first.status;
      if (first.status !== 200 || !first.data || first.data.ok !== true || typeof first.data.response !== 'string' || !first.data.response.trim()) {
        record.result = 'STOPPED: first request was not a confirmed success; no replay sent.';
        record.finishedUTC = new Date().toISOString(); save(); return;
      }
      record.firstGatewayRequestId = first.data.requestId;
      record.conversationId = first.data.conversationId;
      record.firstAnswer = first.data.response;
      record.requestsSent = 2; save();
      var second = await request('/api/vet-assistant', 'POST', payload);
      record.secondHTTP = second.status;
      record.secondGatewayRequestId = second.data && second.data.requestId;
      record.result = second.status === 409 ? 'HTTP CHECK PASS. SIM execution count still requires log verification.' : 'HTTP CHECK FAILED. Do not repeat this test.';
      record.finishedUTC = new Date().toISOString(); save();
    } catch (e) {
      record.result = 'STOPPED: outcome unknown. No automatic retry. Restore Emergency Stop and inspect logs.';
      record.finishedUTC = new Date().toISOString();
      try { save(); } catch (ignored) { show(); }
    } finally {
      busy = false; button.disabled = attempted || !ready;
      if (attempted) session.textContent = 'Test stopped. Restore Emergency Stop to ON now. Do not run it again.';
    }
  });
})();
