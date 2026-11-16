# -*- coding: utf-8 -*-
"""Respiratory, nasal discharge, cough and digital-pulse Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umnpneu': ('University of Minnesota Extension — Pneumonia in horses', 'https://extension.umn.edu/agriculture/animals-and-livestock/horse/pneumonia-horse'),
 'petplace': ('PetPlace — Bacterial Pneumonia in the Horse', 'https://petplace.com/article/horses/general/bacterial-pneumonia-in-the-horse'),
 'equimedpp': ('EquiMed (NC State, Equine Disease Quarterly) — Equine Pleuropneumonia', 'https://equimed.com/news/health/equine-pleuropneumonia-considered-the-most-severe-form-of-pneumonia'),
 'equusnasal': ('EQUUS — Runny nose: When is it serious?', 'https://equusmagazine.com/horse-care/runny-nose-when-is-it-serious'),
 'equuscough': ('EQUUS — When to worry about coughing in horses', 'https://equusmagazine.com/horse-care/worry-coughs'),
 'ufasra': ('UF/IFAS Extension — Understanding Equine Asthma and Recurrent Airway Obstruction (RAO) in the Horse, VM142', 'https://journals.flvc.org/edis/article/download/118499/141796/265158'),
 'extresp': ('eXtension Horses — Taking a horse\'s respiration', 'https://horses.extension.org/?p=718'),
 'horseresp': ('The Horse — Diagnosing Breathing Problems', 'https://thehorse.com/130679/diagnosing-breathing-problems/'),
 'equimedpulse': ('EquiMed (Equine Guelph) — Take Your Horse\'s Digital Pulse', 'https://equimed.com/news/health/take-your-horse-s-digital-pulse'),
})
HELD = {
 'VET-QA-0404':'laminitis-signs question filed under respiratory; duplicate of /qa/lameness/signs-of-laminitis-and-founder/',
 'VET-QA-0415':'vet-check frequency; no source reviewed gives a schedule',
 'VET-QA-0435':'generic "what tests diagnose the cause" with no condition named',
}
PAGES = [
 dict(slug='signs-of-pneumonia-in-horses', ids=['VET-QA-0423'], urgent=True,
  q='What are the signs of pneumonia in horses?',
  title='Signs of Pneumonia in Horses',
  meta='Pneumonia can cause yellow or cream nasal discharge, depression, persistent fever, cough and faster breathing. Call your vet promptly; it can worsen quickly.',
  short='Possible signs are yellow or cream-colored nasal discharge, depression and persistent fever. After shipping, a horse may stand with elbows out, lie down more and resist moving. Horses can have a large reserve, so signs may appear late. Call your veterinarian promptly.',
  body='''<h2>Signs (University of Minnesota Extension)</h2>
<ul>
<li>Yellow or cream-colored nasal discharge, depression and persistent fever.</li>
<li>Viral respiratory infections, which can lead to pneumonia, may cause fever, clear nasal discharge, throat lymph node swelling, poor appetite and cough.</li>
<li>Shipping pleuropneumonia may cause a horse to stand with its elbows held out, lie down more and resist moving.</li>
</ul>
<p>PetPlace notes horses have a large respiratory reserve, so pneumonia may be well established by the time an increased breathing rate, cough or fever shows. EquiMed adds that horses with pleuropneumonia do not always have nasal discharge or cough; subtler signs include fever above 101.5°F, weight loss, reduced appetite and malaise.</p>
<p><strong>Call your veterinarian promptly</strong> for these signs; diagnosis needs a thorough work-up. See <a href="/qa/respiratory/how-pneumonia-is-diagnosed/">how it is diagnosed</a> and <a href="/qa/respiratory/signs-of-serious-respiratory-problems/">emergency signs</a>.</p>''',
  src=['umnpneu','petplace','equimedpp'], rel=['how-pneumonia-is-diagnosed','pneumonia-treatment-and-recovery','signs-of-serious-respiratory-problems']),

 dict(slug='how-pneumonia-is-diagnosed', ids=['VET-QA-0403','VET-QA-0413'], urgent=False,
  q='How is pneumonia diagnosed, and what tests confirm it?',
  title='How Pneumonia Is Diagnosed in Horses',
  meta='Vets diagnose pneumonia with an exam, blood work, chest ultrasound, a tracheal wash and culture to find the germ and the antibiotics that work against it.',
  short='Vets use blood work to gauge how ill the horse is, thoracic ultrasound to see how much lung is damaged, a trans-tracheal wash to collect a sterile lung sample, and culture and sensitivity to identify the germ and which antibiotics work.',
  body='''<h2>Tests (University of Minnesota Extension)</h2>
<ul>
<li><strong>Blood work</strong> (CBC and biochemistry) to gauge how severe the systemic illness is.</li>
<li><strong>Thoracic ultrasound</strong> to see how much of the lung surface is damaged.</li>
<li><strong>Trans-tracheal wash</strong> to collect a sterile lung fluid sample.</li>
<li><strong>Culture and sensitivity</strong> to identify the specific pathogen and which antibiotics it responds to.</li>
</ul>
<p>Minnesota says diagnosing pneumonia and its exact cause requires a thorough work-up. EquiMed says pleuropneumonia is confirmed by imaging of the lungs and sampling of the airways to identify bacterial infection. These tests are done by a veterinarian. See <a href="/qa/respiratory/signs-of-pneumonia-in-horses/">signs</a>.</p>''',
  src=['umnpneu','equimedpp'], rel=['signs-of-pneumonia-in-horses','pneumonia-treatment-and-recovery','pneumonia-complications-and-prevention']),

 dict(slug='pneumonia-treatment-and-recovery', ids=['VET-QA-0430','VET-QA-0414'], urgent=False,
  q='What is the treatment plan for pneumonia, and how long does recovery take?',
  title='Pneumonia Treatment and Recovery Time in Horses',
  meta='Mild to moderate pneumonia often responds to antibiotics and supportive care. Treatment may last 7 days to 4 weeks, or months for pleuropneumonia.',
  short='Mild to moderate cases often respond to antibiotics, anti-inflammatory drugs and supportive care. PetPlace says treatment may range from 7 days to 4 weeks or longer, and EquiMed says pleuropneumonia can need months of antimicrobials. Your vet sets the plan.',
  body='''<h2>Treatment (University of Minnesota Extension)</h2>
<ul>
<li>Mild to moderate cases often respond well to antibiotics, anti-inflammatory drugs and supportive care.</li>
<li>Severe cases are harder to treat because permanent lung damage can occur.</li>
<li>The antibiotic is chosen using culture and sensitivity results.</li>
</ul>
<h2>How long it takes</h2>
<ul>
<li>Minnesota gives no timeframe.</li>
<li>PetPlace says treatment length varies with severity and may range from 7 days to 4 weeks or longer.</li>
<li>EquiMed says as pleuropneumonia resolves, horses may move from injectable to oral antimicrobials, and long-term treatment at home may be needed for multiple months.</li>
</ul>
<p>The sources give no doses; your veterinarian decides drugs and recheck timing. See <a href="/qa/respiratory/monitoring-pneumonia-recovery-at-home/">monitoring at home</a>.</p>''',
  src=['umnpneu','petplace','equimedpp'], rel=['how-pneumonia-is-diagnosed','monitoring-pneumonia-recovery-at-home','pneumonia-complications-and-prevention']),

 dict(slug='monitoring-pneumonia-recovery-at-home', ids=['VET-QA-0406','VET-QA-0422'], urgent=True,
  q='How can I monitor a horse with pneumonia at home, and what shows improvement or worsening?',
  title='Monitoring a Horse With Pneumonia at Home',
  meta='Check temperature once or twice a day and watch appetite, cough and breathing. Call your vet if fever returns, breathing worsens or the horse stops eating.',
  short='PetPlace advises checking the rectal temperature once or twice a day. Also note appetite, cough, nasal discharge and breathing effort. Worsening, such as a returning fever, harder breathing or loss of appetite, means call your veterinarian right away.',
  body='''<h2>What to track</h2>
<ul>
<li>Rectal temperature once or twice a day (PetPlace home care).</li>
<li>Discharge color, odor, amount and thickness; appetite and water intake; coughing; and dullness (EQUUS).</li>
<li>Breathing rate and effort; see <a href="/qa/respiratory/normal-respiratory-rate-in-horses/">normal respiratory rate</a>.</li>
</ul>
<h2>Better or worse?</h2>
<p>The sources reviewed give no list of improvement markers. A horse that is eating, brighter and has a normal temperature is generally moving in the right direction, but your veterinarian should confirm and decide when to recheck. <strong>Call your vet right away</strong> for a returning or persistent fever, harder or faster breathing, thicker or foul discharge, or loss of appetite. The University of Minnesota page gives no home monitoring steps beyond knowing the signs. See <a href="/qa/respiratory/signs-of-serious-respiratory-problems/">emergency signs</a>.</p>''',
  src=['petplace','equusnasal','umnpneu'], rel=['pneumonia-treatment-and-recovery','signs-of-serious-respiratory-problems']),

 dict(slug='pneumonia-complications-and-prevention', ids=['VET-QA-0420','VET-QA-0410'], urgent=False,
  q='What are the complications of untreated pneumonia, and how can I prevent it?',
  title='Pneumonia Complications and Prevention in Horses',
  meta='Pneumonia can cause permanent lung damage and reduced performance. Reduce travel stress, keep vaccines current and manage chronic illness to help prevent it.',
  short='Complications include permanent lung damage, reduced long-term performance and, after transport, infection of the pleural cavity. To help prevent it, reduce stress when horses travel or mix, keep vaccinations current, and manage conditions such as Cushing\'s, EMS and airway disease.',
  body='''<h2>Complications (University of Minnesota Extension)</h2>
<ul>
<li>Permanent lung tissue damage.</li>
<li>Reduced long-term athletic performance, depending on the extent of damage.</li>
<li>Pleural cavity involvement in shipping pleuropneumonia.</li>
<li>Secondary bacterial infection following a viral infection.</li>
</ul>
<p>The sources reviewed give no figures for outcomes of untreated cases; EQUUS says a cough after trailering has the best chance of survival if treated within 48 hours.</p>
<h2>Prevention</h2>
<ul>
<li>Reduce stress, especially when horses mix with others or travel long distances: break up long trips and keep a regular routine.</li>
<li>Ask your vet about conditions that raise risk, named as Cushing's disease, equine metabolic syndrome and inflammatory airway disease; keep them under management.</li>
<li>Keep vaccinations current against common respiratory infections and know the signs of pneumonia.</li>
</ul>
<p>See <a href="/qa/infectious/ehv-1-prevention-and-isolation/">biosecurity and isolation</a>.</p>''',
  src=['umnpneu','equuscough'], rel=['signs-of-pneumonia-in-horses','pneumonia-treatment-and-recovery','preventing-cough-and-respiratory-problems']),

 dict(slug='causes-of-nasal-discharge-in-horses', ids=['VET-QA-0416','VET-QA-0427'], urgent=False,
  q='What are common causes of nasal discharge in horses?',
  title='Common Causes of Nasal Discharge in Horses',
  meta='Clear watery discharge in a well horse is often dust irritation. Thick yellow discharge suggests infection, and foul smell suggests tooth or sinus infection.',
  short='Clear, watery discharge in an otherwise well horse is usually minor irritation from dust or hay. Thick yellow pus-like mucus may mean bacterial or viral infection or strangles; foul smell may mean a tooth or sinus infection; food from the nose suggests choke.',
  body='''<h2>By type of discharge (EQUUS)</h2>
<ul>
<li><strong>Clear and watery, horse otherwise well:</strong> usually minor irritation from inhaled hay or dust, or a dusty eye draining through the nostril.</li>
<li><strong>Small bright-red trickle that stops within minutes:</strong> likely a scratch from a stick or stemmy hay.</li>
<li><strong>Foul-smelling:</strong> possibly an infection such as a tooth or sinus, sometimes with facial swelling on one side.</li>
<li><strong>Thin, gray, frothy mucus:</strong> likely a guttural pouch infection.</li>
<li><strong>Dark blood:</strong> blood collected in the sinuses or guttural pouches; if it gushes with the head lowered, the respiratory tract may be involved.</li>
<li><strong>Thick, yellow, pus-filled mucus:</strong> bacterial or viral infection, or strangles; fever and cough are typically present.</li>
<li><strong>Saliva and chewed food:</strong> choke.</li>
</ul>
<p>Only a veterinarian can tell these apart reliably. See <a href="/qa/respiratory/when-to-call-the-vet-for-nasal-discharge/">when to call the vet</a> and <a href="/qa/infectious/signs-and-complications-of-strangles/">strangles signs</a>.</p>''',
  src=['equusnasal'], rel=['when-to-call-the-vet-for-nasal-discharge','nasal-discharge-treatment-and-recurrence','causes-of-cough-in-horses']),

 dict(slug='when-to-call-the-vet-for-nasal-discharge', ids=['VET-QA-0432','VET-QA-0434'], urgent=True,
  q='What signs mean nasal discharge is getting worse, and what should I do?',
  title='When Nasal Discharge Is Worsening: Call the Vet',
  meta='Call your vet for foul-smelling, thick yellow or bloody discharge, or food from the nose. Isolate the horse from others and track color, odor and fever.',
  short='Call your veterinarian right away for foul-smelling discharge, thick yellow pus-like mucus, dark or steadily flowing blood, or food or saliva from the nose. Isolate a horse that may be contagious and track discharge, appetite, cough, temperature and pulse.',
  body='''<h2>Call right away if you see (EQUUS)</h2>
<ul>
<li>Foul-smelling discharge.</li>
<li>Bright-red blood that flows steadily for 30 minutes or more, or dark blood, especially gushing when the head is lowered.</li>
<li>Thick, yellow, pus-like mucus.</li>
<li>Food or saliva from the nose or mouth with coughing, gagging or panic (choke): remove all food and water until the vet arrives.</li>
</ul>
<h2>What to monitor</h2>
<ul>
<li>Discharge color, odor, amount, consistency and whether one or both nostrils are affected; photos help track changes.</li>
<li>Dullness, appetite and water intake, coughing, temperature and pulse.</li>
</ul>
<h2>Isolation</h2>
<p>If strangles or another contagious disease is suspected, keep the horse in a stall or small turnout at least 10 feet from others, avoid nose-to-nose contact, and wash or sanitize hands (ideally change clothes) before handling other horses. See <a href="/qa/infectious/preventing-and-containing-strangles/">containing strangles</a>.</p>''',
  src=['equusnasal'], rel=['causes-of-nasal-discharge-in-horses','nasal-discharge-treatment-and-recurrence','signs-of-serious-respiratory-problems']),

 dict(slug='nasal-discharge-treatment-and-recurrence', ids=['VET-QA-0436','VET-QA-0437','VET-QA-0412'], urgent=False,
  q='How is nasal discharge treated, and how do I keep it from coming back?',
  title='Nasal Discharge Treatment and Preventing Recurrence',
  meta='Treatment depends on the cause, so a vet must find it first. The sources give no single treatment or recurrence plan. Isolate until a diagnosis is made.',
  short='Treatment depends on the cause, which only a veterinarian can determine; there is no single treatment. The sources reviewed give no recurrence plan. Avoiding dusty hay and bedding may help when dust is the trigger, and a suspected infection means isolation until diagnosis.',
  body='''<h2>Treatment depends on the cause</h2>
<ul>
<li>Choke: remove all food and water until the vet arrives (EQUUS).</li>
<li>Suspected contagious infection: isolate the horse until the vet makes a diagnosis (EQUUS).</li>
<li>Pneumonia: antibiotics, anti-inflammatories and supportive care, guided by culture results (University of Minnesota Extension). See <a href="/qa/respiratory/pneumonia-treatment-and-recovery/">pneumonia treatment</a>.</li>
<li>Dust-related airway disease: environmental management is the most important step (UF/IFAS). See <a href="/qa/respiratory/respiratory-treatment-options/">treatment options</a>.</li>
</ul>
<h2>Preventing recurrence</h2>
<p>EQUUS does not cover treatment or recurrence prevention for nasal discharge. Since the cause varies, recurrence prevention follows the cause: lower-dust hay and bedding for dust irritation, and vaccination and isolation practices for infections. Repeated discharge, especially from one nostril, needs a veterinary work-up. See <a href="/qa/respiratory/causes-of-nasal-discharge-in-horses/">causes</a>.</p>''',
  src=['equusnasal','umnpneu','ufasra'], rel=['causes-of-nasal-discharge-in-horses','when-to-call-the-vet-for-nasal-discharge','respiratory-treatment-options']),

 dict(slug='causes-of-cough-in-horses', ids=['VET-QA-0425'], urgent=False,
  q='What could be causing my horse\'s cough?',
  title='What Causes Coughing in Horses?',
  meta='Coughs come from infections like flu, strangles and pneumonia, heaves, dust, choke or foreign objects. A new or lasting cough needs a vet.',
  short='Common causes include influenza, rhinopneumonitis, strangles, pneumonia, heaves and inflammatory airway disease. Occasional coughing after inhaling dust is normal. A cough with fever, discharge or lethargy, or one that persists a day or two, needs a veterinarian.',
  body='''<h2>Causes (EQUUS)</h2>
<ul>
<li>Common: aspiration pneumonia, inflammatory airway disease, influenza, pleuropneumonia, pneumonia, recurrent airway obstruction ("heaves"), rhinopneumonitis and strangles.</li>
<li>Occasional coughing is normal, such as after inhaling dusty air or debris while eating or drinking.</li>
<li>Less common: tumors pressing on airways, chest injuries, a foreign object such as a piece of hay, and guttural pouch mycosis.</li>
<li>Young horses can cough from ascarid roundworms; foals under 4 months can get <em>Rhodococcus equi</em> pneumonia.</li>
</ul>
<h2>Clues</h2>
<p>EQUUS says heaves typically does not cause fever, while viral infections often do, and thin clear discharge suggests allergies while thick yellow or white suggests bacterial infection. Call your veterinarian for a new cough, a cough with fever, lethargy or discharge, or a dry cough lasting a day or two. See <a href="/qa/respiratory/signs-of-serious-respiratory-problems/">emergency signs</a>.</p>''',
  src=['equuscough'], rel=['preventing-cough-and-respiratory-problems','signs-of-serious-respiratory-problems','common-respiratory-conditions-in-horses']),

 dict(slug='preventing-cough-and-respiratory-problems', ids=['VET-QA-0409','VET-QA-0408','VET-QA-0411'], urgent=False,
  q='How can I prevent coughs, respiratory infections and future respiratory problems?',
  title='Preventing Coughs and Respiratory Problems',
  meta='Cut dust: wet or low-dust hay, hay at or below nose level, low-dust bedding and good ventilation. Keep vaccines current and isolate sick horses.',
  short='Reduce dust and mold by wetting or choosing low-dust hay, feeding hay at or below nose level, and using low-dust bedding in a clean, well-ventilated space. Keep vaccinations current, reduce travel stress, and isolate horses that may be infectious.',
  body='''<h2>Dust and barn environment (EQUUS; UF/IFAS)</h2>
<ul>
<li>Wet the hay or use low-dust hay; place hay on the ground or hang nets below nose level.</li>
<li>Avoid straw bedding; shredded paper or cardboard are suggested low-dust options, and avoid storing hay in a loft above the stalls.</li>
<li>Keep horses on pasture when possible; those that must be stalled need clean, well-ventilated space, with minimal sweeping while they are in.</li>
<li>Round bale hay is high in dust and endotoxin.</li>
<li>Medications relieve signs, but signs return if the horse goes back to a moldy or dusty environment.</li>
</ul>
<h2>Infections</h2>
<ul>
<li>Keep vaccinations current and reduce travel and mixing stress (University of Minnesota Extension).</li>
<li>Isolate a horse suspected of infection, and wash up or change clothes before handling others (EQUUS). See <a href="/qa/infectious/ehv-1-prevention-and-isolation/">biosecurity</a>.</li>
</ul>''',
  src=['equuscough','ufasra','umnpneu'], rel=['causes-of-cough-in-horses','respiratory-treatment-options','pneumonia-complications-and-prevention']),

 dict(slug='common-respiratory-conditions-in-horses', ids=['VET-QA-0417','VET-QA-0418'], urgent=False,
  q='What are common respiratory conditions and issues in horses?',
  title='Common Respiratory Conditions in Horses',
  meta='Common respiratory problems include viral infections, strangles, pneumonia and equine asthma (heaves), plus upper airway problems that affect performance.',
  short='Common problems include viral infections (influenza, herpesvirus), strangles, pneumonia and pleuropneumonia, and equine asthma or heaves. Upper airway problems can affect performance during exercise. Viruses often open the way for secondary bacterial infection.',
  body='''<h2>Common conditions</h2>
<ul>
<li><strong>Viral infections:</strong> described by Minnesota Extension as the most common respiratory infections in horses, including equine herpesvirus and influenza; they more often leave airways open to bacterial infection. See <a href="/qa/infectious/signs-and-complications-of-equine-influenza/">influenza</a> and <a href="/qa/infectious/signs-of-ehv-1-and-rhinopneumonitis/">EHV-1</a>.</li>
<li><strong>Strangles:</strong> see <a href="/qa/infectious/signs-and-complications-of-strangles/">signs and complications</a>.</li>
<li><strong>Pneumonia and shipping pleuropneumonia</strong> (Minnesota).</li>
<li><strong>Equine asthma / RAO (heaves):</strong> a common chronic lung disease with airway narrowing and mucus, with signs such as faster breathing, cough and exercise intolerance (UF/IFAS).</li>
<li><strong>Inflammatory airway disease:</strong> in young horses, typically exercise intolerance and cough while normal at rest; it can fully resolve (UF/IFAS).</li>
<li><strong>Upper airway problems</strong> such as laryngeal hemiplegia and soft palate displacement, which can block much of the airway during exercise (The Horse).</li>
</ul>
<p>See <a href="/qa/respiratory/respiratory-treatment-options/">treatment options</a>.</p>''',
  src=['umnpneu','ufasra','horseresp'], rel=['causes-of-cough-in-horses','respiratory-treatment-options','signs-of-serious-respiratory-problems']),

 dict(slug='normal-respiratory-rate-in-horses', ids=['VET-QA-0419','VET-QA-0407'], urgent=False,
  q='What is a normal respiratory rate for a horse, and how do I monitor respiratory health at home?',
  title='Normal Respiratory Rate for Horses and How to Check',
  meta='Sources give a resting adult rate of about 8 to 12 or 8 to 16 breaths per minute. Count chest rises at rest, learn your horse\'s baseline and note any change.',
  short='eXtension gives 8 to 12 breaths per minute for adults and The Horse gives 8 to 16 at rest; newborn foals run 60 to 80 and older foals 20 to 40. Excitement and heat raise the rate temporarily. Learn your horse\'s own baseline and report a persistent rise.',
  body='''<h2>Normal rates</h2>
<ul>
<li>Adult horses at rest: 8 to 12 breaths per minute (eXtension) or about 8 to 16 (The Horse). The sources differ, so learn your own horse's baseline.</li>
<li>Newborn foals 60 to 80; older foals at rest 20 to 40 (eXtension).</li>
<li>Excitement, hot weather and humidity can raise the rate temporarily; after exercise it can be very high and decline over about 30 minutes (The Horse).</li>
</ul>
<h2>How to check</h2>
<p>Count one inhale and exhale as one breath by watching the chest or flank, or feel air from the nostrils; a stethoscope can pick up airflow over the windpipe. Note whether breaths are shallow or deep and any squeaks or crackles (eXtension). Check at rest, when the horse is calm.</p>
<p>The sources reviewed give no exact threshold for an abnormal resting rate. A rate that stays up, nostril flaring, or visible chest movement with each breath is a reason to call your veterinarian; see <a href="/qa/respiratory/causes-of-high-respiratory-rate/">high respiratory rate</a>.</p>''',
  src=['extresp','horseresp'], rel=['causes-of-high-respiratory-rate','signs-of-serious-respiratory-problems']),

 dict(slug='causes-of-high-respiratory-rate', ids=['VET-QA-0426'], urgent=False,
  q='What could be causing my horse\'s high respiratory rate?',
  title='What Causes a High Respiratory Rate in Horses?',
  meta='Excitement, heat and exercise raise breathing rate temporarily. A rate that stays high may mean heaves, airway disease, pain or infection, and needs a vet.',
  short='Excitement, hot weather and exercise raise the rate temporarily. A rate that stays elevated may point to heaves or inflammatory airway disease, and infection or pain can also raise it. A horse breathing fast at rest should be checked by a veterinarian.',
  body='''<h2>Temporary causes</h2>
<p>Excitement, hot or humid conditions and exercise raise the respiratory rate; the horse also uses breathing to cool down (The Horse; eXtension).</p>
<h2>Causes that need attention</h2>
<ul>
<li>A rate that stays elevated may indicate heaves or inflammatory airway disease (The Horse).</li>
<li>In severe heaves the rate is much higher than normal, the nostrils flare, the chest moves noticeably with each breath and there is often a persistent cough; a "heave line" can develop (The Horse; UF/IFAS).</li>
<li>Pneumonia can raise the rate; PetPlace notes it may be established by the time the rate rises.</li>
</ul>
<p>The sources reviewed also link an elevated heart rate to pain (EQUUS). If the rate stays up at rest, take the temperature and call your veterinarian; see <a href="/qa/respiratory/signs-of-serious-respiratory-problems/">emergency signs</a>.</p>''',
  src=['horseresp','extresp','ufasra','petplace','equusnasal'], rel=['normal-respiratory-rate-in-horses','signs-of-serious-respiratory-problems','common-respiratory-conditions-in-horses']),

 dict(slug='signs-of-serious-respiratory-problems', ids=['VET-QA-0421','VET-QA-0433','VET-QA-0439'], urgent=True,
  q='What signs indicate a serious respiratory problem or emergency, and when should I call a vet?',
  title='Respiratory Emergency Signs: When to Call the Vet',
  meta='Call your vet now for trouble breathing, nostril flaring, a cough after trailering, fever with cough or discharge, or a cough that lasts a day or two.',
  short='Call your veterinarian immediately for trouble breathing, nostril flaring, visible chest effort, a cough starting hours after trailering, or a cough with fever, lethargy or discharge. A new cough, or a dry cough lasting a day or two, also warrants a call.',
  body='''<h2>Call your veterinarian promptly for (EQUUS; The Horse)</h2>
<ul>
<li>Struggling to breathe, seeming short of air, nostrils flaring with each breath, or noticeable chest movement on inhaling and exhaling.</li>
<li>A cough that starts a few hours after trailering; EQUUS says survival odds from shipping fever are best if treated within 48 hours.</li>
<li>A cough with fever, lethargy, or nasal or eye discharge.</li>
<li>A new cough in a horse that has never coughed, or a dry cough lasting a day or two.</li>
<li>A cough with exercise intolerance, limb swelling or a visible pulse along the jugular vein.</li>
<li>Coughing while eating or drinking, or a choke episode where food may have been inhaled.</li>
<li>Any cough in a foal or young horse, especially if several are affected.</li>
</ul>
<h2>Meanwhile</h2>
<p>Take the temperature and keep the horse calm. If an infection is possible, isolate it and wash up or change clothes before handling other horses. See <a href="/qa/respiratory/normal-respiratory-rate-in-horses/">respiratory rate</a> and <a href="/emergency/">our emergency guides</a>.</p>''',
  src=['equuscough','horseresp','equusnasal'], rel=['causes-of-cough-in-horses','causes-of-high-respiratory-rate','signs-of-pneumonia-in-horses']),

 dict(slug='respiratory-treatment-options', ids=['VET-QA-0438'], urgent=False,
  q='What treatment options are available for respiratory issues in horses?',
  title='Respiratory Treatment Options for Horses',
  meta='Treatment depends on the cause: antibiotics for bacterial pneumonia, rest for viral illness, and dust control plus vet-directed drugs for asthma.',
  short='Treatment depends on the diagnosis. Bacterial pneumonia is treated with antibiotics, anti-inflammatories and supportive care; viral illness mainly with rest and supportive care; and equine asthma mainly by cutting dust and mold, with veterinary-prescribed drugs. No dose is given here.',
  body='''<h2>By cause</h2>
<ul>
<li><strong>Pneumonia:</strong> antibiotics, anti-inflammatories and supportive care, chosen using culture results (University of Minnesota Extension). See <a href="/qa/respiratory/pneumonia-treatment-and-recovery/">pneumonia treatment</a>.</li>
<li><strong>Influenza and viral illness:</strong> rest and supportive care. See <a href="/qa/infectious/equine-influenza-treatment-and-recovery/">influenza recovery</a>.</li>
<li><strong>Equine asthma (RAO/heaves):</strong> environmental and dietary management to reduce dust and mold is the most important step, and mild cases may be controlled with it alone. Corticosteroids and bronchodilators give the fastest relief for horses in respiratory distress; your veterinarian chooses the drug, dose and schedule (UF/IFAS).</li>
<li><strong>Inflammatory airway disease in young horses</strong> can fully resolve, with treatment or occasionally on its own (UF/IFAS).</li>
</ul>
<p>RAO is chronic and needs lifelong management; it cannot be cured with short-term treatment (UF/IFAS). Do not give a bronchodilator or steroid without veterinary direction. See <a href="/qa/respiratory/preventing-cough-and-respiratory-problems/">prevention</a>.</p>''',
  src=['umnpneu','ufasra'], rel=['common-respiratory-conditions-in-horses','preventing-cough-and-respiratory-problems','signs-of-serious-respiratory-problems']),

 dict(slug='how-to-check-a-digital-pulse', ids=['VET-QA-0405'], urgent=False,
  q='How can I check my horse\'s digital pulse?',
  title='How to Check a Horse\'s Digital Pulse',
  meta='The digital artery just below the fetlock is the spot to check leg and foot pain. Learn your horse\'s normal pulse when he is well, as it is often faint.',
  short='EquiMed says the best place to gauge leg or foot pain is the digital artery just below the ankle (fetlock) joint. A healthy horse can have a very subtle pulse, so learn your horse\'s baseline by checking daily for at least a week while he is well.',
  body='''<h2>Where and when (EquiMed / Equine Guelph)</h2>
<ul>
<li>Check the digital artery just below the ankle (fetlock) joint, the recommended spot for assessing leg or foot pain.</li>
<li>Healthy horses can have a very subtle pulse, so learn your horse's baseline while he is well.</li>
<li>To set a resting average, check daily or every other day for at least one week, then average the readings.</li>
<li>Pulse can vary with exercise, temperature, stress and excitement, so check when the horse is calm.</li>
</ul>
<p>The EquiMed page gives no step-by-step finger placement; ask your veterinarian or farrier to show you. A pulse that feels stronger than usual is a reason to call; see <a href="/qa/respiratory/causes-of-a-strong-digital-pulse/">strong digital pulse</a>.</p>''',
  src=['equimedpulse'], rel=['causes-of-a-strong-digital-pulse','signs-of-serious-respiratory-problems']),

 dict(slug='causes-of-a-strong-digital-pulse', ids=['VET-QA-0424','VET-QA-0428','VET-QA-0431','VET-QA-0429'], urgent=True,
  q='What causes a strong digital pulse, what should I do, and what tests are used?',
  title='Strong Digital Pulse in Horses: Causes and Action',
  meta='A strong digital pulse can mean laminitis, a hoof bruise, abscess, a close shoeing nail or a fracture. Call your veterinarian promptly.',
  short='A stronger-than-usual pulse at the fetlock can point to laminitis, a bruise, a shoeing nail placed close to sensitive tissue, a fracture, or an abscess. Call your veterinarian promptly. The source reviewed gives no diagnostic tests or home treatment.',
  body='''<h2>Causes (EquiMed / Equine Guelph)</h2>
<ul>
<li>Laminitis.</li>
<li>A bruise.</li>
<li>A nail placed close to the sensitive tissue during shoeing.</li>
<li>A fracture.</li>
<li>Inflammation from infection, such as an abscess.</li>
</ul>
<h2>What to do</h2>
<p><strong>Call your veterinarian promptly.</strong> The source reviewed does not say what to do after finding a strong pulse, when to call, or which tests a vet would use. Treat it as a reason for a veterinary exam rather than something to manage at home. See <a href="/qa/lameness/signs-of-laminitis-and-founder/">signs of laminitis</a>, <a href="/qa/lameness/hoof-abscess-signs-and-treatment/">hoof abscess</a> and <a href="/qa/lameness/when-to-call-the-vet-for-hoof-problems/">when to call the vet for hoof problems</a>.</p>''',
  src=['equimedpulse'], rel=['how-to-check-a-digital-pulse','signs-of-serious-respiratory-problems']),
]
