# -*- coding: utf-8 -*-
"""Digestive health Q&A (non-colic GI). Same rules as qa_colic.py.
Held for lack of a verified source (see HELD): not published."""
import qa_colic as C
S = dict(C.S)
S.update({
 'eceim': ('ECEIM Consensus Statement — Equine Gastric Ulcer Syndrome in Adult Horses (J Vet Intern Med, 2015)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4858038'),
 'sykes': ('The Horse — How to Prevent Gastric Ulcers in Horses (Dr. Ben Sykes, NAEP 2024)', 'https://thehorse.com/1132826/how-to-prevent-gastric-ulcers-in-horses/'),
 'merckgi': ('Merck Veterinary Manual (Owner Version) — Intestinal Disorders Other than Colic in Horses', 'https://www.merckvetmanual.com/veterinary/horse-owners/digestive-disorders-of-horses/intestinal-disorders-other-than-colic-in-horses'),
 'hc': ('Horse Canada — Equine Diarrhea (Dr. Ashley Whitehead, University of Calgary)', 'https://horse-canada.com/magazine/health/equine-diarrhea/'),
 'petmd': ('PetMD — Diarrhea in Horses', 'https://www.petmd.com/horse/conditions/digestive/c_hr_diarrhea'),
 'hbhr': ('Horse &amp; Rider — Hay Belly', 'https://horseandrider.com/horse-life/hay-belly/'),
 'hbmb': ('Mad Barn — Hay Belly in Horses', 'https://madbarn.com/hay-belly-in-horses/'),
 'hipar': ('Horse Illustrated — Equine University: Parasite Infestation', 'https://www.horseillustrated.com/equine-university-horse-college-horse-health-college-session-200-parasite-infestation-article/amp'),
 'avma': ('AVMA — Internal Parasites of the Horse', 'https://ebusiness.avma.org/files/productdownloads/InternalParasiteHorse_En.pdf'),
 'usuegus': ('Utah State University Extension — Preventing and Managing Equine Gastric Ulcer Syndrome (K. Bell, K. Hoopes DVM; Aug 2024)', 'https://extension.usu.edu/equine/research/preventing-and-managing-equine-gastric-ulcer-syndrome'),
 'sykesvt': ('Vet Times — Equine gastric ulcer syndrome (Ben Sykes; 24 Sept 2021)', 'https://www.vettimes.com/clinical/equine/equine-gastric-ulcer-syndrome-cpdequinegi'),
 'osurefeed': ('Oklahoma State University Extension — Refeeding the Poorly Conditioned Horse (K. Hiney; L. Gilliam, DVM, DACVIM; no date shown)', 'https://extension.okstate.edu/fact-sheets/refeeding-the-poorly-conditioned-horse.html'),
 'lsumal': ('LSU AgCenter — Feeding Malnourished Horses, Pub. 3598 (N. Walker, PhD; April 2017)', 'https://www.lsuagcenter.com/~/media/system/2/a/6/5/2a65d9775f4bd9409b88faed610a6725/pub3598%20feeding%20malnourished%20horsepdf.pdf'),
 'horseomep': ('The Horse — Omeprazole discontinuation and rebound gastric hyperacidity in horses', 'https://thehorse.com/?p=123766'),
})
HELD = {
 'VET-QA-0089':'answer is about eye tearing, not diet — mismatched; eye topic',
 'VET-QA-0090':'generic diet question; no topic',
 'VET-QA-0093':'generic care-instructions question; no topic',
 'VET-QA-0107':'generic monitoring question; no topic',
 'VET-QA-0138':'generic weight/health question; nutrition topic',
 'VET-QA-0097':'answer repeats diet text, does not answer the medication question',
 
 'VET-QA-0144':'overlaps colic/diarrhea/ulcer pages; no unique content',
 'VET-QA-0096':'pot-belly exercise: no verified source',
 'VET-QA-0099':'eye topic','VET-QA-0103':'eye topic','VET-QA-0109':'eye topic','VET-QA-0131':'eye topic','VET-QA-0141':'eye topic (question text only)',
 
 
}
PAGES = [
 dict(slug='signs-of-gastric-ulcers', ids=['VET-QA-0126','VET-QA-0127','VET-QA-0129','VET-QA-0130'], urgent=False,
  q='What are the signs of gastric ulcers in horses?',
  title='Signs of Gastric Ulcers in Horses',
  meta='Gastric ulcer signs such as poor appetite, weight loss and poor performance are not specific, and many horses show none. Diagnosis needs a vet’s scope exam.',
  short='Signs linked to gastric ulcers include poor appetite, poor body condition, weight loss, coat changes, behavior changes, mild colic and poor performance. They are not specific, and many affected horses show none, so a veterinarian has to diagnose ulcers.',
  body='''<h2>Signs linked to ulcers</h2>
<p>The European College of Equine Internal Medicine (ECEIM) consensus statement links gastric ulcers loosely to poor appetite, poor body condition, weight loss, diarrhea, coat changes, behavior changes, colic and poor performance. The authors say the epidemiological support for most of these links is weak, they do not consider the signs specific enough to diagnose ulcers, and many affected horses show no signs at all.</p>
<h2>Why a vet exam matters</h2>
<ul>
<li>Gastroscopy (a scope exam of the stomach) is the only reliable way to diagnose ulcers in a living horse. No reliable blood test exists.</li>
<li>The consensus authors advise against starting treatment without gastroscopy.</li>
<li>Squamous ulcers (upper stomach) and glandular ulcers (lower stomach) have different causes, and treatment differs. See <a href="/qa/gi/gastric-ulcer-treatment-options/">treatment options</a>.</li>
</ul>
<p>The same signs can come from other problems, including dental disease, parasites and mild colic, so the next step is a call to your veterinarian, not a supplement. See <a href="/qa/gi/how-to-prevent-gastric-ulcers/">how to prevent ulcers</a>.</p>''',
  src=['eceim','sykes'], rel=['how-to-prevent-gastric-ulcers','gastric-ulcer-treatment-options','gastric-ulcer-treatment-time-and-recovery']),

 dict(slug='how-to-prevent-gastric-ulcers', ids=['VET-QA-0104','VET-QA-0105','VET-QA-0110','VET-QA-0111','VET-QA-0112','VET-QA-0134','VET-QA-0135'], urgent=False,
  q='How can gastric ulcers be prevented, and how can diet help manage them?',
  title='How to Prevent Gastric Ulcers in Horses',
  meta='Ulcer risk is linked to long gaps between forage meals, high starch, hard exercise and stress. See the feeding and management steps veterinary sources suggest.',
  short='The strongest documented risk factors are exercise intensity and duration, high starch intake and long gaps between forage meals. Keeping forage in the stomach, limiting grain, giving continuous water and reducing stress are the steps veterinary sources recommend.',
  body='''<h2>Documented risk factors</h2>
<p>The ECEIM consensus statement lists exercise intensity and duration as the strongest factors for squamous ulcers, plus high starch intake (above about 2 g per kg of body weight daily), long gaps between forage meals, straw as the only forage, intermittent water access and fasting. Evidence on pasture turnout and high-fiber feeding was conflicting.</p>
<h2>Feeding steps</h2>
<ul>
<li><strong>Keep forage in front of the horse.</strong> The consensus suggests continuous pasture or frequent forage meals (4 to 6 a day), with at least 1.5 kg of hay dry matter per 100 kg of body weight daily.</li>
<li><strong>Minimize grain.</strong> The consensus suggests no more than 1 g of starch per kg of body weight per meal.</li>
<li><strong>Provide water continuously.</strong></li>
<li><strong>Alfalfa hay before exercise.</strong> Dr. Ben Sykes says alfalfa is the best hay for squamous ulcers and most protective offered before exercise, and one study found beet pulp reduced squamous ulcer risk about fivefold. He also advises against exercising first thing in the morning on an empty stomach.</li>
</ul>
<h2>Management steps</h2>
<ul>
<li><strong>Exercise duration:</strong> Sykes suggests averaging under 30 to 40 minutes a day at the trot or faster.</li>
<li><strong>Stress (glandular ulcers):</strong> he recommends two to three rest days a week, a regular routine, fewer handlers, and treating pain sources such as lameness or poor saddle fit.</li>
</ul>
<p>These are one expert's recommendations plus consensus points; ask your veterinarian to tailor them to your horse. Diet alone does not replace diagnosis — see <a href="/qa/gi/signs-of-gastric-ulcers/">signs of gastric ulcers</a>.</p>''',
  src=['eceim','sykes'], rel=['signs-of-gastric-ulcers','gastric-ulcer-treatment-options','how-to-increase-a-horses-water-intake']),

 dict(slug='gastric-ulcer-treatment-options', ids=['VET-QA-0114','VET-QA-0119','VET-QA-0142','VET-QA-0143'], urgent=False,
  q='What treatment options are available for gastric ulcers?',
  title='Gastric Ulcer Treatment Options in Horses',
  meta='Vets treat squamous and glandular gastric ulcers differently. See what the ECEIM consensus says about omeprazole, sucralfate, antacids and management.',
  short='Treatment is prescribed by a veterinarian and depends on whether the ulcers are squamous or glandular. Omeprazole is the preferred drug for squamous ulcers; for glandular ulcers the consensus authors recommend it with sucralfate. Management changes support either.',
  body='''<h2>Squamous ulcers (upper stomach)</h2>
<p>The ECEIM consensus names omeprazole, a proton pump inhibitor that reduces stomach acid, as the preferred drug. Ranitidine is an alternative if omeprazole is unavailable or ineffective. The authors consider no add-on therapies justified for squamous disease.</p>
<h2>Glandular ulcers (lower stomach)</h2>
<p>Glandular lesions respond less well to omeprazole alone: in one trial only about 25% healed after 28 to 35 days. The authors recommend omeprazole with sucralfate, which forms a protective layer, and do not recommend antimicrobials routinely because benefit is unproven.</p>
<h2>What does not replace treatment</h2>
<ul>
<li><strong>Antacids</strong> give only short relief (about two hours or less) and should not be used alone.</li>
<li><strong>Nutraceuticals</strong> have mixed evidence.</li>
</ul>
<h2>Management alongside medication</h2>
<p>Feeding and stress changes help; see <a href="/qa/gi/how-to-prevent-gastric-ulcers/">preventing gastric ulcers</a>. Do not give or stop ulcer medication on your own. Dose, product and length of treatment are your veterinarian's decision. See <a href="/qa/gi/gastric-ulcer-treatment-time-and-recovery/">treatment time and recovery</a>.</p>''',
  src=['eceim','sykes'], rel=['gastric-ulcer-treatment-time-and-recovery','signs-of-gastric-ulcers','how-to-prevent-gastric-ulcers']),

 dict(slug='gastric-ulcer-treatment-time-and-recovery', ids=['VET-QA-0115','VET-QA-0116','VET-QA-0117','VET-QA-0118','VET-QA-0124','VET-QA-0128'], urgent=False,
  q='How long does ulcer treatment take, and how do I know it is working?',
  title='Gastric Ulcer Treatment Time and Recovery',
  meta='Squamous ulcers typically heal within about 3 to 4 weeks of treatment; glandular ulcers heal more slowly. A repeat scope, not signs alone, confirms healing.',
  short='In the consensus statement, squamous ulcers typically heal within about 21 to 28 days of treatment, while glandular ulcers heal more slowly and may need 8 weeks or more. Signs are unreliable, so your veterinarian confirms healing with a repeat scope.',
  body='''<h2>What studies report</h2>
<ul>
<li><strong>Squamous ulcers:</strong> the ECEIM consensus says healing that occurs typically does so by about 21 days, but only about 70 to 80% of lesions heal within 28 days.</li>
<li><strong>Glandular ulcers:</strong> response is poorer; the authors advise a control gastroscopy at about 4 weeks and at least 8 weeks of combination therapy before other treatments are considered.</li>
</ul>
<h2>How do you know it is working?</h2>
<p>The consensus authors do not treat signs as specific, because many horses show none, so appetite or attitude changes cannot confirm healing. The authors recommend repeat gastroscopy before stopping treatment for squamous disease. If lesions persist, a biopsy may be recommended.</p>
<p>Duration is set by your veterinarian from the type and severity of ulcers and the repeat exam. Do not stop medication early because the horse looks better. See <a href="/qa/gi/gastric-ulcer-treatment-options/">treatment options</a>.</p>''',
  src=['eceim'], rel=['gastric-ulcer-treatment-options','signs-of-gastric-ulcers','how-to-prevent-gastric-ulcers']),

 dict(slug='causes-of-diarrhea-in-horses', ids=['VET-QA-0120'], urgent=False,
  q='What causes diarrhea in adult horses?',
  title='Causes of Diarrhea in Adult Horses',
  meta='Adult horse diarrhea can come from infection, antibiotics, parasites, sand, toxins, stress and diet changes. See the causes vet sources list.',
  short='Causes include infections such as Salmonella, antibiotics, parasites, sand, toxins and stress or diet changes. A cause is found in fewer than half of cases, so a veterinarian should assess any diarrhea that lasts or keeps returning.',
  body='''<h2>Causes listed by the Merck Veterinary Manual</h2>
<ul>
<li><strong>Infections</strong> — Salmonella (stressors such as surgery, transport, diet changes and antibiotics can trigger it), toxin-producing Clostridia, and Potomac horse fever, especially on pastures near creeks or rivers.</li>
<li><strong>Medications</strong> — antibiotics can trigger diarrhea.</li>
<li><strong>Parasites</strong> — strongyles, Giardia and Cryptosporidium.</li>
<li><strong>Sand, toxins</strong> and colitis-X.</li>
<li><strong>Diet and stress</strong> — lush pasture, alfalfa hay, grain overload, and stress such as trailering or showing can soften manure.</li>
<li><strong>Chronic causes</strong> (a month or longer) — long-term intestinal inflammation or cancer, diet-related shifts in gut bacteria, and long-term heart or liver disease.</li>
</ul>
<p>Merck notes that a cause is identified in under half of cases, and treatment often begins before the cause is known. Because some causes are contagious, see <a href="/qa/gi/when-to-call-the-vet-for-horse-diarrhea/">when to call the vet</a> and <a href="/qa/gi/how-to-prevent-diarrhea-in-horses/">prevention</a>.</p>''',
  src=['merckgi','petmd'], rel=['when-to-call-the-vet-for-horse-diarrhea','how-to-prevent-diarrhea-in-horses','how-vets-diagnose-horse-diarrhea']),

 dict(slug='when-to-call-the-vet-for-horse-diarrhea', ids=['VET-QA-0132','VET-QA-0139','VET-QA-0140'], urgent=True,
  q='When should I call the vet for diarrhea, and what signs mean it is getting serious?',
  title='When to Call the Vet for Horse Diarrhea',
  meta='Diarrhea in adult horses can cause severe dehydration fast. See the warning signs — fever, pain, lethargy, tacky gums — and when veterinary sources say to call.',
  short='Call your veterinarian for diarrhea that lasts more than a day or two or keeps recurring, and sooner if the horse has a fever, abdominal pain, lethargy, poor appetite, blood or mucus, or signs of dehydration. Adult horse diarrhea can become serious quickly.',
  body='''<h2>Call your vet if</h2>
<ul>
<li>Diarrhea lasts more than a day or two, or occurs repeatedly (Merck).</li>
<li>There is fever, severe watery stool, abdominal pain, blood or mucus in manure, poor appetite or lethargy (Merck).</li>
<li>You see any noticeable change in manure — University of Calgary's Dr. Ashley Whitehead advises calling your vet as soon as manure changes, because colitis can be present without obviously watery manure.</li>
</ul>
<h2>Dehydration signs</h2>
<p>Dr. Whitehead describes tacky or squeaky gums as a red flag, and skin pinched on the eyelid that stays tented for more than two seconds as a usual indicator of dehydration. Merck warns that large intestinal fluid losses can become massive quickly and that severely affected horses may die within about 24 hours if untreated.</p>
<h2>While you wait</h2>
<ul>
<li>Isolate the horse from others, since the cause may be infectious (Merck; PetMD).</li>
<li>Keep clean water available (PetMD).</li>
<li>Be ready to give your vet vital signs and details about the manure.</li>
</ul>
<p>Possible complications include dehydration, endotoxemia and laminitis. If your horse also shows colic signs, see <a href="/qa/colic/what-to-do-if-your-horse-has-colic/">what to do for colic</a>.</p>''',
  src=['merckgi','hc','petmd'], rel=['causes-of-diarrhea-in-horses','how-vets-diagnose-horse-diarrhea','how-to-prevent-diarrhea-in-horses']),

 dict(slug='how-vets-diagnose-horse-diarrhea', ids=['VET-QA-0098'], urgent=False,
  q='What tests might a vet use to find the cause of diarrhea?',
  title='How Vets Diagnose Horse Diarrhea',
  meta='A vet works through history, a physical exam for dehydration, and lab tests such as fecal testing and bloodwork. A cause is found in fewer than half of cases.',
  short='A veterinarian typically takes a history, checks hydration and gut sounds, and may run fecal tests, bloodwork and other diagnostics. A cause is found in under half of cases, so treatment often starts before the cause is known.',
  body='''<h2>Typical steps</h2>
<ul>
<li><strong>History</strong> — changes in diet or routine, recent travel, exposure to new horses, and vaccination and deworming records (PetMD).</li>
<li><strong>Physical exam</strong> — signs of dehydration (dry, tacky gums, skin tent, sunken eyes), plus heart, lungs and gut sounds.</li>
<li><strong>Fecal testing</strong> — for infectious agents and parasites.</li>
<li><strong>Endoscopy</strong> — if gastric ulcers or stress are suspected.</li>
</ul>
<p>Merck says a cause is identified in under half of cases and treatment often begins before it is known: fluids and electrolytes for dehydration, plus other measures chosen by the vet. Some infectious causes, such as Salmonella, are contagious, so your vet may advise isolation. See <a href="/qa/gi/when-to-call-the-vet-for-horse-diarrhea/">when to call the vet</a>.</p>''',
  src=['petmd','merckgi'], rel=['causes-of-diarrhea-in-horses','when-to-call-the-vet-for-horse-diarrhea','how-to-prevent-diarrhea-in-horses']),

 dict(slug='how-to-prevent-diarrhea-in-horses', ids=['VET-QA-0108'], urgent=False,
  q='How can I prevent diarrhea in horses?',
  title='How to Prevent Diarrhea in Horses',
  meta='Reduce diarrhea risk with gradual feed changes, clean feed and water, less stress, and isolating new or sick horses. A guide based on Merck and AAEP advice.',
  short='Change feed gradually, avoid moldy hay, limit grain, protect feed and water from fecal contamination, reduce stress, and isolate and vet-check new horses. Some causes cannot be prevented, so call your vet about diarrhea that lasts.',
  body='''<h2>Feeding</h2>
<ul>
<li>Introduce new hay and feed changes gradually (AAEP; Penn Vet).</li>
<li>Avoid moldy or poor hay, and limit grain-based feed to no more than half the diet, split into smaller meals (AAEP).</li>
<li>Merck lists lush pasture, alfalfa hay and grain overload among triggers of soft manure.</li>
</ul>
<h2>Biosecurity and stress</h2>
<ul>
<li>Isolate new arrivals and have a veterinarian check them; Merck gives 2 to 3 weeks for isolation.</li>
<li>Protect feed and water from contamination by rodents, birds and manure.</li>
<li>Clean and disinfect housing, and remove manure from sick horses promptly.</li>
<li>Minimize stress; stressors such as transport and surgery can trigger Salmonella.</li>
<li>Avoid unprescribed medications (AAEP); antibiotics in particular can trigger diarrhea (Merck).</li>
</ul>
<p>For Potomac horse fever, Merck notes that available vaccines are not very effective and suggests turning off barn lights at night to reduce insects. See <a href="/qa/gi/causes-of-diarrhea-in-horses/">causes of diarrhea</a>.</p>''',
  src=['merckgi','aaep','penn'], rel=['causes-of-diarrhea-in-horses','when-to-call-the-vet-for-horse-diarrhea','how-to-increase-a-horses-water-intake']),

 dict(slug='pot-belly-in-horses-causes-and-tests', ids=['VET-QA-0094','VET-QA-0102','VET-QA-0113'], urgent=False,
  q='What causes a pot belly in horses, and could parasites be responsible?',
  title='Pot Belly in Horses: Causes and Tests',
  meta='A pot belly can come from low-quality forage (hay belly), heavy parasite burden or other problems. See how to tell them apart and what tests your vet may use.',
  short='A pot belly most often reflects low-quality forage (“hay belly”) but can also come from heavy parasite burdens or other problems such as colic. You cannot tell at home; a veterinary exam and fecal egg count help find the cause.',
  body='''<h2>Common causes</h2>
<ul>
<li><strong>Hay belly.</strong> Mad Barn describes the main cause as poor hindgut fermentation of high-fiber, low-quality forage. Horse &amp; Rider describes a belly that hangs low and out to the sides, with a dull coat and poor muscle over the chest and rear, more often in seniors.</li>
<li><strong>Parasites.</strong> Horse Illustrated notes that heavy infestation shows as an unthrifty, pot-bellied appearance with a rough coat; the AVMA says heavily infested horses often have a poor coat and poor condition.</li>
<li><strong>Other problems.</strong> Mad Barn says a large belly can also indicate parasites, colic or other health concerns that need ruling out.</li>
</ul>
<h2>Finding the cause</h2>
<p>The AVMA says strongyle infestation is confirmed by seeing eggs in manure under a microscope. Horse Illustrated recommends a fecal egg count once or twice a year for every horse, and your veterinarian can design a deworming program. A pot belly alone is not a reliable sign of parasites; ask your vet to examine the horse and review the diet. See <a href="/qa/gi/pot-belly-in-horses-diet/">diet for a pot belly</a>.</p>
<p><em>Note: veterinary schools publish little on this topic, so this page relies partly on equine nutrition and horse-care publications.</em></p>''',
  src=['hbmb','hbhr','hipar','avma'], rel=['pot-belly-in-horses-diet','how-to-prevent-diarrhea-in-horses','how-to-prevent-gastric-ulcers']),

 dict(slug='pot-belly-in-horses-diet', ids=['VET-QA-0095','VET-QA-0133','VET-QA-0136','VET-QA-0137'], urgent=False,
  q='What dietary changes can help reduce a pot belly?',
  title='Diet Changes for a Pot Belly in Horses',
  meta='For hay belly, better-quality forage with enough protein and fiber is the usual fix. See what horse-care sources recommend and why to rule out parasites first.',
  short='When the cause is hay belly, sources recommend better-quality, higher-protein and higher-fiber forage rather than more grain. Rule out parasites and other causes with your veterinarian first, and change feed gradually.',
  body='''<h2>What sources recommend for hay belly</h2>
<ul>
<li><strong>Feed better hay.</strong> Horse &amp; Rider recommends higher-protein, higher-fiber hay; protein supports muscle and better body composition.</li>
<li><strong>Mix hay with pasture.</strong> If a horse mostly grazes grass, supplement with quality hay.</li>
<li><strong>Dietary or gut support.</strong> Mad Barn says dietary changes or gut support are needed to resolve hay belly.</li>
<li><strong>Change feed gradually</strong> (AAEP; Penn Vet).</li>
</ul>
<h2>Before changing the diet</h2>
<p>A large belly can come from parasites or other problems, so have your vet examine the horse and check manure. See <a href="/qa/gi/pot-belly-in-horses-causes-and-tests/">causes and tests</a>. An equine nutritionist or veterinarian can balance protein, minerals and calories for your horse.</p>
<p><em>Note: this page relies partly on horse-care and nutrition publications; veterinary schools publish little on pot belly.</em></p>''',
  src=['hbhr','hbmb','aaep','penn'], rel=['pot-belly-in-horses-causes-and-tests','how-to-prevent-gastric-ulcers','how-to-increase-a-horses-water-intake']),

 dict(slug='how-to-increase-a-horses-water-intake', ids=['VET-QA-0106'], urgent=False,
  q='How can I increase my horse’s water intake?',
  title='How to Increase a Horse’s Water Intake',
  meta='Constant access to clean water, salt, mashes and warm water in winter encourage drinking and lower impaction risk. See what veterinary sources recommend.',
  short='Provide fresh water at all times, and encourage drinking with salt, mashes or warm water in winter. Low water intake is linked to impaction colic, so call your vet if your horse stops drinking.',
  body='''<h2>What veterinary sources recommend</h2>
<ul>
<li><strong>Fresh water at all times</strong> (AAEP; Penn Vet).</li>
<li><strong>Salt blocks, mashes or warm water in winter</strong> to encourage drinking (Penn Vet).</li>
<li><strong>Maximize water intake</strong> as part of colic prevention, along with turnout and routine (UC Davis).</li>
</ul>
<p>Low water intake is linked to large-intestine impaction (Merck). A horse that stops drinking, has tacky gums or shows colic signs needs a call to your vet — see <a href="/qa/colic/signs-of-colic/">signs of colic</a> and <a href="/qa/colic/diet-and-manure-impaction-in-horses/">diet and manure impaction</a>.</p>''',
  src=['aaep','penn','ucd','merck'], rel=['how-to-prevent-diarrhea-in-horses','pot-belly-in-horses-diet','when-to-call-the-vet-for-horse-diarrhea']),

 dict(slug='omeprazole-use-rebound-and-treatment-cautions', ids=['VET-QA-0123','VET-QA-0101','VET-QA-0100','VET-QA-0092'], urgent=False,
  q='What are the side effects and cautions of ulcer treatment with omeprazole, including long-term use and combining it with other medications?',
  title='Omeprazole for Horse Ulcers: Rebound and Cautions',
  meta='Omeprazole lowers stomach acid. Some horses relapse after stopping, and NSAIDs promote ulcers. Sources do not cover long-term safety or interactions.',
  short='Omeprazole lowers stomach acid to treat ulcers. A reviewed study found some horses relapse quickly after stopping because of rebound acid, and tapering did not help for courses of eight weeks or less. Vets advise limiting anti-inflammatory painkillers, which promote ulcers. The sources do not cover long-term safety or most drug combinations.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Omeprazole is a proton-pump inhibitor that lowers stomach acid and helps treat both squamous and glandular ulcers (The Horse).</li>
<li><strong>Rebound acid:</strong> some horses relapse quickly after stopping, attributed to "rebound gastric hyperacidity" in which gastrin levels spike and stimulate excess acid. In the study, gastrin returned to normal within two days of stopping (The Horse).</li>
<li><strong>Tapering:</strong> the researchers found tapering did not reduce rebound acidity, and concluded it is not justified for courses of eight weeks or less. Owners should focus on management in the 48 hours after the last dose.</li>
<li><strong>After treatment:</strong> plenty of roughage, reduced exercise, turnout and avoiding prolonged fasting are recommended (The Horse).</li>
<li><strong>Combining with other medications:</strong> the one caution given is that veterinarians advise limiting anti-inflammatory painkillers, using them only when necessary, because they are known to promote ulcers; this matters most if the horse is also fasting (The Horse).</li>
</ul>
<h2>What the sources do not cover</h2>
<p>The study involved 14 retired Thoroughbred racehorses over 57 days, so it may not apply to all horses or longer courses (The Horse). The article does not address long-term safety beyond eight weeks, calcium or other nutrient absorption, drug interactions beyond NSAIDs, or doses. The British Horse Society ulcer page gives no medication side effects either. Do not start, stop or combine medications without your veterinarian. Call your veterinarian for colic signs, weight loss or a horse that stops eating. See <a href="/qa/gi/gastric-ulcer-treatment-options/">ulcer treatment options</a> and <a href="/qa/gi/how-to-prevent-gastric-ulcers/">preventing ulcers</a>.</p>''',
  src=['horseomep'], rel=['gastric-ulcer-treatment-options','gastric-ulcer-treatment-time-and-recovery','how-to-prevent-gastric-ulcers']),

 dict(slug='long-term-effects-of-untreated-gastric-ulcers', ids=['VET-QA-0091','VET-QA-0121','VET-QA-0122'], urgent=False,
  q='What are the long-term effects of gastric ulcers or "acid reflux" if left untreated in horses?',
  title='Untreated Gastric Ulcers in Horses: Long-Term Effects',
  meta='Sources link ulcers to poor appetite, weight loss, colic and lower performance, but report no outcomes for untreated horses. Evidence on performance is limited.',
  short='No source read reports what happens to horses whose ulcers go untreated. Utah State lists signs such as weight loss, colic and behavior change. A 2021 Vet Times review calls the evidence that ulcers lower performance limited but moderate. If your horse shows these signs, ask your veterinarian.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Utah State University Extension (2024) lists subtle signs of ulcers (dull coat, poor appetite, lower performance) and more serious ones (weight loss, trouble keeping body condition, behavior changes, abdominal discomfort and colic). It advises long-term management after healing to prevent recurrence.</li>
<li>Vet Times (Dr. Ben Sykes, 2021) says squamous ulcer disease has been linked to fussy eating and poorer body condition. He suggests reduced intake could slow recovery and weight regain between races in racehorses.</li>
<li>The same review says studies link ulcers to performance problems, but the evidence is limited and the causal link is not proven. Several findings come from conference abstracts or retrospective work, and some views are the author's opinion.</li>
</ul>
<h2>What the sources do not say</h2>
<ul>
<li>Neither source reports outcomes for untreated horses or describes complications such as perforation or chronic disease.</li>
<li>"Acid reflux" is not the standard term in these sources. They use equine gastric ulcer syndrome, with squamous and glandular forms, so this page answers for ulcers.</li>
</ul>
<p>Do not wait to see what happens. Call your veterinarian about weight loss, a horse that stops eating, or repeated colic. See <a href="/qa/gi/signs-of-gastric-ulcers/">signs of gastric ulcers</a> and <a href="/qa/gi/gastric-ulcer-treatment-options/">treatment options</a>.</p>''',
  src=['usuegus','sykesvt'], rel=['signs-of-gastric-ulcers','gastric-ulcer-treatment-options','how-to-prevent-gastric-ulcers']),

 dict(slug='signs-of-malnutrition-in-horses', ids=['VET-QA-0125'], urgent=False,
  q='What are the signs of malnutrition in horses?',
  title='Signs of Malnutrition in Horses',
  meta='Extension sources judge malnutrition by body condition score: prominent spine, ribs, tailhead and hip bones. A vet should find the cause before refeeding.',
  short='Sources judge malnutrition by body condition score on a 1 to 9 scale. At a score of 1 or 2 the spine, ribs, tailhead and pelvis stand out and little or no fat covers them. Weight loss has many causes, so a veterinarian should examine the horse, and refeeding must be done slowly.',
  body='''<h2>How malnutrition is recognized</h2>
<ul>
<li>Oklahoma State University Extension scores body condition from 1 to 9 by visible and palpable fat. At 1, the spine, ribs, tailhead and pelvic bones stand out and no fat can be felt. At 2, a small amount of fat remains over parts of the spine and the ribs, shoulders and neck are only faintly visible.</li>
<li>LSU AgCenter describes a score of 3 as thin: fat covers only about halfway along the spine, the ribs are easy to see, the tailhead stands out, and the pelvis, hip and withers bones look prominent. A score of 5 is moderate: a level back, ribs felt easily but not seen, and a rounded withers.</li>
<li>LSU says a horse may be considered starved if it loses more than 15 percent of its body weight in 60 days or less.</li>
<li>OSU notes some athletic horses are lean yet healthy, so no universal cutoff exists.</li>
</ul>
<h2>Causes</h2>
<p>OSU lists inadequate energy or protein intake as the most common nutritional cause, along with malabsorption, parasites, old age and disease. Illnesses that reduce appetite can also cause it, and some elderly horses struggle to keep condition even with good care.</p>
<h2>Why a veterinarian is needed</h2>
<ul>
<li>OSU says a vet should examine the horse, including the mouth, and run diagnostics before and during refeeding because the cause shapes the plan.</li>
<li>LSU warns of refeeding syndrome when a malnourished horse is fed too quickly. It can appear 3 to 10 days after calories increase, and complications include organ failure and death.</li>
<li>OSU describes refeeding as difficult even with expert oversight and advises watching for laminitis signs such as tender walking or reluctance to move; contact a vet immediately if they appear.</li>
</ul>
<h2>What the sources do not cover</h2>
<p>This page gives no feed amounts or schedules, and the sources do not diagnose a specific horse. OSU shows no publication date. Weight loss can also come from dental disease, parasites or endocrine disease; see <a href="/qa/gi/pot-belly-in-horses-causes-and-tests/">pot belly causes and tests</a> and <a href="/qa/metabolic/signs-of-ppid-cushings/">signs of PPID</a>.</p>''',
  src=['osurefeed','lsumal'], rel=['pot-belly-in-horses-causes-and-tests','signs-of-gastric-ulcers','pot-belly-in-horses-diet']),
]
