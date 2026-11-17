# -*- coding: utf-8 -*-
"""Build /qa/ pages from tools/qa_<topic>.py. Run from repo root: python3 -I tools/build_qa.py"""
import re, sys, json, os, html
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import qa_colic, qa_gi, qa_metabolic, qa_lameness, qa_infectious, qa_skin, qa_respiratory, qa_hoof, qa_dental, qa_eye, qa_wounds, qa_neuro
T = qa_colic
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://horseveterinarian.ai'
SUF = ' | HorseVeterinarian.AI'
TOPICS = [
 dict(key='colic', name='Colic', url='/qa/colic/', mod=qa_colic, h1='Colic Questions &amp; Answers',
      hub_title='Colic Questions and Answers for Horse Owners', hub_meta='Source-checked answers to common horse colic questions: signs, what to do, when to call the vet, sand colic, prevention, surgery and recovery.',
      call='If your horse is showing signs of colic right now, stop reading and call your veterinarian or nearest equine emergency hospital. This page is educational and cannot assess your horse.',
      desc='%d questions: signs, what to do, prevention, sand colic and surgery.', overview=('/conditions/colic/','Colic Overview'), emerg=('/emergency/colic-emergency/','Colic Emergency Protocol')),
 dict(key='gi', name='Digestive Health', url='/qa/gi/', mod=qa_gi, h1='Digestive Health Questions &amp; Answers',
      hub_title='Horse Digestive Health Questions and Answers', hub_meta='Source-checked answers on gastric ulcers, diarrhea, pot belly and water intake in horses. Educational information, not veterinary advice.',
      call='If your horse has severe diarrhea, signs of dehydration, or colic signs right now, call your veterinarian or nearest equine emergency hospital. This page is educational and cannot assess your horse.',
      desc='%d questions: gastric ulcers, diarrhea, pot belly and water intake.', overview=('/conditions/ulcers/','Gastric Ulcers Overview'), emerg=('/emergency/colic-emergency/','Colic Emergency Protocol')),
 dict(key='metabolic', name='Metabolic &amp; Endocrine', url='/qa/metabolic/', mod=qa_metabolic, h1='Metabolic &amp; Endocrine Questions &amp; Answers',
      hub_title='Horse PPID, EMS and Insulin Resistance Questions and Answers', hub_meta='Source-checked answers on PPID (Cushing’s), equine metabolic syndrome, insulin resistance, diet, exercise and laminitis risk. Educational only.',
      call='If your horse is suddenly sore on its front feet, reluctant to move, or has stopped eating, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: PPID, EMS, insulin resistance, diet, exercise and laminitis risk.', overview=('/conditions/laminitis/','Laminitis Overview'), emerg=('/emergency/lameness/','Lameness Emergency Guide')),
 dict(key='lameness', name='Lameness &amp; Hooves', url='/qa/lameness/', mod=qa_lameness, h1='Lameness, Hoof &amp; Limb Questions &amp; Answers',
      hub_title='Horse Lameness, Hoof and Limb Questions and Answers', hub_meta='Source-checked answers on laminitis, tendons, splints, back pain, kissing spines, hoof abscesses, cellulitis and more. Educational only.',
      call='If your horse is suddenly lame, will not bear weight, or has a hot, swollen leg or foot, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: laminitis, tendons, splints, back pain, hooves and leg swelling.', overview=('/conditions/laminitis/','Laminitis Overview'), emerg=('/emergency/lameness/','Lameness Emergency Guide')),
 dict(key='infectious', name='Infectious Disease &amp; Fever', url='/qa/infectious/', mod=qa_infectious, h1='Infectious Disease, Biosecurity &amp; Fever Questions &amp; Answers',
      hub_title='Horse Infectious Disease and Fever Questions and Answers', hub_meta='Source-checked answers on strangles, EHV-1, equine influenza, West Nile virus, fever and biosecurity. Educational only; call your vet.',
      call='If your horse has a fever, a weak or wobbly hind end, trouble breathing or swallowing, or swollen jaw lymph nodes, call your veterinarian right away and isolate the horse. This page is educational and cannot assess your horse.',
      desc='%d questions: strangles, EHV-1, influenza, West Nile, fever and biosecurity.', overview=('/conditions/strangles/','Strangles Overview'), emerg=('/emergency/fever/','Fever Emergency Guide')),
 dict(key='skin', name='Skin &amp; Allergy', url='/qa/skin/', mod=qa_skin, h1='Skin, Allergy &amp; Hives Questions &amp; Answers',
      hub_title='Horse Skin, Allergy and Hives Questions and Answers', hub_meta='Source-checked answers on rain rot, scratches, hives, allergies, anaphylaxis, mange and ringworm. Educational only; call your vet.',
      call='If your horse has swelling of the face or airways, trouble breathing, very pale gums, collapse, or a hot, swollen, painful leg, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: rain rot, scratches, hives, allergies, mange and ringworm.', overview=('/conditions/rain-rot/','Rain Rot Overview'), emerg=('/emergency/wound-care/','Wound Care Emergency Guide')),
 dict(key='respiratory', name='Respiratory', url='/qa/respiratory/', mod=qa_respiratory, h1='Respiratory, Cough &amp; Nasal Discharge Questions &amp; Answers',
      hub_title='Horse Respiratory, Cough and Nasal Discharge Questions', hub_meta='Source-checked answers on pneumonia, cough, nasal discharge, breathing rate, equine asthma and the digital pulse. Educational only; call your vet.',
      call='If your horse is struggling to breathe, has flared nostrils, a cough after trailering, a fever with cough or discharge, or food coming from the nose, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: pneumonia, cough, nasal discharge, breathing rate and digital pulse.', overview=('/conditions/heaves/','Heaves Overview'), emerg=('/emergency/fever/','Fever Emergency Guide')),
 dict(key='hoof', name='Hoof Care and Farrier', url='/qa/hoof/', mod=qa_hoof, h1='Hoof Care, Farrier &amp; Hoof Balance Questions &amp; Answers',
      hub_title='Horse Hoof Care and Farrier Questions and Answers', hub_meta='Source-checked answers on trimming and shoeing intervals, hoof abscesses, hoof imbalance, supplements and rotated coffin bone. Educational only; call your vet.',
      call='If your horse is suddenly lame, will not bear weight, or has a hot hoof with a bounding pulse, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: farrier schedules, hoof abscesses, hoof balance, supplements and coffin bone rotation.', overview=('/conditions/laminitis/','Laminitis Overview'), emerg=('/emergency/lameness/','Lameness Emergency Guide')),
 dict(key='dental', name='Dental and Oral', url='/qa/dental/', mod=qa_dental, h1='Dental, Teeth Floating &amp; Wolf Teeth Questions &amp; Answers',
      hub_title='Horse Dental, Teeth Floating and Wolf Teeth Questions', hub_meta='Source-checked answers on dental exams, teeth floating, wolf teeth, missing teeth and eating problems. Educational only; call your veterinarian.',
      call='If your horse is choking, drooling without chewing, has sudden mouth pain, or facial swelling or one-sided nasal discharge, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: dental exams, teeth floating, wolf teeth, missing teeth and eating problems.', overview=('/conditions/colic/','Colic Overview'), emerg=('/emergency/not-eating/','Not Eating Emergency Guide')),
 dict(key='eye', name='Eye', url='/qa/eye/', mod=qa_eye, h1='Eye, Uveitis &amp; Corneal Ulcer Questions &amp; Answers',
      hub_title='Horse Eye, Uveitis and Corneal Ulcer Questions', hub_meta='Source-checked answers on watery eyes, cloudy eyes, uveitis, corneal ulcers and eye injury prevention. Educational only; call your veterinarian.',
      call='If your horse is squinting, holding an eye shut, or has a cloudy eye, swelling or thick or bloody discharge, call your veterinarian right away. Eye problems are nearly always emergencies. This page is educational and cannot assess your horse.',
      desc='%d questions: watery eyes, cloudy eyes, uveitis, corneal ulcers and preventing eye injuries.', overview=('/emergency/lacerations/','Lacerations Emergency Guide'), emerg=('/emergency/eye-injury/','Eye Injury Emergency Guide')),
 dict(key='wounds', name='Wounds and Trauma', url='/qa/wounds/', mod=qa_wounds, h1='Wounds, Proud Flesh &amp; Shock Questions &amp; Answers',
      hub_title='Horse Wound, Proud Flesh and Shock Questions', hub_meta='Source-checked answers on wound care, infection signs, proud flesh and shock in horses. Educational only; call your veterinarian right away for emergencies.',
      call='If your horse has heavy or spurting bleeding, a wound near a joint or tendon, a puncture, or signs of shock such as a weak pulse and cold limbs, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: wound care, infection signs, proud flesh and shock.', overview=('/emergency/lacerations/','Lacerations Emergency Guide'), emerg=('/emergency/wound-care/','Wound Care Emergency Guide')),
 dict(key='neurologic', name='Neurologic and Behavior', url='/qa/neurologic/', mod=qa_neuro, h1='Neurologic Signs, Anxiety &amp; Behavior Questions &amp; Answers',
      hub_title='Horse Neurologic, Anxiety and Behavior Questions', hub_meta='Source-checked answers on neurologic signs, stumbling, rehab, anxiety, behavior and travel stress in horses. Educational only; call your vet for emergencies.',
      call='If your horse is stumbling, weak, falling, cannot get up, or shows sudden behavior or head changes, call your veterinarian right away. This page is educational and cannot assess your horse.',
      desc='%d questions: neurologic signs, rehab, anxiety, behavior and travel stress.', overview=('/conditions/epm/','EPM'), emerg=('/emergency/lameness/','Lameness Emergency Guide')),
]
TOPIC = TOPICS[0]
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
def hero_call():
    return '  <div class="emergency-callout">\n    <div class="emergency-callout-icon">🚨</div>\n    <p>%s</p>\n  </div>' % TOPIC['call']
