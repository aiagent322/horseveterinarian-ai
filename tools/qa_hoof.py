# -*- coding: utf-8 -*-
"""Hoof care, farrier and hoof-balance Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'purdue': ('Purdue University Veterinary Hospital — Equine Hoof Abscesses', 'https://www.vet.purdue.edu/hospital/equine/tips/equine-hoof-abscesses.php'),
 'whw': ('World Horse Welfare — Hoof abscesses in horses', 'https://worldhorsewelfare.org/advice/hoof-abscesses-in-horses'),
 'equimedint': ('EquiMed — Importance of Proper Trimming and Shoeing Intervals for Horses', 'https://equimed.com/news/health/importance-of-proper-trimming-and-shoeing-intervals'),
 'kerhoof': ('Kentucky Equine Research — Look to Excellent Nutrition for Better Hoof Quality (industry source; page promotes a branded supplement)', 'https://ker.com/?p=13726'),
 'horsebal': ('The Horse — Hoof balance and trimming schedules', 'https://thehorse.com/?p=16080'),
 'hhbalance': ('Horse & Hound — Understanding hoof balance', 'https://www.horseandhound.co.uk/horse-care/horse-care-tips/understanding-hoof-balance-47715'),
 'acvslam': ('American College of Veterinary Surgeons — Laminitis in Horses', 'https://acvs.org/?p=6108'),
 'equuslife': ('EQUUS — Life after Equine Laminitis', 'https://equusmagazine.com/horse-care/life-after-equine-laminitis-8484'),
})
HELD = {
 'VET-QA-0159':'"specific hoof care products" question; no source reviewed recommends products',
 'VET-QA-0173':'"specific treatment plan" with no condition named in the record',
 'VET-QA-0163':'cracked heels = scratches/pastern dermatitis; covered at /qa/skin/ scratches pages (avoids near-duplicate)',
 'VET-QA-0179':'cracked heels = scratches; see /qa/skin/preventing-scratches/',
 'VET-QA-0191':'cracked heels = scratches; see /qa/skin/scratches-treatment-and-recovery-time/',
}
PAGES = [
 dict(slug='how-often-to-trim-or-shoe-a-horse', ids=['VET-QA-0167','VET-QA-0168','VET-QA-0169','VET-QA-0170','VET-QA-0171'], urgent=False,
  q='How often should a horse\'s hooves be trimmed, shod or checked by a farrier?',
  title='How Often Should Hooves Be Trimmed or Shod?',
  meta='Farrier visits typically run every 5 to 8 weeks. Light-work horses may go 10 to 12, performance horses 5 to 7. Growth, footing and workload shift it.',
  short='EquiMed says farriers typically visit every 5 to 8 weeks, and shoes may be reset every 4 to 14 weeks, averaging 6 to 10. The Horse gives 10 to 12 weeks for horses in light work and 5 to 7 for performance horses. Your farrier sets the schedule for your horse.',
  body='''<h2>Typical intervals</h2>
<ul>
<li>Farrier visits are typically every 5 to 8 weeks, depending on the horse's needs, growth rate and whether it is shod or just trimmed (EquiMed).</li>
<li>Shoes may be reset or replaced every 4 to 14 weeks, with 6 to 10 weeks as the average (EquiMed).</li>
<li>Horses not ridden or in light work: every 10 to 12 weeks; performance horses: every 5 to 7 weeks (The Horse).</li>
<li>Fast-growing, unbalanced feet can develop overly long toes within 3 to 4 weeks, while balanced feet with good conformation may go two months or longer (EquiMed).</li>
</ul>
<h2>What changes the interval</h2>
<p>Hoof growth rate (about ¼ to ⅜ inch a month, varying by horse), balance, workload, footing (soft or wet ground wears little; gravel wears more), hoof toughness, season and shoe wear (EquiMed). Young horses grow faster, and hooves grow slower in cold months (The Horse).</p>
<p>Check and clean the feet between visits. The sources reviewed do not cover thin-walled hooves specifically; ask your farrier how often your horse needs a visit. See <a href="/qa/hoof/signs-of-hoof-problems-and-when-to-call/">signs to call the farrier sooner</a>.</p>''',
  src=['equimedint','horsebal'], rel=['signs-of-hoof-problems-and-when-to-call','improving-hoof-health-and-strength','hoof-imbalance-signs-and-effects']),

 dict(slug='signs-of-hoof-problems-and-when-to-call', ids=['VET-QA-0177','VET-QA-0178'], urgent=True,
  q='What are common signs of hoof problems in horses?',
  title='Signs of Hoof Problems in Horses',
  meta='Call the farrier sooner for long toes, cracks, loose shoes, thrush or white line disease. A tender or lame horse needs a veterinarian, not just a trim.',
  short='Signs include toes growing too long, feet out of balance, chipped or cracked walls, loose or missing shoes, thrush and white line disease. A horse that becomes tender or lame needs prompt attention, and sudden severe lameness or heat in the hoof means call your veterinarian.',
  body='''<h2>Signs to call the farrier sooner (EquiMed)</h2>
<ul>
<li>Toes growing too long, or feet that look out of balance.</li>
<li>Hoof walls growing down around the shoe at the heels.</li>
<li>Loose, worn or missing shoes, or protruding nails.</li>
<li>Chipped or cracked walls, or cracks extending up the wall.</li>
<li>Thrush (dark, grimy, foul-smelling secretions in the frog clefts) or white line disease.</li>
<li>A horse that becomes tender or lame, especially on rocky ground.</li>
</ul>
<h2>Other problems to watch for (The Horse)</h2>
<p>Hoof cracks, sole bruises, abscesses, thrush, white line disease or gravel, hot or close nails and corns.</p>
<h2>When it is a vet problem</h2>
<p><strong>Call your veterinarian</strong> for sudden lameness, a horse that will not bear weight, heat in the hoof or a bounding digital pulse; these can mean an abscess, laminitis or a fracture (World Horse Welfare). See <a href="/qa/lameness/when-to-call-the-vet-for-hoof-problems/">when to call the vet for hoof problems</a>.</p>''',
  src=['equimedint','horsebal','whw'], rel=['how-often-to-trim-or-shoe-a-horse','hoof-abscess-causes-and-prevention','hoof-imbalance-signs-and-effects']),

 dict(slug='hoof-abscess-causes-and-prevention', ids=['VET-QA-0176','VET-QA-0164','VET-QA-0165'], urgent=False,
  q='What causes hoof abscesses, and how can I prevent them?',
  title='Hoof Abscess Causes and Prevention',
  meta='Bacteria enter through a sole puncture, diseased white line or bruise. Routine farrier care and avoiding wet-dry swings help prevent abscesses.',
  short='Bacteria usually enter through a sole puncture or a diseased white line, and a sole bruise can lead to one. Risk rises with thin soles, Cushing\'s disease, laminitis and swings between very wet and dry ground. Routine farrier care and clean, dry footing help prevent them.',
  body='''<h2>Causes and risk factors</h2>
<ul>
<li>Bacteria enter the hoof, usually through a sole puncture or a diseased white line; a sole bruise can also lead to an abscess (Purdue).</li>
<li>Fluid builds inside the hoof capsule, raising pressure and causing severe pain (Purdue).</li>
<li>Weakened structures: a stretched white line, seedy toe, puncture wounds (such as badly placed shoe nails), small cracks and bruising from stones (World Horse Welfare).</li>
<li>Other risk factors: thin soles, Cushing's disease (PPID), laminitis, swings between very wet and very dry conditions, overgrown flaring hooves and poor nutrition (World Horse Welfare).</li>
</ul>
<p>Often there is no obvious reason. Abscesses are more common in front feet than hind feet.</p>
<h2>Prevention</h2>
<ul>
<li>Routine farrier care to keep feet well trimmed, lowering the risk of white line separation and thrush (Purdue).</li>
<li>Pick out hooves regularly to remove stones, and consider shoes for thin-soled horses (Purdue).</li>
<li>Avoid repeated exposure to very wet, muddy ground alternating with dry stables; brush off mud rather than rinsing it, and provide hardstanding and shelter (World Horse Welfare).</li>
<li>Work with a nutritionist or vet on diet, and monitor horses with thin soles, Cushing's disease or laminitis.</li>
</ul>
<p>The sources note there is no sure way to prevent all abscesses. Repeated abscesses should be investigated by your vet. See <a href="/qa/lameness/hoof-abscess-signs-and-treatment/">signs and treatment</a>.</p>''',
  src=['purdue','whw'], rel=['hoof-abscess-complications-and-monitoring','signs-of-hoof-problems-and-when-to-call','improving-hoof-health-and-strength']),

 dict(slug='hoof-abscess-complications-and-monitoring', ids=['VET-QA-0160','VET-QA-0182','VET-QA-0172','VET-QA-0185'], urgent=True,
  q='Can a hoof abscess cause complications, and how do I tell if it is improving or getting worse?',
  title='Hoof Abscess Complications and Worsening Signs',
  meta='Untreated abscesses can infect the coffin bone or damage the hoof wall. Relief after a burst is a good sign; fever or poor appetite means call your vet.',
  short='Complications include a burst at the coronary band, infection of the coffin bone (pedal osteitis) and damage to the bone or hoof wall if untreated. Lameness usually eases once an abscess bursts. Fever, loss of appetite or spreading swelling are reasons to call your veterinarian.',
  body='''<h2>Complications</h2>
<ul>
<li>The fluid may burst out at the coronary band, leaving a temporary defect, or through the sole (Purdue).</li>
<li>In severe cases the coffin bone becomes infected (pedal osteitis); without treatment, the coffin bone or hoof wall can be damaged (Purdue).</li>
<li>Swelling can run from the coronary band up to the knee or hock (Purdue).</li>
<li>Cushing's disease can cause recurrent abscesses and other infections (World Horse Welfare).</li>
</ul>
<h2>Improving</h2>
<p>Once the abscess bursts the horse usually gets immediate relief and lameness improves; the area must be kept clean until fully healed (World Horse Welfare). Purdue gives no monitoring checklist.</p>
<h2>Worsening: call your veterinarian</h2>
<p>The sources reviewed list no formal worsening signs. World Horse Welfare names a raised temperature and loss of appetite as signs of severe pain, and similar signs can come from tendon injuries, laminitis or fractures. Call your vet for a horse that is not improving, has swelling above the hoof, a fever, or is unable to bear weight, and for any recurrent abscess. Purdue calls abscesses "rarely life-threatening" but advises prompt evaluation. See <a href="/qa/hoof/hoof-abscess-causes-and-prevention/">causes and prevention</a>.</p>''',
  src=['purdue','whw'], rel=['hoof-abscess-causes-and-prevention','signs-of-hoof-problems-and-when-to-call','rotated-coffin-bone-treatment-and-outlook']),

 dict(slug='improving-hoof-health-and-strength', ids=['VET-QA-0156','VET-QA-0157','VET-QA-0161','VET-QA-0174','VET-QA-0188'], urgent=False,
  q='How can I strengthen my horse\'s hooves and improve hoof health, including diet and living conditions?',
  title='Strengthening Hooves: Diet, Care and Living Conditions',
  meta='Good hooves come from balanced feed with enough energy and protein, regular farrier care, clean dry footing and exercise. Results take at least 6 to 12 months.',
  short='Hoof quality starts with a balanced diet: enough energy first, then good-quality protein and minerals. Add regular farrier care, regular exercise, clean footing and avoiding swings between wet and dry. KER says building strong hooves takes at least six to twelve months.',
  body='''<h2>Diet (Kentucky Equine Research; The Horse)</h2>
<ul>
<li>Check total energy intake first: horses in negative energy balance break down protein, which can cause a secondary shortfall.</li>
<li>The hoof wall is about 93% protein; protein-deficient diets reduce growth and cause splitting and cracking.</li>
<li>Use feeds balanced for minerals; zinc, calcium and vitamin A are named as important, with no amounts given.</li>
<li>Extra fat had little effect on hoof growth rate or strength.</li>
<li>Hoof growth is slow: months pass before current diet shows in the feet, and building strong hooves takes at least six to twelve months.</li>
</ul>
<p>The KER page is an industry source that promotes a branded supplement, so treat that recommendation as promotional. See <a href="/qa/hoof/hoof-supplements-and-biotin/">supplements and biotin</a>.</p>
<h2>Care and living conditions</h2>
<ul>
<li>Regular trimming or shoeing and cleaning the feet (EquiMed).</li>
<li>Regular exercise tends to mean healthier hooves; soft, grassy pasture wears hooves less than hard, rocky ground (The Horse).</li>
<li>Avoid repeated swings between very wet, muddy ground and dry stabling; brush off mud and provide hardstanding and shelter (World Horse Welfare).</li>
<li>Hot, dry climates can make horn brittle, and harsh dressings can dry out the outer horn (KER).</li>
</ul>
<p>The sources reviewed give no specific diet plan or product recommendations; ask your vet or an equine nutritionist.</p>''',
  src=['kerhoof','horsebal','equimedint','whw'], rel=['hoof-supplements-and-biotin','how-often-to-trim-or-shoe-a-horse','hoof-abscess-causes-and-prevention']),

 dict(slug='hoof-supplements-and-biotin', ids=['VET-QA-0175','VET-QA-0190'], urgent=False,
  q='Should I consider supplements for hoof health, and which help?',
  title='Hoof Supplements and Biotin: What the Evidence Says',
  meta='Biotin helped some horses in studies but not all, and it only affects new hoof growth. Fix the diet and farrier care first, then ask your vet about supplements.',
  short='Biotin has helped some horses in studies but not all, and it only affects newly grown horn, so changes take months. KER suggests trying biotin, methionine and zinc if hooves stay poor despite good feed and farrier care. Check the diet first and ask your vet.',
  body='''<h2>What the sources say (Kentucky Equine Research)</h2>
<ul>
<li>Biotin is the most studied hoof nutrient. Supplemental biotin helped some horses but not all; a failure in one horse does not predict failure in another.</li>
<li>Biotin only affects new horn, so changes near the coronary band can take several weeks to appear, and a German study saw improvement after eight to 15 months.</li>
<li>In that study, hoof condition worsened in seven of 10 horses when supplementation was reduced or stopped, and horn growth rate was the same in treated and control horses.</li>
<li>Most commercial hoof supplements contain methionine; zinc, calcium and vitamin A are also named.</li>
<li>If hooves remain poor despite good feed and farrier care, the page suggests trying biotin, methionine and zinc.</li>
</ul>
<p>The KER page is an industry source that also promotes a branded product, and it gives no doses for the other nutrients. Check that the basic diet is balanced first, and ask your veterinarian or nutritionist before adding a supplement. See <a href="/qa/hoof/improving-hoof-health-and-strength/">improving hoof health</a>.</p>''',
  src=['kerhoof'], rel=['improving-hoof-health-and-strength','how-often-to-trim-or-shoe-a-horse']),

 dict(slug='rotated-coffin-bone-treatment-and-outlook', ids=['VET-QA-0180','VET-QA-0186','VET-QA-0184','VET-QA-0162'], urgent=False,
  q='What are the treatment options, long-term effects, signs of improvement and diet for a rotated coffin bone?',
  title='Rotated Coffin Bone: Treatment, Outlook and Diet',
  meta='A rotated coffin bone (founder) is permanent. Care combines treating the cause, pain control, farrier work and a low-starch diet. Many become pasture sound.',
  short='Founder is considered permanent because laminae do not regrow. Care combines treating the cause, pain control, therapeutic trimming or shoeing guided by radiographs, and a low-starch diet. Many horses reach pasture soundness; some need lifelong care. Your vet and farrier plan it together.',
  body='''<h2>Treatment (ACVS; EQUUS)</h2>
<ul>
<li>Treat the underlying cause immediately, with intensive anti-inflammatory and pain control, cold therapy and careful nursing (ACVS).</li>
<li>Once stable, focused hoof care such as trimming, deep or sand bedding, sole pads, boots and special shoeing to restore alignment (ACVS).</li>
<li>Radiographs give a baseline for tracking progress and guide shoeing decisions such as breakover and heel support (EQUUS).</li>
</ul>
<h2>Long-term outlook</h2>
<ul>
<li>Dead laminae do not regrow, and a displaced bone permanently changes the hoof's structure; some horses need lifelong therapy (EQUUS).</li>
<li>Mild cases may return to work; a more common best case is a pasture-sound horse (ACVS). Severe, uncontrolled cases may lead to euthanasia being considered.</li>
<li>Possible complications include laminitis in the opposite limb, repeated flare-ups and hoof abscesses (ACVS).</li>
</ul>
<h2>Signs of improvement (EQUUS)</h2>
<p>Growth rings become more even from heel to toe, the wall grows out evenly and existing cracks grow out; in low-grade cases the sole thickens. The best-case X-ray shows no movement of the coffin bone. ACVS gives no specific improvement signs.</p>
<h2>Diet (ACVS)</h2>
<p>A low carbohydrate and starch diet, limited grass intake especially in spring, and soaked or steamed hay for laminitis-prone horses. The sources give no specific plan. See <a href="/qa/lameness/laminitis-treatment-options/">laminitis treatment options</a> and <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</p>''',
  src=['acvslam','equuslife'], rel=['hoof-abscess-complications-and-monitoring','hoof-imbalance-correction-and-prevention','improving-hoof-health-and-strength']),

 dict(slug='hoof-imbalance-signs-and-effects', ids=['VET-QA-0183','VET-QA-0181'], urgent=False,
  q='What are the signs and long-term effects of chronic hoof imbalance?',
  title='Chronic Hoof Imbalance: Signs and Long-Term Effects',
  meta='Imbalance shows as a long toe with low heel, a broken-back pastern angle or uneven feet. Left alone it worsens, with heel bruising, cracks and tendon risks.',
  short='Common signs are a long toe with a low heel and a "broken-back" hoof-pastern angle, or a high heel with a dished toe. Over time this shifts weight to the heel and raises the risk of heel bruising, navicular problems, deep digital tendonitis and hoof cracks. Deviations worsen with neglect.',
  body='''<h2>Signs (The Horse; Horse &amp; Hound)</h2>
<ul>
<li><strong>Long toe, low heel:</strong> common in all types of horses; the pastern-to-hoof angle becomes "broken-back".</li>
<li><strong>High heels with a dished toe:</strong> often seen in young horses.</li>
<li><strong>Side-to-side imbalance:</strong> the outside toe strikes the ground before the heel, loading the lower limb unevenly (Horse &amp; Hound).</li>
<li>Good balance means matching sides, an even front-to-back division, a straight pastern-to-wall line and an easy breakover; a farrier assesses this on flat, level ground.</li>
</ul>
<h2>Long-term effects</h2>
<ul>
<li>Long toe, low heel shifts weight onto the heel, raising the risk of heel bruising, navicular problems and deep digital tendonitis (The Horse).</li>
<li>Imbalances can cause hoof cracks (The Horse).</li>
<li>"All hoof and leg deviations from the ideal get worse with neglect" (The Horse).</li>
<li>Horse &amp; Hound calls imbalance one of the most common problems associated with lameness in the foot.</li>
</ul>
<p>The Horse gives no formal list of signs. Ask your farrier to assess balance. See <a href="/qa/hoof/hoof-imbalance-correction-and-prevention/">correction and prevention</a>.</p>''',
  src=['horsebal','hhbalance'], rel=['hoof-imbalance-correction-and-prevention','how-often-to-trim-or-shoe-a-horse','signs-of-hoof-problems-and-when-to-call']),

 dict(slug='hoof-imbalance-correction-and-prevention', ids=['VET-QA-0187','VET-QA-0166','VET-QA-0158','VET-QA-0189'], urgent=False,
  q='How is chronic hoof imbalance corrected, prevented and monitored?',
  title='Correcting and Preventing Hoof Imbalance',
  meta='Correction is differential trimming, sometimes with shoe changes, and can take three to five shoeing sessions. Regular farrier visits help prevent imbalance.',
  short='Correction usually needs differential trimming of the hoof walls, with or without shoe adjustments, and commonly takes three to five shoeing sessions; some conformation may prevent full correction. Regular farrier care prevents drift. The sources give no exercises or therapies.',
  body='''<h2>Correction (Horse &amp; Hound; The Horse)</h2>
<ul>
<li>Correction generally requires differential trimming of the hoof walls, with or without adjusting the thickness of the branch of the shoe.</li>
<li>It commonly takes three to five shoeing sessions, though a horse with poor conformation may never be fully corrected (Horse &amp; Hound).</li>
<li>Careful trimming can improve high-heel, dished-toe feet but may not fully fix them; in young horses, conformation-related imbalances may be improved within the first year of life, and from about 1 to 3 years managing the defect causes less damage than trying to "fix" it (The Horse).</li>
</ul>
<h2>Prevention and monitoring</h2>
<ul>
<li>Regular farrier visits: fast-growing, unbalanced feet can develop overly long toes within 3 to 4 weeks (EquiMed).</li>
<li>Watch for cracks, sole bruises, abscesses, thrush, white line disease, hot or close nails and corns (The Horse).</li>
<li>Check that toes are not growing long, walls are not growing around the shoe and the horse stays sound (EquiMed).</li>
</ul>
<p>The sources reviewed give no exercises or therapies for chronic imbalance and no expected duration or improvement checklist beyond the above. A farrier and vet should plan it together. See <a href="/qa/hoof/hoof-imbalance-signs-and-effects/">signs and effects</a>.</p>''',
  src=['hhbalance','horsebal','equimedint'], rel=['hoof-imbalance-signs-and-effects','how-often-to-trim-or-shoe-a-horse','rotated-coffin-bone-treatment-and-outlook']),
]
