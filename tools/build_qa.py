# -*- coding: utf-8 -*-
"""Build /qa/ pages from tools/qa_<topic>.py. Run from repo root: python3 -I tools/build_qa.py"""
import re, sys, json, os, html
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import qa_colic as T
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://horseveterinarian.ai'
SUF = ' | HorseVeterinarian.AI'
TOPIC = dict(key='colic', name='Colic', url='/qa/colic/')
tpl = open(os.path.join(ROOT, 'conditions/colic/index.html'), encoding='utf-8').read()
head = tpl[:tpl.index('<div class="page-hero">')]
foot = tpl[tpl.rindex('<div class="adslot" aria-label="Advertisement">'):]
EXTRA_CSS = '''.page-hero.calm{background:linear-gradient(135deg,var(--forest) 0%,#07261D 100%)}
.short-answer{background:var(--teal-pale);border:1px solid rgba(26,107,90,0.2);border-left:4px solid var(--teal);border-radius:var(--radius);padding:14px 16px;margin-bottom:20px}
.short-answer h2{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--forest);margin:0 0 6px;font-family:inherit}
.short-answer p{font-size:1rem;color:var(--ink);line-height:1.6;margin:0}
.urgent-box{background:#FDECEC;border:1px solid rgba(180,30,30,.3);border-left:4px solid var(--alert);border-radius:var(--radius);padding:14px 16px;margin-bottom:20px;font-size:.92rem;line-height:1.6;color:#5A0E0E}
.src-list{font-size:.82rem;color:var(--ink-soft);line-height:1.7;padding-left:18px}
.qa-list{list-style:none;padding:0}.qa-list li{border-bottom:1px solid rgba(0,0,0,.08);padding:10px 0}.qa-list a{font-weight:700;color:var(--forest);text-decoration:none}.qa-list a:hover{text-decoration:underline}.qa-list span{display:block;font-size:.82rem;color:var(--ink-soft);margin-top:2px}
'''
def esc(s): return html.escape(s, quote=True)
def fit_title(t):
    full = t + SUF
    full = full if len(full) <= 60 else t
    assert len(full) <= 60, full
    return full
def shell(title, meta, path, crumbs, ld_name):
    assert 70 <= len(meta) <= 160, (len(meta), meta)
    h = head
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(title), h, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*"', lambda m: m.group(1) + esc(meta) + '"', h)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*"', lambda m: m.group(1) + esc(meta) + '"', h)
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*"', lambda m: m.group(1) + esc(meta) + '"', h)
    h = re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*"', lambda m: m.group(1) + esc(title) + '"', h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*"', lambda m: m.group(1) + SITE + path + '"', h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*"', lambda m: m.group(1) + SITE + path + '"', h)
    h = h.replace('</style>', EXTRA_CSS + '</style>', 1)
    h = h.replace('class="sn-link active"', 'class="sn-link"')
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(crumbs)]
    ld1 = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    ld2 = {"@context": "https://schema.org", "@type": "MedicalWebPage", "name": title, "url": SITE + path, "description": meta,
           "publisher": {"@type": "Organization", "name": "Bridle & Bit Magazine", "url": "https://www.bridleandbit.com"},
           "inLanguage": "en-US", "audience": {"@type": "MedicalAudience", "audienceType": "Patient"}}
    block = '<script type="application/ld+json">%s</script>\n<script type="application/ld+json">%s</script>\n' % (json.dumps(ld1), json.dumps(ld2))
    h = re.sub(r'(<script type="application/ld\+json">.*?</script>\s*){2}', lambda m: block, h, count=1, flags=re.S)
    return h
HERO_CALL = '''  <div class="emergency-callout">
    <div class="emergency-callout-icon">🚨</div>
    <p>If your horse is showing signs of colic right now, stop reading and call your veterinarian or nearest equine emergency hospital. This page is educational and cannot assess your horse.</p>
  </div>'''
def sidebar(cur):
    links = ''.join('<a href="%s%s/">%s</a>' % (TOPIC['url'], p['slug'], esc(p['title'])) for p in T.PAGES)
    return '''  <aside class="sidebar" aria-label="Related resources">
    <div class="sidebar-vet"><h3>Find an Equine Vet</h3><p>This guide is educational only. For any health concern affecting your horse, contact a licensed equine veterinarian.</p><a href="/find-a-vet/">Find a Vet Near You →</a></div>
    <div class="sidebar-card"><h3>Colic Questions</h3>%s<a href="/qa/colic/">All colic questions →</a></div>
    <div class="sidebar-card"><h3>Emergency Resources</h3><a href="/emergency/colic-emergency/">Colic Emergency Protocol</a><a href="/conditions/colic/">Colic Overview</a><a href="/emergency/">All Emergency Guides →</a></div>
  </aside>''' % links
