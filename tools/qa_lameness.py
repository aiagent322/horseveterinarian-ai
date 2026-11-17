# -*- coding: utf-8 -*-
"""Lameness, hoof and limb Q&A. Same rules as qa_colic.py: sourced claims only, no doses, gaps stated."""
import qa_colic as C
S = dict(C.S)
S.update({
 'ucdlam': ('UC Davis Center for Equine Health — Laminitis', 'https://ceh.vetmed.ucdavis.edu/node/3031'),
 'aaeplam': ('AAEP — Laminitis (Andrew H. Parks, Vet MB, Diplomate ACVS)', 'https://aaep.org/issue/laminitis-0'),
 'merlam': ('Merck Veterinary Manual — Laminitis in Horses', 'https://www.merckvetmanual.com/musculoskeletal-system/disorders-of-the-foot-in-horses/laminitis-in-horses'),
 'umnbow': ('University of Minnesota Extension — Bowed tendons in horses', 'https://extension.umn.edu/horse-health/bowed-tendons-horses'),
 'hctend': ('Horse Canada — Tendon injuries (Dr. Judith Koenig, Ontario Veterinary College)', 'https://horse-canada.com/magazine/health/tendon-injuries/'),
 'umnsplint': ('University of Minnesota Extension — Splints and bucked shins in horses', 'https://extension.umn.edu/horse-health/splints-and-bucked-shins-horses'),
 'mosplint': ('University of Missouri Extension — Splints in Horses', 'https://extension.missouri.edu/g2742'),
 'acvskiss': ('American College of Veterinary Surgeons — Overriding/Impinging Dorsal Spinous Processes', 'https://www.acvs.org/?p=14789'),
 'umnback': ('University of Minnesota Extension — Back pain in your horse', 'https://extension.umn.edu/horse-health/back-pain-your-horse'),
 'uconnback': ('UConn Extension — Preventing Back Pain in Horses (EXT121)', 'https://extension.uconn.edu/publication/back-pain-horses/'),
 'horsesusp': ('The Horse — Suspensory Ligament Branch Injuries', 'https://thehorse.com/1104617/suspensory-ligament-branch-injuries/'),
 'umnabs': ('University of Minnesota Open Textbook — Hoof Abscesses (Large Animal Surgery)', 'https://open.lib.umn.edu/largeanimalsurgery/chapter/hoof-abscesses/'),
 'bhsbruise': ('British Horse Society — Bruised sole in horses', 'https://www.bhs.org.uk/horse-care-and-welfare/health-care-management/hoof-care/bruised-sole-in-horses/'),
 'horsehoof': ('The Horse — Understanding and overcoming 7 common equine foot issues', 'https://thehorse.com/1133041/horse-hoof-capsule-conditions/'),
 'hcswell': ('Horse Canada — Swollen legs: causes and cures', 'https://horse-canada.com/magazine/health/swollen-legs-causes-cures/'),
 'horselymph': ('The Horse — Lymphangitis: A Frustrating Condition in Horses', 'https://thehorse.com/?p=48795'),
 'horsesupp': ('The Horse — Oral Joint Supplements: Do They Work? (AAEP Convention)', 'https://thehorse.com/124636/oral-joint-supplements-do-they-work/'),
 'tamuoa': ('Texas A&M Veterinary Medicine — What to Know About Equine Osteoarthritis', 'https://vetmed.tamu.edu/news/pet-talk/what-to-know-about-equine-osteoarthritis/'),
 'aaepjoint': ('AAEP — Joint Medications for Lameness (Espy and Harper, reviewed 2016)', 'https://old.aaep.org/horsehealth/lameness-joint-medications'),
 'hcligament': ('Horse Canada — A long road to recovery: tendon and ligament injuries', 'https://horse-canada.com/magazine/health/a-long-road-to-recovery-tendon-and-ligament-injuries/'),
 'rameyligament': ('Horse Network — Rehabilitating tendon and ligament injuries (David Ramey, DVM, March 2019)', 'https://horsenetwork.com/?p=28150'),
 'kersupp': ('Kentucky Equine Research — Research Update: Joint Supplements for Horses', 'https://ker.com/?p=13515'),
})
HELD = {
 'VET-QA-0293':'generic diet question with no condition named','VET-QA-0302':'generic home pain management; no condition named','VET-QA-0316':'generic activity restriction; no condition named',
 'VET-QA-0318':'generic rest question; no condition named','VET-QA-0319':'generic rest question; no condition named','VET-QA-0364':'generic treatment question; no condition named',
 'VET-QA-0384':'generic pain management; no condition named','VET-QA-0379':'muscle strain rest: no verified source','VET-QA-0382':'muscle strain exercises: no verified source',
 'VET-QA-0339':'neck pain: no verified source',
 'VET-QA-0310':'stifle injury: sources found cover only locked stifle','VET-QA-0315':'stifle injury recovery: no verified source','VET-QA-0324':'stifle injury signs: no verified source',
 'VET-QA-0342':'stifle injury tests: no verified source','VET-QA-0352':'stifle rehab: no verified source','VET-QA-0372':'stifle surgery: no verified source',
 
 
 'VET-QA-0306':'splint prevention: sources give none','VET-QA-0309':'splint prevention: sources give none','VET-QA-0299':'kissing spines prevention: source gives none',
 'VET-QA-0321':'bowed tendon shoeing/padding: source gives none',
}
P = '/qa/lameness/'
PAGES = [
 dict(slug='what-is-laminitis-and-founder', ids=['VET-QA-0345','VET-QA-0346'], urgent=False,
  q='What are laminitis and founder?',
  title='What Are Laminitis and Founder in Horses?',
  meta='Laminitis is injury to the tissue that attaches the hoof wall to the coffin bone. Founder is its most severe form. See causes and why it needs a vet fast.',
  short='Laminitis is injury and swelling of the tissue that attaches the hoof wall to the coffin bone. Founder is the severe form, where the bone can separate from the hoof and rotate. UC Davis calls laminitis irreversible, so treatment aims to limit further damage.',
  body='''<h2>Definitions</h2>
<ul>
<li><strong>Laminitis:</strong> injury and swelling of the tissue that attaches the hoof wall to the coffin bone (UC Davis). The AAEP says it is commonly called founder.</li>
<li><strong>Founder:</strong> the most severe form. When the attachments fail, the coffin bone can separate from the hoof and rotate, causing intense pain (UC Davis).</li>
</ul>
<h2>Causes</h2>
<p>UC Davis lists endocrine disorders, especially EMS and PPID; overloading a healthy leg while the other limb is injured; excess grain or sugar-rich pasture; toxic plants such as black walnut shavings; prolonged work on hard surfaces ("road founder"); and sepsis or systemic inflammation. Merck says endocrine dysfunction is probably the most common underlying cause today. The AAEP also lists illnesses such as diarrhea and retained placenta, and says the exact mechanism is still debated.</p>
<h2>Outlook</h2>
<p>UC Davis says laminitis is irreversible and outcomes vary widely. The AAEP says mild cases may return to work with no visible hoof changes, while severe cases can take months to rehabilitate or lead to euthanasia.</p>
<p>See <a href="/qa/lameness/signs-of-laminitis-and-founder/">signs of laminitis</a>, <a href="/qa/lameness/laminitis-treatment-options/">treatment</a> and <a href="/qa/lameness/preventing-laminitis-and-founder/">prevention</a>.</p>''',
  src=['ucdlam','aaeplam','merlam'], rel=['signs-of-laminitis-and-founder','laminitis-treatment-options','preventing-laminitis-and-founder']),

 dict(slug='signs-of-laminitis-and-founder', ids=['VET-QA-0334','VET-QA-0356','VET-QA-0358','VET-QA-0359','VET-QA-0360','VET-QA-0361'], urgent=True,
  q='What are the signs of laminitis, and what should I watch for as it develops or recovers?',
  title='Signs of Laminitis and Founder in Horses',
  meta='Watch for lameness, reluctance to move, shifting weight, a sawhorse stance, warm hooves and a stronger pulse. Laminitis is an emergency, so call your vet.',
  short='Signs include lameness (often in the front feet), reluctance to move, shifting weight or a sawhorse stance, warm hooves, and faster breathing and heart rate. The AAEP says to treat suspected laminitis as an emergency and call your veterinarian promptly.',
  body='''<h2>Signs (UC Davis and AAEP)</h2>
<ul>
<li>Lameness of varying severity, often in the front feet</li>
<li>Reluctance to move, or reluctance to lie down and get up</li>
<li>Shifting weight between feet, or a "sawhorse stance" with the front feet forward</li>
<li>Warm hooves and an increased digital pulse (AAEP); swollen limbs (UC Davis)</li>
<li>Faster breathing and heart rate (UC Davis)</li>
<li>Mild cases can be hard to detect; severe pain may make a horse reluctant to lift a foot (AAEP)</li>
</ul>
<h2>Signs the problem is progressing or has become chronic</h2>
<p>UC Davis says to watch for hoof changes such as a cleft at the coronary band or a dished shape, and for weight loss. The AAEP says chronic cases show gait changes and abnormally shaped hooves. The AAEP also says the disease is unpredictable and can worsen suddenly, which is why a veterinarian should guide monitoring.</p>
<p>The sources reviewed do not give a day-by-day home checklist. Ask your veterinarian what to track and how often. Horses with PPID or EMS are at higher risk; see <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">laminitis in PPID and EMS</a>.</p>''',
  src=['ucdlam','aaeplam'], rel=['what-is-laminitis-and-founder','laminitis-treatment-options','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='laminitis-treatment-options', ids=['VET-QA-0366','VET-QA-0367'], urgent=False,
  q='What treatments are available for laminitis and founder?',
  title='Laminitis and Founder Treatment Options',
  meta='Treatment focuses on pain control, supportive hoof care and treating the underlying cause, with your vet and farrier working together. See UC Davis and AAEP.',
  short='Treatment centers on pain control, supportive care, hoof support and treating the underlying cause, with the owner, veterinarian and farrier working together. No drug has been proven to stop the disease, according to the AAEP.',
  body='''<h2>Common elements</h2>
<ul>
<li><strong>Find and treat the cause</strong> — for example infection or hormonal disease (AAEP), such as PPID or EMS (UC Davis).</li>
<li><strong>Pain control and supportive care</strong> with anti-inflammatory medication; opiates may be used in serious cases (UC Davis).</li>
<li><strong>Stall rest on deep bedding</strong>, with sling support in severe cases (UC Davis).</li>
<li><strong>Cold therapy</strong> such as ice baths or boots (UC Davis). The AAEP says cooling appears to help most when started early.</li>
<li><strong>Hoof support</strong> — the AAEP describes supporting the sole with sand, deep shavings, foam or silicone padding. Whether to remove shoes is decided case by case.</li>
<li><strong>Farrier work</strong> with X-ray-guided trimming and shoeing (UC Davis). In the chronic stage the AAEP says hoof care is the main approach.</li>
<li><strong>Diet</strong> — low sugar and low calorie, and treatment of the underlying disease (UC Davis).</li>
</ul>
<p>Drug choice and dose are your veterinarian's decisions. The AAEP says no drug has been proven to stop the disease, and that recovery is slow. See <a href="/qa/lameness/signs-of-laminitis-and-founder/">signs of laminitis</a>.</p>''',
  src=['ucdlam','aaeplam'], rel=['what-is-laminitis-and-founder','preventing-laminitis-and-founder','signs-of-laminitis-and-founder']),

 dict(slug='preventing-laminitis-and-founder', ids=['VET-QA-0305','VET-QA-0354','VET-QA-0355'], urgent=False,
  q='How can I prevent laminitis, and what should I feed a horse prone to it?',
  title='Preventing Laminitis and Founder in Horses',
  meta='UC Davis advises limiting sugary pasture, keeping sugar and carbohydrates low in at-risk horses, regular farrier care and a healthy weight. See feeding links.',
  short='UC Davis advises limiting high-sugar pasture, keeping sugar and carbohydrates low in at-risk horses, scheduling regular farrier visits, maintaining a healthy weight and supporting the uninjured limb after an injury.',
  body='''<h2>Prevention steps (UC Davis)</h2>
<ul>
<li>Limit high-sugar pasture, especially for horses with EMS or PPID.</li>
<li>Keep sugar and carbohydrates low in at-risk horses.</li>
<li>Schedule regular farrier visits so hooves stay balanced.</li>
<li>Maintain a healthy weight, using weight tapes or body condition scoring.</li>
<li>Support the uninjured limb after an injury to the opposite leg.</li>
</ul>
<h2>Feeding a horse prone to laminitis</h2>
<p>Merck says diet-related laminitis is thought to result from excessive non-structural carbohydrates (NSC), and that obesity and insulin resistance predispose horses to pasture-associated laminitis. The AAEP lists grain overload and grass high in fructans (a sugar) as triggers. For hay analysis, NSC targets, weighing rations and pasture limits, see <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS and insulin resistance</a>. Ask your veterinarian to test for PPID and EMS in older, overweight or previously laminitic horses.</p>
<p>The sources reviewed give no pasture sugar thresholds. See <a href="/qa/lameness/what-is-laminitis-and-founder/">what laminitis is</a>.</p>''',
  src=['ucdlam','merlam','aaeplam'], rel=['what-is-laminitis-and-founder','signs-of-laminitis-and-founder','laminitis-treatment-options']),

 dict(slug='bowed-tendon-signs-and-seriousness', ids=['VET-QA-0320','VET-QA-0331','VET-QA-0344'], urgent=False,
  q='What is a bowed tendon, what are the signs, and how serious is it?',
  title='Bowed Tendon in Horses: Signs and Seriousness',
  meta='A bowed tendon is swelling in the superficial or deep digital flexor tendon that makes the leg look bowed. See risks, signs and why healing is slow.',
  short='A bowed tendon is swelling in the superficial or deep digital flexor tendon that makes the back of the leg look bowed. The superficial tendon is affected far more often. Healing is slow, and the University of Minnesota says full recovery can take 8 to 11 months.',
  body='''<h2>What it is</h2>
<p>University of Minnesota Extension says a bowed tendon is swelling in the superficial or deep digital flexor tendon, which makes the leg look bowed. The bow can appear anywhere from the knee or hock down to the pastern, and the superficial tendon is affected much more often.</p>
<h2>Signs</h2>
<p>The visible bow is the sign Minnesota describes. Horse Canada (Dr. Judith Koenig, Ontario Veterinary College) says tendon injury produces the classic signs of inflammation: swelling and heat. Pain on touch and lameness are not described on the Minnesota page, so a veterinary exam is needed to judge the injury.</p>
<h2>Risk</h2>
<p>Chronic tendon stress or an injury can cause it. Racehorses, polo ponies and jumpers are at higher risk, and uneven pressure from leg bandages can also cause swelling (Minnesota).</p>
<h2>How serious is it?</h2>
<p>Severity varies, and complete healing takes a long time: Minnesota gives 8 to 11 months for the tendon to repair fully. Premature work can re-injure it. See <a href="/qa/lameness/bowed-tendon-treatment-and-recovery/">treatment and recovery</a>.</p>''',
  src=['umnbow','hctend'], rel=['bowed-tendon-treatment-and-recovery','preventing-tendon-injuries','ligament-injury-signs-and-diagnosis']),

 dict(slug='bowed-tendon-treatment-and-recovery', ids=['VET-QA-0294','VET-QA-0296','VET-QA-0297','VET-QA-0317','VET-QA-0322','VET-QA-0347','VET-QA-0350','VET-QA-0353','VET-QA-0365'], urgent=False,
  q='How is a bowed tendon treated, how long is recovery, and what if it gets worse?',
  title='Bowed Tendon Treatment and Recovery Time',
  meta='Care is complete rest, then a controlled, gradual return to exercise guided by repeat ultrasounds. Minnesota says full recovery can take 8 to 11 months.',
  short='Usual care is complete rest, anti-inflammatory medication and a controlled, gradual return to exercise, guided by repeat ultrasounds. University of Minnesota Extension says full recovery can take 8 to 11 months. Premature work can re-injure the tendon.',
  body='''<h2>Treatment</h2>
<ul>
<li><strong>Complete rest</strong>, then a <strong>controlled, gradual return to exercise</strong>, with anti-inflammatory drugs (Minnesota).</li>
<li><strong>Repeat ultrasounds</strong> help time the return to exercise so it is as fast as possible without re-injury.</li>
<li><strong>Surgery</strong> is sometimes used.</li>
<li><strong>Newer options</strong> such as cell injections and shockwave therapy have pros and cons. Minnesota says most have shown little benefit or possible harm, and rehabilitation may take longer with them.</li>
</ul>
<h2>Recovery time</h2>
<p>Signs may ease within days with rest and anti-inflammatory drugs, but Minnesota says complete repair takes 8 to 11 months. The program is set by your veterinarian for your horse; the sources reviewed give no specific exercises, shoeing or diet changes for a bowed tendon.</p>
<h2>If it worsens</h2>
<p>Premature work or stress can bring the swelling back and re-injure the tendon (Minnesota). If swelling, heat or lameness returns, contact your veterinarian before continuing the program.</p>''',
  src=['umnbow','hctend'], rel=['bowed-tendon-signs-and-seriousness','preventing-tendon-injuries','ligament-injury-signs-and-diagnosis']),

 dict(slug='preventing-tendon-injuries', ids=['VET-QA-0311','VET-QA-0351'], urgent=False,
  q='How can I prevent tendon injuries and bowed tendons?',
  title='How to Prevent Tendon Injuries in Horses',
  meta='Avoid uneven bandage pressure, avoid premature work after injury, and check legs for heat and swelling after work. See what Minnesota and Horse Canada advise.',
  short='Sources reviewed point to a few steps: avoid uneven pressure from leg bandages, avoid premature work after an injury, watch for signs the horse is reaching its limits, and check the legs for heat and swelling after work.',
  body='''<h2>What the sources say</h2>
<ul>
<li><strong>Bandage pressure.</strong> University of Minnesota Extension says uneven pressure from leg bandages can cause swelling.</li>
<li><strong>Do not return to work too soon.</strong> Premature work or stress can re-injure a healing tendon (Minnesota).</li>
<li><strong>Know the horse's limits.</strong> Dr. Judith Koenig (Horse Canada) advises watching for signs the horse is reaching its limits and slowing down, taking a long break or stopping.</li>
<li><strong>Check after work.</strong> Horse Canada describes checking for signs of inflammation again after riding.</li>
</ul>
<p>Minnesota notes racehorses, polo ponies and jumpers are at higher risk. The sources reviewed do not give a full prevention program; ask your veterinarian about conditioning and footing for your discipline. See <a href="/qa/lameness/bowed-tendon-signs-and-seriousness/">signs of a bowed tendon</a>.</p>''',
  src=['umnbow','hctend'], rel=['bowed-tendon-signs-and-seriousness','bowed-tendon-treatment-and-recovery','ligament-injury-signs-and-diagnosis']),

 dict(slug='ligament-injury-signs-and-diagnosis', ids=['VET-QA-0300','VET-QA-0333','VET-QA-0349'], urgent=False,
  q='What are the signs of a ligament injury, how is it diagnosed, and can it cause long-term problems?',
  title='Suspensory Ligament Injury: Signs and Diagnosis',
  meta='Heat, thickening and pain when pressed or flexed can signal a suspensory ligament branch injury. Ultrasound is the main diagnostic tool. See the outlook.',
  short='This page covers suspensory ligament branch injuries, one common ligament injury. Heat, thickening and pain on pressure or flexion are indicators, but lameness does not always occur. Ultrasound is the main tool for diagnosis. Scarring and increased fetlock drop predicted poorer soundness.',
  body='''<p>The source reviewed describes <strong>suspensory ligament branch injuries</strong> specifically; other ligaments may differ.</p>
<h2>Signs (The Horse)</h2>
<ul>
<li>Heat, thickening, and pain when the area is pressed or the leg is flexed.</li>
<li>Lameness does not always occur, so a horse may show no obvious limp.</li>
<li>Inflammation can limit performance, and the injury can sometimes lead to fluid buildup and arthritis in the fetlock.</li>
</ul>
<h2>Diagnosis</h2>
<p>Ultrasound is the main tool for diagnosing and monitoring these injuries; enlargement, scarring and fiber disruption help guide prognosis. Newer options include Doppler ultrasound, tissue characterization, elastography and MRI.</p>
<h2>Long-term outlook</h2>
<p>In show horses lame from a branch injury, about 43% returned to normal work, according to the article. Scarring around the ligament and increased fetlock drop predicted poorer future soundness, and moderate injuries in young Thoroughbreds were linked to a higher risk of reinjury. The article does not cover treatment or rest timelines; your veterinarian sets those.</p>''',
  src=['horsesusp'], rel=['bowed-tendon-signs-and-seriousness','preventing-tendon-injuries','back-pain-causes-and-signs']),

 dict(slug='splints-in-horses', ids=['VET-QA-0329','VET-QA-0337','VET-QA-0348','VET-QA-0371'], urgent=False,
  q='What are splints in horses, how are they treated, and when should I call the vet?',
  title='Splints in Horses: Signs, Treatment and Outlook',
  meta='Splints are inflamed or fractured splint bones beside the cannon bone. Rest and anti-inflammatories are usual, and most horses return to work. See when to call.',
  short='Splints are inflamed or fractured splint bones beside the cannon bone. The area is tender at first, and a hard lump may remain. Usual treatment is rest and anti-inflammatory medication, and most horses return to work.',
  body='''<h2>What they are and the signs</h2>
<p>University of Minnesota Extension says splints are inflamed or fractured splint bones, which lie on either side of the cannon bone. At first the area over the bone is painful to the touch, and the horse may or may not be lame. A permanent hard swelling may remain but usually stops hurting after the early swelling fades. The University of Missouri says lameness is most common in 2-year-olds in training and is most obvious while trotting or working.</p>
<h2>Treatment</h2>
<p>Minnesota says splints are usually treated with rest and anti-inflammatory drugs. Missouri says the horse should be rested on soft ground for at least 30 days, with medication as the veterinarian chooses. Your veterinarian designs the plan.</p>
<h2>Long-term effect on performance</h2>
<p>Most horses with splints recover and return to work (Minnesota). Occasionally a callus forms around a fractured splint bone and damages nearby ligaments behind the cannon bone; surgery may then be needed, and these horses face a greater risk of long-term lameness.</p>
<h2>When to call the vet</h2>
<p>The sources do not list call criteria. Because a splint is either inflamed or fractured bone, and the two are treated differently, have a veterinarian examine any new swelling on the cannon bone, especially if lameness is obvious or the horse will not bear weight.</p>''',
  src=['umnsplint','mosplint'], rel=['bowed-tendon-signs-and-seriousness','ligament-injury-signs-and-diagnosis','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='kissing-spines-signs-and-diagnosis', ids=['VET-QA-0313','VET-QA-0335'], urgent=False,
  q='What are the signs of kissing spines, and how is it diagnosed?',
  title='Kissing Spines in Horses: Signs and Diagnosis',
  meta='Kissing spines means back bone projections sit too close or touch. Signs include bucking, head tossing and canter trouble. See how vets diagnose it.',
  short='Kissing spines occurs when the bony projections on the back vertebrae sit too close together or touch. Signs include bucking, head tossing and trouble with canter transitions, but some horses show no signs. Diagnosis combines a lameness evaluation with imaging.',
  body='''<h2>What it is</h2>
<p>The American College of Veterinary Surgeons (ACVS) says the dorsal spinous processes sit too close together or touch, which can cause bone changes and chronic inflammation. It is most often diagnosed in teenage horses, Thoroughbreds and warmbloods are overrepresented, and the middle to rear thoracic spine under the saddle is most commonly affected. The cause is unknown.</p>
<h2>Signs</h2>
<p>Severity varies widely. Some horses show changes on imaging but no symptoms; others cannot be ridden or are sore under light pressure. Under saddle, common signs include bucking, head tossing, trouble with canter transitions, and refusing or rushing fences. Affected horses may be sensitive to touch or have weak back muscling, and lameness can trigger or worsen back pain.</p>
<h2>Diagnosis</h2>
<p>Because the signs are vague, ACVS says a full lameness evaluation is typically done. Palpation, radiographs, ultrasound and local anesthetic at suspected pain sites may be used, and a bone scan in difficult cases. Imaging must be read alongside the whole horse, since many horses with x-ray changes show no back pain.</p>
<p>See <a href="/qa/lameness/kissing-spines-treatment-and-outlook/">treatment and outlook</a>.</p>''',
  src=['acvskiss'], rel=['kissing-spines-treatment-and-outlook','how-back-pain-is-diagnosed','back-pain-causes-and-signs']),

 dict(slug='kissing-spines-treatment-and-outlook', ids=['VET-QA-0298','VET-QA-0301','VET-QA-0330','VET-QA-0338'], urgent=False,
  q='How is kissing spines treated, and what is the long-term outlook?',
  title='Kissing Spines Treatment and Long-Term Outlook',
  meta='Treatment is multimodal: back-strengthening, therapies, injections and sometimes surgery. ACVS reports 80 to 90% of horses return to some level of performance.',
  short='Management is multimodal and relies heavily on home rehabilitation: stretching and strengthening, therapies, injections, and sometimes surgery. ACVS says that with appropriate therapy and rehabilitation the outlook is excellent, with 80 to 90% of horses returning to some level of performance.',
  body='''<h2>Conservative options (ACVS)</h2>
<ul>
<li>Stretching and strengthening the back and core muscles — the main home exercise approach.</li>
<li>Acupuncture or chiropractic care when a veterinarian recommends it.</li>
<li>Oral muscle relaxants for early spasm, and injections: mesotherapy (shallow injections under the skin) or anti-inflammatories placed near the affected vertebrae or the connecting ligament.</li>
</ul>
<p>Drug choice and dose are decided by your veterinarian. ACVS does not give a specific exercise routine.</p>
<h2>Surgical options</h2>
<ul>
<li><strong>Interspinous ligament desmotomy</strong> cuts the ligament between vertebrae, can be done standing, and about 85 to 90% of horses improve, though some relapse months to years later.</li>
<li><strong>Dorsal spinous process ostectomy</strong> removes a wedge of bone, is more invasive, and is reserved for more severe cases.</li>
</ul>
<h2>Long-term outlook</h2>
<p>Continued rehabilitation at home is key to long-term success, and maintaining muscle strength and spinal flexibility is central. Treating any primary lameness matters, since it can drive or worsen back pain (ACVS).</p>''',
  src=['acvskiss'], rel=['kissing-spines-signs-and-diagnosis','back-pain-treatment-options','how-back-pain-is-diagnosed']),

 dict(slug='back-pain-causes-and-signs', ids=['VET-QA-0325','VET-QA-0328'], urgent=False,
  q='What causes back pain in horses, and what are the signs?',
  title='Back Pain in Horses: Causes and Signs',
  meta='Causes include poor saddle fit, rider imbalance, arthritis, injury and overwork. Signs include cold-backed behavior, head tossing and trouble with leads.',
  short='Causes include poor saddle fit, rider imbalance, joint disease, poor conformation, injury, overwork and training methods. Signs can come and go and include cold-backed behavior, stiffness on turns, trouble changing leads, head tossing and soreness when saddled.',
  body='''<h2>Causes</h2>
<ul>
<li>Joint disease such as arthritis; poor conformation; injury; exercise beyond the horse's condition (University of Minnesota).</li>
<li>Poor saddle fit, rider imbalance and training methods (Minnesota). UConn adds a narrow saddle that pinches the withers, a wide saddle that puts rider weight on the spine, and an uneven rider.</li>
<li>Muscle or ligament strain from fatigue, slips, or poorly executed jumps, and kissing spines (UConn).</li>
<li>Secondary back pain from chronic leg lameness, as the horse compensates (UConn).</li>
</ul>
<h2>Signs</h2>
<p>Minnesota says signs can come and go. They include restricted movement, "cold-backed" behavior, reluctance to work, stiffness on tight turns, unwillingness to change leads, loss of hind-limb drive, soreness when saddled or ridden, and head tossing. UConn also lists bucking on upward transitions, resisting girth tightening or standing for mounting, a short hind stride, and reluctance to back up.</p>
<p>Back pain can look like lameness or refusal to work, so see <a href="/qa/lameness/how-back-pain-is-diagnosed/">how it is diagnosed</a> and <a href="/qa/lameness/when-to-call-the-vet-for-back-pain/">when to call the vet</a>.</p>''',
  src=['umnback','uconnback'], rel=['how-back-pain-is-diagnosed','when-to-call-the-vet-for-back-pain','kissing-spines-signs-and-diagnosis']),

 dict(slug='how-back-pain-is-diagnosed', ids=['VET-QA-0343'], urgent=False,
  q='What diagnostic tests are used for back pain in horses?',
  title='How Vets Diagnose Back Pain in Horses',
  meta='Diagnosis starts with checking saddle fit and ruling out lameness. Vets then use palpation, radiographs, ultrasound and local anesthetics to find the source.',
  short='Start by checking saddle fit, looking for injuries and lameness, and reviewing the training program. A veterinarian can then use palpation, radiographs, ultrasound and local anesthetics to find the source and rule out other causes.',
  body='''<h2>Steps</h2>
<ul>
<li><strong>Owner checks:</strong> saddle fit, injuries and lameness, and the training program (University of Minnesota).</li>
<li><strong>Veterinary exam:</strong> palpation, radiographs, ultrasound and local anesthetics to find the source and rule out other causes (Minnesota).</li>
<li><strong>Rule out lameness first.</strong> UConn says a veterinarian should first rule out lameness or another physical problem, then determine whether the pain comes from soft tissue or bone. ACVS notes that a full lameness evaluation is typically done for suspected kissing spines.</li>
</ul>
<p>Back pain often looks like lameness or refusal to work, so a veterinary exam helps sort out the problem. See <a href="/qa/lameness/back-pain-treatment-options/">treatment options</a>.</p>''',
  src=['umnback','uconnback','acvskiss'], rel=['back-pain-causes-and-signs','back-pain-treatment-options','kissing-spines-signs-and-diagnosis']),

 dict(slug='back-pain-treatment-options', ids=['VET-QA-0295','VET-QA-0363'], urgent=False,
  q='What treatments, exercises or therapies help back pain in horses?',
  title='Back Pain in Horses: Treatment and Therapies',
  meta='Treatment depends on the cause: fix tack, treat lameness first, then options such as medication, injections, chiropractic, shockwave and rehab.',
  short='Treat any underlying lameness or condition first. Options mentioned by university sources include medication, regional steroid injections, chiropractic care, shockwave therapy, aqua treadmill work, adjusting saddle fit, and surgery for some conditions. The right choice depends on the cause.',
  body='''<h2>Options described</h2>
<ul>
<li><strong>Treat the underlying problem first</strong>, such as lameness (UConn).</li>
<li><strong>Medication:</strong> a muscle relaxant combined with an anti-inflammatory, or a regional steroid injection (University of Minnesota). Selection and dosing are for your veterinarian.</li>
<li><strong>Chiropractic care</strong> may relieve pain and loosen muscles, and a chiropractor can suggest daily stretches (Minnesota).</li>
<li><strong>Shockwave therapy</strong> may improve circulation and ease spasms; <strong>aqua treadmill</strong> work may help strengthen back muscles (Minnesota).</li>
<li><strong>Saddle fit and warm-up adjustments</strong> (Minnesota).</li>
<li><strong>Rest, controlled exercise and physiotherapy</strong> for some chronic soft-tissue injuries; surgery for kissing spines and some fractures (UConn).</li>
</ul>
<p>The sources reviewed give no specific exercise routines, durations or recovery timelines. UConn says early detection can lead to complete recovery. See <a href="/qa/lameness/kissing-spines-treatment-and-outlook/">kissing spines treatment</a>.</p>''',
  src=['umnback','uconnback'], rel=['how-back-pain-is-diagnosed','preventing-back-pain','kissing-spines-treatment-and-outlook']),

 dict(slug='preventing-back-pain', ids=['VET-QA-0303'], urgent=False,
  q='How can I prevent back pain in my horse?',
  title='How to Prevent Back Pain in Horses',
  meta='Check that tack fits, build work up gradually, warm up before every ride, keep the horse fit and work on rider balance. See guidance from Minnesota and UConn.',
  short='Check that equipment fits, ease horses into work, warm up before every session, keep the horse fit and well-muscled, and work on rider posture and balance with a qualified instructor or trainer.',
  body='''<h2>Prevention steps</h2>
<ul>
<li><strong>Fit.</strong> Make sure equipment fits and does not interfere with movement; pinching or rubbing can cause abnormal movement that leads to back pain. Use a professional saddle fitter if unsure (University of Minnesota).</li>
<li><strong>Build up gradually.</strong> Ease horses into work, especially those that have been off, are young, old or overweight, asking only for work they are conditioned for (Minnesota).</li>
<li><strong>Warm up</strong> with stretching, bending and loosening (Minnesota).</li>
<li><strong>Keep the horse fit and well-muscled</strong>, since weak horses are more prone to soft-tissue injury (UConn).</li>
<li><strong>Rider balance.</strong> Work with a qualified trainer or instructor on posture and balance (Minnesota; UConn).</li>
</ul>
<p>See <a href="/qa/lameness/back-pain-causes-and-signs/">causes and signs</a>.</p>''',
  src=['umnback','uconnback'], rel=['back-pain-causes-and-signs','back-pain-treatment-options','when-to-call-the-vet-for-back-pain']),

 dict(slug='when-to-call-the-vet-for-back-pain', ids=['VET-QA-0357','VET-QA-0369'], urgent=False,
  q='When should I call the vet for back pain, and what signs mean a re-evaluation?',
  title='When to Call the Vet for Back Pain in Horses',
  meta='UConn says to schedule a vet visit if a horse consistently shows back pain signs. Sources give no emergency criteria, so ask your vet what needs a recheck.',
  short='UConn says to schedule a visit if the horse consistently shows one or more signs of back pain. The sources reviewed give no emergency criteria. If a horse is also lame, will not bear weight or has a sudden change, call your veterinarian promptly.',
  body='''<h2>What the sources say</h2>
<ul>
<li>UConn Extension: schedule a veterinary visit if the horse consistently shows one or more signs of back pain.</li>
<li>University of Minnesota: if you suspect back pain, consult your veterinarian to diagnose it and rule out other concerns. The page gives no specific warning signs or urgency criteria.</li>
<li>Back pain can look like lameness or refusal to work, and chronic leg lameness can cause secondary back pain (Minnesota; UConn).</li>
</ul>
<h2>Rechecks</h2>
<p>The sources reviewed do not list specific signs that should trigger re-evaluation after treatment. Reasonable triggers to raise with your vet are signs that persist or return, new lameness, or a change in behavior under saddle. Ask your veterinarian what to watch for in your horse's case. See <a href="/qa/lameness/back-pain-causes-and-signs/">signs of back pain</a>.</p>''',
  src=['uconnback','umnback'], rel=['back-pain-causes-and-signs','how-back-pain-is-diagnosed','back-pain-treatment-options']),

 dict(slug='hoof-abscess-signs-and-treatment', ids=['VET-QA-0332'], urgent=False,
  q='What are the signs of a hoof abscess?',
  title='Hoof Abscess in Horses: Signs and Treatment',
  meta='A hoof abscess often causes sudden, severe lameness with a warm foot and bounding pulse. Vets drain it, and uncomplicated cases have an excellent outlook.',
  short='Typical signs are sudden, severe lameness in one limb, a warm foot, bounding digital pulses and often a swollen pastern. A vet or farrier can find and drain the abscess. The outlook for uncomplicated abscesses is excellent.',
  body='''<h2>Signs</h2>
<ul>
<li>Sudden, severe lameness in one limb, often with reluctance to bear weight; owners may suspect a fracture (University of Minnesota textbook).</li>
<li>A warm foot, bounding digital pulses, and often a swollen pastern; some horses appear three-legged lame (Minnesota; The Horse).</li>
<li>A black spot in normally pale horn when the sole is pared, and black pus. Drainage may appear at the coronary band ("gravel").</li>
</ul>
<h2>Diagnosis and treatment</h2>
<p>Hoof testers usually cause marked pain, though the whole foot is often sensitive. The goal of treatment is drainage. A vet or farrier opens the abscess just enough to drain it. The Horse says the horse should be more comfortable within about 24 hours of drainage, and that opening at the coronary band can leave a crack that takes months to grow out. Afterward the foot is soaked, poulticed or bandaged and tetanus prophylaxis is given; antibiotics are usually not needed (Minnesota).</p>
<h2>Outlook</h2>
<p>Excellent for uncomplicated solar abscesses; guarded to poor if joint structures or the pedal bone are involved, which is uncommon (Minnesota). Call your vet or farrier right away if you suspect an abscess (The Horse). See <a href="/qa/lameness/when-to-call-the-vet-for-hoof-problems/">when to call the vet</a>.</p>''',
  src=['umnabs','horsehoof'], rel=['when-to-call-the-vet-for-hoof-problems','bruised-sole-causes-and-treatment','hot-hooves-causes']),

 dict(slug='bruised-sole-causes-and-treatment', ids=['VET-QA-0304','VET-QA-0368'], urgent=False,
  q='How is a bruised sole treated and prevented?',
  title='Bruised Sole in Horses: Treatment and Prevention',
  meta='A bruised sole is treated with rest, a soft surface and farrier care; pads or boots may help. The BHS says uncomplicated bruises usually resolve in two weeks.',
  short='Contact your farrier or vet. Treatment is rest, reduced exercise, a soft deeply bedded surface, and farrier care, with pads or boots if the sole is thin. The British Horse Society says uncomplicated bruises usually resolve within two weeks.',
  body='''<h2>Treatment (BHS)</h2>
<ul>
<li>Contact your farrier first if you suspect a bruised sole.</li>
<li>Rest, reduce exercise and provide a soft, deeply bedded surface; brief cold hosing may reduce inflammation.</li>
<li>The farrier may remove the shoe or pare around the bruise to relieve pressure, and may use hoof boots, pads or a bandage if the sole is thin or damaged.</li>
<li>Uncomplicated bruises usually resolve within two weeks; monitor daily. A hematoma or abscess may need drainage.</li>
</ul>
<p>The Horse says a farrier may use a leather or plastic pad with soft silicone or foam packing under the bruise, and that healing can take weeks to months depending on severity.</p>
<h2>Prevention</h2>
<ul>
<li>Keep up regular trimming and shoeing with a registered farrier.</li>
<li>Avoid excessive work on hard, stony or frozen ground, especially with thin soles; use pads or boots on rough terrain under farrier or vet guidance.</li>
<li>Pick out hooves before and after exercise, and keep stable and standing areas clean and dry.</li>
</ul>
<p>Call the vet if the horse is lame, the bruise is very large or there is no improvement (BHS). See <a href="/qa/lameness/preventing-hoof-problems/">preventing hoof problems</a>.</p>''',
  src=['bhsbruise','horsehoof'], rel=['preventing-hoof-problems','hoof-abscess-signs-and-treatment','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='hot-hooves-causes', ids=['VET-QA-0323','VET-QA-0340'], urgent=False,
  q='What causes heat in a horse’s hooves?',
  title='What Causes Hot Hooves in Horses?',
  meta='Warm hooves can signal laminitis, a hoof abscess or a bruised sole, often with a stronger digital pulse. Because laminitis is an emergency, call your vet.',
  short='A warm hoof is a warning sign. Sources link it to laminitis, hoof abscess and bruised soles, usually with a stronger digital pulse. Because laminitis is an emergency, call your veterinarian if the heat comes with lameness or reluctance to move.',
  body='''<h2>Conditions sources link to warm hooves</h2>
<ul>
<li><strong>Laminitis</strong> — the AAEP lists heat in the feet and an increased digital pulse among signs of acute laminitis, and UC Davis lists warm hooves among signs owners should watch for.</li>
<li><strong>Hoof abscess</strong> — a warm foot with bounding digital pulses (University of Minnesota textbook; The Horse).</li>
<li><strong>Bruised sole</strong> — the hoof may feel warmer than usual with a stronger digital pulse (British Horse Society).</li>
</ul>
<p>The sources reviewed do not say how to tell these apart at home. A veterinarian or farrier can use hoof testers and imaging. If heat comes with lameness, shifting weight or reluctance to move, treat it as possible laminitis and call your vet. See <a href="/qa/lameness/signs-of-laminitis-and-founder/">signs of laminitis</a>.</p>''',
  src=['aaeplam','ucdlam','umnabs','bhsbruise'], rel=['signs-of-laminitis-and-founder','hoof-abscess-signs-and-treatment','bruised-sole-causes-and-treatment']),

 dict(slug='preventing-hoof-problems', ids=['VET-QA-0307','VET-QA-0312'], urgent=False,
  q='How can I prevent hoof problems and protect my horse’s hooves?',
  title='How to Prevent Hoof Problems in Horses',
  meta='Regular farrier care, limited mud and wet, clean dry stalls, picking feet and a balanced diet help protect hooves. See what The Horse and BHS advise.',
  short='Regular farrier care, limiting mud and wet exposure, clean dry bedding, picking out feet and a balanced diet all help. Avoid long stretches on hard or stony ground, especially for thin-soled horses.',
  body='''<h2>Steps from the sources</h2>
<ul>
<li><strong>Farrier care.</strong> Regular care by a skilled farrier helps prevent imbalanced, overgrown or cracked hooves (The Horse). UC Davis also lists regular farrier visits.</li>
<li><strong>Moisture and hygiene.</strong> Limit mud exposure, bed stalls at least 4 inches deep, clean stalls at least daily, and pick feet regularly; avoid prolonged wetness or excessive dryness (The Horse).</li>
<li><strong>Nutrition.</strong> A balanced diet with adequate protein and biotin supports hoof quality, and dietary changes can take up to a year to show because a full new hoof takes that long to grow (The Horse).</li>
<li><strong>Footing.</strong> Avoid excessive work on hard, stony or frozen ground, pick out hooves before and after exercise, and check for loose shoes (BHS).</li>
</ul>
<p>The sources reviewed give no set trimming or shoeing interval; your farrier sets it. See <a href="/qa/lameness/bruised-sole-causes-and-treatment/">bruised soles</a>.</p>''',
  src=['horsehoof','bhsbruise','ucdlam'], rel=['bruised-sole-causes-and-treatment','hoof-abscess-signs-and-treatment','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='when-to-call-the-vet-for-hoof-problems', ids=['VET-QA-0370'], urgent=True,
  q='When should I call a vet for hoof problems?',
  title='When to Call the Vet for Hoof Problems',
  meta='Call right away for suspected laminitis, a suspected hoof abscess, a penetrating injury, or a bruise that is lame, very large or not improving.',
  short='Call your veterinarian right away for suspected laminitis, a suspected abscess or a penetrating injury, and if a bruise is very large, the horse is lame or there is no improvement.',
  body='''<h2>Call promptly for</h2>
<ul>
<li><strong>Suspected laminitis.</strong> UC Davis says to call a veterinarian immediately; the AAEP calls it an emergency, though not a "5-minute" one. See <a href="/qa/lameness/signs-of-laminitis-and-founder/">signs of laminitis</a>.</li>
<li><strong>Suspected hoof abscess.</strong> The Horse says to call your vet or farrier right away. Sudden severe lameness may be mistaken for a fracture (University of Minnesota textbook).</li>
<li><strong>A penetrating injury</strong> to the hoof should be seen by a vet immediately (BHS).</li>
<li><strong>A bruised sole</strong> when the horse is lame, the bruise is very large, there is no improvement, or symptoms continue or worsen; X-rays may be needed to rule out a pedal bone fracture in severe cases (BHS).</li>
</ul>
<p>Do not wait for a hot, sore foot to settle. See <a href="/qa/lameness/hot-hooves-causes/">causes of hot hooves</a> and our <a href="/emergency/lameness/">lameness emergency guide</a>.</p>''',
  src=['ucdlam','aaeplam','horsehoof','umnabs','bhsbruise'], rel=['signs-of-laminitis-and-founder','hoof-abscess-signs-and-treatment','bruised-sole-causes-and-treatment']),

 dict(slug='signs-of-cellulitis-and-lymphangitis', ids=['VET-QA-0392','VET-QA-0387'], urgent=True,
  q='What are the signs of cellulitis (lymphangitis, "big leg"), and what complications can occur?',
  title='Signs of Cellulitis and Lymphangitis (Big Leg)',
  meta='A rapidly swollen, painful, warm leg with fever and severe lameness suggests cellulitis or lymphangitis. Call your vet immediately; delays risk lasting damage.',
  short='Signs include rapid, severe leg swelling (often a hind leg), pain, severe lameness and fever of 102 to 105°F. Call your veterinarian immediately. Untreated or severe cases can become chronic, and the limb may never return to normal.',
  body='''<h2>Signs</h2>
<ul>
<li>Sudden, severe swelling, usually in a hind leg, that can reach the hock or knee or higher (Horse Canada; The Horse).</li>
<li>Fever of 102 to 105°F, severe lameness, pain when the leg is touched (both sources).</li>
<li>Some horses lose appetite, tremble, breathe or pulse faster, or sweat.</li>
<li>Pitting edema: finger pressure leaves an imprint (The Horse). Clear yellowish fluid may ooze from the most swollen areas (Horse Canada).</li>
<li>Signs can begin as late as 2 to 3 weeks after an injury, and the cause can be a skin break too small to see (Horse Canada).</li>
</ul>
<h2>How it differs from stocking up</h2>
<p>Horse Canada says stocking up is usually temporary, causes little discomfort beyond stiffness, and improves with exercise; cellulitis and lymphangitis are far more serious, with systemic illness and fever.</p>
<h2>Complications</h2>
<p>Severe or untreated cases can become chronic or recurrent, and tissue under the skin may stay permanently thickened (Horse Canada). The Horse says the limb may never return to normal and chronically affected horses can develop wartlike growths and thickened skin folds. In rare worst cases it can be fatal (Horse Canada). Call your vet immediately; see <a href="/qa/lameness/cellulitis-treatment-and-immediate-steps/">treatment and immediate steps</a>.</p>''',
  src=['hcswell','horselymph'], rel=['cellulitis-treatment-and-immediate-steps','preventing-cellulitis-and-lymphangitis','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='cellulitis-treatment-and-immediate-steps', ids=['VET-QA-0380','VET-QA-0393','VET-QA-0394'], urgent=True,
  q='Are antibiotics needed for cellulitis, what should I do immediately, and how do I monitor progress?',
  title='Cellulitis and Lymphangitis: Treatment and First Steps',
  meta='Call your vet immediately. Treatment includes antibiotics and anti-inflammatories, cold water early, and walking to move fluid. Avoid bandaging a swelling leg.',
  short='Call your veterinarian immediately. Sources say antibiotics and anti-inflammatories are the expected treatment. Cold water, keeping the leg from staying wet, and encouraging walking are described as early steps. Bandaging during the acute phase can be dangerous.',
  body='''<h2>Are antibiotics needed?</h2>
<p>Yes, in the sources reviewed. The Horse says an acute episode calls for aggressive antibiotics and anti-inflammatories, and Horse Canada says antibiotics are the expected treatment alongside an anti-inflammatory for swelling and pain. Drug choice and dose are your veterinarian's call. The Horse notes long-term antibiotics for prevention have had inconsistent results.</p>
<h2>Immediate steps</h2>
<ul>
<li><strong>Call your veterinarian immediately</strong> (Horse Canada).</li>
<li>Cold water or ice, but do not let the leg stay wet, which can further damage the skin (The Horse). Horse Canada describes cold hosing for the first 48 hours, then alternating cold and hot compresses.</li>
<li>Encourage walking to move fluid back up the leg; movement is essential for recovery (The Horse). Horse Canada describes short sessions of mild exercise.</li>
<li>The Horse's author considers bandaging in the acute phase dangerous, because swelling continues above the wrap.</li>
<li>Never put poultices, DMSO or clay on broken skin (Horse Canada).</li>
</ul>
<h2>Monitoring</h2>
<p>The sources give no schedule or specific recovery markers. Simple cases may take several weeks to heal (Horse Canada). Report to your vet if swelling, fever or lameness is not easing or spreads. See <a href="/qa/lameness/signs-of-cellulitis-and-lymphangitis/">signs</a>.</p>''',
  src=['hcswell','horselymph'], rel=['signs-of-cellulitis-and-lymphangitis','preventing-cellulitis-and-lymphangitis','when-to-call-the-vet-for-hoof-problems']),

 dict(slug='preventing-cellulitis-and-lymphangitis', ids=['VET-QA-0385','VET-QA-0386'], urgent=False,
  q='How can I prevent cellulitis or lymphangitis from recurring?',
  title='Preventing Cellulitis and Lymphangitis in Horses',
  meta='Keep legs clean and dry, treat minor injuries at once, keep stalls clean and exercise regularly. Recurrence is common, so ask your vet about a plan.',
  short='Horse Canada advises good nutrition and healthy weight, a clean stall with fresh bedding, regular exercise, prompt treatment of minor injuries, and clean, dry legs. The Horse says recurrence is common, and early treatment of swelling may improve outcomes.',
  body='''<h2>Prevention (Horse Canada)</h2>
<ul>
<li>Good nutrition and a healthy weight</li>
<li>A clean stall with fresh bedding</li>
<li>Regular exercise</li>
<li>Prompt treatment of minor injuries</li>
<li>Keeping legs clean and dry</li>
</ul>
<h2>Recurrence</h2>
<p>The Horse says recurrence is common. Massage may help move fluid out of the limb, and compressive wraps or stockings may help control swelling between episodes. Topical ointments, immune stimulants and long-term antibiotics have been tried with inconsistent results. Early detection and treatment of swelling may improve outcomes in recurrent cases. Ask your veterinarian before using wraps or any preventive medication, and wear gloves when treating affected horses with ulcerative lymphangitis (Horse Canada).</p>
<p>See <a href="/qa/lameness/signs-of-cellulitis-and-lymphangitis/">signs of cellulitis</a>.</p>''',
  src=['hcswell','horselymph'], rel=['signs-of-cellulitis-and-lymphangitis','cellulitis-treatment-and-immediate-steps','preventing-hoof-problems']),

 dict(slug='joint-supplements-for-arthritis', ids=['VET-QA-0381','VET-QA-0388'], urgent=False,
  q='Do joint supplements help horses with arthritis?',
  title='Do Joint Supplements Help Horses With Arthritis?',
  meta='Veterinary researchers say evidence for oral joint supplements is limited and product quality varies. Ask your vet before relying on them for arthritis pain.',
  short='Evidence is limited. A researcher at the AAEP convention said many oral joint supplements lack scientific support, with low bioavailability and variable quality. Kentucky Equine Research says researchers still struggle to prove they work. Ask your veterinarian.',
  body='''<h2>What the sources say</h2>
<ul>
<li>Dr. Wayne McIlwraith (Colorado State University), reported by The Horse from an AAEP convention, said it is unclear how and when to use oral joint supplements because many have low bioavailability, poor quality, low recommended doses and a lack of scientific evidence. Glucosamine and chondroitin sulfate were the focus.</li>
<li>Kentucky Equine Research (a nutrition company) says supplement quality varies markedly by ingredients and manufacturer, and that researchers still struggle to prove the products work even though many owners perceive a benefit. It describes a multimodal approach to osteoarthritis that can include anti-inflammatory drugs, corticosteroids and supplements, depending on the horse.</li>
</ul>
<p>These are older and industry-linked sources; they do not cover other arthritis treatments. Have your veterinarian diagnose the cause of the lameness and advise on any supplement.</p>''',
  src=['horsesupp','kersupp'], rel=['back-pain-causes-and-signs','ligament-injury-signs-and-diagnosis','bowed-tendon-treatment-and-recovery']),
 dict(slug='arthritis-causes-treatment-and-outlook', ids=['VET-QA-0383','VET-QA-0389','VET-QA-0390','VET-QA-0391'], urgent=False,
  q='What causes arthritis in horses, how is it treated and managed, and what are the long-term effects?',
  title='Horse Arthritis: Causes, Treatment and Outlook',
  meta='Osteoarthritis is a progressive joint disease from wear or past injury. Management combines activity, weight and hoof care with vet-directed medical care.',
  short='Osteoarthritis is a progressive breakdown of joint cartilage, from everyday wear or from an earlier joint injury. Management is multifaceted: activity level, body weight, hoof care and medical or surgical therapy chosen by your veterinarian. The sources reviewed give no long-term prognosis and name no home pain treatment.',
  body='''<h2>What it is and what causes it</h2>
<ul>
<li>Osteoarthritis is a progressive disease that gradually breaks down a joint's cartilage; the inflammation causes pain and swelling (Texas A&amp;M).</li>
<li><strong>Primary:</strong> slow breakdown from everyday wear and tear; performance horses are at particular risk.</li>
<li><strong>Secondary:</strong> follows an injury severe enough to start cartilage breakdown; risk factors include joint infections, joint fractures, ligament and tendon injuries and existing joint defects (Texas A&amp;M).</li>
<li>Early signs are often subtle, such as behavior changes or reduced willingness to work (Texas A&amp;M).</li>
</ul>
<h2>Treatment and management</h2>
<ul>
<li>Texas A&amp;M describes a multifaceted approach: adjusting activity, managing body weight and condition, appropriate hoof care, and medical and surgical therapy. It advises working with your veterinarian on an individualized plan.</li>
<li>AAEP (an article reviewed in 2016) lists categories of joint treatment: joint-injected lubricants, injectable cartilage products, corticosteroids, oral supplements and anti-inflammatory drugs. It says owners should rely on their veterinarian to decide when joint injections are appropriate, and that X-ray changes often mean damage is already irreversible.</li>
<li>AAEP notes anti-inflammatory drugs can cause stomach ulcers and reduced kidney blood flow. Do not give pain medication without veterinary direction.</li>
<li>The article's evidence claims for supplements are mixed and some trials were industry-funded; see <a href="/qa/lameness/joint-supplements-for-arthritis/">joint supplements</a>.</li>
</ul>
<h2>Long-term effects and home pain management</h2>
<p>Texas A&amp;M gives no prognosis and says research is ongoing. The sources reviewed name no specific home pain treatments and no doses, so none are listed. Ask your veterinarian what is safe at home. Prompt treatment of the original injury matters most for secondary arthritis (Texas A&amp;M). Call your veterinarian for lameness, swelling or a change in willingness to work. See <a href="/qa/lameness/ligament-injury-treatment-and-healing-time/">ligament injury treatment</a>.</p>''',
  src=['tamuoa','aaepjoint'], rel=['joint-supplements-for-arthritis','ligament-injury-signs-and-diagnosis','preventing-tendon-injuries']),

 dict(slug='ligament-injury-treatment-and-healing-time', ids=['VET-QA-0362','VET-QA-0314','VET-QA-0327'], urgent=False,
  q='How are ligament injuries treated, how long do they take to heal and how can they be prevented?',
  title='Horse Ligament Injury: Treatment, Healing, Prevention',
  meta='Controlled rest and slow rehab are the core of ligament injury care. Timelines run from months to a year; your vet guides ultrasound checks and return to work.',
  short='Ligament injuries need a veterinary exam, then controlled rest and a slow, graded rehabilitation program. Sources describe pain-free horses within weeks but full recovery taking about 8 to 9 months, and sometimes six months to a year or more. Returning to work too early raises re-injury risk.',
  body='''<h2>Treatment</h2>
<ul>
<li>In the first 24 hours, cold therapy, stable bandages and stall rest are used and a veterinarian should assess the injury; anti-inflammatory drugs may be prescribed, with stall rest until heat and swelling subside, which can take up to two weeks (Horse Canada).</li>
<li>Once the leg is no longer sore, a slow controlled program begins with hand-walking, gradually increasing duration and intensity before riding (Horse Canada).</li>
<li>Ultrasound is the main diagnostic tool and repeat scans can track healing (Horse Canada). Dr. David Ramey notes serial scans can be costly.</li>
<li>Regenerative and other options such as stem cells, platelet-rich plasma and shockwave exist, but some are unproven (Horse Canada). Dr. Ramey argues that no treatment has been shown to beat controlled rest and rehabilitation.</li>
</ul>
<h2>Healing time</h2>
<ul>
<li>Horse Canada says the full process can last six months to a year or more.</li>
<li>Dr. Ramey says less severe injuries often look pain-free within about three to eight weeks but the horse is not ready for work; full recovery often takes eight to nine months.</li>
<li>Re-injury risk is high because tendon and ligament tissue has limited blood supply, and the junction between scar tissue and normal tissue is a common site of re-injury (Horse Canada).</li>
</ul>
<p>Timelines depend on the injury; ask your veterinarian for yours. See <a href="/qa/lameness/ligament-injury-signs-and-diagnosis/">signs and diagnosis</a>.</p>
<h2>Prevention (Horse Canada)</h2>
<ul>
<li>Learn what your horse's legs normally feel and look like and check regularly for heat, pain and swelling.</li>
<li>Overwork from poor conditioning, intense training or riding a tired horse is the most common cause; keep horses fit and rest them when tired.</li>
<li>Other avoidable causes include poor hoof balance, incorrect shoeing or trimming, repetitive concussion and improper boot or bandage use. Falls, slips, uneven terrain and conformation are harder to control.</li>
</ul>''',
  src=['hcligament','rameyligament'], rel=['ligament-injury-signs-and-diagnosis','arthritis-causes-treatment-and-outlook','preventing-tendon-injuries','bowed-tendon-treatment-and-recovery']),
]
