# -*- coding: utf-8 -*-
"""Metabolic and endocrine Q&A (PPID/Cushing's, EMS, insulin dysregulation). Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'hsvg13': ('Horse-Side Vet Guide — Depressed, dull or lethargic horse (Doug Thal, DVM, Dipl. ABVP; last modified Dec 2024)', 'https://horsesidevetguide.com/drv/Observation/13'),
 'uflcall': ('University of Florida Large Animal Hospital — When It\'s Time to Call the Vet (Sept 2025)', 'https://largeanimal.vethospitals.ufl.edu/2025/09/10/when-its-time-to-call-the-vet/'),
 'wcvm': ('University of Saskatchewan WCVM — Pituitary Pars Intermedia Dysfunction (PPID)', 'https://vmc.usask.ca/care/equine-health/resources/ppid.php'),
 'ucdems': ('UC Davis Center for Equine Health — Equine Metabolic Syndrome', 'https://ceh.vetmed.ucdavis.edu/node/3021'),
 'umnems': ('University of Minnesota Equine Center — Equine Metabolic Syndrome: Management', 'https://vetmed.umn.edu/equine/research/equine-genetics-and-genomics-laboratory/projects/equine-metabolic-syndrome/management'),
 'usu': ('Utah State University Extension — Managing Equine Metabolic Syndrome', 'https://extension.usu.edu/equine/research/managing-equine-metabolic-syndrome.php'),
 'uconn': ('UConn Extension — Insulin Resistance in Horses: Does It Matter?', 'https://extension.uconn.edu/?p=16735'),
 'vetire': ('Veterinary Ireland Journal — Pituitary Pars Intermedia Dysfunction: Old Disease, New Tests', 'https://veterinaryirelandjournal.com/focus/273-pituitary-pars-intermedia-dysfunction-old-disease-new-tests'),
 'merckppid': ('Merck Veterinary Manual (Professional) — Hypertrichosis Associated With Adenomas of the Pars Intermedia in Horses', 'https://www.merckvetmanual.com/veterinary/endocrine-system/the-pituitary-gland/hypertrichosis-associated-with-adenomas-of-the-pars-intermedia'),
 'aaepeeg': ('AAEP / Equine Veterinary Education — New PPID Diagnostic Recommendations from the Equine Endocrinology Group', 'https://pubs.aaep.org/0A4370h/EVEMay2018/html/31.html'),
 'hcppid': ('Horse Canada — Pituitary Pars Intermedia Dysfunction', 'https://horse-canada.com/magazine/health/pituitary-pars-intermedia-dysfunction/'),
})
HELD = {
 
 'VET-QA-0260':'generic metabolic-monitoring question; no verified interval','VET-QA-0262':'insulin monitoring interval: no verified source','VET-QA-0289':'generic treatment question for unnamed condition',
}
PAGES = [
 dict(slug='signs-of-ppid-cushings', ids=['VET-QA-0266','VET-QA-0275','VET-QA-0277'], urgent=False,
  q='What are the signs of PPID (equine Cushing’s disease)?',
  title='Signs of PPID (Cushing’s) in Horses',
  meta='The classic PPID sign is a long coat that will not shed. Others: sweating, pot belly, weight and muscle loss, lethargy and laminitis. See what vets look for.',
  short='The most common and distinctive sign of PPID is a long coat that fails to shed in spring. Others include excessive sweating, a pot-bellied look, weight loss with muscle wasting, lethargy, more infections and laminitis. It mostly affects horses around 15 and older.',
  body='''<h2>Signs described by veterinary sources</h2>
<ul>
<li><strong>Long coat that does not shed.</strong> The University of Saskatchewan's WCVM calls this the most common and unique sign. Merck calls it hypertrichosis and says it is associated with PPID.</li>
<li><strong>Excessive sweating.</strong></li>
<li><strong>Increased thirst and urination, poor muscle tone, weakness, sleepiness</strong>, abnormal fat distribution and swelling above the eyes (Merck).</li>
<li><strong>Pot-bellied look, weight loss, muscle wasting and lethargy</strong>, with greater susceptibility to infection (WCVM).</li>
<li><strong>Laminitis.</strong> WCVM calls laminitis the main factor limiting the lifespan of PPID horses. See <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">signs of laminitis</a>.</li>
</ul>
<h2>Who is affected</h2>
<p>WCVM says PPID typically affects horses around 15 and older, and that signs generally worsen with age. The Veterinary Ireland Journal reports up to 30% of older animals affected, and notes that PPID and EMS share signs such as laminitis, abnormal fat deposition and irregular cycles, so vets recommend testing for both.</p>
<p>A long coat in a small pony is sometimes mistaken for a normal winter coat, delaying diagnosis. These signs do not prove PPID; see <a href="/qa/metabolic/how-ppid-is-diagnosed/">how PPID is diagnosed</a>.</p>''',
  src=['wcvm','merckppid','vetire'], rel=['how-ppid-is-diagnosed','ppid-treatment-options','signs-of-laminitis-in-endocrine-disease']),

 dict(slug='how-ppid-is-diagnosed', ids=['VET-QA-0258'], urgent=False,
  q='How is Cushing’s disease (PPID) diagnosed?',
  title='How PPID (Cushing’s) Is Diagnosed in Horses',
  meta='Vets diagnose PPID with a blood ACTH test, sometimes a TRH stimulation test, adjusted for season. Learn why timing matters and why insulin is often tested too.',
  short='A veterinarian diagnoses PPID with a blood test for the hormone ACTH, and sometimes a TRH stimulation test. Results change with the season, so testing is timed and interpreted by a vet. Insulin is often tested too, because PPID and EMS can occur together.',
  body='''<h2>The main tests</h2>
<ul>
<li><strong>Resting (basal) ACTH</strong> — a blood test. Higher-than-normal levels support PPID, and WCVM says this is often enough when signs are obvious. With few signs, a vet may repeat it in six months or use another test.</li>
<li><strong>TRH stimulation test</strong> — AAEP and the Equine Endocrinology Group (EEG) describe it, measuring ACTH before and after the injection, for horses with early signs or a normal resting ACTH.</li>
</ul>
<h2>Seasonal effects</h2>
<p>ACTH rises naturally in the fall. WCVM says testing is avoided then to prevent false positives; the EEG recommends using seasonally adjusted reference ranges, and notes that fall testing can raise the sensitivity of resting ACTH in horses with early signs. Your veterinarian chooses when to test.</p>
<h2>Insulin testing</h2>
<p>PPID can occur with insulin dysregulation, so the Veterinary Ireland Journal says current recommendations are to test for both together. Merck notes that insulin insensitivity is common in PPID but also occurs in EMS, so it does not diagnose PPID by itself.</p>
<p>Testing a horse with no signs is not currently recommended, according to a published review. See <a href="/qa/metabolic/signs-of-ppid-cushings/">signs of PPID</a> and <a href="/qa/metabolic/ppid-treatment-options/">treatment options</a>.</p>''',
  src=['wcvm','aaepeeg','vetire','merckppid'], rel=['signs-of-ppid-cushings','ppid-treatment-options','how-ems-is-diagnosed']),

 dict(slug='ppid-treatment-options', ids=['VET-QA-0253','VET-QA-0278','VET-QA-0288'], urgent=False,
  q='What treatment and management options are there for PPID?',
  title='PPID (Cushing’s) Treatment Options in Horses',
  meta='PPID has no cure, but a daily prescription medication plus coat clipping, hoof care and vet follow-up control signs. See what WCVM and Merck say to expect.',
  short='PPID cannot be cured, but a veterinarian can control signs with a daily prescription medication, pergolide, and management such as clipping the coat. Many horses live long, healthy lives with proper management.',
  body='''<h2>Medication</h2>
<p>WCVM says the standard treatment is daily pergolide (Prascend), a drug that acts like dopamine. Vets typically start low and raise the dose until signs are controlled, and the dose may need adjusting over time. Owners often see improvement after six to eight weeks. Possible side effects are lethargy or reduced appetite for a few days and, rarely, diarrhea or colic; the dose may then be reduced. Dose and schedule are your veterinarian's decision.</p>
<h2>Management alongside medication</h2>
<ul>
<li><strong>Clip the coat</strong> in summer (WCVM); Merck says frequent clipping manages the long coat.</li>
<li><strong>Keep up regular vet and farrier visits</strong>, and stay current on vaccines and deworming.</li>
<li><strong>Watch for laminitis</strong> — see <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">signs of laminitis</a>.</li>
</ul>
<h2>Outlook</h2>
<p>The prognosis is generally good. Treatment controls signs but does not stop progression; doses may need to rise and some horses become harder to control (WCVM). See <a href="/qa/metabolic/ppid-monitoring-and-retesting/">monitoring and retesting</a>.</p>''',
  src=['wcvm','merckppid','hcppid'], rel=['ppid-monitoring-and-retesting','ppid-diet','how-ppid-is-diagnosed']),

 dict(slug='ppid-monitoring-and-retesting', ids=['VET-QA-0261','VET-QA-0263'], urgent=False,
  q='How often should a horse with PPID be monitored?',
  title='How Often to Monitor a Horse With PPID',
  meta='WCVM recommends reassessing PPID horses about every six months, with repeat testing to check hormone levels. Learn what to watch between visits.',
  short='WCVM recommends assessing horses with PPID about every six months, with diagnostic tests repeated to check whether hormone levels have normalized. Watch for laminitis and changes in coat, weight and energy in between.',
  body='''<h2>Veterinary follow-up</h2>
<p>The University of Saskatchewan's WCVM recommends assessing horses with PPID every six months, and says diagnostic tests can be repeated to check whether hormone levels have normalized. Retest timing is your veterinarian's call, especially after a medication dose change or if signs return.</p>
<h2>What owners can watch between visits</h2>
<ul>
<li><strong>Laminitis signs:</strong> front-foot soreness, reluctance to move, a backward-rocking stance, and an exaggerated lift of the front feet when walking (WCVM). Call your vet promptly.</li>
<li><strong>Coat:</strong> failure to shed or a changing coat.</li>
<li><strong>Weight, muscle, energy and appetite</strong>, including appetite after a medication change.</li>
</ul>
<p>See <a href="/qa/metabolic/ppid-treatment-options/">treatment options</a> and <a href="/qa/metabolic/is-endocrine-treatment-working-or-worsening/">is treatment working?</a></p>''',
  src=['wcvm'], rel=['ppid-treatment-options','signs-of-laminitis-in-endocrine-disease','is-endocrine-treatment-working-or-worsening']),

 dict(slug='ppid-diet', ids=['VET-QA-0245','VET-QA-0280','VET-QA-0281','VET-QA-0282'], urgent=False,
  q='What dietary changes are recommended for a horse with PPID?',
  title='Diet for a Horse With PPID (Cushing’s)',
  meta='Sources do not give a PPID-only diet. When a PPID horse also has insulin dysregulation, the low-sugar, low-starch EMS approach applies. See what vets recommend.',
  short='The veterinary sources reviewed give no diet specific to PPID. PPID often occurs with insulin dysregulation, and then the low-sugar, low-starch approach used for EMS applies. Thin PPID horses may need extra calories. Your veterinarian sets the plan.',
  body='''<h2>What the sources say</h2>
<ul>
<li>WCVM's PPID page does not cover diet.</li>
<li>PPID and insulin dysregulation (ID) can occur together; UC Davis notes PPID may worsen insulin resistance, and the Veterinary Ireland Journal says unrewarding PPID outcomes were likely tied to missed concurrent ID. Testing for both is recommended.</li>
<li>If a PPID horse has ID, the EMS feeding approach applies: limit non-structural carbohydrates (NSC) and analyze hay. See <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS and insulin resistance</a>.</li>
<li>PPID can cause weight loss and muscle wasting (WCVM), and UC Davis says thin horses with ID need more calories from roughage, fat or protein sources.</li>
</ul>
<p>Ask your veterinarian whether your horse has ID, whether it is thin or overweight, and what ration balancer to use. Supplements are covered in <a href="/qa/metabolic/supplements-for-cushings-and-insulin-resistance/">supplements for Cushing's and insulin resistance</a>.</p>''',
  src=['wcvm','ucdems','vetire'], rel=['diet-for-ems-and-insulin-resistance','supplements-for-cushings-and-insulin-resistance','ppid-treatment-options']),

 dict(slug='signs-of-ems-and-insulin-resistance', ids=['VET-QA-0265','VET-QA-0271','VET-QA-0276'], urgent=False,
  q='What are the signs of EMS and insulin resistance?',
  title='Signs of EMS and Insulin Resistance in Horses',
  meta='Most horses with EMS are overweight with fat at the neck and tailhead, but thin horses can be affected. Laminitis is the main danger. See signs and risks.',
  short='Most horses with EMS are overweight, with fat built up around the neck, ribs and tailhead, and they are at high risk of laminitis. Thinner horses can also have insulin dysregulation, so testing is needed to know.',
  body='''<h2>Signs and risk factors</h2>
<ul>
<li><strong>Excess body fat</strong> — UC Davis describes fat building up around the neck, ribs and tailhead in most affected horses; thinner horses can also have insulin dysregulation.</li>
<li><strong>Laminitis</strong> — the main danger. UC Davis says EMS makes laminitis easier to develop and it can be life-threatening. See <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">signs of laminitis</a>.</li>
<li><strong>Breeds and types:</strong> ponies, donkeys, Arabians and mustangs are commonly affected.</li>
<li><strong>Feeding and lifestyle:</strong> insulin rises too much after high-sugar or high-starch meals; abundant feed with little exercise adds risk. UConn notes horses had lower insulin sensitivity on high sugar/starch feeds.</li>
<li><strong>Age:</strong> UConn says horses over 20 seem more prone to insulin resistance, probably secondary to PPID.</li>
</ul>
<p>The Veterinary Ireland Journal notes EMS and PPID share signs, so vets test for both. See <a href="/qa/metabolic/how-ems-is-diagnosed/">how EMS is diagnosed</a>.</p>''',
  src=['ucdems','uconn','vetire'], rel=['how-ems-is-diagnosed','diet-for-ems-and-insulin-resistance','signs-of-laminitis-in-endocrine-disease']),

 dict(slug='how-ems-is-diagnosed', ids=['VET-QA-0286','VET-QA-0287'], urgent=False,
  q='What tests diagnose EMS and other metabolic or endocrine disease?',
  title='How EMS and Endocrine Disease Are Diagnosed',
  meta='Vets screen for EMS with morning glucose and insulin blood tests, may use dynamic tests, and check older horses for PPID. Learn which tests are used.',
  short='Vets screen for EMS with morning blood glucose and insulin samples taken before feeding, sometimes followed by dynamic tests of insulin response. Older horses are also checked for PPID, with an ACTH test.',
  body='''<h2>EMS and insulin dysregulation</h2>
<p>UC Davis says screening uses morning blood glucose and insulin samples taken before feeding. If results do not settle the question, vets use dynamic tests that assess insulin response or sensitivity — oral sugar, oral glucose, insulin tolerance and combined glucose/insulin tolerance tests. Stress can affect results, so sampling at home is preferred. Interpretation is a veterinary job.</p>
<h2>PPID</h2>
<p>PPID is tested with a blood ACTH measurement, sometimes with a TRH stimulation test; see <a href="/qa/metabolic/how-ppid-is-diagnosed/">how PPID is diagnosed</a>. UC Davis says older horses should also be checked for PPID because it may worsen insulin resistance, and the University of Guelph's lab notes ACTH, insulin and glucose testing may be indicated together when signs are supportive.</p>
<p>Hay analysis is not a diagnostic test but is central to management; see <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</p>''',
  src=['ucdems','vetire','wcvm'], rel=['signs-of-ems-and-insulin-resistance','how-ppid-is-diagnosed','diet-for-ems-and-insulin-resistance']),

 dict(slug='diet-for-ems-and-insulin-resistance', ids=['VET-QA-0248','VET-QA-0251','VET-QA-0252','VET-QA-0254','VET-QA-0255','VET-QA-0279','VET-QA-0283','VET-QA-0284'], urgent=False,
  q='What diet is recommended for a horse with EMS or insulin resistance?',
  title='Diet for Horses With EMS or Insulin Resistance',
  meta='Diet is the core of EMS care: limit sugar and starch, test hay NSC, weigh rations and lose weight gradually. See what UC Davis and Minnesota advise.',
  short='Diet is the core of management: limit non-structural carbohydrates (sugar and starch), have hay analyzed, weigh rations, and aim for gradual weight loss. Avoid sudden severe feed cuts. Your veterinarian sets calorie targets for your horse.',
  body='''<h2>Core steps</h2>
<ul>
<li><strong>Lower the NSC.</strong> Both UC Davis and Minnesota say to reduce energy for weight loss and lower the non-structural carbohydrate (NSC) content of the diet. UC Davis says ideally under 10% of hay dry matter.</li>
<li><strong>Analyze the hay.</strong> UC Davis says analysis is the most reliable way to know NSC content; neither alfalfa nor grass hay is automatically safe or unsafe. Minnesota advises low-NSC grass hay with mineral and vitamin supplementation.</li>
<li><strong>Soaking hay</strong> lowers sugars but unpredictably, and it leaches minerals (UC Davis). Utah State describes soaking as leaching part of the NSC.</li>
<li><strong>Weigh rations.</strong> UC Davis suggests overweight horses start at 1.5% of ideal body weight in forage daily, with adjustment by the veterinarian; weighing matters because flakes vary.</li>
<li><strong>Remove grain.</strong> In overfed horses, removing all grain sometimes is enough to start weight loss (Minnesota).</li>
<li><strong>Use a ration balancer</strong> for vitamins and minerals without extra calories, and check that pellets are under 10% NSC (UC Davis).</li>
<li><strong>Limit pasture.</strong> Restrict grazing, use a muzzle or eliminate grazing; take extra care in spring and autumn (UC Davis). Severely insulin-resistant horses with recurrent laminitis may need to stay off pasture permanently (Minnesota).</li>
</ul>
<h2>Go gradually</h2>
<p>UC Davis warns against sudden feed restriction, which can raise blood fats and worsen insulin resistance. It also warns that an overweight horse that stops eating can develop dangerous fat buildup in the liver, which often needs emergency veterinary care. Call your vet if your horse stops eating.</p>
<p>Thin horses need more calories (UC Davis). See <a href="/qa/metabolic/safe-weight-management-for-horses/">safe weight management</a> and <a href="/qa/metabolic/supplements-for-cushings-and-insulin-resistance/">supplements</a>.</p>''',
  src=['ucdems','umnems','usu'], rel=['exercise-for-insulin-resistant-horses','safe-weight-management-for-horses','long-term-management-of-ems']),

 dict(slug='exercise-for-insulin-resistant-horses', ids=['VET-QA-0249','VET-QA-0259'], urgent=False,
  q='Can exercise help manage insulin resistance, and how often?',
  title='Exercise for Insulin-Resistant Horses',
  meta='Regular exercise improves insulin sensitivity and weight loss, except in horses sore from laminitis. See a suggested starting program from Minnesota.',
  short='Yes. Regular activity improves insulin sensitivity and helps weight loss, except for horses painful from laminitis. Minnesota suggests starting at about 20 to 30 minutes two to three times a week and building to five sessions, but your vet decides what is safe.',
  body='''<h2>What sources say</h2>
<ul>
<li><strong>It helps.</strong> University of Minnesota says regular activity improves insulin sensitivity and supports weight loss; USU adds that exercise can produce a sustained increase in insulin sensitivity.</li>
<li><strong>A starting point.</strong> Minnesota suggests about 20 to 30 minutes of riding or longeing two to three times a week, gradually increasing to five sessions a week.</li>
<li><strong>Sequence.</strong> USU suggests starting with diet changes to begin weight loss, then adding low-impact exercise and increasing as appropriate.</li>
<li><strong>Laminitis.</strong> UC Davis says exercise is not recommended during active laminitis; walking may be approved by a veterinarian for controlled laminitis.</li>
</ul>
<p>Exercise needs vary with soundness and condition, so get your vet's go-ahead first. See <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</p>''',
  src=['umnems','usu','ucdems'], rel=['diet-for-ems-and-insulin-resistance','long-term-management-of-ems','signs-of-laminitis-in-endocrine-disease']),

 dict(slug='long-term-management-of-ems', ids=['VET-QA-0269','VET-QA-0270'], urgent=False,
  q='What are the long-term management strategies for EMS?',
  title='Long-Term Management of EMS in Horses',
  meta='EMS cannot be cured but most horses are managed with diet, exercise, careful pasture and lifelong vet guidance. Medication is used only in some cases.',
  short='EMS cannot be cured, so management is lifelong: a low-NSC diet at a healthy weight, regular exercise, restricted pasture and ongoing veterinary guidance. Most horses can be managed with diet and exercise alone; medication is used in some cases.',
  body='''<h2>The long-term plan</h2>
<ul>
<li><strong>Diet</strong> — see <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</li>
<li><strong>Exercise</strong> — see <a href="/qa/metabolic/exercise-for-insulin-resistant-horses/">exercise</a>.</li>
<li><strong>Pasture control</strong> — extra care in spring and autumn, when sugar levels are higher (UC Davis).</li>
<li><strong>Medication if needed</strong> — Minnesota says most horses and ponies can be managed with diet and exercise alone; levothyroxine can induce weight loss and improve insulin sensitivity but only in certain circumstances, and should always be prescribed and monitored by a veterinarian. UC Davis lists thyroxine or metformin when diet and exercise are not enough.</li>
<li><strong>Check for PPID</strong> in older horses (UC Davis).</li>
<li><strong>Lifelong veterinary guidance</strong> (UC Davis). Outcomes vary: easy keepers and horses with persistently high insulin can be harder to manage.</li>
</ul>
<p>The sources reviewed do not set a monitoring interval for EMS; ask your veterinarian when to retest.</p>''',
  src=['ucdems','umnems'], rel=['diet-for-ems-and-insulin-resistance','ems-prevention','long-term-effects-of-untreated-endocrine-disease']),

 dict(slug='ems-prevention', ids=['VET-QA-0247','VET-QA-0256'], urgent=False,
  q='Can EMS be prevented?',
  title='Preventing EMS in Horses',
  meta='UC Davis advises keeping at-risk breeds at a healthy weight, feeding to ideal body condition, and managing pasture in high-sugar seasons to reduce EMS risk.',
  short='Prevention centers on weight and feeding: keep high-risk breeds at a healthy weight, feed to an ideal body condition score, give regular exercise and manage pasture carefully during high-sugar seasons.',
  body='''<h2>UC Davis prevention guidance</h2>
<ul>
<li>Keep high-risk breeds — ponies, donkeys, Arabians, mustangs — at a healthy weight.</li>
<li>Feed to an ideal body condition score rather than generic guidelines.</li>
<li>Manage pasture carefully during high-sugar seasons.</li>
</ul>
<p>UC Davis also notes that these breeds store energy efficiently, which becomes a problem with plentiful food and little exercise, so regular exercise is part of prevention. The sources reviewed do not describe a way to prevent PPID. See <a href="/qa/metabolic/signs-of-ems-and-insulin-resistance/">signs of EMS</a>.</p>''',
  src=['ucdems','uconn'], rel=['signs-of-ems-and-insulin-resistance','diet-for-ems-and-insulin-resistance','safe-weight-management-for-horses']),

 dict(slug='safe-weight-management-for-horses', ids=['VET-QA-0257'], urgent=False,
  q='How can I safely manage my horse’s weight?',
  title='Safe Weight Management for Horses',
  meta='Safe weight loss is gradual: weigh feed, limit sugar and starch, add exercise, and avoid sudden feed cuts. See UC Davis guidance for overweight horses.',
  short='Weigh feed, base it on forage, limit sugar and starch, add regular exercise and aim for gradual weight loss. Sudden feed cuts can raise blood fats and worsen insulin resistance, and an overweight horse that stops eating needs a vet.',
  body='''<h2>Steps from veterinary sources</h2>
<ul>
<li><strong>Weigh the ration</strong> — flakes of hay vary (UC Davis).</li>
<li><strong>Feed to ideal body condition</strong> rather than generic guidelines (UC Davis).</li>
<li><strong>Lose weight gradually.</strong> UC Davis warns that sudden feed cuts can raise blood fats and worsen insulin resistance.</li>
<li><strong>Add exercise</strong> as the horse's soundness allows (Minnesota; USU).</li>
<li><strong>Control pasture</strong> with limited turnout or a grazing muzzle (UC Davis).</li>
</ul>
<p>Thin horses need more calories from roughage, fat or protein sources (UC Davis). Have your veterinarian assess body condition and test for EMS or PPID before a major change. See <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</p>''',
  src=['ucdems','umnems','usu'], rel=['diet-for-ems-and-insulin-resistance','exercise-for-insulin-resistant-horses','ems-prevention']),

 dict(slug='long-term-effects-of-untreated-endocrine-disease', ids=['VET-QA-0267','VET-QA-0268'], urgent=False,
  q='What are the long-term effects of untreated endocrine disease or insulin resistance?',
  title='Long-Term Effects of Untreated Endocrine Disease',
  meta='Untreated PPID and insulin resistance raise the risk of laminitis, the main factor limiting lifespan in PPID. See what veterinary sources say about progression.',
  short='The main long-term danger is laminitis, which WCVM calls the main factor limiting the lifespan of horses with PPID. EMS also makes laminitis easier to develop. PPID signs generally worsen with age, and treatment controls signs without stopping progression.',
  body='''<h2>PPID</h2>
<ul>
<li>Laminitis is the main factor limiting a PPID horse's lifespan (WCVM).</li>
<li>Other signs progress: weight loss, muscle wasting, lethargy and greater susceptibility to infection; signs generally worsen with age.</li>
<li>Treatment controls signs but does not stop progression, and horses may become harder to control (WCVM).</li>
</ul>
<h2>EMS and insulin resistance</h2>
<ul>
<li>EMS makes laminitis easier to develop, and laminitis can be life-threatening (UC Davis).</li>
<li>Overweight horses that stop eating can develop dangerous liver fat buildup (UC Davis).</li>
<li>EMS cannot be cured; many horses improve with diet and exercise.</li>
</ul>
<p>Early testing and management are the best protection. See <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">signs of laminitis</a>.</p>''',
  src=['wcvm','ucdems'], rel=['signs-of-laminitis-in-endocrine-disease','long-term-management-of-ems','ppid-treatment-options']),

 dict(slug='signs-of-laminitis-in-endocrine-disease', ids=['VET-QA-0272'], urgent=True,
  q='What are the signs of laminitis I should watch for?',
  title='Signs of Laminitis in Horses With PPID or EMS',
  meta='Watch for front-foot soreness, reluctance to move, a backward-rocking stance and exaggerated front-foot lift. Laminitis is an emergency, so call your vet.',
  short='Warning signs include front-foot soreness, reluctance to move, a backward-rocking stance and an exaggerated lift of the front feet when walking. Horses with PPID or EMS are at higher risk. Call your veterinarian promptly.',
  body='''<h2>Signs (WCVM)</h2>
<ul>
<li>Soreness in the front feet</li>
<li>Reluctance to move</li>
<li>A stance with the weight rocked backward</li>
<li>An exaggerated lift of the front feet when walking</li>
</ul>
<h2>Why horses with PPID or EMS are at risk</h2>
<p>WCVM says horses with PPID have a higher risk of laminitis, and UC Davis says affected EMS horses are at high risk, especially with pasture access or high-carbohydrate feed. Laminitis is painful, and the hoof separates from the underlying bone.</p>
<p>Do not exercise a horse that is sore from laminitis unless your vet says so (UC Davis; Minnesota). See our <a href="/conditions/laminitis/">laminitis overview</a> and <a href="/emergency/lameness/">lameness emergency guide</a>.</p>''',
  src=['wcvm','ucdems','umnems'], rel=['signs-of-ems-and-insulin-resistance','signs-of-ppid-cushings','long-term-effects-of-untreated-endocrine-disease']),

 dict(slug='supplements-for-cushings-and-insulin-resistance', ids=['VET-QA-0246'], urgent=False,
  q='Are there natural supplements that help horses with Cushing’s disease or insulin resistance?',
  title='Supplements for Cushing’s and Insulin Resistance',
  meta='UC Davis says cinnamon, chromium and magnesium have not been shown to improve insulin sensitivity in experiments. Ask your vet before adding supplements.',
  short='UC Davis says popular supplements such as cinnamon, chromium and magnesium have not been shown to improve insulin sensitivity in experiments. WCVM’s PPID page does not cover herbal remedies. Check any supplement with your veterinarian.',
  body='''<h2>What the sources say</h2>
<ul>
<li>UC Davis: cinnamon, chromium and magnesium have not been shown to improve insulin sensitivity in experiments.</li>
<li>WCVM's PPID page does not address supplements or herbal remedies.</li>
<li>A ration balancer for vitamins and minerals, without added calories, is part of the standard EMS feeding approach (UC Davis); soaking hay leaches minerals, so mineral supplementation matters.</li>
</ul>
<p>Some supplements add sugar or starch. Ask your vet before adding anything, and do not use a supplement in place of testing or prescribed medication. See <a href="/qa/metabolic/diet-for-ems-and-insulin-resistance/">diet for EMS</a>.</p>''',
  src=['ucdems','wcvm'], rel=['diet-for-ems-and-insulin-resistance','ppid-diet','ppid-treatment-options']),

 dict(slug='is-endocrine-treatment-working-or-worsening', ids=['VET-QA-0273','VET-QA-0274','VET-QA-0285'], urgent=False,
  q='How do I know if treatment is working or my horse’s condition is getting worse?',
  title='Is Treatment Working? PPID and EMS Progress',
  meta='PPID owners often see improvement after six to eight weeks of treatment. Warning signs of worsening include laminitis. Only repeat testing confirms control.',
  short='For PPID, WCVM says owners often see improvement after six to eight weeks of treatment, and repeat tests show whether hormone levels have normalized. Laminitis signs, weight change and a coat that stops shedding are warning signs. Your vet confirms progress with testing.',
  body='''<h2>PPID</h2>
<ul>
<li>Improvement: owners often see it after six to eight weeks of treatment (WCVM).</li>
<li>Confirmation: tests can be repeated to check whether hormone levels have normalized, and WCVM recommends assessment every six months.</li>
<li>Worsening: dose may need to rise, and laminitis signs call for prompt veterinary attention.</li>
</ul>
<h2>EMS and insulin resistance</h2>
<ul>
<li>Healthy weight and fat distribution are management goals (UC Davis; Minnesota).</li>
<li>Laminitis signs mean the condition is not controlled — see <a href="/qa/metabolic/signs-of-laminitis-in-endocrine-disease/">signs of laminitis</a>.</li>
<li>The sources reviewed give no interval for retesting insulin; ask your vet.</li>
</ul>
<p>See <a href="/qa/metabolic/ppid-monitoring-and-retesting/">PPID monitoring</a>.</p>''',
  src=['wcvm','ucdems','umnems'], rel=['ppid-monitoring-and-retesting','signs-of-laminitis-in-endocrine-disease','long-term-management-of-ems']),

 dict(slug='common-causes-of-lethargy-in-horses', ids=['VET-QA-0264','VET-QA-0250'], urgent=True,
  q='What causes lethargy in horses, and can diet or environment be the reason?',
  title='Common Causes of Lethargy in Horses',
  meta='Lethargy can come from digestive, infectious, toxic, organ or metabolic disease, or feed and plant hazards. A dull horse needs a vet exam to find the cause.',
  short='A lethargic or depressed horse has a sign, not a diagnosis. One veterinary guide lists digestive, infectious, toxic, organ, metabolic and injury causes, including grain overload, moldy corn, poisonous plants and under-nutrition. Taken alone the sign is too broad to point to one cause, so a veterinarian needs to examine the horse.',
  body='''<h2>What it looks like</h2>
<p>Horse-Side Vet Guide (Dr. Doug Thal) describes a depressed or lethargic horse as sleepy or drowsy, with a hanging head or lip, usually not eating, and uninterested in people, herd mates or surroundings. Standing with the head down in heat or at midday can be normal.</p>
<h2>Causes listed (Horse-Side Vet Guide)</h2>
<ul>
<li><strong>Digestive:</strong> colic, impactions, gastric ulcers, intestinal inflammation and colitis.</li>
<li><strong>Infectious:</strong> respiratory viruses, pneumonia, strangles, equine influenza, herpesvirus, Potomac horse fever and West Nile virus, among others.</li>
<li><strong>Organ and metabolic:</strong> kidney, liver, heart and blood disorders, diabetes, low blood sugar and under-nutrition.</li>
<li><strong>Toxic, injury and other:</strong> many plant, feed and chemical poisonings, abscesses, fractures, snake bites, insect stings, and stress or anxiety.</li>
</ul>
<h2>Diet and environment</h2>
<ul>
<li><strong>Diet:</strong> the guide lists carbohydrate or grain overload, moldy corn and aflatoxins, monensin and selenium toxicity, and under-nutrition.</li>
<li><strong>Environment:</strong> poisonous plants and weeds, blister beetles, lead, rodenticides, snake and insect bites, smoke inhalation, and mosquito-borne and tick-borne diseases.</li>
</ul>
<h2>What the sources do not say</h2>
<p>The guide says depression taken alone is usually too broad a sign to narrow the problem, and other signs help your veterinarian choose tests. It does not explain how to tell these causes apart or how to treat them, and it advises against giving flunixin on your own without knowing the cause. Endocrine disease is another possible cause; see <a href="/qa/metabolic/signs-of-ppid-cushings/">signs of PPID</a>. Check the horse as described in <a href="/qa/metabolic/when-to-call-the-vet-for-a-lethargic-horse/">when to call the vet</a>.</p>''',
  src=['hsvg13'], rel=['when-to-call-the-vet-for-a-lethargic-horse','signs-of-ppid-cushings','long-term-effects-of-untreated-endocrine-disease']),

 dict(slug='when-to-call-the-vet-for-a-lethargic-horse', ids=['VET-QA-0290'], urgent=True,
  q='When should I call the vet for a lethargic horse?',
  title='When to Call the Vet for a Lethargic Horse',
  meta='Call at once if a lethargic horse will not eat, shows colic signs, or has a fever or fast heart rate, even after hours. Check temperature and pulse first.',
  short='Call your veterinarian immediately, even after hours, if a dull horse has no appetite, shows signs of colic, or has a resting fever or fast heart rate. Horse-Side Vet Guide gives over 101°F and over 48 beats per minute; the University of Florida gives a fever over 101.5°F for adults and lists depression as a reason to call.',
  body='''<h2>Call immediately, even outside business hours (Horse-Side Vet Guide)</h2>
<ul>
<li>The horse has no appetite and is obviously depressed.</li>
<li>Any signs of colic.</li>
<li>A resting horse has a temperature above 101°F (38.3°C) or a heart rate above 48 beats per minute.</li>
</ul>
<h2>Call at first office hours</h2>
<p>The guide lists mild or occasional dullness in a horse that seems normal otherwise. It does not spell out more criteria for this level.</p>
<h2>University of Florida list</h2>
<p>The University of Florida Large Animal Hospital lists fever (adult temperature above 101.5°F), loss of appetite or difficulty eating, depression or anxiety, diarrhea beyond loose manure from excitement or trailering, and difficulty breathing among reasons to call. It says to call your vet sooner rather than later.</p>
<p>The two sources give slightly different fever thresholds; ask your veterinarian what is normal for your horse.</p>
<h2>What to check while you call</h2>
<ul>
<li>Temperature, pulse and breathing rate, and whether the horse walks straight lines and circles normally.</li>
<li>Appetite: offer a small amount of a feed the horse likes.</li>
<li>Manure output and signs of abdominal pain such as rolling or looking at the flank.</li>
<li>Recent feed or management changes, new horses on the property, and any cough, swelling or lameness.</li>
</ul>
<p>Do not give painkillers before talking to your veterinarian; the guide advises against giving flunixin on your own without knowing the cause. See <a href="/qa/metabolic/common-causes-of-lethargy-in-horses/">causes of lethargy</a> and <a href="/emergency/">emergencies</a>.</p>''',
  src=['hsvg13','uflcall'], rel=['common-causes-of-lethargy-in-horses','signs-of-ppid-cushings','long-term-effects-of-untreated-endocrine-disease']),
]