def sidebar(cur):
    links = ''.join('<a href="%s%s/">%s</a>' % (TOPIC['url'], p['slug'], esc(p['title'])) for p in T.PAGES)
    return '''  <aside class="sidebar" aria-label="Related resources">
    <div class="sidebar-vet"><h3>Find an Equine Vet</h3><p>This guide is educational only. For any health concern affecting your horse, contact a licensed equine veterinarian.</p><a href="/find-a-vet/">Find a Vet Near You →</a></div>
    <div class="sidebar-card"><h3>%s Questions</h3>%s<a href="%s">All questions →</a></div>
    <div class="sidebar-card"><h3>Emergency Resources</h3><a href="%s">%s</a><a href="%s">%s</a><a href="/emergency/">All Emergency Guides →</a></div>
  </aside>''' % (TOPIC['name'], links, TOPIC['url'], TOPIC['emerg'][0], TOPIC['emerg'][1], TOPIC['overview'][0], TOPIC['overview'][1])
def page(p, videos):
    path = '%s%s/' % (TOPIC['url'], p['slug'])
    title = fit_title(p['title'])
    h = shell(title, p['meta'], path, [('Home', '/'), ('Q&A', '/qa/'), (TOPIC['name'], TOPIC['url']), (p['title'], path)], p['title'])
    cls = 'page-hero' if p['urgent'] else 'page-hero calm'
    urgent = ('<div class="urgent-box"><strong>Urgent:</strong> this can become life-threatening quickly. If your horse is unwell now, call your veterinarian first, then use this page.</div>' if p['urgent'] else '')
    vid = ''
    if videos.get(p['slug']):
        vid = '<h2>Related videos</h2><p>Externally produced educational videos selected for topic fit. They have <strong>not</strong> been medically reviewed by HorseVeterinarian.AI.</p>' + ''.join(videos[p['slug']])
    srcs = ''.join('<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>' % (T.S[k][1], T.S[k][0]) for k in p['src'])
    rel = ''.join('<a href="%s%s/" class="related-link"><span class="related-link-title">%s</span><span class="related-link-arrow">→</span></a>' % (TOPIC['url'], r, esc(next(x['title'] for x in T.PAGES if x['slug'] == r))) for r in p['rel'])
    main = '''<div class="%s">
  <div class="breadcrumb"><a href="/">Home</a> › <a href="/qa/">Q&amp;A</a> › <a href="%s">%s</a></div>
  <div class="page-hero-eyebrow">%s · Q&amp;A</div>
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
    <div class="related-grid">%s<a href="%s" class="related-link"><span class="related-link-title">%s</span><span class="related-link-arrow">→</span></a></div>
  </main>
%s
</div>
''' % (cls, TOPIC['url'], TOPIC['name'], TOPIC['name'], esc(p['q']), hero_call(), urgent, p['short'], p['body'], vid, srcs, rel, TOPIC['overview'][0], TOPIC['overview'][1], sidebar(p['slug']))
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
''' % (' › '.join('<a href="%s">%s</a>' % (u, n) for n, u in crumbs[:-1]) + ' › ' + crumbs[-1][0], h1, hero_call(), intro, listing, sidebar('')) + foot
def build_topic(tp):
    global T, TOPIC
    T = tp['mod']; TOPIC = tp
    vpath = os.path.join(ROOT, 'tools/qa_videos_%s.json' % tp['key'])
    videos = {}
    if os.path.exists(vpath):
        from build_qa_videos import render
        videos = render(json.load(open(vpath)))
    for p in T.PAGES:
        d = os.path.join(ROOT, 'qa', tp['key'], p['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(p, videos))
    lst = '<ul class="qa-list">' + ''.join('<li><a href="%s%s/">%s</a><span>%s</span></li>' % (tp['url'], p['slug'], esc(p['q']), esc(p['short'][:140].rsplit(' ', 1)[0]) + '…') for p in T.PAGES) + '</ul>'
    open(os.path.join(ROOT, 'qa', tp['key'], 'index.html'), 'w', encoding='utf-8').write(hub(
        tp['hub_title'], tp['hub_meta'], tp['url'], [('Home', '/'), ('Q&A', '/qa/'), (tp['name'], tp['url'])], tp['h1'],
        'Each answer is checked against veterinary sources, such as the AAEP, Merck Veterinary Manual and university veterinary programs, and links to them. Educational only.', lst))
    print(tp['key'], len(T.PAGES), 'pages')
def main():
    for tp in TOPICS: build_topic(tp)
    global TOPIC, T
    TOPIC = TOPICS[0]; T = TOPICS[0]['mod']
    listing = '<ul class="qa-list">' + ''.join('<li><a href="%s">%s</a><span>%s</span></li>' % (tp['url'], tp['name'], tp['desc'] % len(tp['mod'].PAGES)) for tp in TOPICS) + '</ul>'
    open(os.path.join(ROOT, 'qa/index.html'), 'w', encoding='utf-8').write(hub(
        'Horse Health Questions and Answers', 'Source-checked horse health questions and answers from HorseVeterinarian.AI, starting with colic and digestive health. Educational only.',
        '/qa/', [('Home', '/'), ('Q&A', '/qa/')], 'Horse Health Q&amp;A',
        'Source-checked answers to common horse health questions, published topic by topic.', listing))
main()
