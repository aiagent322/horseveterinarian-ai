# -*- coding: utf-8 -*-
"""Senior horse care Q&A (source-first; no package records). Same rules as qa_colic.py. No doses, no feed amounts."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnsenior': ('University of Minnesota Extension — Caring for Your Senior Horse (J. Wilson, DVM, and L. Bullock; reviewed 2024; original date not stated)', 'https://extension.umn.edu/horse-health/caring-your-senior-horse'),
 'okolder': ('Oklahoma State University Extension — Caring for the Older Horse (K. Hiney, PhD, and D. McFarlane, DVM, PhD; no date shown)', 'https://extension.okstate.edu/fact-sheets/caring-for-the-older-horse.html'),
 'ugaolder': ('University of Georgia Extension Bulletin 1368 — Caring for the Older Horse: Common Problems and Solutions (K. Duberstein; updated Aug 26, 2024)', 'https://fieldreport.caes.uga.edu/?p=27809'),
})
HELD = {}
PAGES = [
 dict(slug='caring-for-a-senior-horse', ids=[], urgent=False,
  q='How do I care for a senior horse, and how often should it see the vet?',
  title='Caring for a Senior Horse: Checkups and Care',
  meta='Extension sources advise annual or twice-yearly vet exams with a dental check and body condition score, plus continued vaccines and deworming.',
  short='Extension sources say there is no fixed age at which a horse becomes old. They advise annual or twice-yearly veterinary exams with a dental check, weight estimate and body condition score, and continued vaccines and deworming after retirement. Call your veterinarian about changes in weight, movement or behavior.',
  body='''<h2>When is a horse a senior?</h2>
<p>The University of Georgia (K. Duberstein) says there is no fixed age at which a horse becomes old and that horses age at different rates; many live into their late 20s or early 30s. Oklahoma State notes that chronological age can differ from physiological age.</p>
<h2>Checkups</h2>
<ul>
<li>The University of Minnesota advises a physical exam annually or twice a year, including a dental check, body weight estimate and body condition score, a soundness check and vaccine planning.</li>
<li>Routine blood and urine screening can reveal subtler age-related organ problems (University of Minnesota).</li>
<li>Vets use the findings to plan care and nutrition for the next 6 to 12 months (University of Minnesota).</li>
<li>Vaccines and deworming continue after retirement, and a horse that is still active may need more frequent vaccines (University of Minnesota). Lifelong parasite control supports digestive health (University of Georgia).</li>
</ul>
<h2>Keep records between visits</h2>
<p>Oklahoma State advises scoring body condition and weighing the horse about every two months, with photos, and more often as the horse ages. Daily observation makes gradual changes easy to miss.</p>
<h2>What the sources do not cover</h2>
<p>These sources give no full vaccination schedule, no doses and no housing guidance. See <a href="/qa/senior-care/feeding-a-senior-horse/">feeding</a>, <a href="/qa/senior-care/why-is-my-older-horse-losing-weight/">weight loss</a> and <a href="/qa/senior-care/common-health-problems-in-older-horses/">common health problems</a>.</p>''',
  src=['umnsenior','ugaolder','okolder'], rel=['feeding-a-senior-horse','why-is-my-older-horse-losing-weight','common-health-problems-in-older-horses']),

 dict(slug='feeding-a-senior-horse', ids=[], urgent=False,
  q='What should I feed a senior horse?',
  title='Feeding a Senior Horse: Teeth, Feed and Forage',
  meta='Worn teeth make chewing harder. Extension sources suggest easier-to-chew feeds, an undisturbed feeding spot and vet-guided weight plans.',
  short='Extension sources say older horses need a high-quality diet that is easier to chew, because worn or loose teeth limit how well they eat. Senior feeds are often pelleted and more energy-dense. Needs vary by horse, and overweight or insulin-resistant horses need a monitored plan from a veterinarian.',
  body='''<h2>Why feeding changes</h2>
<p>Oklahoma State says loose or missing teeth and changes in tooth roots can make chewing harder and often lead to weight loss. The University of Georgia says nutritional needs vary widely between individual older horses; some need little change and others need a special diet.</p>
<h2>What the sources suggest</h2>
<ul>
<li>Oklahoma State presents higher-quality, easier-to-chew feed as the top priority, and says no confirmed evidence of reduced digestibility with age has been reported.</li>
<li>The University of Minnesota says senior-formulated feeds are often pelleted, easier to chew and more energy-dense, and that palatability varies by brand. Pellets can be the main feed if teeth are too worn for hay.</li>
<li>The University of Georgia says softer feeds and easily digested fiber sources can help horses that struggle to keep weight, and feeds should be free of mold and dust. Check liver and kidney function before adding supplements.</li>
<li>Oklahoma State advises avoiding high-starch feeds because of insulin sensitivity concerns, and says older horses may need an undisturbed feeding spot and extra eating time.</li>
<li>Oklahoma State says soaking feed can reduce choke risk, and that poor chewing raises the risk of choke and impaction colic.</li>
</ul>
<h2>Overweight horses</h2>
<p>Oklahoma State says obese or insulin-resistant horses need a monitored weight-loss plan. The University of Georgia says excess weight stresses bones and joints. Ask your veterinarian to design the plan; see <a href="/qa/metabolic/safe-weight-management-for-horses/">safe weight management</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page gives no feed amounts or product names. Your veterinarian can set amounts for your horse. See <a href="/qa/dental/missing-teeth-causes-and-diet-changes/">missing teeth and diet changes</a> and <a href="/qa/senior-care/why-is-my-older-horse-losing-weight/">weight loss</a>.</p>''',
  src=['okolder','umnsenior','ugaolder'], rel=['why-is-my-older-horse-losing-weight','caring-for-a-senior-horse']),

 dict(slug='why-is-my-older-horse-losing-weight', ids=[], urgent=True,
  q='Why is my older horse losing weight?',
  title='Why Is My Older Horse Losing Weight?',
  meta='Worn or loose teeth are a common cause of weight loss in older horses, but illness is possible. Have your vet examine any horse losing weight.',
  short='Extension sources link weight loss in older horses to worn or loose teeth, reduced nutrient absorption, and other illness such as Cushing syndrome. Weight loss is a warning sign, so have your veterinarian examine the horse. Call promptly if there is choking, colic signs or a sudden change.',
  body='''<h2>Causes named by the sources</h2>
<ul>
<li><strong>Teeth:</strong> Oklahoma State and the University of Minnesota say worn, loose or lost teeth make chewing harder and can lead to weight loss. The University of Georgia says horses left without extra care can become emaciated.</li>
<li><strong>Absorption:</strong> the University of Minnesota says the gut absorbs nutrients less efficiently with age, which can cause weight loss or loose manure.</li>
<li><strong>Eating conditions:</strong> Oklahoma State says arthritis or competition from other horses can make older horses eat less.</li>
<li><strong>Hormone disease:</strong> the University of Georgia lists weight changes and muscle loss among signs of PPID (Cushing disease); see <a href="/qa/metabolic/signs-of-ppid-cushings/">signs of PPID</a>.</li>
</ul>
<h2>What to do</h2>
<p>The University of Minnesota lists weight loss or loose manure as a warning sign and advises regular exams with a body condition score. Oklahoma State advises tracking body condition, weight, topline muscle, fat distribution and coat so changes are caught early. Call your veterinarian to examine a horse that is losing weight rather than only changing the feed.</p>
<h2>Call promptly if</h2>
<p>The horse is choking or shows colic signs. Oklahoma State says poor chewing raises the risk of choke and impaction colic, and the University of Minnesota says older horses are more prone to certain colic that needs prompt care. See the <a href="/emergency/choke/">choke emergency guide</a> and the <a href="/emergency/colic-emergency/">colic emergency guide</a>.</p>
<h2>What the sources do not cover</h2>
<p>The sources give no weight-loss threshold that means an emergency, and this page gives none. See <a href="/qa/senior-care/feeding-a-senior-horse/">feeding a senior horse</a> and <a href="/qa/dental/missing-teeth-causes-and-diet-changes/">missing teeth</a>.</p>''',
  src=['okolder','umnsenior','ugaolder'], rel=['feeding-a-senior-horse','caring-for-a-senior-horse','common-health-problems-in-older-horses']),

 dict(slug='common-health-problems-in-older-horses', ids=[], urgent=False,
  q='What health problems are common in older horses?',
  title='Common Health Problems in Older Horses',
  meta='Extension sources list dental wear, arthritis, Cushing syndrome, colic from fatty tumors, heaves and lumps as common in older horses.',
  short='Extension sources list dental wear, arthritis, Cushing syndrome (PPID), colic from fatty tumors, heaves, skin lumps and declining immunity as more common in older horses. Muscle loss and gradual coordination changes also occur. Report changes to your veterinarian rather than assuming they are only age.',
  body='''<h2>By body system (University of Minnesota)</h2>
<ul>
<li><strong>Digestive:</strong> worn or lost teeth, less efficient absorption, and a higher likelihood of colic from small intestine blockage by fatty tumors (lipomas), which needs prompt care.</li>
<li><strong>Muscles and joints:</strong> arthritis, with stiffness and reduced range of motion, and muscle loss often along the topline.</li>
<li><strong>Endocrine and immune:</strong> Cushing syndrome can lead to laminitis and raises infection risk because elevated cortisol weakens the immune response.</li>
<li><strong>Respiratory:</strong> heaves (recurrent airway obstruction) tends to worsen with age.</li>
<li><strong>Nervous:</strong> coordination may decline slightly; neck arthritis or spinal changes can cause progressive loss of coordination.</li>
<li><strong>Skin:</strong> lumps, often melanomas in gray horses, and red or raised spots on lightly haired skin around the eyes and muzzle. The University of Minnesota says early detection often allows successful local treatment.</li>
</ul>
<h2>Other points from the sources</h2>
<ul>
<li>Oklahoma State says about half of horses over 15 have osteoarthritis and that owners often miss lameness and hoof problems that veterinarians later diagnose.</li>
<li>The University of Georgia says arthritis is the most common soundness problem in older horses and can often be managed well. It says PPID mainly affects horses in their 20s.</li>
</ul>
<h2>When to call</h2>
<p>The University of Georgia says to contact a veterinarian as soon as possible if PPID signs appear. The University of Minnesota lists arthritis signs, colic, weight loss or loose manure, lumps, laminitis and progressive loss of coordination as warning signs. See <a href="/qa/lameness/arthritis-causes-treatment-and-outlook/">arthritis</a>, <a href="/qa/metabolic/signs-of-ppid-cushings/">signs of PPID</a> and <a href="/qa/senior-care/why-is-my-older-horse-losing-weight/">weight loss</a>.</p>
<h2>What the sources do not cover</h2>
<p>They give little on treatment of heart, respiratory or reproductive conditions, and no diagnoses can be made from this page.</p>''',
  src=['umnsenior','okolder','ugaolder'], rel=['why-is-my-older-horse-losing-weight','caring-for-a-senior-horse','feeding-a-senior-horse']),

 dict(slug='exercise-and-saddle-fit-for-older-horses', ids=[], urgent=False,
  q='How much should I exercise an older horse, and does saddle fit change?',
  title='Exercise and Saddle Fit for Older Horses',
  meta='Daily light exercise or turnout, longer warm-ups and cool-downs, regular hoof trims and saddle fit checks help older horses. Ask your vet about workload.',
  short='Extension sources recommend daily light exercise or turnout, longer warm-ups and cool-downs, regular hoof trimming and regular saddle fit checks, since older horses often lose back muscle. Both overwork and inactivity can harm arthritic joints, so ask your veterinarian to guide the workload.',
  body='''<h2>Exercise</h2>
<ul>
<li>Daily light exercise or turnout helps maintain usefulness, and older horses need longer warm-ups and cool-downs (University of Minnesota; Oklahoma State).</li>
<li>For arthritis, adjust workload; both overwork and inactivity can harm joints (University of Minnesota).</li>
<li>Consistent exercise helps maintain mobility (Oklahoma State). The University of Georgia adds that turnout and exercise matter for older horses that gain too much weight.</li>
</ul>
<h2>Hooves and comfort</h2>
<p>The University of Minnesota says regular hoof trimming supports balanced weight bearing and reduces joint stress. The University of Georgia says hoof neglect and poor hoof growth can worsen arthritis. Oklahoma State advises comfortable bedding where the horse can lie down and get up easily, and says reluctance to lift a hoof or stand for the farrier may indicate foot pain.</p>
<h2>Saddle fit</h2>
<p>If the horse is still ridden, check saddle fit regularly. The University of Minnesota says senior horses often have less back muscle, which makes them more prone to saddle sores.</p>
<h2>When to ask your veterinarian</h2>
<p>Stiffness, swelling, lameness or limited range of motion are arthritis signs listed by the University of Minnesota. The sources give no exercise schedules or limits, so ask your veterinarian what suits your horse. See <a href="/qa/lameness/arthritis-causes-treatment-and-outlook/">arthritis</a> and <a href="/qa/senior-care/caring-for-a-senior-horse/">caring for a senior horse</a>.</p>''',
  src=['umnsenior','okolder','ugaolder'], rel=['caring-for-a-senior-horse','common-health-problems-in-older-horses']),
]
