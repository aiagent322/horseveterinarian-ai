# -*- coding: utf-8 -*-
"""Winter / cold weather Q&A (source-first; no package records). Same rules as qa_colic.py. No feed amounts."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnwinter': ('University of Minnesota Extension — Caring for Your Horse in the Winter (M. DeBoer, A. Jaqueth, K. Martinson; C. Clanton, M. Hathaway, K. Martinson, C. Williams; reviewed 2022)', 'https://extension.umn.edu/horse-care-and-management/caring-your-horse-winter'),
 'psuwinter': ('Penn State Extension — Equine Winter Wellness Tips (O. Watson; updated Feb 20, 2024)', 'https://extension.psu.edu/equine-winter-wellness-tips'),
 'psublanket': ('Penn State Extension — When to Blanket a Horse (A. Swinker; updated May 4, 2026)', 'https://extension.psu.edu/when-to-blanket-a-horse'),
})
HELD = {}
PAGES = [
 dict(slug='do-horses-need-blankets-in-winter', ids=[], urgent=False,
  q='Does my horse need a blanket in winter?',
  title='Do Horses Need Blankets in Winter?',
  meta='Many horses with thick winter coats and shelter do not need blankets, but clipped, thin, old, young or wet horses may. Never blanket a wet horse.',
  short='Penn State Extension says horses with thick winter coats often do not need a blanket, and a dry sheltered area matters most. A blanket may be needed for clipped, very young, very old, thin or cold-unacclimated horses, or when a horse is likely to get wet. Never blanket a wet horse.',
  body='''<h2>When blanketing may be needed</h2>
<ul>
<li>Turnout has no shelter and temperature or wind chill falls to about 5 F or below (Penn State; University of Minnesota).</li>
<li>The horse is likely to get wet; rain, ice or freezing rain is a bigger concern than snow (Penn State).</li>
<li>The horse is clipped, very young or very old, or not acclimated to cold, such as one moved from a warmer region; Penn State says adapting can take about three weeks.</li>
<li>The horse has a body condition score of 3 or lower or is in poor health (Penn State; University of Minnesota).</li>
</ul>
<h2>When it may not be needed</h2>
<p>Penn State says horses with thick, woolly coats hold heat well and often do not need a blanket. The University of Minnesota says the natural winter coat keeps a horse warm, and that wet hair loses its insulating value, so keep the coat dry.</p>
<h2>Blanket care</h2>
<ul>
<li>Never blanket a wet horse, and remove a wet blanket promptly (Penn State; University of Minnesota).</li>
<li>Make sure the blanket fits; poor straps can cause rubs or sores (Penn State).</li>
<li>Remove blankets regularly to inspect the horse and readjust a twisted blanket (Penn State; University of Minnesota says daily).</li>
<li>Take the blanket off on warm days so the horse does not sweat under it (Penn State).</li>
</ul>
<h2>What the sources do not cover</h2>
<p>They do not recommend blanket weights or materials. See <a href="/qa/winter-care/signs-a-horse-is-too-cold/">signs a horse is too cold</a> and <a href="/qa/winter-care/winter-shelter-hoof-care-and-exercise-for-horses/">shelter</a>.</p>''',
  src=['psublanket','umnwinter','psuwinter'], rel=['signs-a-horse-is-too-cold','winter-shelter-hoof-care-and-exercise-for-horses','feeding-horses-in-cold-weather']),

 dict(slug='water-in-winter-and-impaction-colic-risk', ids=[], urgent=True,
  q='Why does my horse drink less in winter, and can that cause colic?',
  title='Water in Winter and Impaction Colic Risk',
  meta='Horses drink less in cold weather, and low water intake can lead to impaction colic. Keep water cool but unfrozen and call your vet for colic signs.',
  short='The University of Minnesota says winter horses need plenty of water, and that drinking too little leads to eating less and can cause impaction colic over days to weeks. Keep water between 45 and 65 F and unfrozen, and call your veterinarian for colic signs or a horse that stops eating.',
  body='''<h2>Why it matters</h2>
<p>The University of Minnesota says dry feed holds little moisture and winter pasture provides almost none, so horses need more drinking water. When horses drink too little, they eat less and can develop impaction colic; an impaction develops over days to weeks of poor intake, not in one day. Penn State agrees that reduced drinking raises impaction colic risk and that dry winter hay provides little water.</p>
<h2>What the sources advise</h2>
<ul>
<li>Keep water between 45 and 65 F (University of Minnesota; Penn State). In one study cited by Minnesota, ponies drank about 40 percent more when water stayed above freezing.</li>
<li>Check heated tanks for worn wiring or shock hazards and clean waterers regularly (University of Minnesota).</li>
<li>If there is no power, break ice on buckets at least twice daily (Penn State).</li>
<li>Do not count on snow as water; it carries risks including digestive problems and colic (University of Minnesota; Penn State).</li>
<li>Offer salt. Penn State advises against adding salt to water and suggests a salt block or plain salt in feed; the University of Minnesota says loose salt may be easier for horses to use in cold weather.</li>
</ul>
<h2>Call your veterinarian</h2>
<p>If a horse shows colic signs or stops eating, call your veterinarian. The sources used here do not list colic warning signs, so see the <a href="/emergency/colic-emergency/">colic emergency guide</a> and <a href="/qa/exercise/signs-of-dehydration-in-horses/">signs of dehydration</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page gives no electrolyte amounts. See <a href="/qa/winter-care/feeding-horses-in-cold-weather/">feeding in cold weather</a>.</p>''',
  src=['umnwinter','psuwinter'], rel=['feeding-horses-in-cold-weather','winter-shelter-hoof-care-and-exercise-for-horses']),

 dict(slug='feeding-horses-in-cold-weather', ids=[], urgent=False,
  q='How should I change my horse feeding in cold weather?',
  title='Feeding Horses in Cold Weather',
  meta='Extension sources say forage is the best source of extra winter energy because digestion makes heat. Check body condition by touch under thick coats.',
  short='The University of Minnesota says cold raises a horse energy needs and forage is the best source of extra energy, because fermenting fiber in the gut produces body heat; grain produces less. Thick winter coats can hide weight loss, so check body condition regularly by touch.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Cold raises energy needs, and the lowest temperature a horse can handle before needing extra heat (its lower critical temperature) depends on coat thickness, size, shelter and more (University of Minnesota; Penn State).</li>
<li>Forage is the best source of extra energy because fermentation in the gut produces heat; grain produces less (University of Minnesota).</li>
<li>Monitor body condition regularly, since thick winter coats can hide weight loss (University of Minnesota).</li>
<li>Thin horses, with a body condition score under 3 and possibly 4, lack fat reserves to generate heat and should be blanketed (Penn State).</li>
<li>Offer salt; loose salt may work better than blocks in cold weather (University of Minnesota).</li>
</ul>
<h2>Why water belongs in the plan</h2>
<p>Reduced drinking raises impaction colic risk. See <a href="/qa/winter-care/water-in-winter-and-impaction-colic-risk/">water in winter</a>.</p>
<h2>What the sources do not cover</h2>
<p>This page gives no hay or grain amounts, since needs vary with the horse and conditions. Ask your veterinarian or county extension office about amounts for your horse. Older or underweight horses may need extra attention; see <a href="/qa/senior-care/feeding-a-senior-horse/">feeding a senior horse</a>.</p>''',
  src=['umnwinter','psuwinter'], rel=['water-in-winter-and-impaction-colic-risk','do-horses-need-blankets-in-winter']),

 dict(slug='winter-shelter-hoof-care-and-exercise-for-horses', ids=[], urgent=False,
  q='What shelter, hoof care and exercise do horses need in winter?',
  title='Winter Shelter, Hoof Care and Exercise for Horses',
  meta='Extension sources advise wind and wet protection, good ventilation, daily hoof picking, traction care and keeping horses moving. Ask your vet or farrier.',
  short='Extension sources advise shelter from wind, sleet and storms, good barn ventilation, picking out hooves daily to remove packed snow, continued trimming, traction on icy ground, and keeping horses moving. Ask your veterinarian or farrier about your horse.',
  body='''<h2>Shelter and ventilation</h2>
<ul>
<li>Horses need protection from wind, sleet and storms; a stable, open-sided shed, or trees if no building is available, works (University of Minnesota). Horses with shelter tolerate much colder temperatures than those without.</li>
<li>Penn State lists a three-sided run-in shed, a barn or enclosed area, or a dense tree line as acceptable options.</li>
<li>Keep barns ventilated to limit dust, moisture, ammonia and mold, even in heated barns, and clean indoor stalls daily (Penn State; University of Minnesota on respiratory health).</li>
</ul>
<h2>Hooves</h2>
<p>The University of Minnesota says hooves grow more slowly in winter but trimming is still needed every 6 to 12 weeks, hooves should be picked out daily after heavy snow to remove packed ice or snowballs, barefoot horses generally have better traction, and shod horses may need snow pads or studs. See <a href="/qa/hoof/how-often-to-trim-or-shoe-a-horse/">how often to trim or shoe</a>.</p>
<h2>Exercise and footing</h2>
<ul>
<li>Keep horses moving as much as possible, since confinement can cause leg swelling; use caution in deep snow and on ice (University of Minnesota).</li>
<li>Use sand or a thin layer of wood ash or manure for traction, not a sand-and-salt mix (University of Minnesota).</li>
<li>A trace clip can shorten cool-down time, but clipped horses need extra feed, shelter and blanketing (University of Minnesota).</li>
</ul>
<h2>What the sources do not cover</h2>
<p>They do not say when to call a veterinarian about leg swelling or hoof problems. See <a href="/qa/hoof/signs-of-hoof-problems-and-when-to-call/">signs of hoof problems</a>.</p>''',
  src=['umnwinter','psuwinter'], rel=['do-horses-need-blankets-in-winter','signs-a-horse-is-too-cold']),

 dict(slug='signs-a-horse-is-too-cold', ids=[], urgent=False,
  q='How can I tell if my horse is too cold?',
  title='Signs a Horse Is Too Cold: Shivering and Coat',
  meta='Shivering is a clear sign a horse has reached its lower critical temperature. A wet or flat coat loses insulation. Add shelter and ask your vet if unsure.',
  short='Penn State Extension says shivering is a clear sign a horse has reached its lower critical temperature, the point where it must make extra heat. A fluffed coat is the natural warming response, so a wet or flat coat may leave the horse without that protection. Add shelter and ask your veterinarian if unsure.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Shivering suggests the horse has reached its lower critical temperature (Penn State).</li>
<li>A fluffed coat traps insulating air; a wet, muddy or flat coat reduces that protection, as do ice and strong wind (Penn State).</li>
<li>The lower critical temperature varies with climate, age, body condition, coat, shelter, blankets and health, and horses acclimated to cold have a lower one (Penn State).</li>
</ul>
<h2>What to do</h2>
<p>Provide a dry, sheltered area first; Penn State says this matters more than blanketing in cold wet weather. Consider a blanket for the horses listed on <a href="/qa/winter-care/do-horses-need-blankets-in-winter/">the blanketing page</a>, and never blanket a wet horse. Penn State says blankets are generally needed for thin, very young, old or sick horses.</p>
<h2>What the sources do not cover</h2>
<p>They give no temperature readings for a cold-stressed horse and no treatment. A horse that is shivering, weak or not eating should be seen by a veterinarian. See <a href="/qa/winter-care/winter-shelter-hoof-care-and-exercise-for-horses/">shelter</a>.</p>''',
  src=['psuwinter','psublanket'], rel=['do-horses-need-blankets-in-winter','winter-shelter-hoof-care-and-exercise-for-horses']),
]
