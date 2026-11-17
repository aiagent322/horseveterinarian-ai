# -*- coding: utf-8 -*-
"""Wounds and trauma Q&A (wounds, proud flesh, shock). Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'acvswound': ('American College of Veterinary Surgeons — General Wound Management in Horses', 'https://www.acvs.org/large-animal/general-wound-management'),
 'equusinfect': ('EQUUS — 6 signs that your horse\'s wound is infected', 'https://equusmagazine.com/injuries-and-first-aid/six-signs-of-infection'),
 'equusfirstaid': ('EQUUS — First Aid for Horse Wounds', 'https://equusmagazine.com/horse-care/first_aid_wounds_021110-8370'),
 'tamuwound': ('Texas A&M Veterinary Medicine — Topical Wound Care for Horses', 'https://vetmed.tamu.edu/news/pet-talk/topical-wound-care-for-horses/'),
 'equimedwound': ('EquiMed — Horse wound treatment', 'https://equimed.com/health-centers/first-aid/articles/horse-wound-treatment'),
 'aaepproud': ('AAEP — Understanding Proud Flesh', 'https://old.aaep.org/horsehealth/understanding-proud-flesh'),
 'smegt': ('Stable Management (University of Minnesota veterinary student author) — Prevention of Exuberant Granulation Tissue', 'https://stablemanagement.com/articles/prevention-exuberant-granulation-tissue-proud-flesh-30490/'),
 'equimedshock': ('EquiMed — Horse First Aid for Shock', 'https://equimed.com/health-centers/first-aid/articles/horse-first-aid-for-shock'),
 'hcshock': ('Horse Canada — Shock: when the body shuts down (October 2014)', 'https://horse-canada.com/magazine/health/shock-when-the-body-shuts-down/'),
})
HELD = {}
PAGES = [
 dict(slug='when-to-call-the-vet-for-a-horse-wound', ids=['VET-QA-0492'], urgent=True,
  q='When should I call a vet for a horse wound?',
  title='When to Call the Vet for a Horse Wound',
  meta='Call right away for heavy or spurting bleeding, wounds near a joint or tendon, punctures, lameness, a lodged object or signs of shock. Have any wound checked.',
  short='Call your veterinarian right away for heavy or spurting bleeding, a puncture, a wound over a joint or tendon, lameness, an object still lodged, or leaking yellowish fluid. ACVS says to have any wound checked, since a small puncture can be more dangerous than a large shallow cut.',
  body='''<h2>Call right away</h2>
<ul>
<li>Heavy bleeding; bright red blood that spurts with the heartbeat may mean a cut artery and pressure alone may not stop it (EquiMed; EQUUS).</li>
<li>Clear or yellowish fluid leaking from a deep cut or puncture near a joint or tendon (EQUUS). Wounds over a joint, tendon sheath or bursa need prompt veterinary care (EquiMed; Texas A&amp;M).</li>
<li>Puncture wounds, which are considered the most serious, especially in the foot (EquiMed).</li>
<li>Severe lameness, visible distortion of the area, or an object still lodged in the wound (EQUUS).</li>
<li>A full-thickness wound or one reaching bone, joints, tendons, vessels or nerves; significant dirt or debris; or reluctance to bear weight (ACVS).</li>
<li>Signs of shock even with a minor wound: irregular breathing, weak pulse, vacant look, cold ears and feet (EQUUS).</li>
<li>Wounds that pull apart when the horse moves, or leg wounds below the knee (Texas A&amp;M).</li>
</ul>
<h2>Have it checked</h2>
<p>ACVS advises having any wound checked, since a small puncture can be more dangerous than a large shallow cut. While waiting, apply a pressure bandage or press directly on the wound and keep pressure on until the vet arrives (EQUUS). Check tetanus status; Texas A&amp;M says tetanus is always a risk. See the <a href="/emergency/wound-care/">wound care emergency guide</a> and <a href="/emergency/lacerations/">lacerations guide</a>.</p>''',
  src=['acvswound','equusfirstaid','equimedwound','tamuwound'], rel=['wound-care-and-infection-prevention','signs-of-wound-infection','shock-causes-signs-and-first-aid']),

 dict(slug='wound-care-and-infection-prevention', ids=['VET-QA-0486','VET-QA-0484'], urgent=True,
  q='What are the best practices for wound care and for preventing infection in horse wounds?',
  title='Horse Wound Care and Preventing Infection',
  meta='Control bleeding with pressure, rinse with saline, watch daily for infection and keep tetanus current. Call your vet for deep, puncture or joint-area wounds.',
  short='Control bleeding with firm pressure, then rinse the wound gently with water or saline and check it daily for infection. Deep, dirty, puncture or joint-area wounds need a veterinarian. Keep tetanus vaccination current. Healing cells need some moisture, so drying a wound out is not the goal.',
  body='''<h2>First aid and cleaning</h2>
<ul>
<li>Control bleeding with a pressure bandage or direct pressure, using clean material, and keep pressure until the vet arrives (EQUUS). ACVS describes pressing an absorbent pad over the area and covering it with an elastic wrap.</li>
<li>Rinse with tap water or saline; saline can be made by dissolving two tablespoons of table salt in a gallon of distilled water (EQUUS; Texas A&amp;M). Use gentle pressure; this removes about 80 percent of contaminants (EQUUS).</li>
<li>Remove embedded debris and keep anything you pull out for the vet; do not remove objects from the eye or torso (EQUUS).</li>
<li>Very dirty wounds may need an iodine-based antimicrobial wash (Texas A&amp;M).</li>
</ul>
<h2>Preventing infection</h2>
<ul>
<li>Healing cells need some moisture, so drying out oozing is not the goal; an antibiotic topical ointment can add moisture if needed (Texas A&amp;M). EQUUS describes applying an over-the-counter antibiotic ointment to shallow wounds until a scab forms. Ask your vet which product suits the wound.</li>
<li>Deep or dirty wounds may need a systemic antibiotic from the vet (EQUUS).</li>
<li>Check the wound daily for the first few days for gray or greenish tissue, a foul smell or heavy drainage (EQUUS). See <a href="/qa/wounds/signs-of-wound-infection/">signs of wound infection</a>.</li>
<li>Leg wounds may need a bandage to limit dirt contamination and skin movement; some cuts and abrasions do not (Texas A&amp;M).</li>
<li>Keep tetanus vaccinations current (Texas A&amp;M); the vet can give a booster if needed (EQUUS).</li>
</ul>
<p>The sources reviewed give no bandage-change schedule or doses. See <a href="/qa/wounds/when-to-call-the-vet-for-a-horse-wound/">when to call the vet</a>.</p>''',
  src=['equusfirstaid','acvswound','tamuwound'], rel=['when-to-call-the-vet-for-a-horse-wound','signs-of-wound-infection','proud-flesh-causes-and-prevention']),

 dict(slug='signs-of-wound-infection', ids=['VET-QA-0485'], urgent=True,
  q='What are the signs of wound infection in horses?',
  title='Signs of Wound Infection in Horses',
  meta='Warning signs are heat, swelling that worsens or returns, foul odor, spreading redness, green or yellow discharge and rising tenderness. Call your vet.',
  short='EQUUS lists six signs of an infected wound: heat, swelling that worsens or returns, a foul or sweet odor, redness or red streaks, bright green or yellow discharge, and tenderness that grows or spreads. Call your veterinarian if you see any of them.',
  body='''<h2>Six signs (EQUUS)</h2>
<ul>
<li><strong>Heat:</strong> the wound and surrounding skin feel unusually warm; compare with the same spot on the other side.</li>
<li><strong>Swelling:</strong> swelling that worsens or returns after going down. Swelling in the first hours is normal.</li>
<li><strong>Odor:</strong> a foul or sharp smell, especially a sickly-sweet one.</li>
<li><strong>Color:</strong> redness around the wound, particularly red streaks spreading outward; it is harder to see on dark skin.</li>
<li><strong>Discharge:</strong> clear or creamy is typical; bright green or yellow suggests infection.</li>
<li><strong>Tenderness:</strong> more sensitive to touch than before, or soreness spreading to nearby tissue.</li>
</ul>
<p><strong>Call your veterinarian</strong> if you notice any of these. Also check daily for gray or greenish tissue and heavy drainage in the first few days (EQUUS first aid article). ACVS lists swelling and heat as warning signs and notes fever and discharge are not covered; wounds involving a joint or tendon carry risks of hard-to-treat infection, arthritis and lasting lameness. See <a href="/qa/wounds/wound-care-and-infection-prevention/">wound care and infection prevention</a>.</p>''',
  src=['equusinfect','equusfirstaid','acvswound'], rel=['wound-care-and-infection-prevention','when-to-call-the-vet-for-a-horse-wound','proud-flesh-causes-and-prevention']),

 dict(slug='proud-flesh-causes-and-prevention', ids=['VET-QA-0481','VET-QA-0482'], urgent=False,
  q='What causes proud flesh in horses and how can it be prevented?',
  title='Proud Flesh in Horses: Causes and Prevention',
  meta='Proud flesh is excess granulation tissue, common on lower-leg wounds. Prevention centers on early veterinary care, saline flushing, rest and bandage management.',
  short='Proud flesh (exuberant granulation tissue) is overgrown healing tissue, most common on wounds below the knee or hock where skin moves a lot. Prevention centers on prompt vet examination, thorough cleaning, flushing with saline, resting the limb and careful bandage management.',
  body='''<h2>What it is and why it forms</h2>
<ul>
<li>It is an overgrowth of granulation tissue: pink, bumpy, blood-vessel rich and without nerve endings (AAEP).</li>
<li>More common on wounds below the knee or hock or over joints where skin moves a lot (ACVS); distal limbs have high tissue tension and constant motion (AAEP).</li>
<li>Chronic inflammation, low oxygen in the wound, bone fragments, foreign material and ongoing movement can keep it going (Stable Management).</li>
<li>Too much moisture encourages it (Texas A&amp;M).</li>
</ul>
<h2>Prevention</h2>
<ul>
<li>Have a vet examine the wound and remove foreign material, bone fragments and dead tissue; flush promptly, preferably with a balanced saline solution (AAEP).</li>
<li>Let the vet choose the dressing and bandage; rest the limb (AAEP).</li>
<li>Bandage management is the main focus: bandages can create a low-oxygen, moist environment that favors granulation tissue, so the article advises avoiding bandages on wounds healing by second intention when possible and removing one once a good granulation bed forms (Stable Management).</li>
<li>Avoid most topical agents, since many increase inflammation or damage new skin cells (Stable Management). "Preventing EGT is easier than treating it."</li>
</ul>
<p>Sources conflict somewhat on bandaging (Texas A&amp;M says light pressure can limit excess tissue). Follow your vet's plan for the specific wound. Call your vet for deep wounds, wounds over joints or tendons, or any sign of proud flesh (AAEP). See <a href="/qa/wounds/proud-flesh-treatment-and-products/">treatment and products</a>.</p>''',
  src=['aaepproud','acvswound','smegt','tamuwound'], rel=['proud-flesh-treatment-and-products','wound-care-and-infection-prevention','when-to-call-the-vet-for-a-horse-wound']),

 dict(slug='proud-flesh-treatment-and-products', ids=['VET-QA-0487','VET-QA-0479'], urgent=False,
  q='What are the treatment options and product types for proud flesh?',
  title='Proud Flesh Treatment Options and Product Types',
  meta='A vet may trim proud flesh level with the wound edge, use topical steroids or silicone dressings, or graft large wounds. Ask your vet before using any product.',
  short='Excess granulation tissue calls for veterinary care. Options include trimming it level with the wound edge (painless, but it bleeds), topical steroids to reduce inflammation, silicone-containing dressings, and skin grafts for very large wounds. Ask your vet before using any proud flesh product.',
  body='''<h2>Treatment options (veterinary)</h2>
<ul>
<li>Check for lingering infection or inflammation (AAEP).</li>
<li>Topical steroids can reduce inflammation and limit excess granulation tissue; one or two applications may be enough, and prolonged use can interfere with healing (AAEP; Stable Management).</li>
<li>Trimming (surgical debridement) is needed when proud flesh rises above the surrounding skin, because skin cannot grow over it; trimming bleeds but is painless, and a temporary bandage may be needed for the first few hours (AAEP; Stable Management).</li>
<li>Very large wounds may need skin grafts, usually with a surgeon (AAEP).</li>
</ul>
<h2>Product types</h2>
<ul>
<li>Over-the-counter products are marketed as proud flesh preventives; ask your vet which suits your situation (AAEP).</li>
<li>Medical-grade honey dressings are described as antibacterial and moisture-keeping and appear effective, but no clinical data is given (AAEP).</li>
<li>Silicone-containing dressings reduce the likelihood of excess granulation tissue and can be used long term with fewer side effects than corticosteroids (Stable Management).</li>
</ul>
<p>The sources give no brand names or doses, and none are listed here. Excessive granulation tissue calls for veterinary care (Texas A&amp;M). See <a href="/qa/wounds/proud-flesh-causes-and-prevention/">causes and prevention</a>.</p>''',
  src=['aaepproud','smegt','tamuwound'], rel=['proud-flesh-causes-and-prevention','wound-care-and-infection-prevention','when-to-call-the-vet-for-a-horse-wound']),

 dict(slug='shock-causes-signs-and-first-aid', ids=['VET-QA-0488','VET-QA-0489','VET-QA-0483'], urgent=True,
  q='What causes shock in horses, what are the immediate steps and how can it be prevented?',
  title='Shock in Horses: Causes, Signs and First Aid',
  meta='Shock follows major blood or fluid loss, severe infection, colic or trauma. Call your vet immediately, keep the horse calm and loosely covered.',
  short='Shock follows major blood or fluid loss, severe infection, colic, heat stroke, poisoning or major trauma. Signs include a weak, fast pulse, shallow breathing, pale gums and cold limbs. Call your veterinarian immediately, keep the horse calm and loosely covered, and control any bleeding.',
  body='''<h2>Causes (EquiMed; Horse Canada)</h2>
<ul>
<li>Hypovolemic: heavy bleeding or fluid loss such as severe diarrhea or dehydration.</li>
<li>Septic (toxic): severe infection releasing bacteria and endotoxins into the bloodstream.</li>
<li>Also heart problems, nervous system damage from severe trauma, and severe allergic reaction.</li>
<li>Common triggers named: injury, colic, extreme fear, blood loss, dehydration, heavy sweating, heat stroke, snakebite and poisoning.</li>
</ul>
<h2>Signs</h2>
<p>A quiet or depressed horse with pale or slightly purple gums, shivering, cold limbs, profuse sweating, a rapid weak pulse, shallow rapid breathing, and anxiety or confusion; most stay standing, severe cases may collapse (Horse Canada). EQUUS adds a vacant look and cold ears and feet, and says to look for shock even with a seemingly minor wound.</p>
<h2>Immediate steps: call your veterinarian right away</h2>
<ul>
<li>Call the vet immediately and ask what to do while waiting (Horse Canada; EquiMed).</li>
<li>Cover the horse loosely with a blanket, watching for overheating; keep the horse calm and let it settle in a comfortable position (Horse Canada; EquiMed).</li>
<li>Control any bleeding; support broken bones before moving the horse (EquiMed). Do not move or treat the wounds of a horse who seems to be in shock (EQUUS).</li>
<li>If the horse can walk, move it to a safe enclosed shelter and put on a halter; encourage drinking (Horse Canada).</li>
<li>Do not dismiss nosebleeds; they can cause serious blood loss (Horse Canada).</li>
</ul>
<h2>Prevention</h2>
<p>Horse Canada says early veterinary care is the best defence: call a vet whenever symptoms appear, even if unsure. The sources reviewed give no other prevention steps. See <a href="/qa/wounds/shock-complications-and-recovery/">complications and recovery</a>.</p>''',
  src=['equimedshock','hcshock','equusfirstaid'], rel=['shock-complications-and-recovery','when-to-call-the-vet-for-a-horse-wound','wound-care-and-infection-prevention']),

 dict(slug='shock-complications-and-recovery', ids=['VET-QA-0490','VET-QA-0491','VET-QA-0480'], urgent=True,
  q='What are the complications of shock in horses, and how do I monitor recovery?',
  title='Shock in Horses: Complications and Recovery Signs',
  meta='Untreated shock can lead to organ failure and death. Rare complications include gut damage, tying-up and kidney problems. Recovery is directed by your vet.',
  short='Without prompt treatment shock leads to organ failure and death. Horse Canada describes rare later complications including gut damage, tying-up and long-term kidney effects. Healthy gums are moist and bright pink. Recovery monitoring should be directed by your veterinarian.',
  body='''<h2>Complications</h2>
<ul>
<li>Without immediate treatment, lack of oxygen shuts down vital organs and the horse may lose consciousness and die (EquiMed; Horse Canada).</li>
<li>Possible complications, described as rare: sections of the gut may die, muscles may become more prone to tying-up, and kidney function may be compromised long-term (Horse Canada).</li>
<li>EquiMed gives no separate complications section.</li>
</ul>
<h2>Signs of recovery and monitoring</h2>
<ul>
<li>Healthy gums are moist and bright pink; press the gums and the white mark should return to pink within one or two seconds, and a slower return may indicate shock (Horse Canada).</li>
<li>A heart rate above 80 beats per minute may signal a serious problem (Horse Canada).</li>
<li>The vet checks gum color, heart rate and respiratory rate, and aims to stabilize the horse and restore blood pressure and circulation; treatment of the underlying cause is essential (Horse Canada).</li>
</ul>
<p>The sources reviewed give no recovery timeline, recheck schedule or full list of recovery signs; EquiMed does not describe improvement signs at all. Keep your vet informed and follow their monitoring instructions; call right away if gums turn pale again, the horse becomes depressed, cold or sweaty, or breathing or pulse worsen. See <a href="/qa/wounds/shock-causes-signs-and-first-aid/">causes, signs and first aid</a>.</p>''',
  src=['equimedshock','hcshock'], rel=['shock-causes-signs-and-first-aid','when-to-call-the-vet-for-a-horse-wound','signs-of-wound-infection']),
]
