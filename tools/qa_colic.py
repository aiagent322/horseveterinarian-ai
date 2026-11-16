# -*- coding: utf-8 -*-
"""Colic Q&A content. Every claim is paraphrased from the listed sources.
ids = HorseVet-QA-Clean record IDs merged into the page (permanent IDs, never renumbered).
No drug dosages, no diagnosis language, no unsourced numeric thresholds."""

S = {
 'aaep': ('AAEP — Colic: Minimizing Its Incidence and Impact on Your Horse', 'https://old.aaep.org/horsehealth/colic-minimizing-its-incidence-and-impact-your-horse'),
 'merck': ('Merck Veterinary Manual (Owner Version) — Colic in Horses', 'https://www.merckvetmanual.com/horse-owners/digestive-disorders-of-horses/colic-in-horses'),
 'ucd': ('UC Davis Center for Equine Health — Colic: A Pain in the Gut', 'https://cehhorsereport.vetmed.ucdavis.edu/node/1421'),
 'penn': ('Penn Vet New Bolton Center — Colic: What You Can Do', 'https://www.vet.upenn.edu/new-bolton-center/clinical-services/emergency-critical-care/colic-what-you-can-do/'),
 'uaz': ('University of Arizona Cooperative Extension — Sand Colic (AZ1759)', 'https://extension.arizona.edu/sites/extension.arizona.edu/files/pubs/az1759-2018.pdf'),
 'whw': ('World Horse Welfare — Colic in Horses', 'https://www.worldhorsewelfare.org/advice/colic-in-horses'),
 'ill': ('University of Illinois Veterinary Medicine — Colic Survival Rate: Review of 254 Cases', 'https://vetmed.illinois.edu/2020/03/19/colic-survival-rate/'),
 'ita': ('Animals (2023) — Short-Term Survival and Postoperative Complications in Horses Undergoing Colic Surgery: A Multicentre Study', 'https://iris.unito.it/retrieve/handle/2318/1898153/1116249/animals-13-01107%20(1).pdf'),
 'umn': ('University of Minnesota Large Animal Surgery — Surgery Complications', 'https://open.lib.umn.edu/largeanimalsurgery/chapter/surgerycomplications/'),
 'acvs': ('American College of Veterinary Surgeons — Colic', 'https://acvs.org/?p=4047'),
 'equus': ('EQUUS — What to Do First When Your Horse Colics', 'https://equisearch.com/articles/response-colic-54184/'),
 'equus2': ('EQUUS — 5 Ways to Prevent Sand Colic', 'https://equusmagazine.com/horse-care/prevention-sand-colic-25412'),
 'hr': ('Horse &amp; Rider — Avoid Sand Colic', 'https://horseandrider.com/horse-health-care/avoid-sand-colic'),
 'ext': ('eXtension Horses — How Do I Prevent Sand Impaction From Causing Colics?', 'https://horses.extension.org/how-do-i-prevent-sand-impaction-from-causing-colics/'),
}

