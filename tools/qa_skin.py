# -*- coding: utf-8 -*-
"""Skin, allergy and hives Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'psurain': ('Penn State Extension — Rain Rot in Horses', 'https://extension.psu.edu/rain-rot-in-horses'),
 'umnscr': ('University of Minnesota Extension — Scratches: a skin problem in horses', 'https://extension.umn.edu/horse-health/scratches'),
 'ucdscr': ('UC Davis Center for Equine Health Horse Report — Scratches', 'https://horsereport.vetmed.ucdavis.edu/node/1151'),
 'equusscr': ('EQUUS — Scratches: Keep this condition from turning chronic', 'https://equusmagazine.com/horse-care/scratches-keep-this-condition-from-turning-chronic'),
 'ucdring': ('UC Davis Center for Equine Health — Ringworm in Horses (Dermatophytosis)', 'https://ceh.vetmed.ucdavis.edu/node/3361'),
 'merckana': ('Merck Veterinary Manual (owner version) — Anaphylactic Reactions in Horses', 'https://www.merckvetmanual.com/horse-owners/immune-disorders-of-horses/disorders-involving-anaphylactic-reactions-type-i-reactions-in-horses'),
 'msdurt': ('MSD Veterinary Manual — Hives (Urticaria) in Animals', 'https://www.msdvetmanual.com/integumentary-system/urticaria/hives-urticaria-in-animals'),
 'wcvmchor': ('Western College of Veterinary Medicine — Chorioptes equi', 'https://wcvm.usask.ca/learnaboutparasites/parasites/chorioptes-equi.php'),
 'thehorserr': ('The Horse — Understanding Rain Rot', 'https://thehorse.com/122494/understanding-rain-rot'),
 'ucdskin': ('UC Davis Center for Equine Health Horse Report — Dermatology issue, Spring 2022', 'https://cehhorsereport.vetmed.ucdavis.edu/sites/g/files/dgvnsk9021/files/inline-files/Horse_Report_Spring_22_web.pdf'),
})
HELD = {
 'VET-QA-0440':'respiratory-complications record filed under skin; belongs to the Respiratory batch and carries unsourced numbers',
 'VET-QA-0442':'hives-recurrence question with no condition named in the record; unsourced',
 'VET-QA-0444':'"specific products" question with no condition named; no source names products',
 'VET-QA-0446':'natural remedies for mange; no source reviewed supports any',
}
U='/qa/skin/'
PAGES = [
 dict(slug='signs-of-rain-rot', ids=['VET-QA-0472'], urgent=False,
  q='What are the early signs of rain rot?',
  title='Early Signs of Rain Rot in Horses',
  meta='Rain rot starts as small raised bumps or scabs with clumps of hair, usually along the topline. The skin is tender, not itchy. Check winter coats by hand.',
  short='Early rain rot shows as small raised bumps or scabs holding clusters of hair, usually on the topline. Removing a scab leaves a bald patch. The skin is typically tender rather than itchy, and a winter coat can hide it, so check by hand.',
  body='''<h2>Early signs (Penn State Extension)</h2>
<ul>
<li>Small raised bumps or scabs containing clusters of hair; removing them leaves bald patches.</li>
<li>Most often on the topline, but also the rump, face and legs.</li>
<li>The skin is typically painful or tender rather than itchy.</li>
<li>Winter coats can hide it, so hands-on checks may be needed.</li>
</ul>
<h2>When it is more serious</h2>
<p>In severe cases, lesions can be large, extend through multiple skin layers and affect how the horse moves. Penn State advises consulting a veterinarian to confirm the cause and plan treatment. See <a href="/qa/skin/rain-rot-treatment-and-products/">treatment</a> and <a href="/qa/skin/when-to-call-the-vet-for-skin-problems/">when to call the vet</a>.</p>''',
  src=['psurain'], rel=['rain-rot-treatment-and-products','rain-rot-spread-and-prevention','when-to-call-the-vet-for-skin-problems']),

 dict(slug='rain-rot-treatment-and-products', ids=['VET-QA-0445'], urgent=False,
  q='How is rain rot treated, and are there specific products I should use?',
  title='Rain Rot Treatment: Steps and Products',
  meta='Treat mild rain rot by bathing with antimicrobial soap, softening scabs before removal and keeping the horse dry. Severe cases may need a vet.',
  short='For minor cases, Penn State advises bathing with an antimicrobial soap, softening scabs before removing them, and keeping the horse dry. Severe cases may need veterinary antibiotic injections. The page names no specific products.',
  body='''<h2>Treatment steps (Penn State Extension)</h2>
<ul>
<li>Minor cases: bathe with an antimicrobial soap, then curry and brush to support healing.</li>
<li>Soften scabs before removing them, since the skin underneath is tender; do not pull them off dry.</li>
<li>Keep the horse dry and reduce exposure to wet conditions and caked mud.</li>
<li>A topical antimicrobial product may be added if needed.</li>
<li>Severe cases: a veterinarian may give antibiotic injections and may take a skin biopsy to confirm the diagnosis.</li>
</ul>
<h2>Products</h2>
<p>The Penn State page mentions topical antimicrobial products in general terms and names no brands, and the sources reviewed give no list of products to avoid. Ask your veterinarian what to use. Most acute cases can heal on their own, but The Horse reports an extension specialist recommending treating even minor cases because lesions can spread and worsen. The sources reviewed give no healing timeline.</p>
<p>See <a href="/qa/skin/rain-rot-spread-and-prevention/">spread and prevention</a>.</p>''',
  src=['psurain','thehorserr'], rel=['signs-of-rain-rot','rain-rot-spread-and-prevention','when-to-call-the-vet-for-skin-problems']),

 dict(slug='rain-rot-spread-and-prevention', ids=['VET-QA-0450','VET-QA-0458'], urgent=False,
  q='Can rain rot spread to other horses, and how do I prevent it?',
  title='Can Rain Rot Spread? Prevention Tips',
  meta='Separate horses with rain rot, disinfect or replace shared grooming tools, and keep horses dry with shelter in heavy rain, less mud and fly control.',
  short='Penn State advises separating horses with rain rot during treatment and disinfecting or replacing shared grooming tools. To prevent it, groom and bathe regularly, shelter horses in heavy rain, limit mud, and control biting flies.',
  body='''<h2>Spread (Penn State Extension)</h2>
<ul>
<li>Separate horses with rain rot from others during treatment.</li>
<li>Disinfect or replace grooming tools and other equipment that touch affected horses.</li>
</ul>
<p>The bacterium (<em>Dermatophilus congolensis</em>) lives on healthy skin in a mostly dormant state, and wet conditions let it cause infection. Infection is most likely when skin is already compromised by high humidity, prolonged rain or biting insects.</p>
<h2>Prevention</h2>
<ul>
<li>Bathe and groom regularly.</li>
<li>Keep horses in a barn or shelter during heavy rain.</li>
<li>Limit access to muddy areas and reduce mud overall.</li>
<li>Manage biting flies (traps, farm sanitation, and insecticide sprays chosen for the fly species).</li>
</ul>
<p>Lighter coat colors and weak or immature immune systems raise the risk. See <a href="/qa/skin/signs-of-rain-rot/">early signs</a>.</p>''',
  src=['psurain'], rel=['signs-of-rain-rot','rain-rot-treatment-and-products','preventing-skin-problems-in-horses']),

 dict(slug='signs-of-scratches-in-horses', ids=['VET-QA-0473'], urgent=False,
  q='What are the signs of scratches in horses?',
  title='Signs of Scratches (Pastern Dermatitis) in Horses',
  meta='Scratches shows as redness, oozing, crusts and sores on the pasterns, sometimes with swelling. A hot, swollen, painful leg needs a vet.',
  short='Scratches causes patchy redness, oozing, crusting, erosions and ulcers on the pastern and heel bulbs, followed by swelling in some horses. The skin may itch and feel tender, and some horses go lame. A hot, swollen, painful leg means call your veterinarian.',
  body='''<h2>Signs (UC Davis; University of Minnesota Extension)</h2>
<ul>
<li>Multiple lesions in the pastern area; early signs are patchy redness, oozing, crusting, skin erosions and ulcers.</li>
<li>Swelling of the affected limb or limbs may follow.</li>
<li>The skin may itch and feel tender.</li>
<li>Some horses become lame, and the lameness can become severe.</li>
<li>Draft breeds, horses with heavy leg feathering and horses with white legs are at higher risk.</li>
</ul>
<h2>Call your vet</h2>
<p>Minnesota Extension says a leg that is hot, swollen and painful means the infection has become more serious; contact your veterinarian. Scratches is an umbrella term for several possible causes, so a vet may need to confirm what is going on. See <a href="/qa/skin/causes-of-scratches-in-horses/">causes</a> and <a href="/qa/lameness/signs-of-cellulitis-and-lymphangitis/">signs of cellulitis</a>.</p>''',
  src=['ucdscr','umnscr'], rel=['causes-of-scratches-in-horses','scratches-treatment-and-recovery-time','when-to-call-the-vet-for-skin-problems']),

 dict(slug='causes-of-scratches-in-horses', ids=['VET-QA-0477'], urgent=False,
  q='What environmental factors contribute to scratches?',
  title='What Causes Scratches in Horses?',
  meta='Constant moisture from mud, wet paddocks and damp bedding is the main trigger for scratches. Heavy leg feathering and wraps can add to the risk.',
  short='Long exposure to moisture, such as muddy fields or damp stalls and bedding, is the main trigger. Mud gives bacteria or fungi a place to take hold. Heavy feathering that traps moisture, ill-fitting boots and other skin irritants can also contribute.',
  body='''<h2>Environmental factors</h2>
<ul>
<li><strong>Constant moisture</strong> from muddy fields, damp stalls or wet bedding irritates delicate skin (University of Minnesota Extension).</li>
<li>Mud and dirty surroundings give bacteria or fungi a good environment to take hold (Minnesota).</li>
<li>Prolonged wetness is a frequent cause or something that keeps the problem going (UC Davis).</li>
<li>Heavy leg feathering can trap moisture; draft breeds are most affected (UC Davis).</li>
<li>EQUUS adds chronic irritation from bell boots that do not fit, coarse arena footing and chemically treated bedding.</li>
</ul>
<h2>Not only the environment</h2>
<p>UC Davis calls pastern dermatitis an umbrella term for several triggers, including allergies, drug reactions, fungi, bacteria, parasites and sun-related changes in white legs. In draft horses, chronic progressive lymphedema is an underlying condition that gets worse with repeated flare-ups and has no permanent cure. Horses with repeated or stubborn scratches need a veterinary workup. See <a href="/qa/skin/preventing-scratches/">prevention</a>.</p>''',
  src=['umnscr','ucdscr','equusscr'], rel=['signs-of-scratches-in-horses','preventing-scratches','scratches-treatment-and-recovery-time']),

 dict(slug='scratches-treatment-and-recovery-time', ids=['VET-QA-0447','VET-QA-0460','VET-QA-0191'], urgent=False,
  q='How is scratches treated, are there recommended products, and how long until it improves?',
  title='Scratches Treatment and How Long It Takes',
  meta='Clip the hair, wash gently once, dry well and soften scabs rather than picking them. Severe cases need a vet. EQUUS says most cases heal within two weeks.',
  short='Clip the hair, wash gently, pat dry and soften scabs rather than picking. Severe cases need veterinary treatment. EQUUS says most cases heal within two weeks, and UC Davis says to reassess if there is no improvement after one week.',
  body='''<p>UC Davis lists cracked heels, greasy heel, mud fever, mud rash and dew poisoning as other names for scratches (pastern dermatitis), so this page also answers cracked-heels treatment.</p>
<h2>Home care for mild cases (University of Minnesota Extension)</h2>
<ul>
<li>Clip the long hair over the affected skin so it stays cleaner and drier.</li>
<li>Clean once with an antibacterial soap, wash gently, and avoid repeated harsh cleansers or disinfectants.</li>
<li>Pat the area dry.</li>
<li>Soften scabs by soaking or sweating them off rather than picking them.</li>
<li>Wash no more than once a day.</li>
</ul>
<h2>Products</h2>
<p>Minnesota says a small amount of a barrier ointment after cleaning can keep skin soft in mild cases, but it can trap dirt and is best when the horse is stalled. Severe cases may need a veterinary-prescribed cream containing an antibiotic, an antifungal and a steroid, and very severe cases oral antibiotics. EQUUS warns against "home remedies" such as bleach. Product choice and any medication belong to your veterinarian.</p>
<h2>How long it takes</h2>
<p>EQUUS says most cases heal within two weeks when cleaned and treated every two to three days. The Minnesota page gives no timeline. UC Davis says starting with antibiotics, clipping and gentle cleansing is acceptable, and if there is no improvement after one week a topical corticosteroid may be added by your vet. See <a href="/qa/skin/preventing-scratches/">preventing recurrence</a>.</p>''',
  src=['umnscr','equusscr','ucdscr'], rel=['signs-of-scratches-in-horses','causes-of-scratches-in-horses','preventing-scratches']),

 dict(slug='preventing-scratches', ids=['VET-QA-0459','VET-QA-0163','VET-QA-0179'], urgent=False,
  q='How can I prevent scratches from recurring?',
  title='Preventing Scratches From Coming Back',
  meta='Limit turnout in wet grass and mud, keep bedding clean and dry, keep lower legs clipped, dry pasterns after bathing and avoid wraps or boots that trap moisture.',
  short='Limit time in wet grass and mud, keep bedding clean and dry, keep the lower legs clipped, dry the pasterns thoroughly after bathing, and avoid long-term boots or wraps that trap moisture. Clean boots and wraps before reuse.',
  body='''<h2>Prevention (UC Davis; University of Minnesota Extension)</h2>
<ul>
<li>Limit turnout in wet grass or mud.</li>
<li>Dry the pasterns thoroughly after bathing; Minnesota advises avoiding hosing the fetlocks and pasterns unless needed.</li>
<li>Keep the lower legs clipped.</li>
<li>Avoid long-term use of boots and wraps that trap moisture, and clean them before reuse.</li>
<li>Maintain clean, dry bedding.</li>
</ul>
<p>UC Davis lists cracked heels, greasy heel, mud fever, mud rash and dew poisoning as other names for scratches (pastern dermatitis), so this page also answers cracked-heels prevention. UC Davis also notes that unpigmented skin is prone to sunburn and that avoiding sun may help pastern dermatitis. If scratches keeps returning, ask your veterinarian to look for an underlying cause. See <a href="/qa/skin/causes-of-scratches-in-horses/">causes</a>.</p>''',
  src=['ucdscr','umnscr','ucdskin'], rel=['causes-of-scratches-in-horses','scratches-treatment-and-recovery-time','preventing-skin-problems-in-horses']),

 dict(slug='common-causes-of-hives-in-horses', ids=['VET-QA-0467'], urgent=False,
  q='What are common causes of hives in horses?',
  title='Common Causes of Hives in Horses',
  meta='Hives often follow insect bites, drug or vaccine reactions, feed or seasonal allergens, and the cause is often never found. Heat and stress can trigger them.',
  short='Common triggers are insect bites, drug or vaccine reactions, food reactions and seasonal environmental allergens, though often no cause is found. Non-allergic triggers include heat, cold, exercise, pressure and stress. Ringworm and autoimmune disease can also cause hives.',
  body='''<h2>Causes (MSD Veterinary Manual; Merck owner version)</h2>
<ul>
<li>Insect bites or stings, drug or vaccine reactions, food reactions and seasonal environmental allergens.</li>
<li>Irritants such as stinging nettle and chemicals, and something inhaled or contacted.</li>
<li>Non-allergic triggers: heat or cold, exercise, pressure and stress.</li>
<li>Ringworm, autoimmune disease and inflammation of blood vessels (vasculitis).</li>
<li>Often, no specific cause is found.</li>
</ul>
<p>UC Davis says hives are a reaction pattern, not a disease. Because causes range from harmless to serious, a veterinarian should confirm what is behind them. See <a href="/qa/skin/how-long-hives-last-and-when-to-call-the-vet/">how long hives last</a>.</p>''',
  src=['msdurt','merckana','ucdskin'], rel=['how-long-hives-last-and-when-to-call-the-vet','hives-treatment-and-care','preventing-hives']),

 dict(slug='how-long-hives-last-and-when-to-call-the-vet', ids=['VET-QA-0441','VET-QA-0461','VET-QA-0462'], urgent=True,
  q='How long do hives last, how long should I monitor them, and are there long-term effects?',
  title='How Long Horse Hives Last and When to Call',
  meta='Hives may fade within 12 to 48 hours, but call your vet at once for facial swelling, trouble breathing or collapse. Chronic hives are rare.',
  short='Allergic hives usually start within 20 minutes of exposure and fade within 24 hours, and may resolve on their own in 12 to 48 hours. Call your veterinarian immediately for trouble breathing, swelling that spreads, pale gums or collapse. Chronic cases are rare.',
  body='''<h2>How long they last</h2>
<ul>
<li>Allergic reactions usually begin within 20 minutes of exposure and fade within 24 hours (Merck owner version).</li>
<li>Mild hives may resolve on their own within 12 to 48 hours; treatment is usually started anyway because it is hard to predict whether they will worsen (MSD Veterinary Manual).</li>
<li>Hives can come back as medication wears off (MSD).</li>
</ul>
<h2>Monitoring and when to call</h2>
<p>The sources reviewed give no set monitoring period, so call your veterinarian when you first see hives. <strong>Treat it as an emergency</strong> if swelling spreads to the face or airways, breathing becomes difficult, gums turn very pale, or the horse collapses: severe cases can progress to anaphylaxis (MSD). See <a href="/qa/skin/signs-of-anaphylaxis-and-severe-allergic-reactions/">anaphylaxis signs</a>.</p>
<h2>Long-term effects</h2>
<p>MSD describes chronic cases as rare and gives no recurrence figures for horses. UC Davis describes a case that relapsed a few weeks after treatment and responded to a second course.</p>''',
  src=['merckana','msdurt','ucdskin'], rel=['hives-treatment-and-care','common-causes-of-hives-in-horses','signs-of-anaphylaxis-and-severe-allergic-reactions']),

 dict(slug='hives-treatment-and-care', ids=['VET-QA-0443'], urgent=False,
  q='What care should I give during treatment for hives?',
  title='Caring for a Horse With Hives',
  meta='Remove the suspected trigger and call your vet. Vets usually choose an antihistamine or corticosteroid, with care in laminitis-prone horses.',
  short='Hives often clear once the trigger is removed or passes. Vets commonly use antihistamines or corticosteroids chosen for the individual horse, with caution about steroids in laminitis-prone horses. Do not give medication without veterinary direction.',
  body='''<h2>What helps</h2>
<ul>
<li>Remove or reduce exposure to the suspected trigger, such as new bedding, a new product or biting insects.</li>
<li>Hives are usually not life-threatening and often resolve once the trigger is removed or passes through the body (Merck owner version).</li>
<li>Antihistamines and glucocorticoids are the main drugs and usually work quickly; glucocorticoids are used with caution in horses prone to laminitis (MSD Veterinary Manual).</li>
<li>A short oral antihistamine course after the first treatment can help prevent a rebound (MSD).</li>
</ul>
<p>The sources give no doses, and your veterinarian chooses drug and dose. Watch for spreading swelling or trouble breathing; see <a href="/qa/skin/how-long-hives-last-and-when-to-call-the-vet/">when to call</a>.</p>''',
  src=['merckana','msdurt'], rel=['common-causes-of-hives-in-horses','how-long-hives-last-and-when-to-call-the-vet','preventing-hives']),

 dict(slug='preventing-hives', ids=['VET-QA-0455'], urgent=False,
  q='How can I prevent hives in a horse?',
  title='Preventing Hives in Horses',
  meta='Avoid known triggers, use fly masks and repellent for insect-triggered hives, and ask your vet about antihistamines or immunotherapy if triggers persist.',
  short='Avoid the trigger or desensitize the horse to it. For insect-triggered hives, use daily repellent, fly masks and keep horses away from areas where biting insects thrive. If triggers cannot be avoided, a vet may suggest daily antihistamines or allergen immunotherapy.',
  body='''<h2>Prevention (MSD Veterinary Manual)</h2>
<ul>
<li>Avoid the trigger or desensitize the animal to it.</li>
<li>For insect-triggered hives, use an insect repellent daily, protective gear such as fly masks, and keep horses away from areas where biting insects thrive.</li>
<li>If triggers cannot be avoided, daily antihistamines may be needed; mast cell stabilizers, allergen immunotherapy and omega-3 fatty acids may also help.</li>
</ul>
<p>Check any repellent label for use on horses. Treatment choices and dosing are your veterinarian's call. See <a href="/qa/skin/allergy-testing-for-horses/">allergy testing</a>.</p>''',
  src=['msdurt'], rel=['common-causes-of-hives-in-horses','allergy-testing-for-horses','preventing-allergic-reactions-and-dermatitis']),

 dict(slug='common-allergens-and-triggers-in-horses', ids=['VET-QA-0466','VET-QA-0451'], urgent=False,
  q='What are common allergens for horses, and how do I identify and avoid them?',
  title='Common Allergens for Horses and How to Spot Them',
  meta='Common allergens include pollen, mold, dust, biting insects, drugs and feed. Timing gives clues: seasonal suggests pollen, year-round suggests mold or dust.',
  short='Common triggers are environmental allergens such as pollen and mold, insect or mite bites, drugs, chemicals and feed. Timing offers clues: seasonal itching suggests pollen, year-round itching suggests mold, barn dust or feed. A vet confirms the cause.',
  body='''<h2>Common allergens (UC Davis; MSD Veterinary Manual)</h2>
<ul>
<li>Environmental allergens such as pollen and mold.</li>
<li>Insect or mite bites; flies and midges can trigger reactions, and some breeds appear more susceptible.</li>
<li>Drugs and vaccines, chemical contact, and feed.</li>
</ul>
<h2>Working out the trigger</h2>
<ul>
<li>Seasonal itching suggests pollen; year-round itching suggests mold, barn dust or feed; itching after shampoos or dips suggests a contact allergy (UC Davis).</li>
<li>Keep a log of when signs appear and what changed (new bedding, feed, products, turnout).</li>
<li>Test results do not always agree, so a vet should interpret them; see <a href="/qa/skin/allergy-testing-for-horses/">allergy testing</a>.</li>
</ul>
<p>Avoiding the trigger is the main prevention; for insects that means fly masks and reducing exposure. Often the specific cause is never found (MSD).</p>''',
  src=['ucdskin','msdurt'], rel=['allergy-testing-for-horses','preventing-allergic-reactions-and-dermatitis','common-causes-of-hives-in-horses']),

 dict(slug='allergy-testing-for-horses', ids=['VET-QA-0449','VET-QA-0465'], urgent=False,
  q='Are there tests to identify allergens in a horse, and are diagnostic tests needed?',
  title='Allergy Testing for Horses: Skin and Blood Tests',
  meta='Vets use intradermal skin tests and blood tests to look for allergens, but results can disagree. Hives are often diagnosed from history and treatment response.',
  short='Intradermal skin tests and blood (serum) tests are used to identify allergens, but they do not always agree. Many hive cases are diagnosed from history, exam and response to treatment, and biopsy is reserved for chronic or unusual cases.',
  body='''<h2>Tests (UC Davis; MSD Veterinary Manual)</h2>
<ul>
<li>Intradermal (skin) and serum (blood) allergy tests are used to identify allergens, but they do not always agree (UC Davis).</li>
<li>Hives are usually diagnosed from history, physical exam and response to treatment; a skin biopsy is reserved for chronic or unusual cases (MSD).</li>
<li>Allergy shots (immunotherapy) had about a 70% success rate in a 17-year UC Davis study; about 85% of responding horses need lifelong treatment, often at reduced frequency.</li>
</ul>
<h2>Do you need them?</h2>
<p>Whether testing is needed is your veterinarian's call; the sources reviewed give no rule. Merck notes ringworm, vasculitis and autoimmune disease can also cause hives. The sources reviewed give no cutoffs for interpreting results. See <a href="/qa/skin/managing-chronic-allergies-in-horses/">chronic allergies</a>.</p>''',
  src=['ucdskin','msdurt','merckana'], rel=['common-allergens-and-triggers-in-horses','managing-chronic-allergies-in-horses','preventing-hives']),

 dict(slug='preventing-allergic-reactions-and-dermatitis', ids=['VET-QA-0452','VET-QA-0453'], urgent=False,
  q='How can I prevent allergic reactions and allergic dermatitis in a horse?',
  title='Preventing Allergic Reactions and Dermatitis',
  meta='Reduce exposure to the trigger: fly masks and repellent, fly breeding control, fans, and fewer dust and mold sources. Ask your vet about immunotherapy.',
  short='The main prevention is reducing exposure to the trigger. For insect allergy, use fly masks and repellent, destroy fly breeding grounds, use fans, and keep horses away from biting insects. A vet may suggest immunotherapy if triggers cannot be avoided.',
  body='''<h2>Reduce exposure</h2>
<ul>
<li>Insects: fly masks and fly spray help (UC Davis); destroy fly breeding grounds, use an approved pesticide in stable areas and use fans to move air (Merck, for sweet itch).</li>
<li>Equine asthma: reducing exposure to allergens is described as the key part of treatment (Merck).</li>
<li>Avoid the trigger or desensitize the horse to it; allergen immunotherapy may help (MSD).</li>
</ul>
<p>The sources reviewed give no preventive steps against anaphylaxis itself, and your veterinarian should plan vaccines and drugs for a horse that has reacted before. See <a href="/qa/skin/common-allergens-and-triggers-in-horses/">common triggers</a>.</p>''',
  src=['ucdskin','merckana','msdurt'], rel=['common-allergens-and-triggers-in-horses','preventing-hives','managing-chronic-allergies-in-horses']),

 dict(slug='managing-mild-allergic-reactions', ids=['VET-QA-0463'], urgent=True,
  q='How should I manage a mild allergic reaction at home?',
  title='Managing a Mild Allergic Reaction in a Horse',
  meta='For mild hives, remove the trigger and call your vet. Give no medication without vet direction; spreading swelling or breathing trouble is an emergency.',
  short='Remove or limit exposure to the suspected trigger and call your veterinarian, who chooses any medication. Mild hives often fade within 24 hours, but treat spreading swelling, labored breathing, pale gums or collapse as an emergency.',
  body='''<h2>What you can do</h2>
<ul>
<li>Remove the suspected trigger, such as a new product, feed or biting insects.</li>
<li>Call your veterinarian; hives often resolve once the trigger is removed or passes, and vets use corticosteroids or other drugs tailored to the horse (Merck owner version).</li>
<li>Keep the horse where you can watch it closely; mild hives usually fade within 24 hours (Merck).</li>
<li>Do not give a medication from your first-aid kit unless your veterinarian tells you to; the sources give no doses.</li>
</ul>
<h2>Escalate to an emergency if</h2>
<p>Swelling spreads to the face or airways, breathing is difficult, gums are very pale, or the horse is shaky or collapses. See <a href="/qa/skin/signs-of-anaphylaxis-and-severe-allergic-reactions/">anaphylaxis signs</a>.</p>''',
  src=['merckana','msdurt'], rel=['signs-of-anaphylaxis-and-severe-allergic-reactions','how-long-hives-last-and-when-to-call-the-vet','hives-treatment-and-care']),

 dict(slug='managing-chronic-allergies-in-horses', ids=['VET-QA-0464'], urgent=False,
  q='How do I manage a horse with chronic allergies?',
  title='Managing a Horse With Chronic Allergies',
  meta='Manage chronic allergies by avoiding triggers, controlling insects and, with your vet, antihistamines or immunotherapy. Many horses need lifelong care.',
  short='Management centers on avoiding triggers and reducing insect exposure. With your veterinarian, options include daily antihistamines and allergen immunotherapy; UC Davis reports about 85% of responding horses need lifelong treatment, often less often over time.',
  body='''<h2>Management options</h2>
<ul>
<li>Avoid the trigger or desensitize the horse to it (MSD Veterinary Manual).</li>
<li>Reduce insect exposure with fly masks, spray and keeping horses away from biting insects (UC Davis).</li>
<li>If triggers cannot be avoided, daily antihistamines may be needed; mast cell stabilizers, allergen immunotherapy and omega-3 fatty acids may also help (MSD).</li>
<li>Allergy shots had about a 70% success rate in a 17-year UC Davis study, injections typically continue for at least one year, and an oral option is now available.</li>
<li>A balanced diet supports skin health (UC Davis).</li>
</ul>
<p>Plans are individual, and the sources give no drug names or protocols. See <a href="/qa/skin/allergy-testing-for-horses/">allergy testing</a>.</p>''',
  src=['msdurt','ucdskin'], rel=['allergy-testing-for-horses','preventing-allergic-reactions-and-dermatitis','common-allergens-and-triggers-in-horses']),

 dict(slug='signs-of-anaphylaxis-and-severe-allergic-reactions', ids=['VET-QA-0471','VET-QA-0474','VET-QA-0476'], urgent=True,
  q='What are the signs of anaphylaxis and severe allergic reactions, and what emergency signs should I watch for?',
  title='Signs of Anaphylaxis in Horses: Emergency Signs',
  meta='Anaphylaxis can cause severe breathing trouble, drooling, pale gums and collapse within seconds to minutes. It is an extreme emergency: call your vet now.',
  short='Anaphylaxis causes severe breathing trouble, sudden diarrhea, heavy drooling, very pale gums, cold limbs, a fast weak pulse, shock and collapse, usually within seconds to minutes. It is an extreme emergency. Call your veterinarian immediately.',
  body='''<h2>Signs (Merck Veterinary Manual, owner version)</h2>
<ul>
<li>Severe breathing trouble, sudden diarrhea and heavy drooling.</li>
<li>Very pale gums, cold limbs, a very fast heart rate with a weak pulse.</li>
<li>Shock, seizures, coma and death.</li>
<li>Facial swelling usually does not occur, but itching around the face and head may.</li>
<li>Signs usually appear within seconds to minutes of exposure.</li>
</ul>
<h2>Other emergency signs</h2>
<p>Swelling that extends to the airways can be life-threatening, and swelling is more serious than hives. Hives that are part of a severe reaction can progress to anaphylaxis (MSD).</p>
<h2>What to do</h2>
<p><strong>Seek emergency veterinary help immediately.</strong> A veterinarian can give intravenous epinephrine and other medications. The sources give no home treatment, and no drug should be given without veterinary direction. See <a href="/emergency/">our emergency guides</a>.</p>''',
  src=['merckana','msdurt'], rel=['managing-mild-allergic-reactions','how-long-hives-last-and-when-to-call-the-vet','when-to-call-the-vet-for-skin-problems']),

 dict(slug='signs-of-mange-in-horses', ids=['VET-QA-0475'], urgent=False,
  q='What are the symptoms of mange in horses?',
  title='Signs of Mange (Mites) in Horses',
  meta='Mange mites cause itching: stamping, biting and rubbing, mostly on the lower legs of feathered horses or the tail head, with scabs and matted hair.',
  short='Itching is the main sign: affected horses stamp, bite and rub. Chorioptic mange, the most common type, usually affects the lower legs of feathered horses, or the tail head in unfeathered horses, with small oozing bumps, scabs and matted coat. Many infested horses show no signs.',
  body='''<h2>Signs (Western College of Veterinary Medicine)</h2>
<ul>
<li>Itching is the main sign: stamping, biting and rubbing the itchy areas.</li>
<li>Lower limbs are most often affected, especially feathers of heavy horses; in unfeathered horses, the tail head.</li>
<li>Small raised bumps with oozing and scabs may form, and the coat may mat.</li>
<li>Many heavily infested horses show no signs; the reason is not fully understood.</li>
<li>Cases are reported more often in winter.</li>
</ul>
<p>Mange signs look like scratches, ringworm and allergies, and mites are confirmed by finding them in hair brushings or skin scrapings, so a vet should check. See <a href="/qa/skin/mange-spread-prevention-and-risks/">spread and prevention</a>.</p>''',
  src=['wcvmchor'], rel=['mange-spread-prevention-and-risks','signs-of-scratches-in-horses','when-to-call-the-vet-for-skin-problems']),

 dict(slug='mange-spread-prevention-and-risks', ids=['VET-QA-0456','VET-QA-0470'], urgent=False,
  q='How do I prevent mange, and what are the risks if it is untreated?',
  title='Preventing Mange in Horses and Risks of Delay',
  meta='Mange mites spread horse to horse and on grooming tools, so treat the whole group, watch new arrivals and clean tack. Mites and itching can persist.',
  short='Chorioptic mites spread directly between horses and on grooming equipment, so diagnosis in one horse means assume the whole group is infested. Prompt diagnosis, extra attention to new arrivals and cleaning tack help. The mites are not known to infect people.',
  body='''<h2>Spread and prevention (Western College of Veterinary Medicine)</h2>
<ul>
<li>Spread is direct, horse to horse, and also through objects such as grooming equipment.</li>
<li>If one horse is diagnosed, assume all horses in the group are infested.</li>
<li>Rapid diagnosis and treatment are central to control; pay particular attention to new arrivals and clean potential fomites such as tack.</li>
<li>Chorioptes equi is not known to infect people.</li>
</ul>
<h2>Risks if untreated</h2>
<p>The page does not describe outcomes of untreated mange directly. It notes that mites and signs can persist even despite repeated treatment, infestation spreads through the group, and scratching can damage the coat and skin. Treatment is difficult: no products are approved in Canada for chorioptic mange in horses, and the page recommends veterinarian-directed treatment of all horses in the group on a schedule. The sources reviewed support no natural remedy. See <a href="/qa/skin/signs-of-mange-in-horses/">signs</a>.</p>''',
  src=['wcvmchor'], rel=['signs-of-mange-in-horses','when-to-call-the-vet-for-skin-problems','preventing-skin-problems-in-horses']),

 dict(slug='signs-of-ringworm-and-fungal-skin-infections', ids=['VET-QA-0469'], urgent=False,
  q='What are the symptoms of fungal skin infections such as ringworm?',
  title='Signs of Ringworm and Fungal Skin Infections',
  meta='Ringworm typically causes round areas of hair loss, sometimes with redness or rash, often at the girth and saddle areas. A hair culture confirms it.',
  short='Ringworm typically causes itchy, round areas of hair loss, sometimes with redness or rash, often at the girth and saddle areas, and it can spread to other parts of the body. A fungal culture of a hair sample confirms it, because other conditions look similar.',
  body='''<h2>Signs (UC Davis Center for Equine Health)</h2>
<ul>
<li>Itchy, round areas of hair loss, sometimes with redness or rash.</li>
<li>Often at the girth and saddle areas, spreading to other parts of the body.</li>
<li>The incubation period can last up to 3 weeks, so exposure can happen before signs appear.</li>
</ul>
<p>Look-alikes include staph infection, rain scald, alopecia areata and occult sarcoid (UC Davis Horse Report). Diagnosis uses a lab fungal culture of a hair sample, so have your veterinarian confirm it. Ringworm can spread to other horses, people and other animals. See <a href="/qa/skin/ringworm-treatment-and-recovery-time/">treatment</a>.</p>''',
  src=['ucdring','ucdskin'], rel=['ringworm-treatment-and-recovery-time','preventing-ringworm-and-fungal-infections','when-to-call-the-vet-for-skin-problems']),

 dict(slug='ringworm-treatment-and-recovery-time', ids=['VET-QA-0448'], urgent=False,
  q='Are there specific treatments for different types of fungal infections?',
  title='Ringworm Treatment and Recovery in Horses',
  meta='Ringworm is usually treated with antifungal shampoos, dips or topical products. Oral drugs carry risks. Untreated, it can take a month or more to clear.',
  short='Antifungal shampoos, dips or topical products are the usual approach. Oral and intravenous options exist but carry risks such as liver damage, so they are veterinary decisions. With topical treatment hair usually regrows in one to four weeks. The sources reviewed cover ringworm only.',
  body='''<h2>Treatment (UC Davis Center for Equine Health)</h2>
<ul>
<li>Antifungal shampoos, dips or topical products are the usual approach.</li>
<li>Oral or intravenous drugs are options but carry risks such as liver damage, so they are your veterinarian's call.</li>
<li>Following veterinary and product instructions improves results; early treatment limits discomfort and spread.</li>
<li>With topical treatment, hair usually regrows within one to four weeks; untreated, the infection can clear on its own but may take a month or more.</li>
</ul>
<p>Isolate affected horses, give each horse its own tack and disinfect tack, blankets and grooming tools. The sources reviewed give no doses, and they do not cover other types of fungal skin infection in detail. See <a href="/qa/skin/preventing-ringworm-and-fungal-infections/">prevention</a>.</p>''',
  src=['ucdring','ucdskin'], rel=['signs-of-ringworm-and-fungal-skin-infections','preventing-ringworm-and-fungal-infections','when-to-call-the-vet-for-skin-problems']),

 dict(slug='preventing-ringworm-and-fungal-infections', ids=['VET-QA-0454'], urgent=False,
  q='How can I prevent fungal infections in a horse?',
  title='Preventing Ringworm and Fungal Infections',
  meta='Keep new horses apart for a few weeks, give each horse its own tack and grooming tools, and disinfect shared gear. Treat early to limit spread.',
  short='Keep new horses separated from the resident group for a few weeks while watching for signs, give each horse its own tack and equipment, and disinfect tack, blankets and grooming tools. Early treatment reduces spread to other horses, people and animals.',
  body='''<h2>Prevention (UC Davis Center for Equine Health)</h2>
<ul>
<li>Keep new horses separated from the resident group for a few weeks and monitor them for signs; the source gives no exact length.</li>
<li>Give each horse its own tack and equipment.</li>
<li>Disinfect tack, blankets, grooming equipment and other possibly contaminated surfaces.</li>
<li>If a lab culture identifies a soil-dwelling species, the ground or stall floor may be treated with bleach; no concentration is given.</li>
<li>Treat promptly; delaying treatment raises the risk of spread to other horses, people and other animals.</li>
</ul>
<p>The fungi normally live in rodents and soil. See <a href="/qa/skin/signs-of-ringworm-and-fungal-skin-infections/">signs</a>.</p>''',
  src=['ucdring','ucdskin'], rel=['signs-of-ringworm-and-fungal-skin-infections','ringworm-treatment-and-recovery-time','preventing-skin-problems-in-horses']),

 dict(slug='common-causes-of-skin-conditions-in-horses', ids=['VET-QA-0468'], urgent=False,
  q='What are common causes of skin conditions in horses?',
  title='Common Causes of Skin Problems in Horses',
  meta='Moisture, bacteria such as rain rot, fungi like ringworm, mites, biting insects and allergies are common causes of skin problems. A vet should diagnose.',
  short='Common causes are moisture and mud (scratches, rain rot), fungi such as ringworm, mites, biting insects and allergies, including hives. Because many conditions look alike, a veterinarian should diagnose a skin problem rather than guessing from appearance.',
  body='''<h2>Common causes</h2>
<ul>
<li><strong>Wet conditions:</strong> rain rot and scratches (Penn State; University of Minnesota Extension).</li>
<li><strong>Fungi:</strong> ringworm (UC Davis).</li>
<li><strong>Mites:</strong> chorioptic mange, usually on the lower legs (WCVM).</li>
<li><strong>Insect bites and allergies:</strong> hives and insect hypersensitivity (UC Davis; MSD).</li>
<li><strong>Summer sores:</strong> fly-deposited stomach worm larvae in damaged skin, typically recurring each summer (UC Davis Horse Report).</li>
<li>Less common: autoimmune disease (pemphigus foliaceus), vasculitis and sun-related changes on unpigmented skin.</li>
</ul>
<p>Look-alikes include staph infection, rain scald, occult sarcoid and alopecia areata, so diagnosis often needs culture, scraping or biopsy. See <a href="/qa/skin/when-to-call-the-vet-for-skin-problems/">when to call the vet</a>.</p>''',
  src=['ucdskin','psurain','umnscr','ucdring','wcvmchor','msdurt'], rel=['preventing-skin-problems-in-horses','when-to-call-the-vet-for-skin-problems','signs-of-rain-rot']),

 dict(slug='preventing-skin-problems-in-horses', ids=['VET-QA-0457'], urgent=False,
  q='How can I prevent my horse from developing skin problems?',
  title='Preventing Skin Problems in Horses',
  meta='Keep horses and bedding dry, limit mud, groom regularly, control flies, avoid sharing tack, clip and dry the lower legs and feed a balanced diet.',
  short='Keep horses and bedding dry and limit mud, groom regularly, control biting flies, avoid sharing tack and clean shared gear, and keep lower legs clipped and dry. A balanced diet supports skin health, and unpigmented skin needs protection from sun.',
  body='''<h2>Prevention</h2>
<ul>
<li><strong>Keep dry:</strong> shelter in heavy rain, limit mud, clean dry bedding, and dry the legs after bathing (Penn State; UC Davis).</li>
<li><strong>Control insects:</strong> fly masks and fly spray help, and strict fly control reduces summer sore recurrence (UC Davis).</li>
<li><strong>Limit spread:</strong> disinfect tack, blankets and grooming tools, and give each horse its own (UC Davis ringworm guidance).</li>
<li><strong>Protect the skin:</strong> unpigmented skin is prone to sunburn; avoid long-term boots or wraps that trap moisture.</li>
<li><strong>Diet:</strong> a balanced diet supports skin health, including minerals and omega-3 fatty acids; vitamins A, B and E may be needed if pasture and hay are limited (UC Davis).</li>
</ul>
<p>Check the skin by hand regularly, especially under a winter coat. See <a href="/qa/skin/common-causes-of-skin-conditions-in-horses/">common causes</a>.</p>''',
  src=['ucdskin','psurain','ucdring'], rel=['common-causes-of-skin-conditions-in-horses','when-to-call-the-vet-for-skin-problems','rain-rot-spread-and-prevention']),

 dict(slug='when-to-call-the-vet-for-skin-problems', ids=['VET-QA-0478'], urgent=True,
  q='When should I call a vet for skin problems in a horse?',
  title='When to Call the Vet for Horse Skin Problems',
  meta='Call your vet for scratching with hair loss or broken skin, a hot swollen leg, severe lesions, suspected ringworm, or any breathing trouble or collapse.',
  short='Call your veterinarian when scratching is frequent enough to cause hair loss, broken skin or scabs, or disrupts eating or sleeping; when a leg is hot, swollen and painful; or when lesions are severe. Trouble breathing, spreading swelling or collapse is an emergency.',
  body='''<h2>Call your veterinarian when</h2>
<ul>
<li>Scratching is frequent enough to cause hair loss, broken skin or scabs, or to disrupt eating or sleeping (UC Davis Horse Report).</li>
<li>A leg becomes hot, swollen and painful (University of Minnesota Extension).</li>
<li>Rain rot is severe, large or affects movement (Penn State).</li>
<li>You suspect ringworm; treat it as soon as possible, because untreated it can take a month or more to resolve and can spread to other horses and people (UC Davis).</li>
<li>Pastern dermatitis keeps returning; early diagnosis helps prevent severe chronic changes.</li>
</ul>
<h2>Emergency</h2>
<p><strong>Call immediately</strong> for swelling that spreads to the face or airways, trouble breathing, very pale gums, collapse or a sudden widespread reaction (Merck). See <a href="/qa/skin/signs-of-anaphylaxis-and-severe-allergic-reactions/">anaphylaxis signs</a> and <a href="/emergency/wound-care/">wound care</a>.</p>''',
  src=['ucdskin','umnscr','psurain','ucdring','merckana'], rel=['common-causes-of-skin-conditions-in-horses','signs-of-anaphylaxis-and-severe-allergic-reactions','preventing-skin-problems-in-horses']),
]
