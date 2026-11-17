# -*- coding: utf-8 -*-
"""Dental and oral Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'umndent': ('University of Minnesota Extension — Caring for your horse\'s teeth', 'https://extension.umn.edu/horse-health/caring-your-horses-teeth'),
 'ufdent': ('UF/IFAS Extension — Equine Dental Care (VM273)', 'https://ask.ifas.ufl.edu/publication/VM273/pdf'),
 'equuswolf': ('EQUUS — Do equine wolf teeth always need to be extracted?', 'https://equusmagazine.com/horse-care/dentistry-equus/do-equine-wolf-teeth-always-need-to-be-extracted'),
 'horsewolf': ('The Horse — Equine Wolf Teeth', 'https://thehorse.com/118149/equine-wolf-teeth/'),
 'horsesenior': ('The Horse — Senior Horse Dental Health', 'https://thehorse.com/113745/senior-horse-dental-health/'),
 'petmdteeth': ('PetMD — Horse Teeth: Anatomy, Dental Care, and Signs Something\'s Wrong (reviewed by a DVM)', 'https://www.petmd.com/horse/horse-teeth'),
 'tslndent': ('Tri-State Livestock News — Exploring the basics of equine dentistry', 'https://www.tsln.com/news/straight-from-the-horses-mouth-exploring-the-basics-of-equine-dentistry/'),
 'abdent': ('Alberta Animal Health Source — Equine dental care', 'https://albertaanimalhealthsource.ca/node/18'),
})
HELD = {
 'VET-QA-0038':'generic feeding-routine question; not dental, no dental source',
 'VET-QA-0039':'insect irritation around the head; not dental, no source reviewed',
 'VET-QA-0041':'travel stress; not dental, no source reviewed',
}
PAGES = [
 dict(slug='how-often-to-have-a-horses-teeth-checked', ids=['VET-QA-0043','VET-QA-0044','VET-QA-0046','VET-QA-0048'], urgent=False,
  q='How often should a horse\'s teeth be checked and floated?',
  title='How Often Should a Horse\'s Teeth Be Checked?',
  meta='Veterinarians recommend a dental exam at least once a year, even with no visible problems. Young and senior horses need more often; floating needs vary.',
  short='Both UF/IFAS and Minnesota Extension recommend a yearly dental exam for every horse, even with no visible problems. Young horses and seniors need more frequent checks. Floating is not needed every year by most horses; your vet decides.',
  body='''<h2>Exams</h2>
<ul>
<li>A dental exam at least once a year for every horse, even when no problems are visible, because some horses adapt to discomfort without showing it (Alberta Animal Health Source; UMN Extension).</li>
<li>UF/IFAS, citing the AAEP: exams within the first 30 days of birth, again at 3 months, and every 6 months until age 5; yearly after age 5.</li>
<li>Aging teeth: twice-yearly exams are advised for seniors (The Horse).</li>
<li>Some horses, especially those with an overbite or underbite, may need floating every year (UMN Extension). PetMD says most horses need floating once or twice a year.</li>
</ul>
<h2>How often to float</h2>
<p>Very few horses need floating every year, though a check is still advised; floating more than once a year without a specific, short-term problem is a red flag, and excessive floating can wear teeth down too soon (Tri-State Livestock News). After a tooth is removed, the opposing tooth may need reduction every six to nine months (The Horse). The sources differ, so ask your veterinarian to set the schedule for your horse. See <a href="/qa/dental/signs-of-dental-problems-in-horses/">signs of dental problems</a>.</p>''',
  src=['abdent','umndent','ufdent','horsesenior','petmdteeth','tslndent'], rel=['signs-of-dental-problems-in-horses','what-teeth-floating-is-and-how-it-helps','teeth-floating-risks-and-aftercare']),

 dict(slug='signs-of-dental-problems-in-horses', ids=['VET-QA-0032','VET-QA-0051','VET-QA-0052','VET-QA-0057','VET-QA-0061'], urgent=True,
  q='What are the signs of dental problems in horses, and which signs mean a more serious problem?',
  title='Signs of Dental Problems in Horses',
  meta='Dropping feed, slow eating, quidding, bad breath, weight loss and bit resistance can signal dental trouble. Nasal discharge or facial swelling needs a vet soon.',
  short='Signs include dropping partly chewed feed, quidding, slow or reluctant eating, bad breath, weight loss and resisting the bit. Facial or jaw swelling, one-sided nasal discharge, pus or bleeding point to something more serious: call your veterinarian. Some horses show no signs.',
  body='''<h2>Common signs</h2>
<ul>
<li>Dropping or wasting feed, quidding (wads of partly chewed hay), slow or picky eating, moving food around the mouth, reduced interest in hard treats (UF/IFAS; PetMD; The Horse).</li>
<li>Head tilting while eating, head tossing, and resisting the bit or bridle (UF/IFAS; UMN Extension).</li>
<li>Bad breath, excess drooling and long stems or whole grain in manure (UF/IFAS; Alberta Animal Health Source).</li>
<li>Weight loss or reduced intake despite adequate feed.</li>
<li>Some horses show no signs until a problem is severe (UF/IFAS).</li>
</ul>
<h2>Signs of a more serious problem: call your veterinarian</h2>
<ul>
<li>Nasal discharge from one side, or swelling below the eye or of the face or jaw, which can indicate an abscess (Tri-State Livestock News; UF/IFAS).</li>
<li>Pus near the cheek or below the jaw, or bleeding from the mouth (UMN Extension; UF/IFAS).</li>
<li>Red, inflamed gums, feed packed between teeth, or broken or missing teeth (UMN Extension).</li>
<li>Any sudden mouth pain, or excessive drooling without chewing (PetMD).</li>
</ul>
<p>Under saddle, head tossing and bit resistance can also come from ulcers or kissing spine, so a vet must confirm the cause (PetMD). See <a href="/qa/dental/when-to-call-the-vet-for-eating-problems/">when to call the vet for eating problems</a>.</p>''',
  src=['ufdent','umndent','petmdteeth','horsesenior','tslndent','abdent'], rel=['common-dental-problems-and-treatment','when-to-call-the-vet-for-eating-problems','head-tossing-and-bit-comfort-with-dental-problems']),

 dict(slug='common-dental-problems-and-treatment', ids=['VET-QA-0050','VET-QA-0062','VET-QA-0040'], urgent=False,
  q='What are common dental problems in horses, how are they treated and how can I prevent more?',
  title='Common Horse Dental Problems and Treatment',
  meta='Sharp points, hooks, ramps, wave mouth, retained caps and gum disease are common. Treatment ranges from floating to extraction; yearly exams help prevent them.',
  short='Common problems are sharp enamel points, hooks and ramps, wave mouth, retained baby-tooth caps, wolf teeth, tooth loss and gum disease. Treatment ranges from routine floating to extraction or surgery by a veterinarian. Yearly exams, ample roughage and correct bit fit help prevent problems.',
  body='''<h2>Common problems</h2>
<ul>
<li>Sharp enamel points on the outer edges of upper teeth and inner edges of lower teeth, which can cause sores (Tri-State Livestock News; UF/IFAS).</li>
<li>Hooks and ramps that hinder chewing and can injure the mouth.</li>
<li>Misalignment such as overbite, underbite or wave mouth, which wear unevenly.</li>
<li>Retained baby-tooth caps, and wolf teeth that may need removal if they interfere with the bit.</li>
<li>Tooth loss, leading to food packing and gum infections or abscesses; periodontal disease can cause tooth loss if untreated.</li>
</ul>
<h2>Treatment options</h2>
<ul>
<li>Routine floating for sharp points; removal of retained caps during a sedated exam; wolf tooth extraction (PetMD).</li>
<li>Veterinarian-prescribed medication or dental surgery; softer diets for worn molars, chosen with the vet (PetMD).</li>
<li>Loose teeth in older horses may need extraction (UF/IFAS).</li>
</ul>
<h2>Prevention (UF/IFAS)</h2>
<p>Yearly professional exams, a balanced diet with ample roughage, monitoring eating, drooling, body condition and behavior, and correct bit fit. The sources give no specific medications or surgical details. See <a href="/qa/dental/how-often-to-have-a-horses-teeth-checked/">exam frequency</a>.</p>''',
  src=['tslndent','ufdent','petmdteeth'], rel=['what-teeth-floating-is-and-how-it-helps','signs-of-dental-problems-in-horses','missing-teeth-causes-and-diet-changes']),

 dict(slug='what-teeth-floating-is-and-how-it-helps', ids=['VET-QA-0042','VET-QA-0058','VET-QA-0033'], urgent=False,
  q='What is teeth floating, what is the procedure like and can all horses have it?',
  title='What Is Teeth Floating and How Does It Help?',
  meta='Floating files down sharp points, hooks and uneven surfaces so a horse can chew evenly. The horse is sedated and the mouth held open with a speculum.',
  short='Floating files down sharp enamel points, hooks and uneven surfaces so the horse can chew evenly and the cheeks and tongue are not cut. The veterinarian sedates the horse, flushes the mouth, uses a speculum and rasps or power tools. Whether a horse can be floated is a veterinary decision.',
  body='''<h2>What it does</h2>
<p>Floating rasps or files down sharp points, hooks and uneven surfaces to restore proper occlusion (UF/IFAS). Unfiled sharp points can wear away the soft tissue of the cheeks and tongue and cause ulcers (UF/IFAS; PetMD). The name comes from a masonry term for leveling bricks (Tri-State Livestock News).</p>
<h2>The procedure (UF/IFAS)</h2>
<ul>
<li>The veterinarian sedates the horse and flushes the mouth with antiseptic mouthwash to remove food.</li>
<li>A speculum holds the mouth open, and lighting and the speculum help locate sharp points.</li>
<li>Hand floats or power tools are used depending on the abnormality. A sedated float takes roughly 30 to 50 minutes (Tri-State Livestock News).</li>
</ul>
<h2>Who can float, and can every horse?</h2>
<p>Only a veterinarian can legally give the sedation; some places let non-veterinarians float under supervision (PetMD; UMN Extension). The sources reviewed do not list which horses cannot be floated; ask your veterinarian about your horse's age and health. See <a href="/qa/dental/teeth-floating-risks-and-aftercare/">risks and aftercare</a>.</p>''',
  src=['ufdent','petmdteeth','tslndent','umndent'], rel=['teeth-floating-risks-and-aftercare','how-often-to-have-a-horses-teeth-checked','common-dental-problems-and-treatment']),

 dict(slug='teeth-floating-risks-and-aftercare', ids=['VET-QA-0031','VET-QA-0054'], urgent=False,
  q='What are the risks of floating a horse\'s teeth and what aftercare is needed?',
  title='Teeth Floating Risks and Aftercare',
  meta='Risks include sedation reactions and tooth damage from improper floating or too-frequent floating. The sources reviewed give no specific aftercare steps.',
  short='Risks named by sources: improper floating can damage teeth and cause pain, over-frequent floating can wear teeth down too soon, and sedation can cause allergic reaction, collapse or excitement. The sources give no aftercare steps; ask your veterinarian.',
  body='''<h2>Risks named in the sources</h2>
<ul>
<li>Improper floating can damage teeth and cause pain and trouble eating; the Alberta Veterinary Medical Association advises against lay dentists (Alberta Animal Health Source).</li>
<li>Sedation should be given under veterinary supervision; possible complications include allergic reaction, collapse and excitement (Alberta Animal Health Source).</li>
<li>Floating more than once a year without a specific, short-term problem is a red flag, because excessive floating can wear teeth down too soon (Tri-State Livestock News).</li>
</ul>
<h2>Aftercare</h2>
<p>The sources reviewed (UF/IFAS, PetMD, Alberta Animal Health Source) do not describe aftercare or recovery steps. Ask your veterinarian for instructions for your horse, and call if your horse will not eat, drools, or has bleeding or swelling afterwards. Not floating carries risk too: unfiled sharp points can cause ulcers and abrasions (UF/IFAS). See <a href="/qa/dental/what-teeth-floating-is-and-how-it-helps/">what floating is</a>.</p>''',
  src=['abdent','tslndent','ufdent','petmdteeth'], rel=['what-teeth-floating-is-and-how-it-helps','how-often-to-have-a-horses-teeth-checked','when-to-call-the-vet-for-eating-problems']),

 dict(slug='wolf-teeth-and-bit-problems', ids=['VET-QA-0034','VET-QA-0049','VET-QA-0055','VET-QA-0053'], urgent=False,
  q='Can wolf teeth cause problems with a bit, and should a wolf tooth be removed?',
  title='Wolf Teeth and Bit Problems: Remove or Leave?',
  meta='Wolf teeth serve no chewing purpose and a bit can press on and loosen them, but not all cause trouble. Removal should be decided for the individual horse.',
  short='Wolf teeth have no chewing function, and a bit can press on and loosen them, which may explain some bitting trouble. Not every wolf tooth causes problems, so EQUUS says removal should be decided for the individual horse. Specific signs of discomfort are not described by the sources.',
  body='''<h2>What they are</h2>
<p>Wolf teeth are technically the first premolar but are vestigial in the horse and serve no real function (EQUUS). A horse can have zero to four; one or two upper teeth is most common. Canines are often mistaken for wolf teeth and are not usually extracted (EQUUS).</p>
<h2>Bit problems and leaving them in</h2>
<ul>
<li>Because of their location and underdeveloped state, a bit can press on and loosen them, which may explain some bitting trouble; size, stability and location affect whether they cause issues (EQUUS).</li>
<li>They usually pose no health risk, but can interfere with bit placement in performance horses and may cause soreness from soft tissue trauma (The Horse).</li>
</ul>
<h2>Should it be removed?</h2>
<p>Extraction is common but should not be automatic; weigh the individual horse's situation, since removal has both benefits and drawbacks (EQUUS). The Horse notes vets and horse people differ on when or whether to remove them. The sources give no specific signs of discomfort and no detailed complications of leaving them in; ask your veterinarian to examine the mouth. See <a href="/qa/dental/wolf-tooth-removal-and-recovery/">removal and recovery</a>.</p>''',
  src=['equuswolf','horsewolf'], rel=['wolf-tooth-removal-and-recovery','head-tossing-and-bit-comfort-with-dental-problems','common-dental-problems-and-treatment']),

 dict(slug='wolf-tooth-removal-and-recovery', ids=['VET-QA-0036','VET-QA-0045','VET-QA-0059','VET-QA-0060'], urgent=False,
  q='How are wolf teeth removed and what is the recovery like?',
  title='Wolf Tooth Removal: Procedure and Recovery',
  meta='Wolf teeth are removed under sedation, often with a local block; The Horse puts recovery at about one day to one week. Tetanus protection matters beforehand.',
  short='A veterinarian cleans the mouth, cuts the gum, loosens the tooth and removes it with forceps, usually under sedation and local anesthetic. The Horse puts recovery at about one day to one week depending on tooth size. The main named risk is damage to the palatine artery.',
  body='''<h2>Procedure (The Horse; EQUUS)</h2>
<ul>
<li>The mouth is cleaned and flushed, the gum around the tooth is cut with an elevator, the ligament is stretched to loosen the tooth, and it is removed with forceps.</li>
<li>Time ranges from a few minutes to about 30 minutes depending on the tooth.</li>
<li>Sedation and local anesthetic are recommended; the procedure is typically straightforward.</li>
</ul>
<h2>Recovery</h2>
<p>The Horse says recovery takes about one day to one week, depending on the horse and the size of the tooth; EQUUS describes minimal recovery time and few complications. Specific aftercare instructions are not given in either source; follow your veterinarian's.</p>
<h2>Risks and tetanus</h2>
<ul>
<li>The main risk named is damage to the palatine artery, causing significant blood loss; large, curved teeth raise the chance of complications (The Horse).</li>
<li>Tetanus bacteria can develop in mouth wounds, and tetanus is usually fatal in horses; the article advises vaccination before the procedure (The Horse). Ask your vet about your horse's status.</li>
</ul>
<p>Call your veterinarian for bleeding that does not stop, swelling or a horse that will not eat after removal. See <a href="/qa/dental/wolf-teeth-and-bit-problems/">wolf teeth and bit problems</a>.</p>''',
  src=['horsewolf','equuswolf'], rel=['wolf-teeth-and-bit-problems','teeth-floating-risks-and-aftercare','when-to-call-the-vet-for-eating-problems']),

 dict(slug='missing-teeth-causes-and-diet-changes', ids=['VET-QA-0056','VET-QA-0047','VET-QA-0030'], urgent=False,
  q='What causes missing teeth in horses, and should the diet change for missing teeth or dental problems?',
  title='Missing Teeth in Horses: Causes and Diet',
  meta='Teeth wear down and eventually run out of reserve crown; jaw shape, loose teeth and fractures also play a part. Diet changes depend on the horse; ask your vet.',
  short='Horse teeth keep erupting to offset wear until the reserve crown runs out. Jaw shape, loose teeth, fractures and infection also contribute. Softer feeds such as chopped hay, soaked cubes or pellets and senior feed may help worn molars, chosen with your veterinarian.',
  body='''<h2>Possible causes (The Horse)</h2>
<ul>
<li>Teeth keep erupting to offset wear, but the reserve crown shrinks with age until the horse "runs out of tooth".</li>
<li>Teeth change shape and angle as they move outward, which can lead to uneven wear.</li>
<li>Loose teeth, widened gaps or fractures can allow infection.</li>
<li>Jaw and mouth shape, often influenced by breeding, such as small mouths and parrot or sow mouth.</li>
</ul>
<p>In younger horses, baby teeth are lost between ages 2 and 5 (PetMD), so a "missing" tooth can be normal tooth change. The sources reviewed list no other specific causes.</p>
<h2>Diet</h2>
<ul>
<li>PetMD: softer diets for worn molars, such as chopped hay, soaked cubes or pellets and senior feeds, chosen with the vet.</li>
<li>The Horse: a lost tooth leaves the opposing tooth with nothing to wear against, so it may need trimming; long forage fibers may be harder to move through the gut. It gives no feeding plan.</li>
<li>UF/IFAS: a balanced diet with ample roughage supports natural wear and dental health.</li>
</ul>
<p>Weight loss and fluid in the manure can signal chewing trouble; a fat, shiny old horse still needs a dental check (The Horse). See <a href="/qa/dental/signs-of-dental-problems-in-horses/">signs of dental problems</a>.</p>''',
  src=['horsesenior','petmdteeth','ufdent'], rel=['signs-of-dental-problems-in-horses','common-dental-problems-and-treatment','when-to-call-the-vet-for-eating-problems']),

 dict(slug='head-tossing-and-bit-comfort-with-dental-problems', ids=['VET-QA-0035','VET-QA-0037'], urgent=False,
  q='Could dental problems cause head tossing, and how can I improve comfort when riding?',
  title='Head Tossing and Dental Problems Under Saddle',
  meta='Head tossing and bit resistance can come from dental problems, but also ulcers or kissing spine. Have your vet examine the mouth and check bit fit.',
  short='Head tossing is listed as a sign of dental discomfort, but ulcers or kissing spine can look the same, so a veterinarian must confirm the cause. Check that the bit fits correctly. The sources reviewed give no riding adjustments.',
  body='''<h2>Dental causes</h2>
<ul>
<li>Head tossing, head tilting and resistance to the bit or bridle are listed signs of dental discomfort (UF/IFAS; UMN Extension; Tri-State Livestock News).</li>
<li>Sharp points can cause sores on the tongue or inner cheek that may hurt during eating or riding (UMN Extension).</li>
<li>Wolf teeth can be pressed on by a bit (EQUUS); see <a href="/qa/dental/wolf-teeth-and-bit-problems/">wolf teeth and bit problems</a>.</li>
</ul>
<h2>Other causes</h2>
<p>Head tossing, gaping and bridling resistance can also stem from ulcers or kissing spine, so a veterinarian must confirm the cause (PetMD).</p>
<h2>Comfort</h2>
<p>UF/IFAS says the bit should fit correctly and not put unnecessary pressure on the teeth or mouth. The sources reviewed give no other riding adjustments. Have a veterinarian examine the mouth before assuming it is a training issue.</p>''',
  src=['ufdent','umndent','tslndent','petmdteeth','equuswolf'], rel=['wolf-teeth-and-bit-problems','signs-of-dental-problems-in-horses','how-often-to-have-a-horses-teeth-checked']),

 dict(slug='when-to-call-the-vet-for-eating-problems', ids=['VET-QA-0063'], urgent=True,
  q='When should I call a vet for eating problems?',
  title='When to Call the Vet for Eating Problems',
  meta='Call your vet right away for choke signs, excessive drooling without chewing or sudden mouth pain. Weight loss, quidding or facial swelling also need an exam.',
  short='Call your veterinarian right away for choke signs (feed or saliva from the nose or mouth, coughing, gagging, a throat lump), excessive drooling without chewing, or sudden mouth pain. Facial swelling, one-sided nasal discharge and weight loss also need an exam.',
  body='''<h2>Call right away (PetMD)</h2>
<ul>
<li>Choke signs: feed or saliva from the nose or mouth, coughing or gagging, difficulty swallowing, a throat lump, lethargy or colic-like symptoms.</li>
<li>Excessive drooling without chewing, which can have causes such as a foreign object, illness or toxins.</li>
<li>Any sudden mouth pain.</li>
</ul>
<h2>Call for an exam soon</h2>
<ul>
<li>Nasal discharge from one side or swelling below the eye or of the face or jaw, which can indicate an abscess (Tri-State Livestock News).</li>
<li>Weight loss, quidding, bad breath or eating more slowly (The Horse; UF/IFAS).</li>
</ul>
<p>The sources reviewed give no timeframe such as "a day of not eating"; a horse that stops eating should be treated as urgent. See the <a href="/emergency/choke/">choke emergency guide</a>, the <a href="/emergency/not-eating/">not-eating guide</a> and <a href="/qa/dental/signs-of-dental-problems-in-horses/">signs of dental problems</a>.</p>''',
  src=['petmdteeth','tslndent','horsesenior','ufdent'], rel=['signs-of-dental-problems-in-horses','missing-teeth-causes-and-diet-changes','teeth-floating-risks-and-aftercare']),
]
