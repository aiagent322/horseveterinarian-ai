# -*- coding: utf-8 -*-
"""Parasite Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'aaeppar': ('AAEP — Internal Parasite Control Guidelines (revised May 2024)', 'https://aaep.org/resource/internal-parasite-control-guidelines/'),
 'umnpar': ('University of Minnesota Extension — Controlling and treating parasites in your horse', 'https://extension.umn.edu/horse-health/controlling-and-treating-parasites-your-horse'),
 'extpar': ('eXtension Horses — Management and Control of Internal Parasites in Horses', 'https://horses.extension.org/management-and-control-of-internal-parasites-in-horses/'),
})
HELD = {}
PAGES = [
 dict(slug='fecal-egg-counts-and-signs-of-worms', ids=['VET-QA-0397','VET-QA-0401'], urgent=False,
  q='How can I tell if a horse has worms, and what are the signs?',
  title='Signs of Worms in Horses and Fecal Egg Counts',
  meta='Many horses with heavy worm burdens look normal. A fecal egg count through your vet finds most parasites; weight loss, dull coat or colic need a vet visit.',
  short='Heavily parasitized horses can look healthy, so testing matters. A fecal egg count through your veterinarian finds most internal parasites but not tapeworms or bots. Possible signs include a dull coat, weight loss, low energy, diarrhea and colic, and young horses show problems more often. Call your vet for colic.',
  body='''<h2>Signs</h2>
<ul>
<li>Heavily parasitized horses can look healthy, with good weight and a glossy coat, while internal damage builds; younger horses more often show a dull coat, low energy, weight loss, coughing or nasal discharge, tail rubbing, colic, poor appetite or diarrhea (eXtension).</li>
<li>Large strongyles can cause fever, diarrhea, appetite loss, weight loss and colic, with recurring colic in chronic infections; small strongyles can cause poor appetite, weight loss, diarrhea, colic and severe thinness (University of Minnesota Extension).</li>
<li>Roundworms mostly affect foals, with poor appetite, slow growth, a dull dry coat and a potbelly. Pinworms cause anal itching and restlessness. Tapeworms and stomach bots often show no signs (UMN).</li>
</ul>
<h2>Testing</h2>
<ul>
<li>Fecal tests such as egg counts and flotation detect most internal parasites, but cannot reliably detect tapeworms or bots (UMN). Worms are rarely visible in manure (eXtension).</li>
<li>AAEP says egg counts do not reliably indicate disease, because they do not correlate with the parasite stages that cause it, and recommends using them once or twice a year to sort horses into low, medium or high shedders.</li>
<li>To check whether a dewormer worked, eXtension suggests recounting eggs about two weeks after treatment.</li>
</ul>
<p><strong>Call your veterinarian</strong> for colic, weight loss, diarrhea or other signs; these have many causes besides worms. See <a href="/qa/parasites/deworming-frequency-and-schedule/">deworming frequency</a>.</p>''',
  src=['extpar','umnpar','aaeppar'], rel=['deworming-frequency-and-schedule','dewormer-types-and-choosing-one','preventing-worm-infestations']),

 dict(slug='deworming-frequency-and-schedule', ids=['VET-QA-0398','VET-QA-0402'], urgent=False,
  q='How often should I deworm a horse, and what schedule is best?',
  title='How Often to Deworm a Horse',
  meta='AAEP advises a baseline of once or twice a year, extra treatment for high egg shedders based on fecal counts, and no fixed year-round schedule.',
  short='AAEP guidelines advise treating all horses at a baseline of once or twice a year, treating high strongyle shedders more often based on fecal egg counts, and stopping fixed year-round intervals such as every two months. Your veterinarian designs the program for your horse and farm.',
  body='''<h2>Current AAEP guidance (revised May 2024)</h2>
<ul>
<li>Treat all horses at a baseline frequency of once or twice a year, and treat high strongyle shedders more often based on their fecal egg count results.</li>
<li>Use fecal egg counts once or twice a year to sort horses into low, medium or high shedders.</li>
<li>Stop deworming on a fixed year-round schedule, such as every two months, and stop rotating drug classes without a reason.</li>
<li>Run fecal egg count reduction tests yearly in each herd or barn to confirm dewormers still work.</li>
</ul>
<h2>Where sources differ</h2>
<p>One extension page still describes deworming about four to six times a year starting at 4 to 8 weeks of age, and rotating classes (eXtension). That conflicts with the AAEP point about fixed schedules and blind rotation, so follow your veterinarian's current program. Climate, season, stocking density and horse age all influence the plan (eXtension). The sources reviewed give no schedule for foals beyond this, and no doses; always read the product label, since some products are toxic to foals (eXtension). See <a href="/qa/parasites/over-deworming-and-resistance/">over-deworming and resistance</a>.</p>''',
  src=['aaeppar','extpar'], rel=['over-deworming-and-resistance','fecal-egg-counts-and-signs-of-worms','dewormer-types-and-choosing-one']),

 dict(slug='dewormer-types-and-choosing-one', ids=['VET-QA-0399','VET-QA-0395'], urgent=False,
  q='What types of dewormers exist, and is there a specific dewormer you recommend?',
  title='Dewormer Types and Choosing One for a Horse',
  meta='Dewormer classes target different parasites and none covers everything. Choose with your vet using fecal egg counts. No product or dose is recommended here.',
  short='Dewormer classes target different parasites, and no single dewormer removes every parasite stage. Macrocyclic lactones are broad but do not cover tapeworms; benzimidazoles and pyrantel cover fewer parasites. This page recommends no product or dose: choose with your veterinarian based on fecal egg counts.',
  body='''<h2>Classes and what they target (UMN Extension)</h2>
<ul>
<li><strong>Benzimidazoles:</strong> roundworms and sometimes adult strongyles; not effective against larval strongyles, tapeworms or bots.</li>
<li><strong>Pyrantel:</strong> roundworms and adult strongyles; not effective against larval strongyles or bots.</li>
<li><strong>Macrocyclic lactones (ivermectin, moxidectin):</strong> roundworms, adult and larval strongyles and bots; not effective against tapeworms. Some veterinarians have stopped using moxidectin because of rare adverse reactions.</li>
<li><strong>Praziquantel combined with ivermectin:</strong> covers all the parasite groups listed.</li>
</ul>
<p>The key to selecting a dewormer is knowing which parasites each ingredient targets (UMN). No dewormer removes every parasite stage (AAEP), and some are unsafe for certain ages or types of horses (eXtension).</p>
<h2>Which one for my horse?</h2>
<p>The sources reviewed do not recommend a single best product, and none is named or dosed here. eXtension says a veterinarian should guide the program, and AAEP ties treatment to fecal egg counts. Ask your vet. See <a href="/qa/parasites/deworming-frequency-and-schedule/">how often to deworm</a>.</p>''',
  src=['umnpar','aaeppar','extpar'], rel=['deworming-frequency-and-schedule','over-deworming-and-resistance','fecal-egg-counts-and-signs-of-worms']),

 dict(slug='over-deworming-and-resistance', ids=['VET-QA-0400'], urgent=False,
  q='What are the risks of over-worming a horse?',
  title='Risks of Over-Deworming a Horse',
  meta='Over-deworming can promote drug-resistant parasites. Use fecal egg counts and your vet\'s plan to treat only as often as needed.',
  short='Over-deworming can promote the growth of resistant parasites, so the goal is to control parasites without treating unnecessarily. Daily dewormers may lead to resistance over time. Yearly fecal egg counts and reduction tests show whether a dewormer is still working.',
  body='''<ul>
<li>Over-deworming can promote the growth of resistant parasites, so the goal is to control parasites without treating unnecessarily (UMN Extension).</li>
<li>Continuous low-level exposure from daily dewormers may lead to resistance over time (UMN).</li>
<li>Yearly fecal egg counts help monitor parasite loads, show whether a dewormer is working and reveal resistance (UMN). AAEP recommends yearly fecal egg count reduction tests in each herd or barn.</li>
<li>No dewormer removes every parasite stage, and AAEP advises stopping fixed year-round intervals and blind class rotation.</li>
</ul>
<p>The sources reviewed do not list other health risks of over-deworming, so none are stated here. Work with your veterinarian on a targeted plan. See <a href="/qa/parasites/deworming-frequency-and-schedule/">how often to deworm</a>.</p>''',
  src=['umnpar','aaeppar'], rel=['deworming-frequency-and-schedule','dewormer-types-and-choosing-one','preventing-worm-infestations']),

 dict(slug='preventing-worm-infestations', ids=['VET-QA-0396'], urgent=False,
  q='How can I prevent worm infestations in a horse?',
  title='Preventing Worm Infestations in Horses',
  meta='Remove or compost manure, avoid overcrowding and feeding off the ground, rotate pastures, isolate new horses and use fecal egg counts with your vet.',
  short='Break the parasite life cycle: keep stalls clean, pick up or compost manure, avoid overcrowding and overgrazing, feed hay off the ground, rotate pastures, and isolate and treat new horses. Use fecal egg counts with your veterinarian to decide who needs deworming.',
  body='''<h2>Management (UMN Extension; eXtension)</h2>
<ul>
<li>Keep stalls clean; compost manure hot enough to kill larvae or spread it on ground horses will not graze.</li>
<li>Pick up or drag manure in pastures and mow to expose eggs and larvae to drying, sunlight and freezing; picking up manure is costly but effective.</li>
<li>Avoid overcrowding and overgrazing; rotational grazing spreads out manure and reduces overgrazing.</li>
<li>Feed from raised feeders or hay racks rather than the ground, and clean buckets and troughs regularly.</li>
<li>Isolate and treat new horses before they join the herd; keep young horses away from adults and heavily contaminated ground.</li>
<li>Grazing cattle or sheep with horses helps because most horse parasites do not infect those species (eXtension).</li>
</ul>
<h2>Targeted testing</h2>
<p>AAEP recommends fecal egg counts once or twice a year to identify high shedders so treatment can be targeted. Management and deworming work together; neither replaces the other (UMN). The sources give no stocking rate for your land, so none is listed. See <a href="/qa/parasites/fecal-egg-counts-and-signs-of-worms/">fecal egg counts</a>.</p>''',
  src=['umnpar','extpar','aaeppar'], rel=['fecal-egg-counts-and-signs-of-worms','deworming-frequency-and-schedule','over-deworming-and-resistance']),
]
