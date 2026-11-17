# -*- coding: utf-8 -*-
"""Eye Q&A (includes corneal-ulcer records filed under GI in the package). Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'aaeperu': ('AAEP / Iowa State — Equine recurrent uveitis: a review of clinical assessment and management (Allbaugh)', 'https://aaep.org/wp-content/uploads/2024/08/Equine-recurrent-uveitis-Allbaugh.pdf'),
 'liveye': ('University of Liverpool Leahurst Equine Practice — Common diseases of the eye', 'https://www.liverpool.ac.uk/media/livacuk/equine/services/pdf/Eyes.pdf'),
 'acvseye': ('American College of Veterinary Surgeons — Ophthalmology Surgical Emergencies in Horses', 'https://www.acvs.org/large-animal/eye-trauma/'),
 'equuseye': ('EQUUS — What\'s Wrong With My Horse\'s Eye?', 'https://mynewhorse.equusmagazine.com/2023/09/12/whats-wrong-with-my-horses-eye/'),
 'equusweepy': ('EQUUS — What to Do if Your Horse\'s Eyes are Weepy', 'https://mynewhorse.equusmagazine.com/2026/01/31/what-to-do-if-your-horses-eyes-are-weepy/'),
 'equusprev': ('EQUUS — Protect your horse from eye injuries', 'https://equusmagazine.com/horse-care/prevent-eye-injuries'),
 'vvc': ('Veterinary Vision Center — 7 common equine eye conditions (veterinary eye practice)', 'https://veterinaryvisioncenter.com/7-common-equine-eye-conditions/'),
 'horseeye': ('The Horse — Big Problems for Equine Eyes', 'https://thehorse.com/198254/big-problems-for-equine-eyes/'),
})
HELD = {
 'VET-QA-0089':'answer is about eye tearing, not diet — mismatched question',
}
PAGES = [
 dict(slug='uveitis-symptoms-and-causes', ids=['VET-QA-0080','VET-QA-0081'], urgent=True,
  q='What are the symptoms and causes of uveitis in horses?',
  title='Uveitis in Horses: Symptoms and Causes',
  meta='Uveitis shows as eye pain: squinting, tearing, light sensitivity and cloudiness. Causes include infection, trauma and an immune response. Call your vet.',
  short='Uveitis is inflammation inside the eye. Signs include squinting, tearing, a cloudy cornea and a small pupil. Causes include infections such as leptospirosis, eye trauma and an overactive immune response; recurrent uveitis is immune-mediated. Any suspected case needs a veterinarian promptly.',
  body='''<h2>Symptoms</h2>
<ul>
<li>Pain signs: squinting and tearing, with light sensitivity and heavy tearing during episodes (AAEP review; EQUUS).</li>
<li>Active-stage findings a vet looks for include corneal swelling (edema), a constricted pupil and inflammation in the eye (AAEP review).</li>
<li>Between episodes the eye may look comfortable but can still carry changes such as cataract or adhesions inside the eye (AAEP review).</li>
<li>Warning signs of eye trouble generally: cloudiness, red, white or yellow discoloration, swelling, rubbing, and thick or bloody discharge (EQUUS).</li>
</ul>
<h2>Causes</h2>
<ul>
<li>Acute uveitis can have infectious, traumatic, tumor or immune-mediated causes (AAEP review).</li>
<li>Systemic infections, named as leptospirosis and equine herpesvirus, eye trauma, or an overactive immune system (Veterinary Vision Center).</li>
<li>Recurrent uveitis (ERU, "moon blindness") is an immune-mediated disease; leptospirosis is the most commonly implicated trigger, but other causes including past eye trauma may trigger it (AAEP review).</li>
<li>ERU is diagnosed after two or more documented episodes; one episode does not mean a horse has ERU (AAEP review).</li>
</ul>
<p><strong>Call your veterinarian</strong> for any squinting, tearing or cloudy eye; signs are not specific to uveitis and corneal ulcers can look similar. Do not use leftover eye medication. See <a href="/qa/eye/uveitis-treatment-and-monitoring/">treatment and monitoring</a>.</p>''',
  src=['aaeperu','equuseye','vvc'], rel=['uveitis-treatment-and-monitoring','uveitis-long-term-effects-and-recurrence','cloudy-eye-causes-and-vision']),

 dict(slug='uveitis-treatment-and-monitoring', ids=['VET-QA-0086','VET-QA-0085'], urgent=True,
  q='What are the treatment options for uveitis, and what should I monitor during treatment?',
  title='Uveitis Treatment Options and Monitoring',
  meta='Uveitis treatment centers on anti-inflammatories and pupil-dilating drops prescribed by a vet, with rechecks. Never self-treat with leftover steroid drops.',
  short='Core treatment is anti-inflammatory medication, usually topical corticosteroids, plus pupil-dilating drops, prescribed by a veterinarian after an eye exam. Therapy is tapered with rechecks. Watch for colic or digestive signs during treatment. Do not use leftover steroid drops.',
  body='''<h2>Treatment options</h2>
<ul>
<li>Anti-inflammatories are the core treatment, usually topical corticosteroids; topical NSAIDs or systemic anti-inflammatories are used in severe cases or when steroids are not suitable (AAEP review).</li>
<li>Topical atropine dilates the pupil and stabilises the blood-aqueous barrier (AAEP review).</li>
<li>Uveitis is usually treated with oral anti-inflammatories and steroid eye drops (Liverpool Leahurst).</li>
<li>Systemic antibiotics for suspected leptospirosis have questionable penetration of the eye and minimal effect on vision (AAEP review).</li>
<li>For frequent recurrences, advanced options such as implants or surgery are described (AAEP review).</li>
</ul>
<h2>Monitoring (AAEP review)</h2>
<ul>
<li>Therapy is tapered and stopped 2 to 4 weeks after signs resolve, confirmed by an eye recheck.</li>
<li>Watch for general illness during treatment, especially colic or gastrointestinal problems.</li>
<li>Seek veterinary evaluation for any recurrence and avoid self-treating with steroids, since corneal ulcers can look similar; steroid drops can make an ulcer worse (Liverpool Leahurst).</li>
</ul>
<p>The sources reviewed give no set recheck schedule; follow your vet's. Call your vet if the eye worsens or the horse shows colic signs. See <a href="/qa/eye/uveitis-long-term-effects-and-recurrence/">long-term effects</a>.</p>''',
  src=['aaeperu','liveye'], rel=['uveitis-symptoms-and-causes','uveitis-long-term-effects-and-recurrence','how-long-eye-problems-take-to-heal-and-if-worse']),

 dict(slug='uveitis-long-term-effects-and-recurrence', ids=['VET-QA-0066','VET-QA-0079','VET-QA-0071'], urgent=False,
  q='What are the long-term effects of uveitis on vision, and can future episodes be prevented?',
  title='Uveitis: Long-Term Effects and Recurrence',
  meta='Recurrent uveitis is the leading cause of equine blindness. Each episode can add damage such as cataract or glaucoma. Prompt treatment helps preserve vision.',
  short='Recurrent uveitis is the leading cause of blindness in horses, and each episode can cause more damage such as cataracts, glaucoma and retinal detachment. Prompt treatment helps preserve vision. Some horses need long-term maintenance therapy; no sure way to prevent episodes is described.',
  body='''<h2>Long-term effects</h2>
<ul>
<li>Recurrent uveitis is the leading cause of blindness in horses and a common cause of chronic eye pain; each new episode can cause more damage, including iris damage, cataracts, glaucoma and retinal detachment (Liverpool Leahurst).</li>
<li>ERU has a poor long-term prognosis, but prompt diagnosis and treatment can help preserve vision (AAEP review).</li>
<li>In one study of 224 horses (338 eyes), 46.9% of eyes lost vision and 12.1% lost the eye; 60.8% of horses had decreased performance (AAEP review).</li>
<li>End-stage eyes are irreversibly blind (AAEP review).</li>
</ul>
<h2>Preventing future episodes</h2>
<ul>
<li>Horses with frequent recurrences may need long-term maintenance therapy decided by the vet (AAEP review).</li>
<li>Seek veterinary evaluation for any recurrence and avoid self-treating with steroids (AAEP review).</li>
<li>The review does not give a prevention protocol, and it says leptospiral vaccination as adjunctive therapy is not supported. Ask your vet what applies to your horse.</li>
<li>Breeding horses with ERU is not recommended (AAEP review).</li>
</ul>
<p>See <a href="/qa/eye/uveitis-treatment-and-monitoring/">treatment and monitoring</a>.</p>''',
  src=['liveye','aaeperu'], rel=['uveitis-symptoms-and-causes','uveitis-treatment-and-monitoring','cloudy-eye-causes-and-vision']),

 dict(slug='cloudy-eye-causes-and-vision', ids=['VET-QA-0076','VET-QA-0082','VET-QA-0067','VET-QA-0068'], urgent=True,
  q='What causes a cloudy eye in horses, what should I monitor and can it affect vision?',
  title='Cloudy Eye in Horses: Causes and Vision Risks',
  meta='A cloudy or bluish eye usually means corneal swelling from ulcers, uveitis, infection or other causes. It needs a vet exam; delay can cost vision.',
  short='A bluish or cloudy eye usually reflects corneal swelling (edema), which can follow ulcers, uveitis, keratitis or other problems. Cloudiness with pain, squinting or discharge needs a veterinarian right away because delay can cost vision. Only an eye exam can find the cause.',
  body='''<h2>Possible causes</h2>
<ul>
<li>A blue cornea is corneal edema (swelling) (ACVS).</li>
<li>Keratitis (corneal inflammation) causes a cloudy corneal appearance and is often painless; causes include infection or the immune system attacking corneal cells (Veterinary Vision Center).</li>
<li>Corneal ulcers, and cataracts linked to long-term uveitis (Liverpool Leahurst).</li>
<li>EQUUS lists trauma, uveitis, ulcers, conjunctivitis, stromal abscesses, tumors and glaucoma among eye problems and says an ophthalmic exam is needed to find the cause.</li>
</ul>
<h2>What to watch for</h2>
<p>Squinting or not fully opening the eye, drooping eyelashes, swelling, rubbing, and thick, yellow or bloody discharge, or a color change in the eye (EQUUS; Liverpool Leahurst).</p>
<h2>Vision</h2>
<p>Severe keratitis can cause visual impairment from scarring, and uveitis can lead to cataracts and glaucoma (Veterinary Vision Center). Outcome depends on the cause. <strong>Call your veterinarian right away</strong> for any cloudy eye, and do not apply leftover medication. See <a href="/emergency/eye-injury/">eye injury emergency guide</a>.</p>''',
  src=['acvseye','vvc','liveye','equuseye'], rel=['signs-of-serious-eye-problems','uveitis-symptoms-and-causes','corneal-ulcer-causes-and-treatment']),

 dict(slug='watery-eye-causes-and-home-care', ids=['VET-QA-0083','VET-QA-0065'], urgent=True,
  q='What can cause a horse\'s eye to water, and what home care is appropriate?',
  title='Watery Eyes in Horses: Causes and Home Care',
  meta='Watery eyes can come from irritants, a blocked tear duct, conjunctivitis or a scratch. Gentle wiping and a fly mask help; thick or bloody discharge needs a vet.',
  short='Causes include dust, wind and flies, a blocked tear duct, conjunctivitis, corneal scratches and uveitis. For mild clear discharge, wipe gently with a clean damp cloth or sterile saline, use low-dust hay and a fly mask, and apply no medication unless your vet directs. Painful or thick discharge needs a vet.',
  body='''<h2>Causes (EQUUS)</h2>
<ul>
<li>Irritants such as wind, dust, flies and pollen: clear discharge from both eyes, with squinting or extra blinking.</li>
<li>A blocked tear duct: excess watering without obvious irritation.</li>
<li>Conjunctivitis (inflamed eyelid lining) from infection, injury or allergies.</li>
<li>A corneal scratch: cloudy or bluish surface, pain, squinting and thick discharge; these can worsen quickly.</li>
<li>Equine recurrent uveitis: light sensitivity, heavy tearing and painful squinting.</li>
</ul>
<h2>Home care for mild clear discharge (EQUUS)</h2>
<ul>
<li>Wipe with a clean damp cloth or sterile saline from the inner corner outward, using a fresh wipe for each eye; avoid touching the eye or using cotton swabs.</li>
<li>Do not apply ointments or over-the-counter medication unless your vet directs you to.</li>
<li>Use low-dust hay and bedding and keep the barn ventilated; use a fly mask in warm months.</li>
<li>Clean the skin under the eyes where tears run and coat it with petroleum jelly, or use a cream your vet prescribes.</li>
</ul>
<p>Mild tearing is usually not serious, but <strong>call your veterinarian</strong> for squinting, a cloudy eye, swelling, or thick, yellow or bloody discharge. See <a href="/qa/eye/watery-eye-vet-exam-and-treatment/">when to have the eye examined</a>.</p>''',
  src=['equusweepy','equuseye'], rel=['watery-eye-vet-exam-and-treatment','signs-of-serious-eye-problems','cloudy-eye-causes-and-vision']),

 dict(slug='watery-eye-vet-exam-and-treatment', ids=['VET-QA-0074','VET-QA-0075','VET-QA-0088','VET-QA-0072'], urgent=True,
  q='How soon should a watery eye be examined, how is it treated and can it be prevented from recurring?',
  title='Watery Eye: Vet Exam, Treatment and Recurrence',
  meta='Most eye problems are treated as emergencies, so have a watery eye checked promptly. A blocked tear duct is flushed by a vet; it may re-block in some horses.',
  short='EQUUS says most eye problems are treated as emergencies, so have a veterinarian check a watery eye promptly; no specific time window is given. A blocked tear duct is flushed with saline by a vet, and some horses re-block within days. A fly mask and low-dust housing help limit irritation.',
  body='''<h2>How soon to have it examined</h2>
<p>Mild tearing is usually not serious and can often be managed at home, but most eye problems are treated as emergencies, so have a vet check the horse promptly to rule out something more serious; delays risk vision loss (EQUUS). The article says "right away" but gives no specific time window. Tearing, bleeding or uneven eye opening should prompt an immediate call (The Horse). A vet exam is the way to tell a blocked duct from a painful eye.</p>
<h2>Treatment (EQUUS)</h2>
<ul>
<li>Blocked tear duct: the vet passes a small tube up through the nose into the duct and flushes it with saline.</li>
<li>Irritation or conjunctivitis: treatment depends on the cause; the vet may prescribe a cream.</li>
<li>Corneal scratches and uveitis need specific veterinary treatment; see <a href="/qa/eye/corneal-ulcer-causes-and-treatment/">corneal ulcers</a> and <a href="/qa/eye/uveitis-treatment-and-monitoring/">uveitis treatment</a>.</li>
</ul>
<h2>Preventing recurrence (EQUUS)</h2>
<ul>
<li>Some horses never have a blocked duct again after flushing; others re-block within days. If blockages keep returning, the owner may choose to leave the duct blocked, which the article says causes no harm over the long term.</li>
<li>Low-dust hay and bedding, a ventilated barn and a fly mask reduce irritation.</li>
</ul>
<p>The article gives no steps to prevent a duct from blocking in the first place.</p>''',
  src=['equusweepy','horseeye'], rel=['watery-eye-causes-and-home-care','signs-of-serious-eye-problems','preventing-eye-injuries-and-eye-problems']),

 dict(slug='corneal-ulcer-causes-and-treatment', ids=['VET-QA-0131','VET-QA-0103','VET-QA-0141'], urgent=True,
  q='What causes corneal ulcers in horses and how are they treated?',
  title='Corneal Ulcers in Horses: Causes and Treatment',
  meta='Corneal ulcers come from trauma, foreign bodies or other damage and can become infected. Treatment is vet-directed eye drops, pain relief and sometimes surgery.',
  short='A corneal ulcer is damage to the cornea, the most common eye injury, often from trauma or foreign material. Treatment is veterinary: anti-inflammatories, pupil-dilating drops and antibiotic or antifungal drops, and surgery for deep ulcers. Corticosteroid drops can make an ulcer worse.',
  body='''<h2>Causes</h2>
<ul>
<li>A corneal ulcer is the most common eye injury; "ulcer" means the cornea is damaged, not an open sore (The Horse).</li>
<li>Foreign bodies such as plant material or metal, and trauma (ACVS); orbital fractures can damage the nerve to the cornea; a disrupted tear film can allow fungal infection (ACVS).</li>
<li>Ulcers easily trap bacteria or fungi from the environment and can deepen (The Horse). Ulcers are not caused by bacteria, but bacteria can stop them healing (Liverpool Leahurst).</li>
<li>Dry eye from nerve or sinus damage can impair healing (The Horse).</li>
</ul>
<h2>Treatment (veterinary)</h2>
<ul>
<li>Medical: anti-inflammatory drugs for pain, pupil dilation to ease iris spasm, topical antibiotics or antifungals, and anti-collagenase serum for melting ulcers; medication may go through a tube placed in the eyelid (ACVS).</li>
<li>Diagnosis uses fluorescein dye, which stains green where the cornea is damaged; a typical course is 5 to 7 days of antibiotic eye drops plus oral anti-inflammatories (Liverpool Leahurst).</li>
<li>Surgical options include conjunctival flap grafts for deep defects, suturing of lacerations and foreign body removal (ACVS).</li>
<li>Corticosteroid eye drops can make an ulcer worse; check with a vet before using any drops (Liverpool Leahurst).</li>
</ul>
<p>"Any corneal injury needs veterinary attention" (ACVS). Keep the horse stalled or use a fly mask to shield the eye from light and insects while waiting (The Horse). See <a href="/qa/eye/can-corneal-ulcers-cause-blindness/">blindness risk</a> and the <a href="/emergency/eye-injury/">eye injury emergency guide</a>.</p>''',
  src=['horseeye','acvseye','liveye'], rel=['can-corneal-ulcers-cause-blindness','how-long-eye-problems-take-to-heal-and-if-worse','signs-of-serious-eye-problems']),

 dict(slug='can-corneal-ulcers-cause-blindness', ids=['VET-QA-0099'], urgent=True,
  q='Can corneal ulcers in horses lead to blindness?',
  title='Can a Corneal Ulcer Cause Blindness in a Horse?',
  meta='Yes, in severe cases: deep infected ulcers can perforate or scar the cornea, and the eye may need removal. Early, aggressive treatment helps the outlook.',
  short='Yes. Deep or infected ulcers can melt, perforate or scar the cornea, and in severe cases the eye cannot be saved. ACVS says bacterial and fungal ulcers have a favorable outlook if recognized early and treated aggressively, so call your veterinarian right away.',
  body='''<h2>How an ulcer can threaten sight</h2>
<ul>
<li>Infection can make an ulcer deeper and worse, even leading to perforation or rupture of the eye; in severe cases vets often cannot save the eye and must remove it (The Horse).</li>
<li>Severe infections can cause vision loss through scarring or other complications (Veterinary Vision Center).</li>
<li>A melting ulcer can progress to a full-thickness hole, which needs emergency surgical repair (ACVS).</li>
</ul>
<h2>Outlook (ACVS)</h2>
<ul>
<li>Bacterial and fungal ulcers: favorable if recognized early and treated aggressively.</li>
<li>Deep ulcers and grafts: good to guarded; scarring is common but usually does not affect vision.</li>
<li>Perforation from infection: guarded without immediate surgery; from trauma: poor.</li>
</ul>
<p><strong>Call your veterinarian right away</strong> for squinting, tearing, a cloudy eye or a closed eye; early treatment improves the outcome. See <a href="/qa/eye/corneal-ulcer-causes-and-treatment/">causes and treatment</a>.</p>''',
  src=['horseeye','vvc','acvseye'], rel=['corneal-ulcer-causes-and-treatment','how-long-eye-problems-take-to-heal-and-if-worse','signs-of-serious-eye-problems']),

 dict(slug='signs-of-serious-eye-problems', ids=['VET-QA-0078'], urgent=True,
  q='What are signs of more serious eye conditions in horses?',
  title='Signs of Serious Eye Problems in Horses',
  meta='Squinting, a closed eye, cloudiness, swelling, drooping lashes, color change or thick, bloody discharge: call your vet right away. Eyes are emergencies.',
  short='Warning signs include squinting or a partly closed eye, cloudiness or color change, eyelid or facial swelling, drooping eyelashes, and thick, yellow or bloody discharge. EQUUS says eye problems are nearly always emergencies, so call your veterinarian right away.',
  body='''<h2>Signs (EQUUS; The Horse; Liverpool Leahurst)</h2>
<ul>
<li>Squinting, frequent blinking or not fully opening the eye; reluctance to go from dark to bright areas.</li>
<li>Eyelashes pointing down instead of straight out, which can mean pain or swelling.</li>
<li>Cloudy or bluish cornea; red, white or yellow discoloration; unusually small pupil in an inflamed eye.</li>
<li>Swelling of the eyelids or around the eye, or one eye looking smaller.</li>
<li>Heavy tearing, or discharge that is thick, yellowish, creamy or blood-tinged; frequent rubbing.</li>
<li>New growths on or near the eye; any change unusual for that horse.</li>
<li>A nosebleed may indicate sinus trauma affecting the eye (The Horse).</li>
</ul>
<h2>What to do</h2>
<p>Eye problems are nearly always emergencies because they can be very painful, progress quickly and cause permanent vision loss (EQUUS). Contact your veterinarian as soon as you notice a problem, leave the eye alone until your vet advises, and do not try to remove embedded objects. Eye injuries make up as many as 10% of equine emergency calls (The Horse). The sources give no severity scale beyond these signs. See the <a href="/emergency/eye-injury/">eye injury emergency guide</a>.</p>''',
  src=['equuseye','horseeye','liveye'], rel=['corneal-ulcer-causes-and-treatment','cloudy-eye-causes-and-vision','how-long-eye-problems-take-to-heal-and-if-worse']),

 dict(slug='how-long-eye-problems-take-to-heal-and-if-worse', ids=['VET-QA-0073','VET-QA-0084'], urgent=True,
  q='How long does a horse\'s eye take to heal, and what should I do if the eye gets worse?',
  title='Eye Healing Time and What to Do If It Worsens',
  meta='Healing time depends on the injury and sources give few figures. If an eye worsens or healing stalls, tell your vet; a recheck or new treatment may be needed.',
  short='Healing time depends on the problem: superficial ulcers usually heal quickly while deeper ones heal slowly and in complicated ways. The sources give few timeframes. If an eye worsens or healing seems poor, tell your veterinarian, who may re-examine the eye or change treatment.',
  body='''<h2>Healing time</h2>
<ul>
<li>Superficial ulcers affecting only the outer layer usually heal quickly; deeper ulcers reaching the stroma heal slowly and in complicated ways (The Horse).</li>
<li>One clinic describes a typical ulcer course as a 5 to 7 day course of antibiotic eye drops plus oral anti-inflammatories (Liverpool Leahurst).</li>
<li>For uveitis, therapy is tapered and stopped 2 to 4 weeks after signs resolve, confirmed by a recheck (AAEP review).</li>
<li>Corneal lacerations present for more than two weeks have a poorer prognosis (ACVS).</li>
</ul>
<p>The Horse gives no healing timeframes, and the sources reviewed give no timeline for most eye problems.</p>
<h2>If the eye gets worse</h2>
<p>If healing seems poor or the eye worsens, tell your veterinarian, who may recommend a follow-up exam or a different or added treatment (EQUUS). Do not start leftover ointment or adjust medication on your own, since some can worsen certain conditions. Call right away for increased squinting, swelling, a color change, or heavier discharge. See <a href="/qa/eye/signs-of-serious-eye-problems/">signs of serious eye problems</a>.</p>''',
  src=['horseeye','liveye','aaeperu','acvseye','equuseye'], rel=['signs-of-serious-eye-problems','corneal-ulcer-causes-and-treatment','uveitis-treatment-and-monitoring']),

 dict(slug='common-treatments-for-eye-problems', ids=['VET-QA-0077','VET-QA-0087'], urgent=True,
  q='What treatments are available for eye conditions in horses?',
  title='Treatments for Eye Conditions in Horses',
  meta='Treatment depends on the diagnosis: eye drops, pain relief, flushing a tear duct or surgery, all decided by a vet. Never use leftover or borrowed eye ointment.',
  short='Treatment depends on the diagnosis made at a veterinary eye exam: antibiotic or antifungal drops for ulcers, anti-inflammatories for uveitis, flushing for a blocked tear duct, and surgery for deep injuries. Never use leftover or borrowed ointment, since some drops worsen certain conditions.',
  body='''<h2>By condition (veterinary treatment)</h2>
<ul>
<li>Corneal ulcers: antibiotic eye drops and pain medication; deep or infected ulcers may need grafting surgery (Veterinary Vision Center; ACVS).</li>
<li>Uveitis: anti-inflammatory and pupil-dilating treatment, with rechecks (AAEP review).</li>
<li>Blocked tear duct: flushing with saline by a vet (EQUUS).</li>
<li>Eyelid lacerations need prompt repair to prevent infection and restore eyelid function (Veterinary Vision Center).</li>
</ul>
<h2>Delivering and protecting</h2>
<ul>
<li>For long-term or serious cases, ask about a subpalpebral lavage, a tube placed through an eyelid for giving medication (EQUUS).</li>
<li>Keep the horse stalled and/or use a fly mask to shield the eye from light and insects while waiting for the vet (The Horse).</li>
</ul>
<h2>What not to do (EQUUS)</h2>
<p>Do not start leftover or borrowed ointment without consulting your vet, since some medications can worsen certain conditions (a steroid ointment can worsen a corneal ulcer), and do not try to remove embedded foreign objects. The sources reviewed give no doses. See <a href="/qa/eye/corneal-ulcer-causes-and-treatment/">corneal ulcer treatment</a>.</p>''',
  src=['vvc','acvseye','aaeperu','equusweepy','equuseye','horseeye'], rel=['corneal-ulcer-causes-and-treatment','uveitis-treatment-and-monitoring','signs-of-serious-eye-problems']),

 dict(slug='preventing-eye-injuries-and-eye-problems', ids=['VET-QA-0069','VET-QA-0070','VET-QA-0109'], urgent=False,
  q='How can I prevent eye injuries and eye problems in my horse?',
  title='Preventing Eye Injuries and Eye Problems',
  meta='Check barns, fences and pastures for hazards, feed hay at ground level, control flies and dust, and watch for early signs. Call your vet for any eye change.',
  short='EQUUS advises walking your property for eye hazards such as protruding nails and splintered boards, feeding hay from the ground, removing burrs and prickly weeds, controlling flies with a mask and face-safe repellent, and watching daily for early signs. Call your vet for any injury.',
  body='''<h2>Prevention (EQUUS)</h2>
<ul>
<li><strong>Hazard walk:</strong> spend about an hour looking for broken bucket snaps, bungee hooks, protruding nails and splinters; check trailers, paddocks and run-in sheds, and wood fencing each season and after storms.</li>
<li><strong>Hay:</strong> a high hay rack lets dust and hay fall into the eyes; feeding from the ground protects the eyes and the respiratory system.</li>
<li><strong>Pasture:</strong> remove prickly bushes, weeds and burdock; reduce head-through-fence grazing by providing more forage inside.</li>
<li><strong>Insects:</strong> use a face-safe repellent, consider a fly mask with a barrier and UV protection, and compost manure and clean paddocks daily.</li>
<li><strong>Riding and handling:</strong> slow or stop in wind so the horse can lower his head; go slowly when removing a bridle or halter so straps clear the eye area.</li>
</ul>
<h2>General problems</h2>
<p>Fly masks reduce conjunctivitis, which is common in summer, and early veterinary assessment helps prevent damage and vision loss (Liverpool Leahurst). Check each horse daily for early signs such as squinting, tearing, rubbing or cloudiness.</p>
<h2>If an injury happens</h2>
<p><strong>Call your veterinarian</strong> for any eye injury, even a minor-looking one; move the horse to a quiet, sheltered place, and do not remove an embedded object or use leftover medication (EQUUS). See the <a href="/emergency/eye-injury/">eye injury emergency guide</a> and <a href="/qa/eye/signs-of-serious-eye-problems/">signs of serious eye problems</a>.</p>''',
  src=['equusprev','liveye'], rel=['signs-of-serious-eye-problems','watery-eye-vet-exam-and-treatment','common-treatments-for-eye-problems']),
]
