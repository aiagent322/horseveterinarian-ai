# -*- coding: utf-8 -*-
"""Hay, forage, water and weight Q&A (source-first; package records 0501-0514 used only as question prompts). Same rules as qa_colic.py. No grain or supplement doses."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnhay': ('University of Minnesota Extension — Hay in Horse Diets', 'https://extension.umn.edu/agriculture/animals-and-livestock/horse/hay-in-horse-diets'),
 'umnanalysis': ('University of Minnesota Extension — Understanding Your Hay Analysis', 'https://extension.umn.edu/horse-nutrition/understanding-your-hay-analysis'),
 'umnbalancer': ('University of Minnesota Extension — Feeding Your Horse a Ration Balancer', 'https://extension.umn.edu/horse-nutrition/feeding-your-horse-ration-balancer'),
 'okwater': ('Oklahoma State University Extension — Water: The Most Important Nutrient', 'https://extension.okstate.edu/fact-sheets/water-the-most-important-nutrient.html'),
 'osubcs': ('Ohio State University Extension — Evaluating Body Composition of Horses (H. Zynda, AS-1024; 2022)', 'https://ohioline.osu.edu/factsheet/as-1024'),
 'ugamold': ('University of Georgia Extension Forage Team — Look Out for Moldy Hay (L. Ray; 2017)', 'https://site.extension.uga.edu/forageteam/2017/03/look-out-for-moldy-hay'),
 'ugamold2': ('University of Georgia Extension Forage Team — Watch Out for Moldy Hay (2022)', 'https://site.extension.uga.edu/forageteam/2022/01/watch-out-for-moldy-hay'),
 'usuforage': ('Utah State University Extension — Equine Nutrition: Forages (reviewed March 2010)', 'https://extension.usu.edu/equine/research/equine-nutrition-forages.php'),
 'ukhay': ('University of Kentucky Cooperative Extension — Choosing Hay for Horses (L. Lawrence, R. Coleman, J. Henning; ID-146)', 'https://afs.afs.prod-web.ca.uky.edu/sites/afs.ca.uky.edu/files/id146.pdf'),
 'aceshay': ('Alabama Cooperative Extension System — Estimating and Supplying Equine Forage Requirements (ANR-3153; 2025)', 'https://www.aces.edu/wp-content/uploads/2025/05/ANR-3153_EstimatingandSupplyingEquineForageRequirments_081525aL-G.pdf'),
 'ugahydr': ('University of Georgia Elevated Equine — Keeping Horses Hydrated (July 2025)', 'https://elevatedequine.uga.edu/2025/07/keeping-horses-hydrated'),
})
HELD = {}
PAGES = [
 dict(slug='how-much-hay-should-a-horse-eat-each-day', ids=[], urgent=False,
  q='How much hay should my horse eat each day?',
  title='How Much Hay Should a Horse Eat Each Day?',
  meta='Extension sources say most horses need about 2 percent of body weight in hay daily and at least 1 percent in forage. Needs vary; ask your vet.',
  short='The University of Minnesota says horses need at least 1 percent of body weight in roughage daily, and most should get about 2 percent in hay. Needs change with age, work, growth, pregnancy and lactation, so ask your veterinarian or extension office about your horse.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Horses need at least 1 percent of body weight in roughage each day; given free access they will eat 2 to 2.5 percent, and most horses should get about 2 percent (University of Minnesota).</li>
<li>Forage should make up at least half the daily ration for any class of horse (University of Minnesota).</li>
<li>Alabama Extension gives 1 percent as the absolute minimum, usually reserved for heavily worked horses on high-grain diets, and about 2 percent as a starting target.</li>
<li>For an idle adult, good-quality grass hay alone can meet nutrient needs (University of Minnesota). Heavier work usually calls for a grain-based concentrate.</li>
</ul>
<h2>What changes the amount</h2>
<p>Minnesota says needs depend on age, weight, activity, growth, and pregnancy or lactation. To use a percentage you need an estimate of body weight; see <a href="/qa/feeding/how-to-estimate-your-horses-weight-and-body-condition/">estimating weight and body condition</a>. Cold weather also raises energy needs; see <a href="/qa/winter-care/feeding-horses-in-cold-weather/">feeding in cold weather</a>.</p>
<h2>When to ask your veterinarian</h2>
<p>Call your veterinarian if a horse stops eating or shows colic signs; see the <a href="/emergency/not-eating/">not eating guide</a>. A horse that needs to gain or lose weight, or has a metabolic problem, needs a plan from your veterinarian; see <a href="/qa/metabolic/safe-weight-management-for-horses/">safe weight management</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page gives no grain amounts. The sources point to the National Research Council <em>Nutrient Requirements of Horses</em> for detailed calculations.</p>''',
  src=['umnhay','aceshay'], rel=['grass-hay-or-alfalfa-for-horses','how-to-estimate-your-horses-weight-and-body-condition','how-to-tell-if-hay-is-unsafe-to-feed']),

 dict(slug='grass-hay-or-alfalfa-for-horses', ids=[], urgent=False,
  q='Should I feed grass hay or alfalfa?',
  title='Grass Hay or Alfalfa for Horses?',
  meta='Alfalfa is higher in energy, protein and calcium than grass hay. Extension sources favor grass or grass-alfalfa mixes for idle or lightly worked horses.',
  short='Extension sources say alfalfa is higher than grass hay in energy, protein and calcium. Grass hay or a grass-alfalfa mix is generally preferred for idle or lightly worked horses, while growing horses, lactating mares and performance horses may need more nutrient-dense hay. Ask your veterinarian.',
  body='''<h2>How they differ</h2>
<ul>
<li>Alfalfa is higher than grass hay in digestible energy, amino acids and calcium (University of Minnesota). Legumes such as alfalfa and clover are typically much higher in protein and calcium than grass hays (University of Kentucky).</li>
<li>The nutrient content within any hay type depends heavily on how mature the plants were when cut; less mature forage is more nutrient-dense (University of Minnesota; University of Kentucky).</li>
</ul>
<h2>Which horses suit which hay</h2>
<ul>
<li>Utah State says the preferred feed for idle or lightly worked horses is grass hay or a grass-alfalfa mix rather than straight alfalfa, and notes a possible calcium-phosphorus imbalance when feeding straight alfalfa without an appropriate mineral mix.</li>
<li>Minnesota says alfalfa may meet the needs of light or moderate work, and grass hay or grass-alfalfa mixes suit growing horses. If feeding a lot of alfalfa, keep the calcium-to-phosphorus ratio near 3 to 1 and never inverted.</li>
<li>Kentucky says higher-nutrient hay suits growing horses, lactating mares and performance horses, while mid- or late-maturity grass hay or alfalfa often suits horses with low nutrient needs.</li>
</ul>
<h2>Whichever you choose</h2>
<p>Utah State says hay should be bright, clean and fresh, and free of dust, mold and contaminants. See <a href="/qa/feeding/how-to-tell-if-hay-is-unsafe-to-feed/">how to tell if hay is unsafe</a>. Horses with insulin resistance, Cushing disease or a history of laminitis need hay chosen with your veterinarian; see <a href="/qa/feeding/how-to-read-a-hay-analysis/">how to read a hay analysis</a>.</p>
<h2>What the sources do not cover</h2>
<p>They do not name a best hay for every horse. Local availability matters, and your county extension office can help you find and compare hay.</p>''',
  src=['umnhay','usuforage','ukhay'], rel=['how-to-read-a-hay-analysis','how-to-tell-if-hay-is-unsafe-to-feed','how-much-hay-should-a-horse-eat-each-day']),

 dict(slug='how-to-read-a-hay-analysis', ids=[], urgent=False,
  q='What should I look for in a hay analysis?',
  title='How to Read a Hay Analysis for Horses',
  meta='A hay analysis shows moisture, protein, fiber, energy, minerals and sugars. Learn what each value means and when to ask a nutritionist for help.',
  short='The University of Minnesota says a hay analysis reports moisture, protein, fiber, energy, minerals, and sugars and starch. Ask for a horse analysis, test each field and cutting separately, compare on a dry matter basis, and work with a horse nutritionist to balance the ration.',
  body='''<h2>Getting it done</h2>
<ul>
<li>Request a horse analysis and test each field and each cutting separately (University of Minnesota).</li>
<li>Check with your lab or county extension office for sampling instructions.</li>
</ul>
<h2>Main values, per University of Minnesota</h2>
<ul>
<li><strong>As-fed versus dry matter:</strong> as-fed includes the water in the hay; dry matter removes it. Use one column consistently; Minnesota recommends dry matter.</li>
<li><strong>Moisture:</strong> about 10 to 15 percent is ideal. Above about 16 percent hay can mold without a preservative, and at very high moisture there is a risk of severe heating and fire.</li>
<li><strong>Crude protein:</strong> most adult horses at maintenance need about 10 percent, and Minnesota gives typical ranges for grass, mixed and legume hays.</li>
<li><strong>ADF and NDF:</strong> fiber values. ADF indicates digestibility, and NDF relates to how much a horse will eat. Lower is better for ADF.</li>
<li><strong>Digestible energy:</strong> used to balance the energy in a ration.</li>
<li><strong>Calcium and phosphorus:</strong> the ratio matters as well as the amounts.</li>
<li><strong>NSC (starch plus water-soluble sugars):</strong> helps identify hay for sugar- or starch-sensitive horses, such as those with insulin resistance or laminitis. Minnesota advises that these horses avoid hay above about 10 to 12 percent NSC or have it soaked first; ask your veterinarian before changing the diet of such a horse.</li>
</ul>
<h2>Next step</h2>
<p>Minnesota says to consult a horse nutritionist after you receive the results to balance the ration, especially if hay quality is a concern or the horse has nutrition problems. See <a href="/qa/feeding/ration-balancers-and-supplements-for-horses/">ration balancers and supplements</a>.</p>
<h2>What the source does not cover</h2>
<p>It does not describe how to take the sample itself.</p>''',
  src=['umnanalysis','umnhay'], rel=['ration-balancers-and-supplements-for-horses','grass-hay-or-alfalfa-for-horses','how-to-tell-if-hay-is-unsafe-to-feed']),

 dict(slug='how-to-tell-if-hay-is-unsafe-to-feed', ids=[], urgent=True,
  q='How can I tell whether hay is unsafe to feed?',
  title='How to Tell if Hay Is Unsafe to Feed a Horse',
  meta='Moldy, dusty or contaminated hay can harm horses. Extension sources say hay should be bright, clean and fresh. Call your vet for colic or breathing signs.',
  short='Extension sources say hay should be bright, clean and fresh and free of dust, mold and contaminants, and that horses are particularly susceptible to moldy forage. Do not feed hay you suspect is moldy, and call your veterinarian if a horse shows colic signs, breathing trouble or stops eating.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Hay should be bright, clean and fresh, and free of dust, mold and other contaminants (Utah State).</li>
<li>Horses are noted as being particularly susceptible to moldy forages, more so if the feed is very dusty or fed in a poorly ventilated area (University of Georgia).</li>
<li>Georgia says mold can cause digestive upset and colic in horses.</li>
<li>Mold can grow on hay with moisture above about 14 to 15 percent (University of Georgia), and Minnesota notes that very wet hay can heat and carry a fire risk.</li>
<li>Dry hay can draw moisture from humid air, particularly on the outer part of the exposed surface (University of Georgia).</li>
</ul>
<h2>What to do</h2>
<ul>
<li>Do not feed hay you suspect is moldy. The sources used here give no safe level of mold for horses.</li>
<li>If you cannot judge a bale, a laboratory test can check moisture and nutrients; see <a href="/qa/feeding/how-to-read-a-hay-analysis/">how to read a hay analysis</a>. Minnesota describes laboratory analysis as the best way to judge hay quality.</li>
</ul>
<h2>Call your veterinarian</h2>
<p>Call your veterinarian for colic signs, coughing or labored breathing, or a horse that stops eating after a feed change. See the <a href="/emergency/colic-emergency/">colic emergency guide</a>, the <a href="/emergency/not-eating/">not eating guide</a>, and <a href="/qa/respiratory/">respiratory questions</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page does not list other hay hazards such as blister beetles or botulism; ask your veterinarian or extension office about risks in your area.</p>''',
  src=['usuforage','ugamold','ugamold2','umnanalysis'], rel=['how-to-read-a-hay-analysis','grass-hay-or-alfalfa-for-horses','how-much-hay-should-a-horse-eat-each-day']),

 dict(slug='ration-balancers-and-supplements-for-horses', ids=[], urgent=False,
  q='Does my horse need a ration balancer or a supplement?',
  title='Ration Balancers and Supplements for Horses',
  meta='A ration balancer supplies vitamins and trace minerals without adding energy. Extension sources say a hay analysis is the best way to find real gaps.',
  short='The University of Minnesota says a ration balancer is a concentrated feed that supplies the vitamins and trace minerals forage may lack, without adding energy. A hay analysis is the best way to find nutrient gaps; ask your veterinarian or a horse nutritionist before adding supplements.',
  body='''<h2>What a ration balancer is</h2>
<p>A commercial feed that supplies trace minerals and vitamins, fed in small amounts and adding no energy (University of Minnesota).</p>
<h2>Who may need one, per Minnesota</h2>
<ul>
<li>Horses that get enough energy from forage but whose hay or pasture lacks vitamins and trace minerals.</li>
<li>Horses fed hay plus cereal grains such as oats or corn, because grains are poor sources of trace minerals and vitamins.</li>
</ul>
<h2>When a commercial feed can replace it</h2>
<p>Only if the feed is designed to supply all essential vitamins and minerals, is fed as the manufacturer directs, and matches the horse type, such as a performance feed for performance horses. Cutting the amount fed to save money or manage weight also cuts the vitamins and minerals.</p>
<h2>Finding real gaps</h2>
<p>Minnesota says laboratory analysis is the best way to judge hay and find nutrient gaps. See <a href="/qa/feeding/how-to-read-a-hay-analysis/">how to read a hay analysis</a>. Ask your veterinarian or a horse nutritionist before adding other supplements. Needs differ for breeding mares; see <a href="/qa/mare-foaling/feeding-a-mare-in-late-pregnancy-and-lactation/">feeding a mare in late pregnancy and lactation</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page names no brands and gives no feeding amounts. It does not cover supplements for specific conditions.</p>''',
  src=['umnbalancer','umnhay'], rel=['how-to-read-a-hay-analysis','how-much-hay-should-a-horse-eat-each-day']),

 dict(slug='how-much-water-and-salt-does-a-horse-need', ids=[], urgent=False,
  q='How much water does my horse need each day, and does it need extra salt?',
  title='How Much Water and Salt Does a Horse Need?',
  meta='A 1,000-pound horse drinks about 10 gallons a day, more in heat or work. Extension sources advise free access to water and salt. Call your vet if it stops.',
  short='Oklahoma State says a 1,000-pound horse drinks about 10 gallons a day, with more needed in heat, with work and during lactation. Georgia says free-choice salt helps meet sodium needs and encourages drinking. A horse that stops drinking or eating needs a call to your veterinarian.',
  body='''<h2>Water</h2>
<ul>
<li>A horse must replace what it loses through manure, urine, sweat, breathing and, for mares, milk; a 1,000-pound horse drinks about 10 gallons a day (Oklahoma State).</li>
<li>Forage-heavy diets raise water needs, while lush pasture holds water so horses drink less (Oklahoma State).</li>
<li>Heat, sweating and exercise raise needs sharply; horses may need up to three weeks to acclimate to heat, and lactation can raise a mare needs by roughly 50 to 75 percent (Oklahoma State).</li>
<li>Overly dry manure raises impaction colic risk (Oklahoma State).</li>
</ul>
<h2>Salt and electrolytes</h2>
<ul>
<li>Georgia says free-choice plain salt blocks or loose salt help meet daily sodium needs and encourage drinking, and gives about 1 to 2 ounces of salt a day for a 1,000-pound horse, more if sweating.</li>
<li>Georgia advises against giving electrolytes daily without need, and says they are not a substitute for free-choice salt and can irritate a dehydrated horse. Always offer clean water alongside electrolytes.</li>
<li>Oklahoma State says horses that eat a lot of salt urinate more, so heavy salt eaters may need intake limited to the daily requirement.</li>
</ul>
<h2>Call your veterinarian</h2>
<p>Call your veterinarian if a horse stops drinking or eating, or shows colic signs. See <a href="/qa/exercise/signs-of-dehydration-in-horses/">signs of dehydration</a>, <a href="/qa/hot-weather/water-and-electrolytes-for-horses-in-hot-weather/">water and electrolytes in hot weather</a> and <a href="/qa/winter-care/water-in-winter-and-impaction-colic-risk/">water in winter</a>.</p>
<h2>What the sources do not cover</h2>
<p>Oklahoma State lists no specific signs of too little water. This page gives no electrolyte products or amounts.</p>''',
  src=['okwater','ugahydr'], rel=['how-much-hay-should-a-horse-eat-each-day','ration-balancers-and-supplements-for-horses']),

 dict(slug='how-to-estimate-your-horses-weight-and-body-condition', ids=[], urgent=False,
  q='How can I estimate my horse weight without a scale?',
  title='How to Estimate Your Horse Weight and Body Condition',
  meta='A livestock scale is most accurate; a weight tape or girth formula gives an estimate. Pair it with body condition scoring and track trends over time.',
  short='Ohio State Extension says a livestock scale is most accurate, a weight tape reads lighter than a scale for many horses, and a formula using heart girth and body length can estimate weight. Body condition scoring on the 1 to 9 Henneke scale shows fat cover. Track trends over time.',
  body='''<h2>Estimating weight</h2>
<ul>
<li>A livestock scale is the most accurate. You can also weigh a truck and trailer with and without the horse and subtract (Ohio State).</li>
<li>Weight tapes usually read lighter than the scale, and the difference varies by horse. Use the same tape and the same spot on the withers each time to track trends (Ohio State).</li>
<li>Without a tape, Ohio State describes a formula: measure heart girth and body length in inches, square the girth, multiply by length and divide by 330 to get pounds.</li>
</ul>
<h2>Body condition and crest</h2>
<ul>
<li>Body condition scoring rates fat cover from 1 to 9 by sight and touch over six body areas; 5 is the general ideal, but the best target depends on workload and age (Ohio State).</li>
<li>Many horses are overweight and owners often underestimate fat. Over-conditioning raises metabolic, heat-stress and joint risks; under-conditioning can point to disease, injury or parasites (Ohio State).</li>
<li>A cresty neck score of 3 or higher signals higher risk of metabolic problems including laminitis (Ohio State). Muscle can look like a crest.</li>
</ul>
<h2>Tracking</h2>
<p>Ohio State recommends regular evaluations with written and photo records, because body composition changes slowly. It gives no set schedule. Rapid weight loss or a horse eating normally but losing weight needs your veterinarian; see <a href="/qa/senior-care/why-is-my-older-horse-losing-weight/">why a horse loses weight</a> and <a href="/qa/metabolic/safe-weight-management-for-horses/">safe weight management</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page does not set a target weight for your horse. Make diet changes with your veterinarian or a nutritionist.</p>''',
  src=['osubcs'], rel=['how-much-hay-should-a-horse-eat-each-day','ration-balancers-and-supplements-for-horses']),
]
