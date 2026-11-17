# -*- coding: utf-8 -*-
"""Foal care Q&A (source-first; no package records). Same rules as qa_colic.py. No doses, no vitals."""
import qa_colic as C
S = dict(C.S)
S.update({
 'aaepneo': ('AAEP — Routine and Emergency Care of the Neonatal Foal (D. Zimmel, DVM; reviewed 2016; no publication date shown)', 'https://old.aaep.org/horsehealth/neonatal-care'),
 'extfoal': ('Extension Horses (eXtension) — Care of the Newborn Foal (Jan 31, 2020; no author listed)', 'https://horses.extension.org/care-of-the-newborn-foal/'),
 'aaepscour': ('AAEP — Foal Diarrhea (R. Dwyer, DVM, University of Kentucky; updated 2020)', 'https://old.aaep.org/horsehealth/foal-diarrhea'),
 'psufoal': ('Penn State Extension — When to Call the Equine Vet (L. Kenny with C. Meuse, VMD; updated Sept 19, 2025)', 'https://extension.psu.edu/when-to-call-the-equine-vet'),
 'merckfoalheat': ('Merck Veterinary Manual (professional version) — Foal Heat Diarrhea (A. Stewart; reviewed Oct 2022, modified Sept 2024)', 'https://www.merckvetmanual.com/digestive-system/intestinal-diseases-in-horses-and-foals/foal-heat-diarrhea'),
})
HELD = {}
PAGES = [
 dict(slug='what-to-expect-after-a-foal-is-born', ids=[], urgent=True,
  q='What should a newborn foal be doing in the first hours, and when do I call the vet?',
  title='What to Expect After a Foal Is Born: The 1-2-3 Rule',
  meta='A healthy foal stands within about 1 hour and nurses within about 2. Call your veterinarian if a milestone is missed. Every foal needs a vet exam in day one.',
  short='The AAEP 1-2-3 rule: a healthy foal stands within about 1 hour, nurses within about 2, and the mare passes the placenta within about 3. If a milestone is missed, call your veterinarian right away. Foals can decline fast, and every foal should get a vet exam in its first 12 to 24 hours.',
  body='''<h2>The 1-2-3 rule</h2>
<ul>
<li><strong>1 hour:</strong> the foal is standing.</li>
<li><strong>2 hours:</strong> the foal is nursing.</li>
<li><strong>3 hours:</strong> the mare has passed the placenta.</li>
</ul>
<p>The AAEP (D. Zimmel, DVM) says to call the veterinarian if a foal misses these milestones, because foals that do not stand and nurse promptly can become hypoglycemic and are at risk of sepsis. Extension Horses gives similar but slightly different timings: standing within about an hour, a first nursing within about an hour, and first steps and a first nap within the first two hours. Treat all of these as approximate and call early.</p>
<h2>What to leave alone</h2>
<ul>
<li>Let the foal stand on its own. Extension Horses says lifting it too early can strain tendons and ligaments and interfere with bonding.</li>
<li>Do not guide the foal to the udder unless it has not nursed by about two hours or the mare rejects it.</li>
<li>Do not cut the umbilical cord right away; see <a href="/qa/foal-care/newborn-foal-umbilical-cord-care/">umbilical cord care</a>.</li>
</ul>
<h2>Vet exam</h2>
<p>The AAEP says all foals should get a full physical exam from a veterinarian within the first 12 to 24 hours of life.</p>
<h2>Call right away during foaling if</h2>
<p>The AAEP lists: the foal is not delivered within 20 to 30 minutes after the water breaks, a red velvet sac appears, or the foal is in an abnormal position.</p>
<h2>What the sources do not cover</h2>
<p>These pages do not give resuscitation steps or normal vital sign ranges, and this page does not either. See <a href="/qa/foal-care/why-colostrum-matters-for-newborn-foals/">colostrum</a> and <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>''',
  src=['aaepneo','extfoal'], rel=['why-colostrum-matters-for-newborn-foals','signs-of-a-sick-foal','newborn-foal-umbilical-cord-care']),

 dict(slug='why-colostrum-matters-for-newborn-foals', ids=[], urgent=True,
  q='Why is colostrum important for a newborn foal?',
  title='Why Colostrum Matters for Newborn Foals',
  meta='Foals get no antibodies before birth, so colostrum is their protection. A vet can test antibody levels. Call your veterinarian if the foal is not nursing.',
  short='Foals receive no antibodies across the placenta, so colostrum, the mare first milk, is their protection. A veterinarian can run a blood test to check how much antibody the foal absorbed. If a foal is not nursing, or you suspect a blood-group mismatch, call your veterinarian.',
  body='''<h2>Why it matters</h2>
<p>The AAEP says foals receive no antibodies across the placenta, so their protection comes from colostrum. The foal absorbs antibodies for a limited time. Extension Horses says that window shrinks sharply after about 12 hours, and the AAEP foal diarrhea article says absorption is best in the first 18 hours.</p>
<h2>Checking that it worked</h2>
<p>A veterinarian can measure the foal IgG level with a blood test. The sources give different timing: 8 to 24 hours (AAEP neonatal care), 12 to 18 hours (AAEP foal diarrhea) and around 6 hours (Extension Horses). Ask your veterinarian when to test. The sources reviewed do not give a cutoff value, so this page does not either.</p>
<h2>Blood-group mismatch (neonatal isoerythrolysis)</h2>
<p>The AAEP says antibodies in the mare colostrum can attack the foal red blood cells, causing hemolytic anemia. Signs include yellow mucous membranes, anemia, exercise intolerance and orange or red urine. The AAEP says the mare can be screened about two weeks before foaling, and if she is positive the foal must not get her colostrum or nurse from her for the first 24 hours; it needs antibody-free colostrum from another source. Extension Horses says to prevent colostrum intake if this is suspected until a veterinarian can test. Call your veterinarian immediately.</p>
<h2>What the sources do not cover</h2>
<p>Amounts to feed, tube feeding and colostrum products are not covered here. Your veterinarian directs these. See <a href="/qa/foal-care/what-to-expect-after-a-foal-is-born/">what to expect after birth</a> and <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>''',
  src=['aaepneo','extfoal','aaepscour'], rel=['what-to-expect-after-a-foal-is-born','signs-of-a-sick-foal']),

 dict(slug='signs-of-a-sick-foal', ids=[], urgent=True,
  q='What are the signs of a sick foal, and when should I call the vet?',
  title='Signs of a Sick Foal and When to Call the Vet',
  meta='Any change in a young foal means calling your veterinarian: not nursing, weakness, diarrhea, rapid breathing, abnormal gums. Do not medicate first.',
  short='Penn State Extension says any change in a young foal requires a call to the veterinarian. Warning signs include not nursing, weakness, diarrhea, rapid breathing, red or yellow gums, swollen joints or navel, and milk from the nose. Do not give medication before talking to your veterinarian.',
  body='''<h2>Call your veterinarian for</h2>
<p>Penn State Extension (L. Kenny with C. Meuse, VMD) says foals have immature immune systems and cannot fight infection as well as adults, so any change in a young foal warrants a call. It lists subtle shifts in nursing or activity, coughing, diarrhea, lameness, lethargy, pale, red or yellow gums or eyes, and swollen or sore joints or navel.</p>
<p>The AAEP neonatal care article adds:</p>
<ul>
<li>milk from the nose or on the face, or orange fluid from the nose</li>
<li>wandering or lack of bonding with the mare</li>
<li>sunken eyes or tearing</li>
<li>weak pasterns, or joint or tendon problems</li>
<li>rapid breathing, bloat or colic</li>
<li>weakness, lethargy or inability to stand</li>
</ul>
<p>The AAEP foal diarrhea article says a full udder on the mare can signal that the foal is not nursing well and is often the first sign of illness; it advises checking the udder twice daily.</p>
<h2>What not to do</h2>
<p>Penn State says not to give medications without first consulting a veterinarian. Extension Horses also says to call if the foal has urine dripping from the navel, limb deformities, a hernia or inward-turned eyelids.</p>
<h2>What the sources do not cover</h2>
<p>These sources give no home treatment and no normal temperature or heart rate ranges, so this page gives none. A foal cannot be assessed from a web page. See <a href="/qa/foal-care/foal-diarrhea-and-foal-heat/">foal diarrhea</a> and <a href="/qa/foal-care/what-to-expect-after-a-foal-is-born/">the 1-2-3 rule</a>.</p>''',
  src=['psufoal','aaepneo','aaepscour','extfoal'], rel=['foal-diarrhea-and-foal-heat','what-to-expect-after-a-foal-is-born','why-colostrum-matters-for-newborn-foals']),

 dict(slug='foal-diarrhea-and-foal-heat', ids=[], urgent=True,
  q='Is diarrhea normal in a foal, and what is foal heat diarrhea?',
  title='Foal Diarrhea and Foal Heat: When to Call the Vet',
  meta='Foal heat diarrhea is mild and appears in the first weeks, but foals under 30 days old with diarrhea need prompt vet care because they dehydrate fast.',
  short='Foal heat diarrhea is a mild, self-limiting diarrhea in an otherwise bright, nursing foal in its first weeks. But the AAEP says foals under 30 days old with diarrhea need prompt veterinary evaluation because they can become dangerously dehydrated within hours. Call your veterinarian.',
  body='''<h2>Foal heat diarrhea</h2>
<p>The Merck Veterinary Manual describes a mild, self-limiting diarrhea from about 4 to 14 days after birth in which the foal stays active and alert with a normal appetite and vital signs. The AAEP puts it at about 7 to 12 days. Merck says the cause is unknown and may involve changes in gut bacteria or diet as the foal starts eating hay and grain; the name comes from the mare first heat, but orphan foals get it too.</p>
<h2>When it is not foal heat</h2>
<p>The AAEP (R. Dwyer, DVM) says diarrhea can come from viruses, bacteria, parasites or non-infectious triggers, and that the exact cause is hard to pinpoint. Foals under 30 days old with diarrhea need prompt veterinary evaluation. Young foals have short intestines that reabsorb less fluid, so they dehydrate quickly. Older foals with severe diarrhea also need immediate care. Extension Horses says to call if diarrhea appears in a newborn, or if an older foal with scours stops nursing or becomes weak or dehydrated.</p>
<h2>What not to do</h2>
<p>The AAEP says to leave treatment decisions to your veterinarian rather than starting antibiotics yourself, since they can disrupt the foal beneficial gut bacteria. Foals with infectious diarrhea should be kept away from other foals.</p>
<h2>Prevention listed by the AAEP</h2>
<p>Keep the foaling area clean and draft-free, remove manure promptly, do not spread manure on pastures, isolate new horses for at least two weeks, and move pregnant mares four to six weeks before foaling so they build local antibodies. Ask your veterinarian about mare vaccination where rotavirus is a concern.</p>
<h2>What the sources do not cover</h2>
<p>Treatments, fluids and tests are not covered here. See <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>''',
  src=['merckfoalheat','aaepscour','extfoal'], rel=['signs-of-a-sick-foal','why-colostrum-matters-for-newborn-foals']),

 dict(slug='newborn-foal-umbilical-cord-care', ids=[], urgent=False,
  q='How do I care for a newborn foal umbilical cord?',
  title='Newborn Foal Umbilical Cord Care',
  meta='Sources advise leaving the cord alone, using only a diluted antiseptic and checking the navel daily. Call your vet for pus, swelling, bleeding or urine drip.',
  short='The AAEP says to leave the cord intact as long as possible so the mare can break it, avoid full-strength iodine, which can scald skin, and check the navel daily for pus, swelling, bleeding or leaking urine. Call your veterinarian if you see any of these.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Leave the cord intact as long as possible so the mare can break it when she stands, which allows maximal blood transfer (AAEP). Extension Horses likewise says not to cut it right away because the foal may still be receiving blood from the placenta.</li>
<li>If it must be broken, the AAEP says to pull it apart near the abdomen rather than cutting it.</li>
<li>Use a diluted antiseptic rather than full-strength iodine, which can scald the skin (AAEP). Ask your veterinarian which product and dilution to use; this page names none.</li>
<li>Check the navel daily for pus, swelling, bleeding or urine leakage (AAEP).</li>
</ul>
<h2>Call your veterinarian if</h2>
<p>You see pus, swelling, bleeding or urine dripping from the navel. Extension Horses says dripping urine may indicate a persistent urachus. Penn State Extension lists a swollen or sore navel as a sign a foal needs a veterinary call. See <a href="/qa/foal-care/signs-of-a-sick-foal/">signs of a sick foal</a>.</p>
<h2>What the sources do not cover</h2>
<p>Treatment of navel infection or persistent urachus is not covered. See <a href="/qa/foal-care/what-to-expect-after-a-foal-is-born/">what to expect after birth</a>.</p>''',
  src=['aaepneo','extfoal','psufoal'], rel=['signs-of-a-sick-foal','what-to-expect-after-a-foal-is-born']),
]
