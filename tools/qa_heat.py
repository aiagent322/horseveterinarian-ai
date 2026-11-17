# -*- coding: utf-8 -*-
"""Hot weather / heat stress Q&A (source-first; no package records). Same rules as qa_colic.py. No amounts or doses."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnheat': ('University of Minnesota Extension — Caring for Horses During Hot Weather (K. Martinson, M. Hathaway, C. Ward, DVM, R. Johnson; reviewed 2024)', 'https://extension.umn.edu/horse/caring-horses-during-hot-weather'),
 'ufheat': ('University of Florida IFAS Extension — Managing Heat Stress in Horses, VM278 (A. Hernandez, C. Wickens, S. Brooks; Dec 2025)', 'https://ask.ifas.ufl.edu/publication/VM278'),
 'ufanhid': ('University of Florida IFAS Extension — Anhidrosis in the Horse (Non-Sweaters), AN362 (L. Patterson-Rosa, M. Mallicote, R. MacKay, S. Brooks; Nov 15, 2020)', 'https://ask.ifas.ufl.edu/publication/AN362'),
 'uconnheat': ('UConn Extension — Heat Stress: Too Hot to Trot? (J. Nadeau; EXT132, June 2025)', 'https://extension.uconn.edu/?p=17076'),
})
HELD = {}
PAGES = [
 dict(slug='signs-of-heat-stress-in-horses', ids=[], urgent=True,
  q='What are the signs of heat stress in horses?',
  title='Signs of Heat Stress in Horses',
  meta='Heavy sweating, fast breathing, a high temperature, tiredness and poor coordination can signal heat stress. Call your vet right away if a horse stops sweating.',
  short='Extension sources list heavy sweating, fast heart and breathing rates, a raised temperature, droopy ears, tiredness, dehydration and reduced eating as signs of heat stress. A horse that stops sweating, breathes heavily, or becomes lethargic or uncoordinated needs your veterinarian right away.',
  body='''<h2>Signs listed by the sources</h2>
<ul>
<li><strong>University of Minnesota:</strong> rectal temperature above 103 F, faster heart and breathing rates, heavy sweating, droopy ears, tiredness, dehydration and reduced feed intake. A skin tent that lingers for several seconds suggests dehydration.</li>
<li><strong>University of Florida IFAS:</strong> fast, shallow breathing, body temperature above about 102 F, a heart rate above roughly 60 beats per minute, erratic behavior or an unsteady, stumbling gait, and heavy sweating.</li>
<li><strong>UConn Extension:</strong> muscle tremors, heavy sweating, collapse, dark urine, dull behavior, dark gums and slow capillary refill.</li>
</ul>
<p>The temperature thresholds differ between sources, and none replaces a veterinarian exam.</p>
<h2>Who is at higher risk</h2>
<p>The University of Minnesota lists older, overweight or out-of-shape horses, young foals, horses with long thick coats, horses that sweat poorly (anhidrosis), horses newly arrived from cooler or drier climates, and horses with Cushing disease.</p>
<h2>When to call</h2>
<p>The University of Minnesota says to call a veterinarian right away if you suspect heatstroke, or if a horse stops sweating, breathes heavily, or becomes lethargic, distressed or uncoordinated. See <a href="/qa/hot-weather/how-to-cool-an-overheated-horse/">how to cool an overheated horse</a> while you wait, and <a href="/qa/hot-weather/heat-exhaustion-heat-cramps-and-heatstroke-in-horses/">heatstroke</a>.</p>
<h2>What the sources do not cover</h2>
<p>They give no treatment protocols beyond cooling and veterinary care, and this page gives none.</p>''',
  src=['umnheat','ufheat','uconnheat'], rel=['how-to-cool-an-overheated-horse','heat-exhaustion-heat-cramps-and-heatstroke-in-horses','keeping-horses-cool-in-hot-weather']),

 dict(slug='how-to-cool-an-overheated-horse', ids=[], urgent=True,
  q='How do I cool down an overheated horse?',
  title='How to Cool Down an Overheated Horse',
  meta='Extension sources say stop work, move to shade, spray with cool water and use fans, and call your vet right away if you suspect heatstroke. No blankets.',
  short='Stop exercise, move the horse into shade with airflow, and spray the head, neck, back, rump and legs with a steady stream of cool water until the horse cools. Do not blanket the horse. Call your veterinarian right away if you suspect heatstroke; the horse may need intravenous fluids.',
  body='''<h2>Steps from the University of Minnesota</h2>
<ol>
<li>Stop exercise and move the horse out of the sun, using fans if available.</li>
<li>Spray the head, back, neck, rump and legs with a steady stream of cool water and keep going until the horse cools.</li>
<li>For a very hot horse (rectal temperature above 105 F), ice can be added to the water; avoid pouring ice water on the hindquarters and focus on the head, neck, back and ribs.</li>
<li>Do not put a blanket or sheet on the horse, since this blocks evaporation.</li>
</ol>
<h2>Other points</h2>
<ul>
<li>UConn Extension advises a few swallows of cool water every few minutes, calling a veterinarian because intravenous fluids may be needed, and walking a hot horse in moving air since still air prevents sweat evaporation. It says concerns that cold water shocks the horse are not supported by the research it cites.</li>
<li>University of Florida IFAS says continuous showering with tap water, or repeatedly scraping and re-wetting the coat with cool water, cooled horses fastest in one study. Showering keeps the horse standing, which prevents a post-exercise walk.</li>
</ul>
<h2>Call your veterinarian</h2>
<p>The University of Minnesota says to call right away if you suspect heatstroke. The sources do not say how long to keep cooling, so keep your veterinarian on the phone. See <a href="/qa/hot-weather/signs-of-heat-stress-in-horses/">signs of heat stress</a> and the <a href="/emergency/fever/">fever emergency guide</a>.</p>
<h2>What the sources do not cover</h2>
<p>Medications and veterinary treatment protocols for heatstroke are not covered.</p>''',
  src=['umnheat','uconnheat','ufheat'], rel=['signs-of-heat-stress-in-horses','heat-exhaustion-heat-cramps-and-heatstroke-in-horses','water-and-electrolytes-for-horses-in-hot-weather']),

 dict(slug='heat-exhaustion-heat-cramps-and-heatstroke-in-horses', ids=[], urgent=True,
  q='What is the difference between heat exhaustion, heat cramps and heatstroke in horses?',
  title='Heat Exhaustion, Heat Cramps and Heatstroke in Horses',
  meta='Extension sources separate heat exhaustion, heat cramps and heatstroke. Heatstroke is life threatening; call your vet immediately for collapse or no sweating.',
  short='UConn Extension separates overheating, heat exhaustion, heat cramps and heatstroke. Heatstroke is the most serious: sweating stops, the skin dries, and collapse or convulsions can follow, with death possible within hours without cooling and emergency veterinary care. Call your veterinarian immediately.',
  body='''<h2>UConn Extension descriptions</h2>
<ul>
<li><strong>Overheating:</strong> muscle tremors, heavy sweating, collapse, dark urine, dull behavior, dark gums and slow capillary refill.</li>
<li><strong>Heat exhaustion:</strong> body temperature, pulse and breathing rise well above normal.</li>
<li><strong>Heat cramps:</strong> seen in horses sweating heavily during hard work in intense heat and linked to electrolyte loss; signs include abdominal or leg spasms, muscle twitching and cramping.</li>
<li><strong>Heatstroke (sunstroke):</strong> the most serious form, with rapid breathing, weakness, incoordination and refusal to work. Sweating stops and the skin dries. Circulatory collapse, delirium and convulsions can follow, and death can occur within hours without cooling and emergency veterinary care.</li>
</ul>
<h2>University of Minnesota on heatstroke</h2>
<p>The University of Minnesota lists a rectal temperature above 106 F with heart and breathing rates that do not slow within 20 minutes of stopping exercise, plus distress, muscle weakness, poor coordination and collapse. Its own table lists a slightly different threshold, so do not rely on a single number.</p>
<h2>What to do</h2>
<p>Call your veterinarian immediately and start cooling; see <a href="/qa/hot-weather/how-to-cool-an-overheated-horse/">how to cool an overheated horse</a>. University of Minnesota and UConn both say heatstroke is an emergency.</p>
<h2>What the sources do not cover</h2>
<p>They do not describe veterinary treatment in detail. A horse cannot be diagnosed from this page.</p>''',
  src=['uconnheat','umnheat'], rel=['how-to-cool-an-overheated-horse','signs-of-heat-stress-in-horses','anhidrosis-in-horses-when-a-horse-stops-sweating']),

 dict(slug='anhidrosis-in-horses-when-a-horse-stops-sweating', ids=[], urgent=True,
  q='What is anhidrosis in horses, and what should I do if my horse stops sweating?',
  title='Anhidrosis in Horses: When a Horse Stops Sweating',
  meta='Anhidrosis is an inability to sweat that leaves a horse unable to cool itself. No proven treatment exists, so call your vet for a horse that stops sweating.',
  short='Anhidrosis is a temporary or permanent inability to sweat, so the horse cannot cool itself when its temperature rises. UF IFAS says severe cases can lead to collapse, seizures and death without prompt care, and that no treatment has met the standard for evidence-based medicine. Call your veterinarian.',
  body='''<h2>What it is</h2>
<p>University of Florida IFAS (Patterson-Rosa, Mallicote, MacKay, Brooks) describes anhidrosis as a temporary or permanent inability to sweat. It is poorly understood, and the underlying cause of the long-lasting form is unknown.</p>
<h2>Signs</h2>
<ul>
<li>Partial or complete loss of sweating, overheating, and fast breathing with flared nostrils.</li>
<li>Reduced appetite and water intake, hair loss on the chest, rump and face, a dull coat and depression.</li>
<li>Severe cases can lead to collapse, seizures and death without prompt care.</li>
</ul>
<h2>Risk factors listed</h2>
<p>Overtraining, electrolyte imbalance, dehydration, moving to a hotter climate without adjusting, sudden hot humid weather, certain medications, being a Thoroughbred or Warmblood, and a family history of the condition.</p>
<h2>Diagnosis and outlook</h2>
<p>Veterinarians can measure sweating capacity with a skin test. Acute, reversible cases may resolve within days or weeks once the trigger is removed. The long-lasting form does not improve with housing, diet or exercise changes, and many horses never regain normal sweating. The authors state no treatment has yet met the minimum standard for evidence-based medicine.</p>
<h2>Management listed</h2>
<p>Work horses in the cooler parts of the day, watch closely for overheating, let horses adjust gradually to a hot humid climate, provide shade, misters or fans, and hose horses down during the hottest hours. The University of Minnesota says to call a veterinarian right away if a horse stops sweating. See <a href="/qa/hot-weather/how-to-cool-an-overheated-horse/">how to cool an overheated horse</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page names no supplements or medications; the source gives none with proven benefit.</p>''',
  src=['ufanhid','umnheat','ufheat'], rel=['how-to-cool-an-overheated-horse','signs-of-heat-stress-in-horses','keeping-horses-cool-in-hot-weather']),

 dict(slug='keeping-horses-cool-in-hot-weather', ids=[], urgent=False,
  q='How do I keep my horse cool and prevent heat stress in hot weather?',
  title='Keeping Horses Cool in Hot Weather',
  meta='Shade, airflow, clean water, riding at cooler hours, a heat index check and gradual acclimation help prevent heat stress. Ask your vet about at-risk horses.',
  short='Extension sources recommend shade, fans for airflow, free access to clean water, riding in the coolest part of the day, hosing after work, haul in cooler hours with a ventilated trailer, and checking the heat index. Horses new to a hot climate need time to acclimate.',
  body='''<h2>Steps listed by the sources</h2>
<ul>
<li><strong>Shade and airflow:</strong> use shade from trees or buildings, remembering that shade shifts and buildings can block airflow; use fans, with misting fans cooling more effectively (University of Minnesota).</li>
<li><strong>Water:</strong> keep clean water available at all times and clean buckets and tanks more often in hot weather (University of Minnesota).</li>
<li><strong>Timing:</strong> ride early in the morning or late at night in hot, humid months and hose horses after work (University of Florida IFAS).</li>
<li><strong>Heat index:</strong> the University of Minnesota advises avoiding riding when air temperature in F plus relative humidity is over 150; US Equestrian guidance, as cited by the University of Florida, calls for close monitoring from 130 to 180 and rescheduling events above 180.</li>
<li><strong>Acclimation:</strong> horses can acclimate to hot, humid weather; the University of Minnesota says roughly 15 to 21 days helps horses moving to hot, humid areas.</li>
<li><strong>Coat and skin:</strong> UConn suggests clipping long coats and removing blankets from stabled horses in extreme heat; the University of Minnesota says masks can help protect light skin from sunburn.</li>
<li><strong>Hauling:</strong> haul in the coolest part of the day with a ventilated trailer and do not park in direct sun with horses inside (University of Minnesota; UConn).</li>
</ul>
<h2>Higher-risk horses</h2>
<p>Older, overweight, out-of-shape, long-coated, newly arrived and Cushing horses are listed as at higher risk (University of Minnesota). Ask your veterinarian about extra precautions. See <a href="/qa/hot-weather/signs-of-heat-stress-in-horses/">signs of heat stress</a>.</p>
<h2>What the sources do not cover</h2>
<p>They give no exact fan or misting-system specifications, so this page gives none.</p>''',
  src=['umnheat','ufheat','uconnheat'], rel=['signs-of-heat-stress-in-horses','water-and-electrolytes-for-horses-in-hot-weather','how-to-cool-an-overheated-horse']),

 dict(slug='water-and-electrolytes-for-horses-in-hot-weather', ids=[], urgent=False,
  q='How much water and what electrolytes do horses need in hot weather?',
  title='Water and Electrolytes for Horses in Hot Weather',
  meta='Extension sources advise unlimited clean water, loose salt and horse-formulated electrolytes only for heavy sweaters. Ask your vet about amounts for your horse.',
  short='Extension sources advise unlimited clean, cool water, frequent offers during work, free access to loose salt, and electrolytes for horses that sweat heavily, using only products made for horses. Heat can lower feed and water intake, so watch for dehydration. Ask your veterinarian about amounts.',
  body='''<h2>Water</h2>
<ul>
<li>Provide unlimited clean, cool water at all times and offer it frequently during work (University of Minnesota).</li>
<li>Heat can reduce feed and water intake, raising the risk of body condition loss and colic (University of Florida IFAS).</li>
<li>UConn says water needs rise sharply with temperature, and a hot horse can have a few swallows of cool water every few minutes.</li>
</ul>
<h2>Salt and electrolytes</h2>
<ul>
<li>Offer free access to loose salt, which the University of Minnesota prefers over a salt block.</li>
<li>Consider electrolytes for horses that sweat heavily; use only products formulated for horses, and offer plain water alongside them because some horses drink less when electrolytes are added (University of Minnesota).</li>
<li>UConn says sweat and urine carry electrolytes out, and losses can reduce thirst and appetite.</li>
</ul>
<h2>Checking hydration</h2>
<p>UConn describes a skin pinch test on the neck or shoulder, where skin that takes more than 1 to 2 seconds to recoil suggests dehydration. See <a href="/qa/exercise/signs-of-dehydration-in-horses/">signs of dehydration</a>.</p>
<h2>What the sources do not cover</h2>
<p>None of these sources gives amounts of water, salt or electrolytes, and this page gives none. Your veterinarian can advise for your horse and may use intravenous fluids if needed. See <a href="/qa/hot-weather/signs-of-heat-stress-in-horses/">signs of heat stress</a>.</p>''',
  src=['umnheat','ufheat','uconnheat'], rel=['signs-of-heat-stress-in-horses','keeping-horses-cool-in-hot-weather']),
]