def page(p, videos):
    path = '%s%s/' % (TOPIC['url'], p['slug'])
    title = fit_title(p['title'])
    h = shell(title, p['meta'], path, [('Home', '/'), ('Q&A', '/qa/'), ('Colic', TOPIC['url']), (p['title'], path)], p['title'])
    cls = 'page-hero' if p['urgent'] else 'page-hero calm'
    urgent = ('<div class="urgent-box"><strong>Urgent:</strong> colic can become life-threatening quickly. If your horse is in pain now, call your veterinarian first, then use this page.</div>' if p['urgent'] else '')
    vid = ''
    if videos.get(p['slug']):
        vid = '<h2>Related videos</h2><p>Externally produced educational videos selected for topic fit. They have <strong>not</strong> been medically reviewed by HorseVeterinarian.AI.</p>' + ''.join(videos[p['slug']])
    srcs = ''.join('<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>' % (T.S[k][1], T.S[k][0]) for k in p['src'])
    rel = ''.join('<a href="%s%s/" class="related-link"><span class="related-link-title">%s</span><span class="related-link-arrow">→</span></a>' % (TOPIC['url'], r, esc(next(x['title'] for x in T.PAGES if x['slug'] == r))) for r in p['rel'])
    main = '''<div class="%s">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/qa/">Q&amp;A</a> › <a href="/qa/colic/">Colic</a></div>
  <div class="page-hero-eyebrow">Colic · Q&amp;A</div>
  <h1>%s</h1>
%s
</div>
<div class="content-wrap" id="main-content">
  <main class="main-col" role="main">
    %s
    <div class="short-answer"><h2>Short answer</h2><p>%s</p></div>
    <div class="article-body">
%s
%s
      <h2>Sources</h2>
      <ul class="src-list">%s</ul>
      <p style="font-size:.8rem">Sources reviewed November 2026. Educational information only; not veterinary advice, and not medically reviewed by a veterinarian.</p>
    </div>
    <div class="section-label" style="margin-top:28px">Related Questions</div>
    <div class="related-grid">%s<a href="/conditions/colic/" class="related-link"><span class="related-link-title">Colic Overview</span><span class="related-link-arrow">→</span></a></div>
  </main>
%s
</div>
''' % (cls, esc(p['q']), HERO_CALL, urgent, p['short'], p['body'], vid, srcs, rel, sidebar(p['slug']))
    return h + main + foot
def hub(title, meta, path, crumbs, h1, intro, listing):
    h = shell(title, meta, path, crumbs, h1)
    return h + '''<div class="page-hero calm">
  <div class="breadcrumb">%s</div>
  <div class="page-hero-eyebrow">Q&amp;A</div>
  <h1>%s</h1>
%s
</div>
<div class="content-wrap" id="main-content">
  <main class="main-col" role="main"><div class="article-body"><p>%s</p></div>%s</main>
%s
</div>
''' % (' › '.join('<a href="%s">%s</a>' % (u, n) for n, u in crumbs[:-1]) + ' › ' + crumbs[-1][0], h1, HERO_CALL, intro, listing, sidebar('')) + foot
def main():
    vpath = os.path.join(ROOT, 'tools/qa_videos_colic.json')
    videos = {}
    if os.path.exists(vpath):
        from build_qa_videos import render
        videos = render(json.load(open(vpath)))
    out = []
    for p in T.PAGES:
        d = os.path.join(ROOT, 'qa/colic', p['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(p, videos)); out.append(p['slug'])
    lst = '<ul class="qa-list">' + ''.join('<li><a href="/qa/colic/%s/">%s</a><span>%s</span></li>' % (p['slug'], esc(p['q']), esc(p['short'][:140].rsplit(' ', 1)[0]) + '…') for p in T.PAGES) + '</ul>'
    open(os.path.join(ROOT, 'qa/colic/index.html'), 'w', encoding='utf-8').write(hub(
        'Colic Questions and Answers for Horse Owners' + '', 'Source-checked answers to common horse colic questions: signs, what to do, when to call the vet, sand colic, prevention, surgery and recovery.',
        '/qa/colic/', [('Home', '/'), ('Q&A', '/qa/'), ('Colic', '/qa/colic/')], 'Colic Questions &amp; Answers',
        'Each answer is checked against veterinary sources, such as the AAEP, Merck Veterinary Manual and university veterinary programs, and links to them. Educational only.', lst))
    open(os.path.join(ROOT, 'qa/index.html'), 'w', encoding='utf-8').write(hub(
        'Horse Health Questions and Answers', 'Source-checked horse health questions and answers from HorseVeterinarian.AI, starting with colic. Educational information, not veterinary advice.',
        '/qa/', [('Home', '/'), ('Q&A', '/qa/')], 'Horse Health Q&amp;A',
        'Source-checked answers to common horse health questions, published topic by topic.',
        '<ul class="qa-list"><li><a href="/qa/colic/">Colic</a><span>%d questions: signs, what to do, prevention, sand colic and surgery.</span></li></ul>' % len(T.PAGES)))
    print(len(out), 'pages')
main()
