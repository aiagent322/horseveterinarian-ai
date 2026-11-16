# -*- coding: utf-8 -*-
"""Infectious disease, biosecurity and fever Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'aaepehv': ('AAEP Infectious Disease Guidelines — Equine Herpesvirus (EHV-1 & EHV-4), 2025', 'https://aaep.org/wp-content/uploads/2021/02/Equine-Herpesvirus-EHV-1-and-EHV-4-Guidelines-final.pdf'),
 'uazehv': ('University of Arizona Extension — Equine Herpesvirus 1 (EHV-1), az2176', 'https://extension.arizona.edu/publication/equine-herpesvirus-1-ehv-1'),
 'mtstr': ('Montana State University Extension — Strangles: Streptococcus equi subsp. equi infection in horses', 'https://animalrangeextension.montana.edu/equine/strangles_document.html'),
 'aaepstr': ('AAEP — Streptococcus equi Infectious Disease Guidelines', 'https://aaep.org/resource/streptococcus-equi-infectious-disease-guidelines/'),
 'ucdwnv': ('UC Davis Center for Equine Health — West Nile Virus', 'https://ceh.vetmed.ucdavis.edu/health-topics/west-nile-virus'),
 'aaepeiv': ('AAEP Infectious Disease Guidelines — Equine Influenza Virus (EIV), 2025', 'https://aaep.org/wp-content/uploads/2021/02/Equine-Influenza-Virus-Guidelines-Final.pdf'),
 'oreiv': ('Oregon Department of Agriculture — Equine Influenza for Veterinarians', 'https://www.oregon.gov/oda/animal-health-feeds-livestock-id/animal-diseases/equine-influenza/Pages/Equine-Influenza-for-Veterinarians.aspx'),
 'extflu': ('eXtension Horses — Equine Influenza', 'https://horses.extension.org/disease-equine-influenza/'),
 'ukyhealth': ('University of Kentucky Extension — Evaluating the Health of Your Horse', 'https://afs.ca.uky.edu/content/evaluating-health-your-horse'),
 'equusfever': ('EQUUS — What to do when your horse has a fever', 'https://equusmagazine.com/diseases/what-fever-means-26391'),
})
HELD = {'VET-QA-0220':'generic "signs to watch" with no condition named'}
PAGES = [
 dict(slug='signs-and-complications-of-strangles', ids=['VET-QA-0193','VET-QA-0217','VET-QA-0221','VET-QA-0232'], urgent=False,
  q='What are the signs and complications of strangles?',
  title='Signs and Complications of Strangles in Horses',
  meta='Strangles starts with fever, then nasal discharge and swollen jaw and throat lymph nodes. Complications include airway blockage and purpura hemorrhagica.',
  short='Fever is the first sign, followed by nasal discharge, depression and swollen lymph nodes in the jaw and throat. Complications include abscesses elsewhere in the body, airway compression and purpura hemorrhagica. Call your vet and isolate a horse with these signs.',
  body='''<h2>Signs (Montana State Extension)</h2>
<ul>
<li>Fever is the first sign, appearing 3 to 14 days after infection.</li>
<li>Fever is usually followed by nasal discharge, depression and swollen lymph nodes in the jaw and throat.</li>
<li>Enlarged nodes can make swallowing difficult and cause respiratory noise, coughing and an extended head-and-neck posture.</li>
<li>Older horses with residual immunity, and vaccinated horses, may have milder disease.</li>
</ul>
<h2>Complications</h2>
<ul>
<li><strong>Metastatic abscesses</strong> ("bastard strangles"): infection spreads to lymph nodes elsewhere, especially the abdomen.</li>
<li><strong>Purpura hemorrhagica:</strong> an immune overreaction after infection or vaccination, causing bleeding and swelling mainly in the lower limbs, chest and abdomen; in severe cases the skin may die.</li>
<li><strong>Airway compression</strong> from complicated retropharyngeal abscesses; a tracheotomy may be needed in extreme cases.</li>
</ul>
<h2>What to do</h2>
<p>The AAEP says strangles commonly produces fever, swollen lymph nodes and purulent nasal discharge, and that affected horses should be isolated. Call your veterinarian for any horse with these signs, and watch for trouble breathing or swallowing, new swelling, or bleeding. See <a href="/qa/infectious/strangles-treatment-and-spread/">treatment and spread</a>.</p>''',
  src=['mtstr','aaepstr'], rel=['strangles-treatment-and-spread','preventing-and-containing-strangles','how-to-take-a-horses-temperature']),

 dict(slug='strangles-treatment-and-spread', ids=['VET-QA-0195','VET-QA-0231'], urgent=False,
  q='How is strangles treated, and can it spread to other animals or people?',
  title='Strangles Treatment and How It Spreads',
  meta='Strangles care is mainly supportive: warm compresses, draining abscesses and anti-inflammatories. It spreads by contact; human infection is rare.',
  short='Treatment is mainly supportive: warm compresses to help swollen nodes mature and drain, antiseptic flushing of ruptured abscesses, and anti-inflammatories. It spreads horse to horse by direct and indirect contact. Infection in people is rare.',
  body='''<h2>Treatment (Montana State Extension)</h2>
<ul>
<li>Mainly supportive care.</li>
<li>Warm compresses can help swollen nodes mature, drain and heal; ruptured abscesses are flushed with antiseptic for several days until drainage stops.</li>
<li>Anti-inflammatory drugs can reduce pain and fever and encourage eating and drinking.</li>
<li>Some abscesses may need surgical incision.</li>
</ul>
<p>The page does not name antibiotics or doses; whether to use them is your veterinarian's decision. Do not treat a suspected case without a vet.</p>
<h2>How it spreads</h2>
<ul>
<li>Direct contact with sick horses or subclinical shedders that show no signs.</li>
<li>Indirect spread through contaminated tack, grooming equipment, feed, water and handlers; insects can transmit it mechanically.</li>
<li>The bacteria usually survive 2 to 4 days in the environment, up to 4 weeks under ideal conditions.</li>
</ul>
<p>Montana State says infection in humans is rare and reported mainly in debilitated people, and caretakers should avoid respiratory and oral contact with exudates. Montana State says a carrier state of variable duration may develop after infection, with intermittent shedding; the page does not say how long. See <a href="/qa/infectious/preventing-and-containing-strangles/">preventing and containing strangles</a>.</p>''',
  src=['mtstr','aaepstr'], rel=['signs-and-complications-of-strangles','preventing-and-containing-strangles','how-to-take-a-horses-temperature']),

 dict(slug='preventing-and-containing-strangles', ids=['VET-QA-0201','VET-QA-0202'], urgent=False,
  q='How do I prevent strangles and stop it spreading to other horses?',
  title='Preventing and Containing Strangles',
  meta='Isolate horses with fever, nasal discharge or swollen nodes, use separate caretakers, check temperatures twice daily and disinfect equipment.',
  short='Isolate any horse with signs, use separate caretakers with protective clothing, take exposed horses\' temperatures twice daily, and clean then disinfect equipment. Vaccines exist but the AAEP says they are not recommended during outbreaks. Your vet should design the protocol.',
  body='''<h2>Containing it</h2>
<ul>
<li>Separate affected horses from unaffected animals, with separate caretakers wearing protective clothing (Montana State Extension).</li>
<li>Take the temperatures of exposed horses twice daily; isolate and test febrile horses.</li>
<li>Clean equipment with detergent to remove organic debris, then soak in a suitable disinfectant.</li>
<li>Febrile horses should be isolated and tested by a veterinarian.</li>
</ul>
<h2>Prevention</h2>
<p>The AAEP says control depends on strict biosecurity, isolation of affected horses and careful management of new arrivals, and that vaccination may help prevent disease but is not recommended during outbreaks. Montana State says intranasal and intramuscular vaccines exist, and that an experienced equine veterinarian should design protocols for individual horses, herds and facilities. The sources reviewed give no vaccine schedule or quarantine length.</p>
<p>See <a href="/qa/infectious/strangles-treatment-and-spread/">how strangles spreads</a>.</p>''',
  src=['mtstr','aaepstr'], rel=['signs-and-complications-of-strangles','strangles-treatment-and-spread','ehv-1-prevention-and-isolation']),

 dict(slug='signs-of-ehv-1-and-rhinopneumonitis', ids=['VET-QA-0218','VET-QA-0223','VET-QA-0225'], urgent=True,
  q='What are the signs of EHV-1 and rhinopneumonitis, and what are the early neurologic signs?',
  title='Signs of EHV-1 and Rhinopneumonitis in Horses',
  meta='Fever above 101.5°F, cough and nasal discharge mark respiratory EHV; a weak hind end, urine dribbling or trouble rising are neurologic. Call your vet.',
  short='The respiratory form (rhinopneumonitis) causes fever above 101.5°F, lethargy, nasal discharge and cough. The neurologic form (EHM) causes a weak or wobbly hind end, urine dribbling and trouble rising. Call your veterinarian immediately for neurologic signs.',
  body='''<h2>Respiratory form (rhinopneumonitis)</h2>
<p>The AAEP and the University of Arizona list fever above 101.5°F (often the first sign), lethargy or poor appetite, nasal discharge, cough, and lower-limb swelling. The AAEP adds swollen lymph nodes and eye inflammation; it is most often seen in weanlings and yearlings, mainly in autumn and winter. EHV-1 is the main cause of abortion outbreaks.</p>
<h2>Neurologic form (EHM)</h2>
<ul>
<li>Unsteadiness, a weak hind end, dragging toes (Arizona).</li>
<li>Hind-limb incoordination, urine retention or dribbling, and inability to rise (AAEP). Arizona adds sitting like a dog, head tilt, behavior changes and seizures.</li>
<li>Neurologic signs are often, but not always, preceded by fever or respiratory signs. The AAEP guidelines do not formally define "early" EHM signs and note that many cases do not follow the classic pattern.</li>
</ul>
<p><strong>Call your veterinarian immediately if neurologic signs appear</strong> (Arizona). EHM is rare but life-threatening, and EHV-1 is reportable in many places. Isolate the horse and take temperatures; see <a href="/qa/infectious/ehv-1-prevention-and-isolation/">isolation and biosecurity</a>.</p>''',
  src=['aaepehv','uazehv'], rel=['how-ehv-1-is-diagnosed','ehv-1-treatment-and-outlook','ehv-1-prevention-and-isolation']),

 dict(slug='how-ehv-1-is-diagnosed', ids=['VET-QA-0205','VET-QA-0206'], urgent=False,
  q='How are EHV-1 and rhinopneumonitis diagnosed?',
  title='How EHV-1 and Rhinopneumonitis Are Diagnosed',
  meta='Vets diagnose EHV-1 with PCR on nasal swabs and blood. Virus isolation and paired blood tests exist. Febrile horses with negative results get retested.',
  short='Vets use PCR on a nasal or nasopharyngeal swab plus a blood sample, which is the AAEP\'s test of choice for rapid detection. Virus isolation and paired blood tests are slower. Febrile horses with negative results and no other cause should be retested.',
  body='''<h2>Tests (AAEP guidelines)</h2>
<ul>
<li><strong>qPCR</strong> on a nasal or nasopharyngeal swab, paired with an EDTA or citrated blood sample, is the test of choice for rapid outbreak detection.</li>
<li><strong>Virus isolation</strong> is the gold standard for confirming infectious virus but is slow and less sensitive.</li>
<li><strong>Paired blood tests</strong> (a fourfold or greater titer rise, 14 to 21 days apart) confirm recent infection but cannot tell EHV-1 from EHV-4 unless an ELISA is used.</li>
<li>In febrile horses with negative initial results and no other cause, retesting in 24 to 72 hours is recommended.</li>
</ul>
<p>The University of Arizona also describes PCR of nasal swabs and whole blood, and notes EHV-1 is reportable. Rhinopneumonitis is the respiratory disease caused by EHV-1 or EHV-4, so the same tests apply. Sampling is done by your veterinarian. See <a href="/qa/infectious/signs-of-ehv-1-and-rhinopneumonitis/">signs</a>.</p>''',
  src=['aaepehv','uazehv'], rel=['signs-of-ehv-1-and-rhinopneumonitis','ehv-1-treatment-and-outlook','ehv-1-prevention-and-isolation']),

 dict(slug='ehv-1-treatment-and-outlook', ids=['VET-QA-0216','VET-QA-0219','VET-QA-0234','VET-QA-0235'], urgent=False,
  q='How is EHV-1 or rhinopneumonitis treated, and what are the complications and long-term effects?',
  title='EHV-1 Treatment, Complications and Long-Term Effects',
  meta='EHV-1 care is supportive and rest. Most horses recover from the respiratory form in 1 to 2 weeks, but neurologic cases can be fatal, and infection is lifelong.',
  short='Supportive care and rest are the main treatments. Most horses recover from the respiratory form in 1 to 2 weeks. Neurologic EHM can need hospitalization, mortality is reported at 15 to 30%, and infection is lifelong with possible re-shedding under stress.',
  body='''<h2>Treatment (University of Arizona)</h2>
<ul>
<li>Supportive care and rest are the main treatments.</li>
<li>Anti-inflammatory medication controls fever, pain and inflammation; antivirals are used in some cases.</li>
<li>Severe neurologic cases may need hospitalization and intensive care.</li>
</ul>
<p>Drug choice and dose are for your veterinarian. The AAEP guidelines do not cover treatment.</p>
<h2>Complications and long-term effects</h2>
<ul>
<li>Most horses recover fully from the respiratory form in 1 to 2 weeks (Arizona).</li>
<li>Horses with EHM may take longer, neurologic signs may never fully resolve, and mortality ranges from 15 to 30% (Arizona). The AAEP says deficits may persist for weeks to months after shedding stops.</li>
<li>Infection is lifelong: recovered horses carry latent virus and may shed again when stressed, for example by travel or illness (AAEP; Arizona).</li>
<li>EHV-1 is the main cause of abortion outbreaks, and foals infected in utero are usually sick at birth (AAEP).</li>
</ul>
<p>See <a href="/qa/infectious/signs-of-ehv-1-and-rhinopneumonitis/">signs</a> and <a href="/qa/infectious/ehv-1-prevention-and-isolation/">biosecurity</a>.</p>''',
  src=['uazehv','aaepehv'], rel=['signs-of-ehv-1-and-rhinopneumonitis','how-ehv-1-is-diagnosed','ehv-1-prevention-and-isolation']),

 dict(slug='ehv-1-prevention-and-isolation', ids=['VET-QA-0192','VET-QA-0194','VET-QA-0196','VET-QA-0208','VET-QA-0228'], urgent=False,
  q='How do I prevent EHV-1 and rhinopneumonitis, how long should a horse be isolated, and can it affect other animals or people?',
  title='EHV-1 Prevention, Biosecurity and Isolation Time',
  meta='Check temperatures twice daily, isolate new arrivals 14 days, never share tack or buckets, ask your vet about vaccines. Confirmed EHM means 28 days.',
  short='Take temperatures twice daily for exposed or traveling horses, isolate new arrivals for 14 days, do not share tack or buckets, and disinfect surfaces. No vaccine is labeled for the neurologic form. Confirmed EHM means a minimum 28-day premises quarantine.',
  body='''<h2>Biosecurity (University of Arizona)</h2>
<ul>
<li>Take temperatures twice daily for exposed horses and those returning from travel; isolate new arrivals and returning horses for 14 days.</li>
<li>Do not share tack, buckets, rags or grooming tools; disinfect stalls, gates and doorknobs; limit visitors and horse-to-horse contact.</li>
<li>Care for healthy horses before sick ones, and change clothes or disinfect after handling sick animals.</li>
<li>Haul only healthy horses with no fever, bring your own buckets and avoid communal troughs.</li>
</ul>
<h2>Isolation time</h2>
<p>The AAEP says recovering horses typically shed for 7 to 10 days, sometimes longer, and exposed horses may need 14 to 28 days of isolation or movement restriction. Confirmed EHM means immediate isolation and quarantine of the premises for at least 28 days, with temperatures checked at least twice daily; the countdown restarts with any new fever, abortion or neurologic case. Arizona says horses with signs should be treated as contagious until cleared by a vet.</p>
<h2>Vaccination</h2>
<p>A vaccine helps prevent the respiratory form and can reduce shedding; none is labeled for the neurologic form. The AAEP recommends boosters every six months for horses that travel or move frequently (via Arizona). The AAEP found no controlled research that vaccinating during an EHM outbreak reduces transmission.</p>
<h2>Other animals and people</h2>
<p>The AAEP says there is no known zoonotic potential for EHV, but mules and donkeys can silently shed EHV-1. People can carry the virus between horses on hands, clothing and equipment (Arizona).</p>''',
  src=['uazehv','aaepehv'], rel=['signs-of-ehv-1-and-rhinopneumonitis','ehv-1-treatment-and-outlook','preventing-and-containing-strangles']),

 dict(slug='signs-and-complications-of-equine-influenza', ids=['VET-QA-0215','VET-QA-0224'], urgent=False,
  q='What are the symptoms and complications of equine influenza?',
  title='Equine Influenza: Symptoms and Complications',
  meta='Equine flu causes fever up to 106°F, a dry harsh cough, lethargy and poor appetite. Secondary bacterial infection can progress to pleuropneumonia.',
  short='Signs include fever up to about 106°F, a dry harsh cough, tiredness, reduced appetite, muscle aches and nasal discharge. Damage to the airway can allow secondary bacterial infection, which if untreated may progress to life-threatening pleuropneumonia.',
  body='''<h2>Symptoms (AAEP)</h2>
<ul>
<li>Fever, up to about 106°F (41.1°C), with tiredness, reduced appetite and muscle aches or weakness.</li>
<li>A dry, harsh cough, often before the fever; some horses never cough.</li>
<li>Mildly swollen throat and jaw lymph nodes; nasal discharge that starts thin and may turn thick and discolored with secondary infection.</li>
<li>Rarely, lower-leg swelling or heart muscle problems.</li>
<li>Signs usually start about 24 hours after exposure, up to 3 days. Horses aged 1 to 5 are most often and most severely affected.</li>
</ul>
<h2>Complications</h2>
<p>Damage to the airway's cleaning mechanism makes secondary bacterial infection common, and untreated cases can progress to life-threatening pleuropneumonia (AAEP). The cough can persist up to 6 weeks after other signs resolve. Call your veterinarian for a horse with fever and cough, and isolate it. See <a href="/qa/infectious/equine-influenza-treatment-and-recovery/">treatment and recovery</a>.</p>''',
  src=['aaepeiv'], rel=['equine-influenza-treatment-and-recovery','preventing-equine-influenza','fever-causes-and-signs']),

 dict(slug='equine-influenza-treatment-and-recovery', ids=['VET-QA-0207','VET-QA-0222','VET-QA-0236'], urgent=False,
  q='How is equine influenza treated, and how long does recovery take?',
  title='Equine Influenza Treatment and Recovery Time',
  meta='Treatment is rest and supportive care. eXtension suggests a week of rest per day of fever, minimum three weeks. The cough can last up to 6 weeks.',
  short='Treatment is rest and supportive care. eXtension advises one week of rest for every day of fever with a three-week minimum. The cough can persist up to 6 weeks and full athletic ability can take up to 6 months to return.',
  body='''<h2>Treatment</h2>
<ul>
<li>Rest and supportive care (Oregon Department of Agriculture).</li>
<li>Whether antibiotics are needed for a secondary bacterial infection is your veterinarian's decision; the AAEP warns that untreated secondary infection can progress to pleuropneumonia.</li>
</ul>
<h2>Recovery time</h2>
<ul>
<li>eXtension: rest one week for every day of fever, with a minimum of three weeks, and restrict strenuous activity.</li>
<li>AAEP: the cough can persist up to 6 weeks after other signs resolve, and full athletic ability may take up to 6 months to return.</li>
</ul>
<h2>Is my horse recovering well?</h2>
<p>The sources reviewed do not list recovery markers. A veterinarian should confirm that the fever has resolved and the horse is eating normally before work resumes, and a new fever, thick nasal discharge or worsening cough should be reported. See <a href="/qa/infectious/how-to-take-a-horses-temperature/">taking a temperature</a>.</p>''',
  src=['extflu','oreiv','aaepeiv'], rel=['signs-and-complications-of-equine-influenza','preventing-equine-influenza','how-to-take-a-horses-temperature']),

 dict(slug='preventing-equine-influenza', ids=['VET-QA-0198','VET-QA-0209'], urgent=False,
  q='How do I prevent equine influenza, and how long should a sick horse be isolated?',
  title='Preventing Equine Influenza and Isolation Time',
  meta='Annual vaccination, isolation of affected horses for 14 days, and 14 days of isolation for horses back from shows help prevent equine flu, says the AAEP.',
  short='The AAEP recommends annual vaccination, with more frequent boosters for young or higher-risk horses. Isolate affected and exposed horses for 14 days, and isolate horses returning from shows or trail rides for at least 14 days with daily temperature checks.',
  body='''<h2>Vaccination (AAEP)</h2>
<ul>
<li>Annual vaccination is the current recommendation; young and higher-risk horses may need it more often.</li>
<li>Vaccinated horses can still become infected and shed virus.</li>
<li>Vaccinating during an outbreak is unlikely to help unless given at least 10 days before exposure.</li>
</ul>
<h2>Isolation</h2>
<ul>
<li>Keep affected and exposed horses apart from susceptible horses for 14 days, ideally in a separate air space, and continue measures for 14 days after the last suspected case resolves.</li>
<li>Isolate horses returning from shows, exhibitions or trail rides for at least 14 days, with temperatures checked at least once daily.</li>
<li>Isolate any horse with respiratory signs immediately until a diagnosis is confirmed.</li>
</ul>
<p>The AAEP says the virus survives on surfaces up to 2 days, in aerosols for several hours and on hands for a few minutes. See <a href="/qa/infectious/signs-and-complications-of-equine-influenza/">symptoms</a>.</p>''',
  src=['aaepeiv'], rel=['signs-and-complications-of-equine-influenza','equine-influenza-treatment-and-recovery','ehv-1-prevention-and-isolation']),

 dict(slug='signs-of-west-nile-virus', ids=['VET-QA-0226'], urgent=True,
  q='What are the symptoms of West Nile virus in horses?',
  title='West Nile Virus Symptoms in Horses',
  meta='West Nile can cause fever, stumbling, weakness, muscle twitching, seizures and head drooping, but many infected horses show no signs. Call your vet right away.',
  short='Signs range from mild flu-like illness to fatal brain inflammation: fever, poor coordination, stumbling, weakness, muscle twitching, seizures, facial drooping, teeth grinding and sensitivity to touch or noise. Many infected horses show no symptoms. Call your veterinarian right away.',
  body='''<h2>Signs (UC Davis)</h2>
<ul>
<li>Fever, poor coordination, stumbling and weakness</li>
<li>Muscle twitching and seizures</li>
<li>Facial and head drooping, teeth grinding</li>
<li>Unusual sensitivity to touch or noise</li>
<li>Severe cases may be unable to stand</li>
</ul>
<p>Infection can range from mild, flu-like illness to fatal brain inflammation, and many infected horses show no symptoms. Because other conditions can look similar, a veterinarian should examine any horse with neurologic signs. Horses and people cannot pass it to each other; it spreads only by mosquito bites. See <a href="/qa/infectious/west-nile-virus-treatment-and-prognosis/">treatment and prognosis</a>.</p>''',
  src=['ucdwnv'], rel=['west-nile-virus-treatment-and-prognosis','preventing-west-nile-virus','signs-of-ehv-1-and-rhinopneumonitis']),

 dict(slug='west-nile-virus-treatment-and-prognosis', ids=['VET-QA-0227','VET-QA-0230'], urgent=False,
  q='How is West Nile virus treated, and what is the prognosis?',
  title='West Nile Virus Treatment and Prognosis in Horses',
  meta='There is no specific cure for West Nile; care is supportive. Many horses recover fully, but UC Davis puts the case fatality rate at about 33%.',
  short='No specific cure exists; care is supportive and may include anti-inflammatory drugs and IV fluids. Many horses recover fully, though some keep gait or behavior problems. UC Davis puts the case fatality rate at about 33%, with worse outcomes in older horses and those that cannot rise.',
  body='''<h2>Treatment (UC Davis)</h2>
<p>There is no specific cure. Care is supportive and may include anti-inflammatory drugs and IV fluids, decided by your veterinarian. Diagnosis uses the IgM capture ELISA, which can detect infection from six days up to two months after exposure.</p>
<h2>Prognosis</h2>
<ul>
<li>Many horses recover fully; some keep gait or behavior problems.</li>
<li>Outcomes are worse for severely affected horses, older horses and horses that cannot rise.</li>
<li>The case fatality rate is about 33%.</li>
</ul>
<p>See <a href="/qa/infectious/signs-of-west-nile-virus/">symptoms</a> and <a href="/qa/infectious/preventing-west-nile-virus/">prevention</a>.</p>''',
  src=['ucdwnv'], rel=['signs-of-west-nile-virus','preventing-west-nile-virus','signs-of-ehv-1-and-rhinopneumonitis']),

 dict(slug='preventing-west-nile-virus', ids=['VET-QA-0199','VET-QA-0203','VET-QA-0204'], urgent=False,
  q='How can I prevent West Nile virus, and how effective is the vaccine?',
  title='Preventing West Nile Virus in Horses',
  meta='The AAEP recommends an annual West Nile vaccine as a core vaccine, plus mosquito control: remove standing water, use repellents, stable at dawn and dusk.',
  short='The AAEP recommends an annual West Nile vaccine as a core vaccine, plus mosquito control: remove standing water, clean water containers, use repellents and bring horses in at dawn and dusk. The sources reviewed give no vaccine efficacy figures.',
  body='''<h2>Vaccination</h2>
<p>UC Davis says the AAEP recommends an annual West Nile vaccine as a core vaccine. UC Davis gives no efficacy data, and the sources reviewed give no effectiveness percentage; ask your veterinarian about timing and boosters for your area.</p>
<h2>Mosquito control (UC Davis)</h2>
<ul>
<li>Remove standing water and clean water containers.</li>
<li>Stock water troughs with fish that eat mosquito larvae.</li>
<li>Use repellents, and bring horses indoors at dawn and dusk, when mosquitoes feed most.</li>
</ul>
<p>The virus is found in all 48 contiguous states and spreads only through mosquito bites (UC Davis). See <a href="/qa/infectious/signs-of-west-nile-virus/">symptoms</a>.</p>''',
  src=['ucdwnv'], rel=['signs-of-west-nile-virus','west-nile-virus-treatment-and-prognosis','ehv-1-prevention-and-isolation']),

 dict(slug='how-to-take-a-horses-temperature', ids=['VET-QA-0197','VET-QA-0210'], urgent=False,
  q='How do I take and monitor my horse\'s temperature safely?',
  title='How to Take and Monitor a Horse\'s Temperature',
  meta='Lubricate a clean thermometer, insert it into the rectum and hold it until the reading finishes. Normal is 99.5 to 101.5°F. Learn your horse\'s own baseline.',
  short='Approach quietly, lubricate a clean thermometer, insert it into the rectum and hold it until the reading finishes. Kentucky Extension gives a normal adult range of 99.5 to 101.5°F. Learn your horse\'s baseline and log readings if you suspect illness.',
  body='''<h2>Taking it safely (University of Kentucky Extension)</h2>
<ul>
<li>Approach quietly and let the horse know you will be at its rear end.</li>
<li>Do not attempt it if the horse will not accept its tail and rear being touched; work on desensitizing first, with an experienced handler on the same side.</li>
<li>Lubricate a clean thermometer with petroleum jelly or mineral oil, insert it into the rectum and hold it in place until the reading finishes. Digital and mercury thermometers both work.</li>
</ul>
<h2>Monitoring</h2>
<ul>
<li>Normal adult temperature is 99.5 to 101.5°F; younger horses usually run at the higher end (Kentucky). EQUUS says normal ranges about 98 to 101°F and owners should learn their horse's own baseline.</li>
<li>Normal swings occur in the evening, on hot days and after exercise (EQUUS), so recheck before assuming fever.</li>
<li>After recovery from a fever, EQUUS suggests checking daily for another week or two, since fevers can return.</li>
<li>For exposed or traveling horses, sources above recommend twice-daily readings.</li>
</ul>
<p>See <a href="/qa/infectious/fever-causes-and-signs/">fever causes and signs</a>.</p>''',
  src=['ukyhealth','equusfever'], rel=['fever-causes-and-signs','fever-treatment-and-when-to-call-the-vet','signs-of-dehydration-in-horses']),

 dict(slug='fever-causes-and-signs', ids=['VET-QA-0211','VET-QA-0212','VET-QA-0229'], urgent=False,
  q='What causes fever in horses, and what are the signs?',
  title='Causes and Signs of Fever in Horses',
  meta='Fever is the immune response to infection such as strangles, flu or Potomac horse fever. Signs include dullness, poor appetite, shivering and faster breathing.',
  short='A true fever is the immune system\'s response, most often to infection. Causes named include strangles, influenza and other viruses, pneumonia, Potomac horse fever, anaplasmosis and endotoxemia. Signs are dullness, poor appetite and, with high fever, shivering, sweating and faster breathing.',
  body='''<h2>Causes (EQUUS; University of Kentucky)</h2>
<ul>
<li><strong>Infection</strong> is the main cause. EQUUS links disease-specific clues to strangles (swollen nodes, thick nasal discharge), virus or pneumonia (cough), Potomac horse fever (diarrhea, laminitis) and anaplasmosis (mild leg swelling).</li>
<li><strong>Endotoxemia</strong> can cause high fever and is linked to colitis and inflamed lungs or uterus.</li>
<li>A slight fever can follow vaccination.</li>
<li>Kentucky lists pain, dehydration, blood loss, pneumonia and colic among causes of elevated temperature.</li>
</ul>
<h2>Not fever</h2>
<p>Exercise, heat and humidity, or inability to sweat cause hyperthermia, not fever; rest, water and cool hosing usually bring it down within about half an hour (EQUUS).</p>
<h2>Signs</h2>
<p>Mild fever: the horse seems dull and may eat less. High fever: chills or shivering, sweating, faster breathing and pulse, and reddened gums (EQUUS). Kentucky adds that fevered horses may stop drinking. The cause cannot be identified at home; see <a href="/qa/infectious/fever-treatment-and-when-to-call-the-vet/">when to call the vet</a>.</p>''',
  src=['equusfever','ukyhealth'], rel=['fever-treatment-and-when-to-call-the-vet','how-to-take-a-horses-temperature','signs-and-complications-of-strangles']),

 dict(slug='fever-treatment-and-when-to-call-the-vet', ids=['VET-QA-0213','VET-QA-0237'], urgent=True,
  q='How is fever treated, when should I call the vet, and what are the complications?',
  title='Horse Fever: Treatment, Complications and When to Call',
  meta='Call your vet for a high fever, one that lasts several days or comes with other illness signs. Never give medication beyond what your vet prescribes.',
  short='EQUUS says to call your veterinarian for a high fever, a fever that does not respond to cold hosing, or one that lasts several days or comes with other signs of illness. Fans and cold hosing can help cool the horse. Never exceed prescribed medication doses.',
  body='''<h2>When to call the vet (EQUUS; Kentucky)</h2>
<ul>
<li>A high fever, defined by EQUUS as 3 or more degrees above normal, or one that does not respond to cold hosing.</li>
<li>A fever that persists several days or comes with other signs of illness.</li>
<li>An elevated or unusually low temperature with other signs of illness (Kentucky).</li>
<li>A fever of 105°F or higher prompts consideration of serious causes such as strangles, anaplasmosis, Potomac horse fever and some viruses (EQUUS).</li>
</ul>
<h2>Treatment</h2>
<p>A mild fever 2 to 3 degrees above normal, lasting a day or two, usually does no harm; rest and recheck periodically (EQUUS). Vets often treat fever mainly when the horse is miserable and not eating or drinking. Fans, cold hosing and cool IV fluids can help cool the horse. EQUUS warns that medication overdoses are toxic, that it is riskier when a horse is not eating or drinking, and that doses must come from your vet. Cause-specific treatment depends on the diagnosis.</p>
<h2>Complications</h2>
<p>Very high or prolonged fever can increase calorie and water use, leading to weight loss and dehydration; the main practical risk is that a miserable horse stops eating and drinking (EQUUS). Fever above 106°F or any prolonged fever can cause physiological harm. See <a href="/emergency/fever/">our fever emergency guide</a>.</p>''',
  src=['equusfever','ukyhealth'], rel=['fever-causes-and-signs','how-to-take-a-horses-temperature','signs-of-dehydration-in-horses']),

 dict(slug='signs-of-dehydration-in-horses', ids=['VET-QA-0214'], urgent=False,
  q='What are the signs of dehydration in horses?',
  title='Signs of Dehydration in Horses',
  meta='Dry gums, a capillary refill time over 2 seconds and a weak, fluttery pulse can point to dehydration. Call your vet if your horse stops drinking or seems ill.',
  short='Dry mucous membranes, a capillary refill time longer than 2 seconds and a weak, fluttery pulse can indicate dehydration. Healthy gums are pink, moist and shiny. Call your veterinarian if the horse has other signs of illness or stops drinking.',
  body='''<h2>Checks (University of Kentucky Extension)</h2>
<ul>
<li><strong>Gums:</strong> dry mucous membranes may indicate dehydration; healthy gums are pink, moist and shiny.</li>
<li><strong>Capillary refill time:</strong> press a thumb on the gum for 2 seconds, release and time how long the color takes to return. Normal is 2 seconds or less; longer can reflect dehydration, infection, fever or blood loss.</li>
<li><strong>Pulse:</strong> in dehydration or blood loss it may feel weak and fluttery.</li>
</ul>
<p>Fevered horses may stop drinking (Kentucky), and prolonged fever can lead to dehydration (EQUUS). The Kentucky page does not cover the skin pinch test. Call your veterinarian for a horse that is not drinking, has diarrhea, or has other signs of illness; see <a href="/qa/infectious/fever-treatment-and-when-to-call-the-vet/">when to call the vet</a> and <a href="/qa/gi/how-to-increase-a-horses-water-intake/">water intake</a>.</p>''',
  src=['ukyhealth','equusfever'], rel=['fever-treatment-and-when-to-call-the-vet','how-to-take-a-horses-temperature','fever-causes-and-signs']),
]
