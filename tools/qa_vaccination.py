# -*- coding: utf-8 -*-
"""Vaccination Q&A (source-first; no package records). Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'psuvacc': ('Penn State Extension — Vaccines for Your Horse (D. Smarsh; updated May 4, 2026)', 'https://extension.psu.edu/spring-vaccines-for-your-horse'),
 'aaepadv': ('AAEP — Vaccination Guidelines: Adverse Reactions (reviewed by AAEP Infectious Disease Committee, 2021)', 'https://aaep.org/guidelines-resources/vaccination-guidelines/adverse-reactions/'),
 'merckvacc': ('Merck Veterinary Manual — Vaccination Program for Horses (A. J. Stewart; full review Oct 2022)', 'https://www.merckvetmanual.com/management-and-nutrition/preventative-health-care-and-husbandry-of-horses/vaccination-program-for-horses'),
 'tvpvacc': ("Today's Veterinary Practice — Vaccination and Internal Parasite Control for Horses", 'https://todaysveterinarypractice.com/equine-medicine/vaccination-and-internal-parasite-control-for-horses/'),
 'hsvginj': ('Horse-Side Vet Guide — Heat, swelling or pain at injection site (D. Thal, DVM)', 'https://horsesidevetguide.com/drv/Observation/264'),
})
HELD = {}
PAGES = [
 dict(slug='which-vaccines-do-horses-need', ids=[], urgent=False,
  q='Which vaccines does my horse need, and are they needed if it never leaves the farm?',
  title='Which Vaccines Do Horses Need? Core vs Risk-Based',
  meta='The AAEP lists four core vaccines for every horse: tetanus, rabies, West Nile and EEE/WEE. Risk-based vaccines depend on travel and exposure. Ask your vet.',
  short='The AAEP calls tetanus, rabies, West Nile virus and EEE/WEE core vaccines that every horse should get each year. Risk-based vaccines such as influenza, strangles and Potomac horse fever depend on location, travel and exposure. Your veterinarian builds the plan for your horse.',
  body='''<h2>Core vaccines</h2>
<p>Penn State Extension (updated May 2026) says the American Association of Equine Practitioners (AAEP) sorts vaccines into core and risk-based groups. Core vaccines are recommended for all horses every year: rabies, tetanus, West Nile virus and EEE/WEE (eastern and western equine encephalomyelitis). Today's Veterinary Practice reports that the AAEP recommends the core vaccines regardless of age, use or geographic location, so a horse that never leaves the farm is still covered by that advice.</p>
<h2>Risk-based vaccines</h2>
<p>Penn State lists equine influenza, strangles, equine herpesvirus (rhinopneumonitis), Potomac horse fever, botulism, equine viral arteritis, anthrax, rotavirus, snake bite and leptospirosis as vaccines given depending on the horse's circumstances. Today's Veterinary Practice says they are chosen by a horse's likelihood of catching a disease and weighed against the risks and cost of vaccinating.</p>
<h2>What to do</h2>
<ul>
<li>Ask your veterinarian which vaccines and risk level apply to each disease for your horse, and whether age, breeding status or vaccination history changes the plan.</li>
<li>Penn State advises against giving every available vaccine without a risk assessment, because that can be costly and unnecessary.</li>
</ul>
<h2>What the sources do not cover</h2>
<p>These sources give no product names or costs. They do not say which risk-based vaccines are needed in a given region. Rabies is also a public-health concern, and the AAEP notes that veterinary supervision is required in most states. See <a href="/qa/vaccination/how-often-do-horses-need-vaccines/">how often horses need vaccines</a> and <a href="/conditions/strangles/">strangles</a>.</p>''',
  src=['psuvacc','tvpvacc','aaepadv'], rel=['how-often-do-horses-need-vaccines','vaccines-for-show-and-traveling-horses','vaccinating-foals-and-broodmares']),

 dict(slug='how-often-do-horses-need-vaccines', ids=[], urgent=False,
  q='How often do horses need vaccines, and when in the year should they get them?',
  title='How Often Do Horses Need Vaccines?',
  meta='Previously vaccinated adults get most vaccines yearly, some twice a year. Mosquito-borne vaccines go in before mosquito season. Your vet sets the schedule.',
  short='Penn State Extension says most vaccines for previously vaccinated adult horses are given annually or twice a year, with West Nile and EEE/WEE given before mosquito season starts. The Merck Veterinary Manual lists tetanus and rabies yearly and gives shorter intervals for some risk-based vaccines.',
  body='''<h2>General timing (Penn State Extension, 2026)</h2>
<ul>
<li>For previously vaccinated adults, most vaccines are given annually or twice a year.</li>
<li>West Nile and EEE/WEE protect against mosquito-borne disease, so they should be given before mosquito season begins in spring.</li>
<li>A yearly vaccine such as rabies may not need repeating in spring if it was given the previous fall.</li>
<li>Protection can take several weeks to develop, so plan ahead.</li>
</ul>
<h2>Booster frequency by vaccine (Merck Veterinary Manual)</h2>
<ul>
<li>Tetanus and rabies: annually.</li>
<li>Influenza: every 6 months for young performance horses and horses exposed at equine events.</li>
<li>Equine herpesvirus (EHV-1/4): every 3 to 6 months for pleasure and performance horses, depending on exposure risk.</li>
<li>Potomac horse fever: annual spring boosters in endemic areas.</li>
<li>Strangles: annually for horses in potential disease situations.</li>
<li>Botulism: where risk exists, a starting series followed by annual boosters.</li>
</ul>
<h2>Limits of these sources</h2>
<p>Penn State gives no detailed schedule. The Merck page is a professional reference that points readers to the AAEP for current US recommendations, and its exposure criteria for EHV are not concrete. A horse that is new to you, has no vaccine records or has had a past reaction needs a plan from your veterinarian. See <a href="/qa/vaccination/vaccine-reactions-in-horses/">vaccine reactions</a>.</p>''',
  src=['psuvacc','merckvacc'], rel=['which-vaccines-do-horses-need','vaccines-for-show-and-traveling-horses','vaccine-reactions-in-horses']),

 dict(slug='vaccines-for-show-and-traveling-horses', ids=[], urgent=False,
  q='Do show horses and horses that travel need extra vaccines?',
  title='Vaccines for Show and Traveling Horses',
  meta='Horses that show, travel or live at busy barns face more exposure. Sources point to influenza, strangles and EHV boosters, chosen with your vet by risk.',
  short='Horses that go to showgrounds or live at barns where horses come and go are more likely to meet contagious disease. Penn State Extension names these as risk factors for risk-based vaccines, and Merck lists influenza boosters for horses exposed at events. Your veterinarian decides which apply.',
  body='''<h2>Risk factors named (Penn State Extension)</h2>
<ul>
<li>Showing or taking the horse to public places, especially showgrounds with many horses.</li>
<li>Barns where horses regularly come and go, since a horse can pick up disease elsewhere and bring it home.</li>
<li>Travel, geographic location, breeding status and other individual factors.</li>
</ul>
<h2>Vaccines the Merck Veterinary Manual ties to these risks</h2>
<ul>
<li>Influenza: recommended for horses at risk from showing, racing or shipping, with boosters every 6 months for horses exposed at equine events.</li>
<li>Strangles: for farms with past problems or horses at risk from shared water or nose-to-nose contact.</li>
<li>EHV-1/4: boosters every 3 to 6 months for pleasure and performance horses, depending on exposure.</li>
</ul>
<h2>Timing and limits</h2>
<p>Penn State notes protection can take weeks to develop, so plan well before an event. The sources do not give event-specific rules, and the AAEP says safety data on giving several vaccines at once are not available. Ask your veterinarian to match the plan to your travel schedule. See <a href="/conditions/strangles/">strangles</a> and <a href="/qa/vaccination/which-vaccines-do-horses-need/">core vs risk-based vaccines</a>.</p>''',
  src=['psuvacc','merckvacc','aaepadv'], rel=['which-vaccines-do-horses-need','how-often-do-horses-need-vaccines','vaccine-reactions-in-horses']),

 dict(slug='vaccinating-foals-and-broodmares', ids=[], urgent=False,
  q='When should foals be vaccinated, and what do broodmares need before foaling?',
  title='Vaccinating Foals and Broodmares',
  meta='Mares are vaccinated before foaling so colostrum protects the foal. Foal timing depends on vaccine status and colostrum; your vet sets the schedule.',
  short='The Merck Veterinary Manual says broodmare vaccines pass antibodies to the foal through colostrum, and those antibodies can blunt the foal\'s response to its own vaccines, so foals of vaccinated mares start later. Foals of unvaccinated mares or with poor antibody transfer start earlier. Your veterinarian sets the dates.',
  body='''<h2>Broodmares (Merck Veterinary Manual)</h2>
<ul>
<li>Rabies, and strangles on endemic farms: about 4 to 6 weeks before foaling.</li>
<li>EHV-4: about 2 to 4 weeks before foaling, to support colostral immunity.</li>
<li>EHV-1 (abortion prevention): given at set points during pregnancy.</li>
<li>Rotavirus: during later pregnancy to raise colostral antibodies.</li>
<li>The page notes the Potomac horse fever booster before foaling likely does not prevent abortion.</li>
</ul>
<h2>Foals</h2>
<ul>
<li>Antibodies from colostrum can blunt a foal's response to vaccines, so schedules are delayed for foals from vaccinated mares that absorbed enough colostrum.</li>
<li>Foals with failed antibody transfer, or from unvaccinated mares, start earlier, around 3 to 4 months for several vaccines.</li>
<li>Examples from the page: tetanus at 6, 7 and 9 months for foals of vaccinated mares versus 3, 4 and 6 months for foals of unvaccinated mares; influenza starting at 9 to 12 months for foals of vaccinated mares.</li>
</ul>
<h2>Where the source is unclear</h2>
<p>The Merck page is a professional reference. It does not give a single age for some vaccines, such as influenza for foals of unvaccinated mares, and its EHV-1/4 foal timing is ambiguous. Penn State notes only that foal and broodmare schedules differ. A foal that did not nurse well or whose mare's vaccine history is unknown should be checked by a veterinarian. See <a href="/qa/vaccination/which-vaccines-do-horses-need/">core vs risk-based vaccines</a>.</p>''',
  src=['merckvacc','psuvacc'], rel=['which-vaccines-do-horses-need','how-often-do-horses-need-vaccines','vaccine-reactions-in-horses']),

 dict(slug='vaccine-reactions-in-horses', ids=[], urgent=True,
  q='What reactions can horses have to vaccines, and when should I call the vet?',
  title='Horse Vaccine Reactions: What to Watch For',
  meta='Mild swelling, soreness, fever or dullness can follow a vaccine. Hives, colic, bleeding under the skin or collapse need a vet. Keep lot numbers.',
  short='The AAEP says some horses have temporary muscle swelling, soreness, fever, reduced appetite or lethargy after a vaccine, usually a normal immune response. Hives, bleeding under the skin, colic or anaphylaxis need veterinary care. Record the vaccine lot number and report reactions to the manufacturer.',
  body='''<h2>Expected vs serious (AAEP)</h2>
<ul>
<li>Temporary swelling or soreness at the injection site, or brief fever, reduced appetite or lethargy, are generally part of a normal immune response.</li>
<li>Severe local reactions can take a long time to treat and recover from.</li>
<li>Rarer whole-body reactions, such as hives, bleeding under the skin, colic or anaphylaxis, need veterinary care.</li>
<li>Reactions are not always predictable and are an inherent risk of vaccination. Horses with weakened immunity, pregnancy or immunosuppressive medication need a benefit-versus-risk assessment.</li>
</ul>
<h2>Swelling, heat or pain at the injection site</h2>
<p>Horse-Side Vet Guide (Dr. Doug Thal) says injection-site swelling and pain most commonly follow a vaccine reaction or improper injection technique. Tell your veterinarian, who will record the reaction and discuss alternatives.</p>
<h2>What to do</h2>
<ul>
<li>Call your veterinarian right away for hives, trouble breathing, colic, collapse, or a large, hot swelling that grows quickly.</li>
<li>Note the vaccine lot and serial numbers in your horse's records; the AAEP says they help if a reaction is investigated.</li>
<li>Report reactions to the manufacturer. They can also go to the USDA Center for Veterinary Biologics.</li>
</ul>
<h2>What the sources do not cover</h2>
<p>The AAEP page does not describe how to treat reactions or what to do before revaccinating a horse that has reacted. It refers readers to a separate AAEP guideline on testing horses with severe past reactions. See <a href="/emergency/fever/">fever emergency guide</a> and <a href="/qa/vaccination/how-often-do-horses-need-vaccines/">how often horses need vaccines</a>.</p>''',
  src=['aaepadv','hsvginj'], rel=['how-often-do-horses-need-vaccines','which-vaccines-do-horses-need','vaccines-for-show-and-traveling-horses']),
]
