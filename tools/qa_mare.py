# -*- coding: utf-8 -*-
"""Mare, foaling and weaning Q&A (source-first; package records 0562-0568 used only as question prompts). Same rules as qa_colic.py. No doses."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnmare': ('University of Minnesota Extension — Caring for Your Mare During Breeding and Foaling', 'https://extension.umn.edu/horse-health/caring-your-mare-during-breeding-and-foaling'),
 'okfoal': ('Oklahoma State University Extension — Foaling Management and Care of the Nursing Foal (Fact Sheet ANSI-3985)', 'https://extension.okstate.edu/fact-sheets/foaling-management-and-care-of-the-nursing-foal'),
 'okbrood': ('Oklahoma State University Extension — Nutritional Considerations for Broodmares (D. Freeman, Fact Sheet ANSI-3975)', 'https://extension.okstate.edu/fact-sheets/nutritional-considerations-for-broodmares'),
 'okwean': ('Oklahoma State University Extension — Weaning and Management of Weanling Horses (D. Freeman, Fact Sheet ANSI-3978)', 'https://extension.okstate.edu/fact-sheets/weaning-and-management-of-weanling-horses'),
 'ugagest': ('University of Georgia Extension — Understanding Gestation in the Mare and the Potential for Problems (Bulletin 1461)', 'https://fieldreport.caes.uga.edu/publications/B1461/understanding-gestation-in-the-mare-and-the-potential-for-problems/'),
})
HELD = {}
PAGES = [
 dict(slug='how-to-prepare-for-your-mare-to-foal', ids=[], urgent=True,
  q='How should I prepare for my mare to foal?',
  title='How to Prepare for Your Mare to Foal',
  meta='Extension sources advise a clean, well-bedded foaling area, moving the mare early, washing and wrapping her tail, and having your vet number ready.',
  short='Extension sources advise a clean, sheltered, well-bedded foaling area, moving the mare there early, washing her and wrapping the tail as foaling nears, and keeping your veterinarian number, clean towels and a watch at hand. Call your veterinarian if anything seems wrong.',
  body='''<h2>The foaling area</h2>
<ul>
<li>Provide a sheltered area that protects against cold, wet weather; Oklahoma State advises at least 200 square feet and clean, large-particle bedding, because shavings can get into a foal nostrils (Oklahoma State).</li>
<li>The University of Minnesota says a grassy paddock or a well-bedded stall works, and clean straw is less likely than other bedding to be inhaled by the foal (Minnesota).</li>
<li>Clean and disinfect the area between foalings (Oklahoma State; Minnesota).</li>
</ul>
<h2>Getting the mare ready</h2>
<ul>
<li>Oklahoma State advises moving the mare to the foaling site about a month early and keeping her separate from other horses so she can adjust.</li>
<li>Accustom a maiden mare to having her udder handled a few weeks ahead (Minnesota).</li>
<li>Oklahoma State advises removing access to endophyte-infected fescue well before foaling, and having a Caslick procedure opened before she foals if she has one.</li>
<li>As foaling nears, wash the vulva, inner thighs and udder and wrap the tail (Minnesota; Oklahoma State).</li>
</ul>
<h2>Have on hand</h2>
<p>Minnesota lists phone numbers for your veterinarian and an experienced neighbor, a watch and notepad, clean towels, navel disinfectant, a bucket with soap and warm water, a trash bag for the placenta, and gloves.</p>
<h2>Plan for trouble</h2>
<p>Know when to call before labor starts. See <a href="/qa/mare-foaling/when-foaling-goes-wrong-red-bag-and-slow-labor/">when foaling goes wrong</a> and <a href="/qa/mare-foaling/signs-a-mare-is-about-to-foal/">signs a mare is about to foal</a>.</p>
<h2>What the sources do not cover</h2>
<p>They do not give a way to predict the hour of foaling. Many mares foal at night (Minnesota). Newborn care is on <a href="/qa/foal-care/what-to-expect-after-a-foal-is-born/">what to expect after a foal is born</a>.</p>''',
  src=['okfoal','umnmare'], rel=['signs-a-mare-is-about-to-foal','when-foaling-goes-wrong-red-bag-and-slow-labor','retained-placenta-in-mares']),

 dict(slug='signs-a-mare-is-about-to-foal', ids=[], urgent=False,
  q='What are the signs a mare is about to foal?',
  title='Signs a Mare Is About to Foal',
  meta='Udder enlargement, wax on the teats, a relaxed tailhead and restlessness point to foaling, but timing varies. Call your vet if milk leaks early.',
  short='Extension sources list an enlarging udder, a dropped belly, softening of the muscles around the tailhead, and waxy beads on the teats. Signs vary between mares and from one pregnancy to the next, so none of them gives an exact hour. Leaking a lot of milk well before term can signal a problem.',
  body='''<h2>Signs listed by extension sources</h2>
<ul>
<li>The belly drops and the udder enlarges, with fast growth in the last weeks (Minnesota; Oklahoma State).</li>
<li>The udder fills and colostrum is present shortly before birth; Minnesota says waxing, meaning dried milk beads on the teats, appears about a day before foaling, and some mares drip milk in the last hours.</li>
<li>The pelvic ligaments and the muscles around the tailhead soften and relax (Minnesota; Oklahoma State).</li>
<li>Oklahoma State says milk calcium rises shortly before foaling, and Minnesota says calcium testing of milk and foaling monitors can help estimate timing but neither is foolproof.</li>
</ul>
<h2>Variation</h2>
<p>Oklahoma State says not all signs appear in every mare and they change with later pregnancies. Maiden mares may show udder development inconsistently. Gestation length alone does not show readiness for birth; Oklahoma State notes gestations of 365 days are not entirely uncommon but a longer gestation may be a sign of foaling problems.</p>
<h2>Call your veterinarian</h2>
<p>Oklahoma State lists excessive milk leaking before birth as a reason to call, because it can signal a possible abortion. Also call for early labor behavior that makes no progress. See <a href="/qa/mare-foaling/when-foaling-goes-wrong-red-bag-and-slow-labor/">when foaling goes wrong</a>.</p>
<h2>What the sources do not cover</h2>
<p>They do not say how to confirm a due date for an individual mare. Ask your veterinarian about your mare.</p>''',
  src=['umnmare','okfoal'], rel=['how-to-prepare-for-your-mare-to-foal','when-foaling-goes-wrong-red-bag-and-slow-labor']),

 dict(slug='when-foaling-goes-wrong-red-bag-and-slow-labor', ids=[], urgent=True,
  q='What should I do if foaling stops progressing or a red bag appears?',
  title='When Foaling Goes Wrong: Red Bag and Slow Labor',
  meta='A red membrane at the vulva, no progress after the water breaks, or an abnormal foal position is an emergency. Call your veterinarian immediately.',
  short='Call your veterinarian immediately if a thick red membrane appears at the vulva, if there is no sign of progress soon after the water breaks, if only one foot or the nose appears first, or if the mare strains without progress. Extension sources advise calling early.',
  body='''<h2>Normal timing, per extension sources</h2>
<ul>
<li>Stage one: restlessness, sweating and colic-like behavior, ending when the water breaks. Oklahoma State says this usually lasts about 1 to 2 hours; Minnesota gives 1 to 6 hours and says it can go unnoticed.</li>
<li>Stage two: delivery. Oklahoma State says it usually takes 15 to 20 minutes after the water breaks, and Minnesota says the water bag should appear within about 10 minutes of the water breaking.</li>
<li>Stage three: the placenta. See <a href="/qa/mare-foaling/retained-placenta-in-mares/">retained placenta</a>.</li>
</ul>
<h2>Call your veterinarian immediately if</h2>
<ul>
<li>A thick red membrane appears instead of the white one (a red bag). Minnesota advises calling right away.</li>
<li>No amnion or foot appears within about 10 minutes of the water breaking, or progress stops for more than 10 minutes (Minnesota).</li>
<li>Delivery runs past 30 minutes (Oklahoma State).</li>
<li>Only one foot appears, the feet are upside down, the nose appears first or a foot is over the head (Minnesota); or the soles appear first, suggesting a backward or upside-down presentation (Oklahoma State).</li>
<li>Stage one lasts more than an hour or two without progress, or colic signs appear (Oklahoma State).</li>
<li>The mare colics after delivery (Minnesota).</li>
</ul>
<p>Minnesota says calling early is recommended. While you wait, if it is safe, wrap the tail, clean the vulva, and open the membranes if the foal is visible or a thick red sac is present. Follow your veterinarian instructions.</p>
<h2>What the sources do not cover</h2>
<p>They do not give hands-on steps for correcting a foal position. Leave that to your veterinarian. Do not pull early; Minnesota says early pulling can injure the birth canal. Foal care afterward is on <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>''',
  src=['umnmare','okfoal'], rel=['how-to-prepare-for-your-mare-to-foal','retained-placenta-in-mares','signs-a-mare-is-about-to-foal']),

 dict(slug='retained-placenta-in-mares', ids=[], urgent=True,
  q='What should I do if the mare has not passed her placenta after foaling?',
  title='Retained Placenta in Mares',
  meta='A placenta not passed within about 3 hours of foaling can lead to infection and laminitis. Save it for inspection and call your veterinarian.',
  short='Extension sources say a placenta not passed within about 3 hours of foaling is a concern because it can lead to serious infection and laminitis. Call your veterinarian, and keep the placenta once it passes so it can be checked for completeness.',
  body='''<h2>Timing</h2>
<p>Minnesota says the placenta should pass within about an hour after birth and advises calling the veterinarian if it has not passed within 3 hours. Oklahoma State says it is usually passed 1 to 3 hours after the foal is born and that a placenta still in place at 3 hours is a concern, since retention can lead to serious infection and laminitis.</p>
<h2>What to do</h2>
<ul>
<li>Call your veterinarian if the placenta has not passed by about 3 hours, or if the mare colics after foaling (Minnesota; Oklahoma State).</li>
<li>Save the placenta for inspection. Oklahoma State says a knowledgeable person should check that it is complete.</li>
<li>Leave any treatment to your veterinarian.</li>
</ul>
<h2>Why completeness matters</h2>
<p>Oklahoma State advises confirming the placenta was fully expelled. A piece left behind can go unnoticed, so ask your veterinarian to look at it even if the mare seems well.</p>
<h2>What the sources do not cover</h2>
<p>They do not describe veterinary treatment, and this page gives none. Laminitis can follow; see <a href="/conditions/laminitis/">laminitis</a>.</p>''',
  src=['umnmare','okfoal'], rel=['when-foaling-goes-wrong-red-bag-and-slow-labor','how-to-prepare-for-your-mare-to-foal']),

 dict(slug='pregnancy-checks-after-breeding-a-mare', ids=[], urgent=False,
  q='What pregnancy checks should I discuss with my vet after breeding a mare?',
  title='Pregnancy Checks After Breeding a Mare',
  meta='Veterinarians usually confirm pregnancy by ultrasound around 14 to 16 days after breeding, then recheck later. Ask your vet about timing for your mare.',
  short='Extension sources describe a first ultrasound around 14 to 16 days after breeding to confirm pregnancy and look for twins, sometimes a check for a heartbeat around day 24 to 25, and another exam around day 30 to 35. Your veterinarian sets the schedule for your mare.',
  body='''<h2>Checks described by Minnesota Extension</h2>
<ul>
<li>Days 14 to 16: first ultrasound to confirm pregnancy, correct any twins, and plan rebreeding if the mare is not pregnant.</li>
<li>Days 24 to 25: sometimes done to detect the embryonic heartbeat.</li>
<li>Days 30 to 35: second exam to confirm the pregnancy continues. Minnesota says a loss before this can be rebred, while a loss after day 35 typically leaves the mare infertile for several months.</li>
</ul>
<p>The University of Georgia says ultrasound is considered the gold standard for pregnancy diagnosis in the mare, is more reliable than palpation and works earlier. It gives about 14 days after ovulation or insemination as the earliest that most technicians will scan with great accuracy.</p>
<h2>Why check early</h2>
<p>Early checks let a non-pregnant mare return to the breeding program sooner and allow a veterinarian to deal with twins (Minnesota).</p>
<h2>Later risk</h2>
<p>Minnesota says abortion risk is higher after day 40 and that older mares face higher risk. Oklahoma State lists excessive milk leaking before birth as a reason to call.</p>
<h2>What the sources do not cover</h2>
<p>This page does not set a schedule for your mare. Ask your veterinarian which exams to book and when. See <a href="/qa/mare-foaling/signs-a-mare-is-about-to-foal/">signs a mare is about to foal</a> for late pregnancy.</p>''',
  src=['umnmare','ugagest'], rel=['signs-a-mare-is-about-to-foal','feeding-a-mare-in-late-pregnancy-and-lactation']),

 dict(slug='feeding-a-mare-in-late-pregnancy-and-lactation', ids=[], urgent=False,
  q='How should feeding be reviewed during late pregnancy and lactation?',
  title='Feeding a Mare in Late Pregnancy and Lactation',
  meta='Extension sources say mares should be in good condition before foaling because lactation sharply raises energy, protein and mineral needs.',
  short='Extension sources say a mare should be in good body condition before foaling, because lactation nearly doubles her energy needs and sharply raises protein and mineral needs. Needs rise in the last months of pregnancy, so review the ration with your veterinarian or extension office.',
  body='''<h2>Late pregnancy</h2>
<ul>
<li>Oklahoma State says mares should stay in fleshy condition because the stress of early lactation can make thin mares lose weight and rebreed less efficiently.</li>
<li>Energy needs rise above maintenance, protein needs increase modestly, and calcium and phosphorus needs increase (Oklahoma State).</li>
<li>Minnesota says that in the last trimester, protein, calcium, phosphorus and sugar needs rise faster than energy, so supplementation is usually needed, and forage alone often falls short on phosphorus and calcium.</li>
<li>Minnesota says natural vitamin E is typically given in the month before foaling to support antibody transfer to the foal; ask your veterinarian.</li>
</ul>
<h2>Lactation</h2>
<ul>
<li>Oklahoma State says energy needs nearly double, protein needs roughly double, and calcium and phosphorus needs double; thin mares take longer to rebreed.</li>
<li>Good-quality forage can reduce how much concentrate is needed (Oklahoma State).</li>
<li>Gaining weight while nursing is difficult and can lead to founder or colic, so condition should be right before foaling (Oklahoma State).</li>
<li>Minnesota says grain is reduced gradually before weaning as milk production declines.</li>
</ul>
<h2>What the sources do not cover</h2>
<p>This page gives no feed amounts, because they depend on the mare, her feed and her body condition. Overfeeding some vitamins can harm mare and fetus (Oklahoma State), so check supplements with your veterinarian. Weaning is on <a href="/qa/mare-foaling/weaning-a-foal/">weaning a foal</a>.</p>''',
  src=['okbrood','umnmare'], rel=['weaning-a-foal','pregnancy-checks-after-breeding-a-mare']),

 dict(slug='weaning-a-foal', ids=[], urgent=False,
  q='How can I plan weaning around a foal health and feeding needs?',
  title='Weaning a Foal: Timing, Methods and Care',
  meta='Most farms wean foals at 4 to 6 months. Foals eating grain well cope better, and gradual separation is less stressful than abrupt weaning.',
  short='Oklahoma State Extension says most farms wean foals between 4 and 6 months of age, earlier weaning raises stress, and a foal is ready when it eats grain well and relies less on its mare. Abrupt separation is the most stressful method. Plan vaccines and deworming with your veterinarian.',
  body='''<h2>Timing and readiness</h2>
<p>Oklahoma State says most farms wean between 4 and 6 months, weaning earlier raises stress especially if the foal is not eating grain, and waiting until about 6 months often produces a sturdier foal. Timing also depends on the mare health and temperament and the foal maturity.</p>
<h2>Before weaning</h2>
<ul>
<li>Offer grain early and use a creep feeder that admits only foals; check the feed daily and remove wet or moldy feed.</li>
<li>Teach foals to be handled, haltered and led beside the mare.</li>
</ul>
<h2>Methods described</h2>
<ul>
<li>Abrupt separation: the most stressful option, and foals should not be left completely isolated.</li>
<li>Progressive separation: adjoining pens so the pair can still see, hear and smell each other while nursing stops, then moving apart after about a week.</li>
<li>Group or familiar-environment weaning: foals stay in their familiar area with peers while the oldest mares are removed first.</li>
</ul>
<h2>After weaning</h2>
<ul>
<li>Watch foals closely for the first 12 to 24 hours and check that facilities have nothing that could trap a leg.</li>
<li>Stress can lead to cribbing and stomach problems; provide forage at all times and split grain into several smaller meals.</li>
<li>Monitor for excessive vocalizing, restlessness or loss of appetite, since stress can weaken immunity.</li>
<li>For the mare, reduce grain and increase exercise. If her udder stays tight for four days, or she runs a fever, have a veterinarian check for mastitis.</li>
</ul>
<h2>What the source does not cover</h2>
<p>It gives no single best method for every farm. Set vaccination and deworming with your veterinarian; see <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>''',
  src=['okwean'], rel=['feeding-a-mare-in-late-pregnancy-and-lactation','how-to-prepare-for-your-mare-to-foal']),
]
