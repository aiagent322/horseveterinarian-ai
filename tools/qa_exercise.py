# -*- coding: utf-8 -*-
"""Exercise, tying-up, hydration, urinary Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'rutgerstie': ('Rutgers Cooperative Extension — Tying-Up in Horses (Fact Sheet FS1277)', 'https://esc.rutgers.edu/fact_sheet/5531/'),
 'pennvitals': ('Penn State Extension — How to Take Your Horse\'s Vital Signs', 'https://extension.psu.edu/how-to-take-your-horses-vital-signs'),
 'umnfirstaid': ('University of Minnesota Extension — Basic Horse First Aid and Preparing for Emergencies', 'https://extension.umn.edu/horse-health/basic-horse-first-aid-and-preparing-emergencies'),
 'msdurolith': ('MSD Veterinary Manual — Urolithiasis in Large Animals', 'https://www.msdvetmanual.com/urinary-system/noninfectious-diseases-of-the-urinary-system-in-large-animals/urolithiasis-in-large-animals'),
 'uflcallvet': ('University of Florida Large Animal Hospital — When It\'s Time to Call the Vet', 'https://largeanimal.vethospitals.ufl.edu/2025/09/10/when-its-time-to-call-the-vet/'),
 'horseulcer': ('The Horse — Gastric Ulcers: Maintaining Horses\' Stomach Health', 'https://thehorse.com/148363/gastric-ulcers-maintaining-horses-stomach-health/'),
})
HELD = {'VET-QA-0155': 'No verifiable source found for kidney-specific diet changes; the veterinary manual reviewed gives no water or kidney diet recommendations.'}
PAGES = [
 dict(slug='tying-up-immediate-steps-and-recovery', ids=['VET-QA-0152','VET-QA-0151'], urgent=True,
  q='What should I do if my horse is tying up, and what are signs of recovery?',
  title='Tying-Up in Horses: Immediate Steps and Recovery',
  meta='Stop work at once and call your vet; a stiff, painful hindquarter, heavy sweating or dark urine is an emergency. Return to work follows your vet\'s plan.',
  short='Stop the activity immediately and call your veterinarian. Rutgers treats tying-up as an emergency, especially with heavy sweating, reluctance to move or dark urine. Dry the horse, blanket if the weather calls for it, and let your vet direct treatment and any return to work.',
  body='''<h2>Signs</h2>
<ul>
<li>Onset often during or shortly after exercise; hindquarters become firm and painful and the gait short and stiff (Rutgers).</li>
<li>Heavy sweating, fast shallow breathing and a raised heart rate can mimic colic (Rutgers).</li>
<li>In severe cases urine turns dark brown or reddish from muscle protein breakdown that can harm the kidneys (Rutgers). UMN also lists brown urine and trouble moving the hindquarters as reasons to call right away.</li>
</ul>
<h2>Immediate steps: call your veterinarian</h2>
<ul>
<li>Stop the activity and have the horse evaluated right away (Rutgers).</li>
<li>Rutgers treats tying-up as a veterinary emergency, especially with profuse sweating, reluctance to move and dark urine; only mild recurrent cases may be handled by an experienced owner.</li>
<li>Encourage gentle movement and circulation without causing further damage; dry the horse off and blanket it if the weather calls for it (Rutgers).</li>
</ul>
<h2>Treatment and recovery</h2>
<p>Treatment generally focuses on hydration, electrolyte replacement, pain control and muscle relaxation, and vets typically recheck blood and urine markers of muscle damage over time (Rutgers). The fact sheet gives no return-to-work timeline or criteria; it says training should resume under veterinary guidance with exercise intensity and duration increased slowly. The sources reviewed give no list of recovery signs, so none are stated here. Ask your vet what to monitor. See <a href="/qa/exercise/preventing-tying-up-exercise-and-diet/">preventing tying-up</a> and the <a href="/emergency/colic-emergency/">colic emergency guide</a>.</p>''',
  src=['rutgerstie','umnfirstaid'], rel=['preventing-tying-up-exercise-and-diet','signs-a-horse-needs-urgent-veterinary-care','signs-of-dehydration-in-horses']),

 dict(slug='preventing-tying-up-exercise-and-diet', ids=['VET-QA-0147','VET-QA-0146','VET-QA-0148','VET-QA-0150'], urgent=False,
  q='How can exercise and diet changes help prevent tying-up, and what is long-term management?',
  title='Preventing Tying-Up: Exercise, Diet, Management',
  meta='Build fitness gradually, limit starch and sugar, manage stress and work with your vet and a nutritionist. Diagnosing the type of tying-up guides management.',
  short='Rutgers advises building fitness gradually, avoiding overexertion, reducing stress, feeding a balanced low-starch, low-sugar diet, and working with a veterinarian and nutritionist. Knowing which type of tying-up a horse has makes management easier. Do not change diet or exercise for a horse with a history without veterinary input.',
  body='''<p>All points here come from the Rutgers Cooperative Extension fact sheet unless noted.</p>
<h2>Exercise and training</h2>
<ul>
<li>Build fitness gradually and avoid overexertion, especially in horses with chronic episodes. Tying-up can be triggered by strenuous exercise in an unfit horse, stress or dietary imbalance.</li>
<li>Stressors such as trailering, separation from herd mates and an uncomfortable environment can trigger episodes; options include feeding an at-risk horse first and providing companionship when stabled alone.</li>
</ul>
<h2>Diet</h2>
<ul>
<li>A balanced, low-starch, low-sugar diet supports health; fat or low-carbohydrate fiber such as beet pulp or soy hulls can raise energy density.</li>
<li>Sodium, potassium and calcium are essential, especially for horses that sweat heavily.</li>
<li>Vitamin E is recommended for horses prone to tying-up because it supports muscle membrane integrity.</li>
<li>Starch and sugar limits differ by type (PSSM versus RER); ask your veterinarian or nutritionist for targets for your horse.</li>
</ul>
<h2>Long-term management</h2>
<p>Knowing whether a horse has RER, PSSM (type 1 or 2) or another form makes management easier, and genetic testing can identify the type 1 PSSM mutation. Work with a veterinarian and a professional nutritionist to tailor care. The fact sheet gives no daily exercise schedule, and none is listed here. See <a href="/qa/exercise/tying-up-immediate-steps-and-recovery/">immediate steps and recovery</a>.</p>''',
  src=['rutgerstie'], rel=['tying-up-immediate-steps-and-recovery','signs-of-dehydration-in-horses']),

 dict(slug='signs-a-horse-needs-urgent-veterinary-care', ids=['VET-QA-0149'], urgent=True,
  q='What signs indicate a horse needs urgent veterinary care?',
  title='Signs a Horse Needs Urgent Veterinary Care',
  meta='Call your vet right away for prolonged or severe colic, deep or bleeding wounds, nervous system signs, breathing trouble, eye injury, abnormal vital signs.',
  short='University of Minnesota Extension says to call your veterinarian right away for colic signs lasting more than 15 to 30 minutes, severe or heavily bleeding wounds, nervous system signs, urinary straining or brown urine, breathing trouble at rest, eye injury or sudden blindness, and vital signs outside normal ranges.',
  body='''<h2>Call right away (University of Minnesota Extension)</h2>
<ul>
<li><strong>Colic:</strong> signs lasting more than 15 to 30 minutes, severe signs, or signs that do not ease with walking.</li>
<li><strong>Wounds:</strong> deep, heavily bleeding, leaking clear sticky fluid, or over a joint; puncture wounds are always urgent.</li>
<li><strong>Lameness:</strong> not using a limb at all, toe dragging, near-falls or abnormal limb movement.</li>
<li><strong>Nervous system:</strong> unusual behavior, lasting muscle twitching, trouble walking, head tilt or seizures.</li>
<li><strong>Urinary:</strong> straining to urinate, trouble moving the hindquarters or brown urine.</li>
<li><strong>Breathing:</strong> noisy breathing or flared nostrils at rest, rapid breathing after injury or illness, bloody nasal discharge.</li>
<li><strong>Eyes:</strong> squinting, sudden blindness, or cuts in the eyelid.</li>
</ul>
<h2>Abnormal vital signs</h2>
<p>UMN says to call if temperature is over 101 F, heart rate over 50, respiratory rate over 30, gums dry, tacky or not pink, or capillary refill over 3 seconds. Learn your horse's normals before an emergency. UF adds seizures, collapse and a horse that cannot get up or move. See the <a href="/emergency/">emergency guides</a>.</p>''',
  src=['umnfirstaid','uflcallvet'], rel=['signs-of-dehydration-in-horses','tying-up-immediate-steps-and-recovery']),

 dict(slug='signs-of-dehydration-in-horses', ids=['VET-QA-0154'], urgent=False,
  q='What are common signs of dehydration in horses?',
  title='Signs of Dehydration in Horses',
  meta='Check gum moisture, capillary refill and the skin pinch test. Dry or tacky gums, slow refill or skin that stays tented mean you should call your vet.',
  short='Healthy gums are moist, smooth and pink, capillary refill takes about 1 to 2 seconds, and skin on the neck or shoulder returns flat within about 1 to 3 seconds. Slow skin return, dry or tacky gums or slow capillary refill point to dehydration or poor circulation, so call your veterinarian.',
  body='''<h2>Checks (Penn State Extension)</h2>
<ul>
<li><strong>Gums:</strong> moist, smooth and pink; pale or dark red gums are abnormal and a veterinarian should be contacted.</li>
<li><strong>Capillary refill:</strong> press a thumb on the gum until a white spot forms, release and time the pink return; about 1 to 2 seconds is normal and a slower return may point to poor circulation.</li>
<li><strong>Skin pliability:</strong> pinch a fold on the shoulder or neck and time how long it takes to flatten; about 1 to 3 seconds is normal, and more than 4 seconds suggests dehydration.</li>
</ul>
<p>Values are for healthy adults at rest; exercise raises them and your horse's own baseline matters most (Penn State).</p>
<h2>When to call</h2>
<p>UMN says to call if gums are dry, tacky or not pink or capillary refill is over 3 seconds. Firm mucus-covered manure may indicate dehydration, and extremely dry feces or none calls for a call (UMN). The sources reviewed give no treatment steps for dehydration at home; ask your veterinarian. See <a href="/qa/exercise/signs-a-horse-needs-urgent-veterinary-care/">urgent signs</a>.</p>''',
  src=['pennvitals','umnfirstaid'], rel=['signs-a-horse-needs-urgent-veterinary-care','tying-up-immediate-steps-and-recovery']),

 dict(slug='preventing-urinary-problems-in-horses', ids=['VET-QA-0153'], urgent=True,
  q='How can I prevent urinary issues in horses?',
  title='Urinary Stones in Horses: Signs and Prevention',
  meta='Urinary stones are uncommon in horses. Signs include painful or bloody urine; a blockage is an emergency. Prevention: balanced minerals, less alfalfa.',
  short='Urinary stones are much less common in horses than in ruminants. Signs include painful or frequent urination, blood in the urine and colic-like signs. Prevention advice centers on balancing mineral intake and restricting high-calcium feeds such as alfalfa. Straining to urinate or brown urine needs a veterinarian right away.',
  body='''<h2>Signs</h2>
<p>Painful or frequent urination, blood in the urine, urine scalding of the skin, dribbling in males, and colic-like signs such as sweating and restlessness (MSD Veterinary Manual). Call right away for straining to urinate or brown urine (UMN). A horse with an obstructing stone is in distress and needs immediate care (MSD).</p>
<h2>Prevention</h2>
<ul>
<li>Balance mineral intake from all feed and water sources.</li>
<li>Restrict high-calcium feeds such as alfalfa and other legumes.</li>
<li>Acidifying urine is hard in hay-fed horses, and long-term acidifying salts carry risks in athletic horses; this is a veterinary decision.</li>
<li>Long-term NSAID use may predispose horses to kidney stones (MSD); ask your vet about any long-term pain medication.</li>
</ul>
<p>The manual reviewed gives no water intake or water quality recommendations, so none are listed. See <a href="/qa/exercise/signs-a-horse-needs-urgent-veterinary-care/">urgent signs</a>.</p>''',
  src=['msdurolith','umnfirstaid'], rel=['signs-a-horse-needs-urgent-veterinary-care','signs-of-dehydration-in-horses']),

 dict(slug='exercise-and-routine-for-horses-with-ulcers', ids=['VET-QA-0145'], urgent=False,
  q='Are there specific exercises or routines to help manage a horse\'s ulcer condition?',
  title='Exercise and Routine for Horses with Ulcers',
  meta='More turnout, daily light exercise, continuous forage and less trailering stress can lower ulcer risk. Diagnosis and treatment come from your veterinarian.',
  short='The Horse recommends more turnout, regular daily exercise (even light work such as longeing or hacking), continuous access to forage and reducing travel stress. Diagnosis and treatment are for your veterinarian, and any diet change for an overweight or restricted horse needs veterinary approval.',
  body='''<h2>Routine changes (The Horse)</h2>
<ul>
<li><strong>Turnout and pasture:</strong> more time outside lets horses move freely and socialize, easing boredom and isolation.</li>
<li><strong>Daily exercise:</strong> regular work helps relieve stress, and light exercise such as longeing or hacking can make a difference.</li>
<li><strong>Forage:</strong> horses produce stomach acid almost constantly, so continuous access to hay or pasture is preferred over twice-daily grain with limited hay; slow-feeding tools may suit overweight horses, with veterinary approval.</li>
<li><strong>Travel:</strong> trailering can raise stress hormones and ulcer incidence; acclimate horses to the trailer, haul with compatible companions and provide hay.</li>
</ul>
<p>The article gives no guidance on when to exercise relative to feeding, and no exercise schedule. Ask your vet what suits a horse with ulcers. See <a href="/conditions/ulcers/">ulcers</a>.</p>''',
  src=['horseulcer'], rel=['signs-a-horse-needs-urgent-veterinary-care','preventing-tying-up-exercise-and-diet']),
]
