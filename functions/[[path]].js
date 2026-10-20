/* Private preview adapter. Cloudflare Access must protect the Pages previews.
 * No SIM credentials, question rewriting, retries, or new request IDs here.
 * Keep ask/ask.js disabled until the protected connection is verified.
 */
const PREVIEW_HOST = /^(?:ask-interface-local|[a-f0-9]{8})\.horseveterinarian-ai\.pages\.dev$/;
const ROUTES = new Map([
  ['/api/vet-assistant', { method: 'POST', upstream: '/api/vet-assistant' }],
  ['/beta/unlock', { method: 'POST', upstream: '/beta/unlock' }],
  ['/api/horsevet-health', { method: 'GET', upstream: '/health' }]
]);
const UNAVAILABLE = 'The assistant is unavailable right now. If your horse may be having an emergency, contact your veterinarian or an equine emergency clinic now.';

function failure(status, extraHeaders = {}) {
  return new Response(JSON.stringify({ ok: false, error: UNAVAILABLE }), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff',
      ...extraHeaders
    }
  });
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const route = ROUTES.get(url.pathname);
  if (!route) return context.next();

  // This release cannot expose the adapter on the production site or base Pages host.
  if (url.protocol !== 'https:' || url.port || !PREVIEW_HOST.test(url.hostname)) {
    return failure(403);
  }
  if (request.method !== route.method) return failure(405, { Allow: route.method });
  if (url.search) return failure(400);

  if (request.method === 'POST') {
    if (request.headers.get('Origin') !== url.origin) return failure(403);
    const site = request.headers.get('Sec-Fetch-Site');
    if (site && site !== 'same-origin') return failure(403);
    const type = (request.headers.get('Content-Type') || '').split(';')[0].trim().toLowerCase();
    if (type !== 'application/json') return failure(415);
  }

  if (!env.HORSEVET_GATEWAY || typeof env.HORSEVET_GATEWAY.fetch !== 'function') {
    return failure(503);
  }

  // Preserve the browser-facing origin for the gateway's same-origin checks.
  // Service binding dispatch selects the Worker; its workers.dev URL is unnecessary.
  url.pathname = route.upstream;
  const upstreamRequest = new Request(url.toString(), request);
  try {
    const upstream = await env.HORSEVET_GATEWAY.fetch(upstreamRequest);
    // Relay body, status, session cookies and Retry-After without interpreting answers.
    const response = new Response(upstream.body, upstream);
    response.headers.set('Cache-Control', 'no-store');
    response.headers.set('X-Content-Type-Options', 'nosniff');
    return response;
  } catch {
    // An unknown outcome must never be retried automatically.
    return failure(502);
  }
}