PAGES = [
 dict(slug='types-of-colic', ids=['VET-QA-0001','VET-QA-0013'], urgent=False,
  q='What are the different types of colic in horses?',
  title='Types of Colic in Horses Explained',
  meta='Colic is abdominal pain, not one disease. Learn the main types — gas, spasm, impaction, displacement, strangulation, sand, enteritis — and how they differ.',
  short='Yes. Colic means abdominal pain, and many different problems can cause it. The main types range from mild, short-lived gas or spasm to life-threatening twists and strangulation. Signs overlap so much that a veterinarian has to work out which type is involved.',
  body='''<h2>The main types</h2>
<ul>
<li><strong>Gas and spasmodic colic</strong> — gas stretches the intestines, or the intestines contract abnormally and painfully. These usually respond to medical care.</li>
<li><strong>Impaction</strong> — feed, sand or other material blocks part of the intestine and makes passing manure difficult. Large-intestine impactions are linked to coarse feed, low water intake and dental problems.</li>
<li><strong>Displacement</strong> — a section of intestine moves out of its normal position. Surgical outcomes are generally good.</li>
<li><strong>Twist (torsion or volvulus) and strangulation</strong> — the intestine twists or its blood supply is cut off. UC Davis describes these as life-threatening and always requiring surgery.</li>
<li><strong>Sand colic</strong> — sand settles in the large intestine, mostly in horses fed on sandy ground. See <a href="/qa/colic/signs-of-sand-colic/">signs of sand colic</a>.</li>
<li><strong>Enteritis and colitis</strong> — inflammation of the intestine, often with diarrhea. These need intensive medical treatment.</li>
<li><strong>Other causes</strong> — enteroliths (mineral stones), fatty tumors (lipomas), adhesions, hernias and parasites.</li>
</ul>
<h2>Why you cannot tell the type at home</h2>
<p>Pawing, flank-watching, rolling and sweating show that a horse is in pain, but they do not show which part of the digestive tract is affected. Persistent or worsening pain points to a more serious problem; intermittent pain points to a milder one — but only an examination sorts out the cause. See <a href="/qa/colic/signs-of-colic/">signs of colic</a> and <a href="/qa/colic/when-to-call-the-vet-for-colic/">when to call the vet</a>.</p>''',
  src=['merck','ucd','aaep','whw'], rel=['signs-of-colic','causes-of-colic','when-to-call-the-vet-for-colic']),

 dict(slug='causes-of-colic', ids=['VET-QA-0014'], urgent=False,
  q='What causes colic in horses?',
  title='What Causes Colic in Horses?',
  meta='Colic has many possible causes, from feed and water problems to sand, parasites and twisted gut. See known risk factors and why some causes stay unknown.',
  short='Colic has many possible causes, and sometimes the cause is never found. Management factors — feed, water, exercise, stress, parasites and teeth — are linked to risk, but a veterinarian has to examine the horse to say what is behind a particular episode.',
  body='''<h2>Conditions that cause colic</h2>
<p>Merck Veterinary Manual lists gas or fluid distention, impaction, spasm, displacement and twisting, reduced blood supply to the intestine, sand accumulation, inflammation (enteritis), adhesions, hernias, enteroliths, lipomas and parasites. It also notes that some causes are never identified.</p>
<h2>Risk factors in the research</h2>
<ul>
<li><strong>Recent stall confinement</strong> — associated with impaction colic.</li>
<li><strong>Diet and feeding</strong> — more than 50% alfalfa in the diet or access to sand is linked to enteroliths and sand colic; feeding errors and rapid feed changes add risk.</li>
<li><strong>Travel and stress</strong> — can reduce gut motility.</li>
<li><strong>Cribbing</strong> — significantly associated with colic, and linked to a specific type of entrapment.</li>
<li><strong>Medical history</strong> — previous abdominal surgery (adhesions); recent antibiotics or anti-inflammatories (colitis); pregnancy or recent foaling (large-colon twist).</li>
<li><strong>Parasites and dental problems</strong> — large strongyles, small strongyles and tapeworms are linked to some forms of colic; poor chewing is linked to large-intestine impaction.</li>
</ul>
<p>Age, breed, size and weather also matter but cannot be changed. For the factors you can change, see <a href="/qa/colic/how-to-prevent-colic/">how to prevent colic</a>.</p>''',
  src=['merck','ucd','aaep'], rel=['types-of-colic','how-to-prevent-colic','signs-of-colic']),

 dict(slug='signs-of-colic', ids=['VET-QA-0017'], urgent=True,
  q='What are the signs of colic in horses?',
  title='Signs of Colic in Horses',
  meta='Colic signs range from subtle to violent: pawing, flank-watching, lip curling, rolling, sweating, fewer droppings. See what to watch for and when to call.',
  short='Signs range from subtle (a horse that is quiet, off feed or curling its upper lip) to violent (repeated rolling, thrashing). A horse rarely shows all of them. Any of these signs is a reason to call your veterinarian.',
  body='''<h2>Common signs</h2>
<ul>
<li>Looking at or turning the head toward the flank; biting or kicking at the belly</li>
<li>Pawing with a front foot</li>
<li>Curling the upper lip — subtle and easy to miss</li>
<li>Stretching out as if to urinate, or straining to pass manure</li>
<li>Repeatedly lying down and getting up; rolling; unusual postures such as sitting like a dog or lying on the back</li>
<li>Reduced interest in food or water; fewer or no droppings</li>
<li>Sweating, rapid breathing or flared nostrils</li>
<li>Abdominal distention, depression, groaning</li>
</ul>
<p>AAEP also lists a pulse above 50 beats per minute among the signs of a problem, and reduced or absent gut sounds.</p>
<h2>Reading the pattern</h2>
<p>Obvious or persistent signs suggest a more serious problem; signs that come and go suggest a milder one. In horses with serious conditions, pain usually persists and can worsen over time. Horses hide pain, so a small change from normal behavior counts — learn what is normal for your horse.</p>
<p>Next steps: <a href="/qa/colic/what-to-do-if-your-horse-has-colic/">what to do if your horse has colic</a> and <a href="/qa/colic/when-to-call-the-vet-for-colic/">when to call the vet</a>.</p>''',
  src=['aaep','merck','equus'], rel=['what-to-do-if-your-horse-has-colic','when-to-call-the-vet-for-colic','how-to-monitor-a-horse-for-colic']),

 dict(slug='what-to-do-if-your-horse-has-colic', ids=['VET-QA-0024','VET-QA-0025'], urgent=True,
  q='What should I do if my horse shows signs of colic?',
  title='What to Do if Your Horse Has Colic',
  meta='If your horse shows colic signs, call your vet first. An educational guide to what to do and not do while you wait, based on AAEP and vet school advice.',
  short='Call your veterinarian right away and tell them it may be colic. Then follow the steps below while you wait. Do not give medication or home remedies unless the vet tells you to.',
  body='''<div class="action-box"><h3>✅ While You Wait — General Educational Guidance</h3><ol>
<li><strong>Call your veterinarian first</strong> and say the horse may have colic. The vet decides whether to come out and gives instructions for your situation.</li>
<li><strong>Take away hay and grain</strong> so nothing adds to a possible blockage. Leave water available, per AAEP, unless your vet says otherwise.</li>
<li><strong>Move the horse to a safe, small enclosure</strong> where you can watch closely, with light if it is getting dark.</li>
<li><strong>Note what you see</strong> — when signs started, when the horse last ate, drank and passed manure, plus pulse, gum color and gut sounds if you can check them safely. See <a href="/qa/colic/how-to-monitor-a-horse-for-colic/">how to monitor a horse for colic</a>.</li>
<li><strong>Ask your vet whether to walk the horse.</strong> AAEP advises resting a horse that stands or lies quietly and walking one that is rolling or at risk of hurting itself, without exhausting it. Penn Vet notes that walking can help gut motility but is not a solution on its own.</li>
<li><strong>Keep yourself safe.</strong> If the horse is thrashing violently, do not put yourself in danger; leave it alone until help arrives.</li>
<li><strong>Be ready to transport</strong> to a hospital if your vet advises it.</li>
</ol></div>
<h2>What not to do</h2>
<ul>
<li><strong>Do not give medication</strong> unless the vet directs it. Sedatives and pain relievers can mask signs the vet needs, and some make colic worse.</li>
<li><strong>Do not pass a tube, give oral liquids or substances, give an enema, or give injections.</strong></li>
<li><strong>Do not use home remedies.</strong> AAEP calls castor oil, kerosene and turpentine useless and dangerous.</li>
</ul>
<p>Our full <a href="/emergency/colic-emergency/">Colic Emergency Protocol</a> covers the same ground. For what the vet may do next, see <a href="/qa/colic/signs-a-horse-may-need-colic-surgery/">signs a horse may need colic surgery</a>.</p>''',
  src=['aaep','penn','equus','merck'], rel=['when-to-call-the-vet-for-colic','signs-of-colic','signs-a-horse-may-need-colic-surgery']),

 dict(slug='when-to-call-the-vet-for-colic', ids=['VET-QA-0028','VET-QA-0029'], urgent=True,
  q='When should I call the vet for colic?',
  title='When to Call the Vet for Colic',
  meta='Call your vet at the first signs of colic and again if pain persists, worsens or returns. See warning signs and what information your veterinarian will ask for.',
  short='Call at the first signs of colic — do not wait to see whether it passes. Call again, or go to an equine hospital as your vet directs, if pain persists, gets worse or returns.',
  body='''<h2>Call at the first signs</h2>
<p>AAEP says to call the veterinarian immediately and to say the horse has colic. Penn Vet adds that if you find a horse ill in the morning, the problem may have started overnight.</p>
<h2>Signs that need urgent attention</h2>
<ul>
<li>Pain that persists or gets worse, or returns after improving</li>
<li>Pain that continues after a veterinarian has given pain relief</li>
<li>Repeated or violent rolling</li>
<li>A heart rate that stays high — Penn Vet lists a rate that stays above 60 as a warning sign for referral</li>
<li>Marked abdominal distention, profuse sweating or weakness</li>
<li>No manure, or a sudden drop in manure</li>
<li>Large-volume reflux when the vet passes a stomach tube</li>
</ul>
<p>If your horse's pain is not controlled at home, or it is dehydrated or may need surgery, your vet may send it to an equine hospital with around-the-clock monitoring.</p>
<h2>What to tell the vet</h2>
<ul>
<li>The signs and how severe they are, and when they began</li>
<li>Pulse, breathing rate, temperature, gum color and moisture, and capillary refill time (about 1 to 2 seconds is normal, per AAEP)</li>
<li>Gut sounds, and the color, consistency and frequency of manure</li>
<li>Recent changes in feed, management or exercise</li>
<li>Medical history, including deworming and past colic</li>
<li>For mares, breeding or pregnancy status</li>
</ul>
<p>If surgery or euthanasia might be needed and the horse is insured, AAEP advises contacting the insurer right away.</p>
<p>See <a href="/qa/colic/what-to-do-if-your-horse-has-colic/">what to do while you wait</a>. This website cannot assess your horse; it is educational only.</p>''',
  src=['aaep','penn','merck'], rel=['what-to-do-if-your-horse-has-colic','signs-of-colic','signs-a-horse-may-need-colic-surgery']),

 dict(slug='how-to-monitor-a-horse-for-colic', ids=['VET-QA-0003'], urgent=False,
  q='How can I monitor a horse for signs of colic?',
  title='How to Monitor a Horse for Colic',
  meta='Learn the daily checks that catch colic early — appetite, water, manure, behavior — and the vital signs and gut sounds worth knowing before you call your vet.',
  short='Know what is normal for your horse, check appetite, water intake, manure and behavior every day, and call your veterinarian when something changes. Vital signs you can safely check give your vet useful information.',
  body='''<h2>Daily checks</h2>
<ul>
<li>Appetite and water intake at each feeding</li>
<li>Manure — how much, how often, and its color and consistency</li>
<li>Attitude and comfort — restlessness, pawing, flank-watching, stretching, repeated lying down</li>
</ul>
<p>AAEP and the UC Davis Center for Equine Health both stress knowing your horse's normal habits so that changes stand out. Recent changes in feed, exercise or routine, travel and a history of colic are worth noting.</p>
<h2>Checks that help your vet (only if safe)</h2>
<ul>
<li><strong>Gut sounds</strong> — listen on both flanks. Penn Vet describes normal as a few gurgles a minute with an occasional louder rumble; silence is not good, and neither is excessive noise.</li>
<li><strong>Heart rate</strong> — Penn Vet gives about 40 beats per minute as a typical resting rate; count the pulse at the facial artery for 15 seconds and multiply by four.</li>
<li><strong>Gums</strong> — color, moisture and capillary refill time (about 1 to 2 seconds is normal, per AAEP).</li>
<li><strong>Temperature and breathing rate</strong> — AAEP lists these among what to tell the vet.</li>
</ul>
<p>If a horse is thrashing, skip the vital signs and keep yourself safe. If anything looks wrong, <a href="/qa/colic/when-to-call-the-vet-for-colic/">call your vet</a> — do not wait for numbers.</p>''',
  src=['aaep','penn','ucd'], rel=['signs-of-colic','when-to-call-the-vet-for-colic','what-to-monitor-after-a-colic-episode']),

 dict(slug='what-to-monitor-after-a-colic-episode', ids=['VET-QA-0026','VET-QA-0027'], urgent=False,
  q='What should I monitor after treatment for colic?',
  title='What to Monitor After a Colic Episode',
  meta='After colic treatment, watch appetite, manure, comfort and gut function and follow your vet’s re-feeding plan. Learn which changes mean calling your vet.',
  short='Watch your horse closely, especially for the first day or so, for returning pain, appetite and normal manure. Follow your veterinarian’s re-feeding and activity instructions, and call if pain returns or manure changes.',
  body='''<h2>What to watch</h2>
<ul>
<li><strong>Comfort</strong> — any return of flank-watching, pawing, stretching or restlessness. Penn Vet says signs that improve and then return are a reason to call.</li>
<li><strong>Appetite</strong> — Penn Vet lists returning appetite as something to watch for.</li>
<li><strong>Manure</strong> — EQUUS notes that manure can stay abnormal after a horse looks comfortable; extreme changes, or changes lasting more than a day, warrant a call to your vet.</li>
<li><strong>Water intake</strong> and general demeanor.</li>
</ul>
<h2>Feeding and activity</h2>
<p>Penn Vet advises returning to the regular diet and routine work gradually and following your veterinarian's direction; controlled hand-walking and grazing are fine. Ask your vet for a written plan covering feed, turnout and medications. For horses that had colic surgery, see <a href="/qa/colic/colic-surgery-recovery-and-aftercare/">surgery recovery and aftercare</a>.</p>
<p>Keep a simple log of appetite, manure and behavior. If your vet gave you medication instructions, follow them exactly.</p>''',
  src=['penn','equus','aaep'], rel=['colic-surgery-recovery-and-aftercare','how-to-prevent-colic','when-to-call-the-vet-for-colic']),

 dict(slug='how-to-prevent-colic', ids=['VET-QA-0002','VET-QA-0004','VET-QA-0005','VET-QA-0006','VET-QA-0010'], urgent=False,
  q='How can I prevent colic in my horse?',
  title='How to Prevent Colic in Horses',
  meta='No program prevents every colic, but steady routines, forage-based feeding, constant water, gradual feed changes, parasite control and dental care reduce risk.',
  short='You cannot prevent every episode, but steady routines, a forage-based diet, constant access to water, gradual feed changes, turnout, parasite control and dental care all reduce risk. Ask your veterinarian to tailor a plan, especially after a prior colic.',
  body='''<h2>Practices recommended by veterinary sources</h2>
<ul>
<li><strong>Keep a consistent routine</strong> for feeding, exercise and turnout, including weekends.</li>
<li><strong>Make forage the foundation.</strong> AAEP recommends good-quality pasture, hay, cubes or haylage, with adult horses getting at least 1% of body weight in roughage daily, and grain-based feeds limited to a supplement of no more than half the diet, split into several smaller meals.</li>
<li><strong>Change feed gradually.</strong> Penn Vet says over several days; UC Davis lists slow feed changes and avoiding feeding errors.</li>
<li><strong>Provide fresh water at all times.</strong> Penn Vet suggests salt, mashes or warm water in winter to encourage drinking.</li>
<li><strong>Provide daily exercise or turnout.</strong> UC Davis lists turnout and routine as modifiable factors.</li>
<li><strong>Use a parasite-control program</strong> designed with your vet, with fecal testing to check that it works.</li>
<li><strong>Schedule dental care.</strong> Penn Vet recommends yearly dental exams and floating.</li>
<li><strong>Reduce stress</strong> from environment or workload changes, and watch closely during transport, shows and foaling.</li>
<li><strong>Check hay, pasture and bedding</strong> for toxins and moldy or poor-quality hay, and avoid feeding on the ground, especially on sandy soil. See <a href="/qa/colic/how-to-prevent-sand-colic/">preventing sand colic</a>.</li>
<li><strong>Avoid unprescribed medications.</strong></li>
<li><strong>Give extra attention to horses with prior colic</strong> and keep accurate records.</li>
</ul>
<p>Should you change the diet after a colic episode? Only gradually, and with your veterinarian: the right changes depend on what caused the episode. See <a href="/qa/colic/diet-and-manure-impaction-in-horses/">diet and manure impaction</a>.</p>''',
  src=['aaep','penn','ucd'], rel=['how-to-prevent-sand-colic','diet-and-manure-impaction-in-horses','causes-of-colic']),

 dict(slug='signs-of-sand-colic', ids=['VET-QA-0011'], urgent=False,
  q='What are the signs of sand colic?',
  title='Signs of Sand Colic in Horses',
  meta='Sand colic can start vaguely: loose manure, reduced appetite, weight loss, mild recurring colic. Learn the signs, home test limits and how vets diagnose it.',
  short='Sand colic often looks like other colic, and early signs can be vague: a horse that seems depressed or off, recurring mild colic, loose manure or diarrhea, and weight loss. Horses on sandy ground or fed from the ground are most at risk.',
  body='''<h2>What owners may notice</h2>
<ul>
<li>Recurring mild colic signs — pawing, flank-watching, restlessness</li>
<li>Loose manure or diarrhea, and reduced appetite</li>
<li>Chronic weight loss</li>
<li>Depression or lethargy rather than obvious pain, in the early stage</li>
<li>In larger accumulations: general colic signs such as sweating, rolling, faster heart and breathing rates, pale gums</li>
</ul>
<p>A horse that is "not acting right" or going off feed may be the first sign, according to University of Arizona Cooperative Extension.</p>
<h2>Why diagnosis needs a vet</h2>
<p>A manure-in-water settling test at home can show that a horse is eating sand, but it does not show whether sand is building up in the gut. A review of 62 horses referred to university hospitals found only 48% had significant sand in their manure (reported by EQUUS), and a 2022 review in <em>Equine Veterinary Education</em> concluded that the test is not reliable for screening. Vets use stethoscope sounds, radiographs (X-rays) and ultrasound.</p>
<p>Because colic signs overlap, any persistent abdominal pain warrants a <a href="/qa/colic/when-to-call-the-vet-for-colic/">call to your vet</a>. Prevention: <a href="/qa/colic/how-to-prevent-sand-colic/">how to prevent sand colic</a>.</p>''',
  src=['uaz','hr','equus2','merck'], rel=['how-to-prevent-sand-colic','signs-of-colic','types-of-colic']),

 dict(slug='how-to-prevent-sand-colic', ids=['VET-QA-0007','VET-QA-0012','VET-QA-0022'], urgent=False,
  q='How can I prevent sand accumulation and sand colic in my horse?',
  title='How to Prevent Sand Colic in Horses',
  meta='Prevent sand colic by not feeding on the ground, using feeders and rubber mats, managing overgrazed pasture and asking your vet about psyllium.',
  short='Reduce how much sand your horse eats: do not feed on the ground, use feeders and mats, keep the diet high in fiber, and manage sandy pasture so horses do not graze it down to the roots. Psyllium may help some horses but should not be the only measure.',
  body='''<h2>Feeding and turnout measures</h2>
<ul>
<li><strong>Do not feed on the ground.</strong> Use tubs, hay nets or feeders; University of Arizona Extension adds that feeders can sit on rubber mats to catch dropped feed, with mats cleaned and feed tubs emptied of fines.</li>
<li><strong>Keep the diet high in fiber</strong> so sand passes through rather than settling. Slow feeders mimic grazing and reduce waste and boredom.</li>
<li><strong>Feed before turning horses out</strong> into sandy pens or arenas.</li>
<li><strong>Manage sandy pastures.</strong> Horses nibbling short grass swallow more sand and soil; a thin or overgrazed pasture is a risk factor.</li>
<li><strong>Provide salt.</strong> Horse &amp; Rider notes that lack of salt can lead horses to eat soil.</li>
</ul>
<h2>Psyllium</h2>
<p>Veterinary sources, including AAEP-cited advice in the University of Arizona guide, describe psyllium as a supplement some veterinarians use in sandy regions, and Merck Veterinary Manual says to give it as a veterinarian directs. The Arizona guide says it should not be relied on as the sole prevention method. Ask your vet whether it suits your horse and how it should be given. Wheat bran does not remove sand, and mineral oil does not move it, according to eXtension and University of Arizona.</p>
<h2>Monitoring</h2>
<p>Ask your veterinarian about periodic checks. A manure test at home has limits (see <a href="/qa/colic/signs-of-sand-colic/">signs of sand colic</a>); radiographs and ultrasound are what vets use to look for sand in the gut.</p>''',
  src=['uaz','hr','merck','ext','equus2'], rel=['signs-of-sand-colic','how-to-prevent-colic','diet-and-manure-impaction-in-horses']),

 dict(slug='impaction-colic-treatment', ids=['VET-QA-0020'], urgent=False,
  q='What are the treatment options for impaction colic?',
  title='Impaction Colic Treatment Options',
  meta='Veterinarians treat impaction colic with pain relief, fluids and sometimes laxatives by stomach tube. Learn what to expect and when surgery may be needed.',
  short='A veterinarian chooses and carries out treatment. It commonly combines pain relief, fluids and substances given by stomach tube to soften the impaction, with close monitoring. If the impaction does not begin to break down, surgery may be needed.',
  body='''<h2>What a vet may do</h2>
<ul>
<li><strong>Pain relief</strong>, chosen to limit side effects.</li>
<li><strong>Fluids</strong> by stomach tube or IV to prevent dehydration.</li>
<li><strong>Substances given by stomach tube</strong> to soften the impaction — Merck lists mineral oil, dioctyl sodium sulfosuccinate or psyllium, often with IV fluids. Strong laxatives that stimulate contractions are not commonly used and may make an impaction worse.</li>
<li><strong>Withholding or restricting feed</strong>, including a muzzle while the impaction softens.</li>
<li><strong>Repeated examinations</strong> to confirm the impaction is moving.</li>
</ul>
<h2>When surgery may be needed</h2>
<p>Merck says that if an impaction has not begun to break down within 3 to 5 days, surgery may be needed. Surgical outcomes vary: Merck reports survival above 95% for large-colon impaction and 60% to 80% for cecal impaction.</p>
<p>Do not give laxatives, oils or other remedies yourself; AAEP warns against giving oral substances before the vet arrives. See <a href="/qa/colic/what-to-do-if-your-horse-has-colic/">what to do while you wait</a> and <a href="/qa/colic/diet-and-manure-impaction-in-horses/">diet and manure impaction</a>.</p>''',
  src=['merck','aaep','ucd'], rel=['diet-and-manure-impaction-in-horses','signs-a-horse-may-need-colic-surgery','types-of-colic']),

 dict(slug='diet-and-manure-impaction-in-horses', ids=['VET-QA-0021'], urgent=False,
  q='What dietary changes can help prevent manure compaction?',
  title='Diet and Manure Impaction in Horses',
  meta='Manure impaction is linked to coarse feed, low water intake, dental problems and stall confinement. See the diet and care steps vet sources recommend.',
  short='The factors veterinary sources link to impaction are coarse feed, low water intake, dental problems and stall confinement. Forage-based feeding, constant water, small frequent meals, gradual changes and good teeth address them.',
  body='''<h2>What is linked to impaction</h2>
<p>Merck Veterinary Manual associates large-intestine impaction with coarse feed, low water intake and dental problems. UC Davis lists recent stall confinement as a risk factor.</p>
<h2>What veterinary sources recommend</h2>
<ul>
<li><strong>Base the diet on forage</strong> and keep grain-based feed to a limited supplement split into smaller meals (AAEP).</li>
<li><strong>Maximize water intake.</strong> Penn Vet suggests salt, mashes or warm water in winter to encourage drinking.</li>
<li><strong>Feed small, frequent meals</strong> and change feeds slowly (UC Davis).</li>
<li><strong>Keep up dental care.</strong> Poor chewing is linked to impaction.</li>
<li><strong>Provide turnout and exercise</strong>, and keep routines consistent.</li>
</ul>
<p>Supplements for gut motility or manure softening should be chosen with your veterinarian rather than added on your own. See <a href="/qa/colic/how-to-prevent-colic/">how to prevent colic</a> and <a href="/qa/colic/impaction-colic-treatment/">impaction colic treatment</a>.</p>''',
  src=['merck','ucd','aaep','penn'], rel=['how-to-prevent-colic','impaction-colic-treatment','how-to-prevent-sand-colic']),

 dict(slug='signs-a-horse-may-need-colic-surgery', ids=['VET-QA-0018'], urgent=True,
  q='What are the signs that a horse might need colic surgery?',
  title='Signs a Horse May Need Colic Surgery',
  meta='Only a vet can decide on colic surgery. Learn the findings that raise concern: pain that will not settle, large reflux, no gut sounds, abnormal exam results.',
  short='Only a veterinarian can decide. Concern grows when pain is uncontrollable or returns after pain relief, when heart rate stays high, and when the exam finds things like large reflux, no gut sounds or a displacement on rectal exam. Early referral improves the odds.',
  body='''<h2>Findings that raise concern</h2>
<p>Merck Veterinary Manual lists these signs that surgery may be needed:</p>
<ul>
<li>Uncontrollable pain, or pain that does not respond to pain medication</li>
<li>Large amounts of fluid (more than 4 liters) from the stomach tube</li>
<li>No intestinal sounds</li>
<li>An abnormal abdominal fluid sample</li>
<li>Obstruction or displacement found on rectal exam</li>
<li>Long-term colic that has not responded to routine treatment</li>
</ul>
<p>Penn Vet adds persistent pain even after sedatives, and a heart rate that stays above 60, as warning signs for referral to a hospital. UC Davis states that strangulating conditions always require surgery.</p>
<h2>Why timing matters</h2>
<p>Merck says surgery should be done promptly and usually means referral to an equine surgeon. AAEP stresses that time is critical when emergency surgery may be needed. If your vet recommends referral, ask about transport and contact your insurer if the horse is insured.</p>
<p>See <a href="/qa/colic/colic-surgery-success-rates/">success rates</a>, <a href="/qa/colic/colic-surgery-risks-and-complications/">risks</a> and <a href="/qa/colic/colic-surgery-recovery-and-aftercare/">recovery</a>. If your horse has colic signs now, <a href="/qa/colic/when-to-call-the-vet-for-colic/">call your vet</a>.</p>''',
  src=['merck','penn','ucd','aaep','acvs'], rel=['colic-surgery-success-rates','colic-surgery-risks-and-complications','when-to-call-the-vet-for-colic']),

 dict(slug='colic-surgery-success-rates', ids=['VET-QA-0019'], urgent=False,
  q='What are the success rates for colic surgery?',
  title='Colic Surgery Success Rates in Horses',
  meta='Survival to hospital discharge after colic surgery ranges widely by hospital and lesion. See figures from Merck, Illinois and an Italian multicentre study.',
  short='Published survival to hospital discharge ranges widely — roughly 50% to more than 80% in Merck’s summary — depending on the lesion, how severe it is and which horses are counted. Your surgeon can give a prognosis for your horse after diagnostics.',
  body='''<h2>Survival to discharge</h2>
<ul>
<li><strong>Merck Veterinary Manual:</strong> survival after colic surgery ranges from about 50% to more than 80%, highest with mild pain and lowest with severe pain.</li>
<li><strong>University of Illinois, 254 horses:</strong> 52% survived to discharge. Among horses that recovered from anesthesia, 83% did. The review reports a range of 32% to 100% across other studies, averaging about 80%, and cautions that counting only horses that recovered from anesthesia can overstate overall survival.</li>
<li><strong>Italian multicentre study, 451 horses at three teaching hospitals:</strong> 68.5% overall survived to discharge; 80% of the 386 that recovered from anesthesia did.</li>
</ul>
<h2>By type of problem (Merck)</h2>
<ul>
<li>Large-colon impaction: over 95%</li>
<li>Cecal impaction: 60% to 80%</li>
<li>Enteroliths: around 95% at specialized practices</li>
</ul>
<p>UC Davis notes that twisted intestine does better with milder twists — good prognosis below 180°, fair from 180° to 270°, poor above 270°.</p>
<h2>What affects the outlook</h2>
<p>Merck lists distended intestines, absent gut sounds, red gums and poor circulation as signs of a worse outlook. The Italian study linked non-survival to age over 14, low body condition, a high packed cell volume on arrival, strangulating lesions and certain surgical factors. Figures come from referral hospitals and do not predict any one horse.</p>
<p>See <a href="/qa/colic/colic-surgery-risks-and-complications/">risks and complications</a> and <a href="/qa/colic/colic-surgery-recovery-and-aftercare/">recovery</a>.</p>''',
  src=['merck','ill','ita','ucd'], rel=['colic-surgery-risks-and-complications','colic-surgery-recovery-and-aftercare','signs-a-horse-may-need-colic-surgery']),

 dict(slug='colic-surgery-risks-and-complications', ids=['VET-QA-0015','VET-QA-0016'], urgent=False,
  q='What are the risks and potential complications of colic surgery?',
  title='Colic Surgery Risks and Complications',
  meta='Possible complications after colic surgery: fever, incision problems, recurrent colic, reflux, diarrhea, adhesions, laminitis. See rates and warning signs.',
  short='Complications are common and range from fever and incision problems to recurrent colic, reflux, diarrhea, adhesions and laminitis. Many are treatable, and the risk depends on the lesion. Your surgeon can give a horse-specific outlook.',
  body='''<h2>How often complications occur</h2>
<p>An Italian multicentre study of 386 horses that recovered from anesthesia reported these complications before discharge:</p>
<ul>
<li>Fever 27.7%; surgical-site infection 25.1%</li>
<li>Postoperative colic 23.5%; reflux 20.4%</li>
<li>Diarrhea 10.1%; thrombophlebitis (inflamed vein) 7.7%</li>
<li>Incisional hernia 5.7%; laminitis 3.1%</li>
</ul>
<p>Rates differ between hospitals and types of surgery.</p>
<h2>Complications described by veterinary surgeons</h2>
<p>The University of Minnesota large-animal surgery text lists ileus (slowed gut), diarrhea, endotoxemia, laminitis, adhesions, incisional infection, incision opening (dehiscence), hernia, peritonitis and continued pain. Merck adds that adhesions are a potential complication and large-colon twist can recur in up to 20% of cases.</p>
<h2>Incision warning signs at home</h2>
<p>Minnesota advises watching for asymmetric or worsening swelling, pain, drainage or fever; normal swelling is cool, painless and moves forward. Call your veterinarian promptly for any of these.</p>
<p>There is also anesthesia risk, and some horses do not survive despite treatment — see <a href="/qa/colic/colic-surgery-success-rates/">success rates</a>. For aftercare see <a href="/qa/colic/colic-surgery-recovery-and-aftercare/">recovery and aftercare</a>.</p>''',
  src=['ita','umn','merck'], rel=['colic-surgery-success-rates','colic-surgery-recovery-and-aftercare','signs-a-horse-may-need-colic-surgery']),

 dict(slug='colic-hospital-stay', ids=['VET-QA-0009'], urgent=False,
  q='How long will my horse need to stay at the veterinary hospital for colic?',
  title='How Long Is a Colic Hospital Stay?',
  meta='A colic hospital stay depends on the cause, response to treatment and any surgery. See typical surgical stays and what hospital teams monitor.',
  short='It depends on the cause, how the horse responds and whether surgery or complications are involved. The University of Minnesota text gives 3 to 4 days for uncomplicated surgical horses and 1 to 2 weeks for complicated cases. Your veterinarian can estimate after rechecks.',
  body='''<h2>Surgical colic</h2>
<p>The University of Minnesota large-animal surgery text says horses with an uncomplicated recovery are typically ready for discharge in 3 to 4 days, while complicated cases can take 1 to 2 weeks. Hospital teams monitor pain, appetite, manure, hydration and the incision, and reintroduce feed gradually.</p>
<h2>Medical colic</h2>
<p>Penn Vet notes that if pain is mild, the horse is not dehydrated and the exam is reassuring, treatment usually happens at home with close monitoring. Horses that are dehydrated, need intensive care or may need surgery go to a referral clinic with around-the-clock monitoring and IV fluids. We have no reliable general figure for how long such stays last; ask your veterinarian.</p>
<p>Plans change day to day. See <a href="/qa/colic/colic-surgery-recovery-and-aftercare/">recovery and aftercare</a> for what happens after discharge.</p>''',
  src=['umn','penn'], rel=['colic-surgery-recovery-and-aftercare','colic-surgery-risks-and-complications','colic-surgery-success-rates']),

 dict(slug='colic-surgery-recovery-and-aftercare', ids=['VET-QA-0008','VET-QA-0023'], urgent=False,
  q='How long is recovery after colic surgery, and what aftercare is needed?',
  title='Colic Surgery Recovery and Aftercare',
  meta='A typical colic surgery recovery plan: stall rest with hand-walking, small paddock turnout, then gradual return to work over about 90 days. Protocols vary.',
  short='A commonly used plan is about 30 days of stall rest with hand-walking, then a small paddock, then a gradual return to normal activity by around 60 to 90 days. Protocols differ by surgeon and horse, so your discharge instructions come first.',
  body='''<h2>A commonly cited timeline</h2>
<p>The University of Minnesota large-animal surgery text gives this example:</p>
<ul>
<li><strong>Days 0–30:</strong> stall rest with hand-walking (about 10 minutes, 3 to 4 times a day) and hand-grazing if grass is available.</li>
<li><strong>Days 30–60:</strong> round pen or small paddock if the incision is healing well; otherwise more hand-walking.</li>
<li><strong>Days 60–90:</strong> gradual return to normal activity. Extra rest is advised after incision or other complications.</li>
</ul>
<p>ACVS says horses with uncomplicated recoveries typically return to work after two to three months of stall, small-paddock and controlled-pasture rest. Some hospitals use other schedules, so follow your own surgeon's plan.</p>
<h2>Aftercare checklist</h2>
<ul>
<li><strong>Incision:</strong> check daily for asymmetric or worsening swelling, pain, drainage or fever. Minnesota advises restricting bouncing activity for the first 60 days to lower hernia risk.</li>
<li><strong>Feeding:</strong> follow the hospital's instructions for gradually returning to full feed.</li>
<li><strong>Medications:</strong> give only as prescribed.</li>
<li><strong>Monitoring:</strong> appetite, water, manure and attitude. The Minnesota text also notes that laminitis risk rises after strangulating lesions, so report sudden foot soreness.</li>
</ul>
<p>Call your veterinarian for fever, worsening pain, reduced manure, poor appetite, diarrhea, or incision changes. See <a href="/qa/colic/colic-surgery-risks-and-complications/">risks and complications</a>.</p>''',
  src=['umn','acvs','merck'], rel=['colic-surgery-risks-and-complications','colic-hospital-stay','what-to-monitor-after-a-colic-episode']),
]
