# -*- coding: utf-8 -*-
"""Neurologic and behavior Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'horseneuro': ('The Horse — Is My Horse Neurologic or Lame?', 'https://thehorse.com/148747/is-my-horse-neurologic-or-lame/'),
 'hineuro': ('Horse Illustrated — Neurological Disorders in Horses', 'https://www.horseillustrated.com/horse-health-neurological-disorders-in-horses/'),
 'uflcallvet': ('University of Florida Large Animal Hospital — When It\'s Time to Call the Vet', 'https://largeanimal.vethospitals.ufl.edu/2025/09/10/when-its-time-to-call-the-vet/'),
 'horserehab': ('The Horse — Rehabilitating the Neurologic Horse', 'https://thehorse.com/1121885/rehabilitating-the-neurologic-horse/'),
 'horseanxious': ('The Horse — Managing the Anxious Horse', 'https://thehorse.com/16954/managing-the-anxious-horse/'),
 'equusnervous': ('EQUUS — How to help a nervous horse', 'https://equusmagazine.com/horse-care/help-nervous-horse'),
 'horsetransport': ('The Horse (UC Davis Center for Equine Health) — How to Reduce Transport Stress in Horses', 'https://thehorse.com/?p=16692'),
})
HELD = {}
PAGES = [
 dict(slug='neurologic-signs-stumbling-and-worsening', ids=['VET-QA-0374','VET-QA-0373','VET-QA-0375'], urgent=True,
  q='What are common signs of neurologic problems in horses, why do they stumble, and what if the condition worsens?',
  title='Horse Neurologic Signs, Stumbling and Worsening',
  meta='Stumbling, toe dragging, weakness, falling or head tilt can signal a neurologic problem. Call your vet promptly, and again right away if signs worsen.',
  short='Incoordination, stumbling, toe dragging, weakness, an abnormal stance, falling, head tilt or sudden behavior change can signal a neurologic problem. Stumbling alone does not identify the cause, since lameness can cause it too. Call your veterinarian promptly, and right away if signs worsen or the horse cannot rise.',
  body='''<h2>Signs owners may notice</h2>
<ul>
<li>Incoordination (ataxia), weakness, knuckling, stumbling or dragging a toe (The Horse).</li>
<li>An abnormal stance, poor balance, difficulty placing the feet, or trouble sensing where the limbs are (The Horse).</li>
<li>Paralysis, muscle twitching or spasms, falling, trouble lying down or getting up, or rapid severe muscle wasting (The Horse).</li>
<li>Behavior changes, head tilt, or drooping eyes, ears or lips (The Horse). Horse Illustrated adds trouble chewing, swallowing or seeing, and unusual posture of the head, neck or tail.</li>
</ul>
<h2>Why horses stumble</h2>
<p>Stumbling and toe dragging occur with both lameness and neurologic disease, so they do not by themselves identify the cause; spontaneous stumbling, tripping and falling point to more severe neurologic deficits (The Horse). Some lameness looks neurologic and some neurologic problems look like lameness, so a veterinarian has to determine the cause (Horse Illustrated). A horse can have both. The sources reviewed give no stumbling prevention steps beyond finding the cause with your vet.</p>
<h2>Call your veterinarian</h2>
<ul>
<li>Call for an unsteady walk or frequent stumbling, seizures, collapse, or a horse that cannot get up or cannot move (University of Florida).</li>
<li>Call whenever you are concerned, if the problem worsens or does not improve quickly, or if there is no obvious cause; some neurologic conditions progress fast and early treatment gives the best chance of recovery (The Horse).</li>
<li>A horse with a neurologic problem can hurt people, itself and other horses (Horse Illustrated). Neurologic horses can also injure themselves and develop secondary musculoskeletal problems (The Horse).</li>
</ul>
<h2>If signs worsen</h2>
<p>The sources reviewed give one instruction: contact a veterinarian promptly. They give no home steps for a worsening or down horse, so none are listed here. The vet may check limb placement, strength, coordination, cranial nerves and gait, and may add imaging, spinal fluid or blood tests (The Horse; Horse Illustrated). See <a href="/conditions/epm/">EPM</a> and <a href="/qa/neurologic/rehabilitation-exercises-for-neurologic-horses/">rehabilitation exercises</a>.</p>''',
  src=['horseneuro','hineuro','uflcallvet'], rel=['rehabilitation-exercises-for-neurologic-horses','anxiety-signs-and-diagnosis']),

 dict(slug='rehabilitation-exercises-for-neurologic-horses', ids=['VET-QA-0378'], urgent=True,
  q='Are there specific exercises that can help neurologic problems in my horse?',
  title='Rehab Exercises for Neurologic Horses',
  meta='Rehab for a neurologic horse starts after a veterinary workup and aims to build proprioception and strength. Exercises must be directed by your vet.',
  short='Rehabilitation can help some neurologic horses, but only after a full veterinary workup and treatment of the underlying cause. The aims are better limb awareness (proprioception), neuromuscular control and strength. Exercises are directed by your veterinarian; balance work tires horses quickly and should progress slowly.',
  body='''<h2>Veterinary workup first</h2>
<p>Rehab follows treatment of the primary cause of the neurologic signs (The Horse). Call your veterinarian before trying any exercise on a wobbly horse. See <a href="/qa/neurologic/neurologic-signs-stumbling-and-worsening/">neurologic signs</a>.</p>
<h2>Goals</h2>
<p>Rehab aims to stimulate proprioception, restore neuromotor control and build strength; recovery can take months or even years depending on the underlying disease (The Horse).</p>
<h2>Exercise types described</h2>
<ul>
<li>Basic physiotherapy: wither and tail pulls, lifting the limbs, core work and weight shifting.</li>
<li>Balance pads, added cautiously once the horse is steady on flat ground and able to lift all four feet; begin under only the front or hind feet before moving to softer pads or all four.</li>
<li>Serpentines across different surfaces, once the horse walks a straight line steadily.</li>
<li>Elastic therapeutic taping over the hindquarters and low-level electrical muscle stimulation, used by professionals.</li>
</ul>
<h2>Cautions and outlook</h2>
<p>Horses can tire quickly during balance work; difficulty should increase slowly based on the individual horse and your vet's recommendations. Recovery is often slow; many horses become sound enough to be at pasture and some can be ridden again in some capacity (The Horse). The source gives no schedules, repetitions or durations, and none are listed here.</p>''',
  src=['horserehab'], rel=['neurologic-signs-stumbling-and-worsening','anxiety-signs-and-diagnosis']),

 dict(slug='anxiety-signs-and-diagnosis', ids=['VET-QA-0241','VET-QA-0244','VET-QA-0240'], urgent=False,
  q='What are the signs of anxiety in horses and how does a vet diagnose it?',
  title='Signs of Anxiety in Horses and How Vets Check',
  meta='Spooking, spinning, pulling back, refusing to stand and bracing can signal fear or anxiety, but pain or illness often sits behind them. Start with a vet exam.',
  short='Signs of a nervous or anxious horse include spooking and spinning, refusing to stand for the farrier, pulling back at the cross ties, and bracing or sitting back. Behavior often has a physical cause, so the first step is a full veterinary exam to rule out pain, illness or ill-fitting tack.',
  body='''<h2>Signs</h2>
<ul>
<li>Spooking and spinning, refusing to stand for the farrier, pulling back at cross ties, and bracing or sitting back (EQUUS).</li>
<li>The Horse describes balking and bolting with vision loss, nervousness or reluctance with chronic pain, and worry or unsafe behavior when separated from herd mates.</li>
<li>Some behavior that looks like anxiety is an expression of a horse's instinct for self-preservation (EQUUS).</li>
</ul>
<h2>How it is worked out</h2>
<p>The sources reviewed describe a sequence rather than a single test. A full veterinary exam comes first to rule out pain, illness or ill-fitting tack (EQUUS). The Horse lists vision loss, chronic pain such as arthritis, navicular syndrome or gastric ulcers, tack fit, diet, training, rider anxiety, lack of exercise and social contact, and genetics as possible contributors; it calls for a dental and lameness check as part of the exam. If nothing physical turns up, the behavior may come from fear or a naturally sensitive temperament (EQUUS). The sources give no formal diagnostic criteria or lab test for anxiety.</p>
<p>Sudden behavior change with stumbling, weakness or head tilt can be neurologic rather than behavioral; see <a href="/qa/neurologic/neurologic-signs-stumbling-and-worsening/">neurologic signs</a>. See also <a href="/qa/neurologic/anxiety-causes-and-management/">causes and management</a>.</p>''',
  src=['equusnervous','horseanxious'], rel=['anxiety-causes-and-management','neurologic-signs-stumbling-and-worsening','behavior-techniques-and-common-behavior-issues']),

 dict(slug='anxiety-causes-and-management', ids=['VET-QA-0243','VET-QA-0239','VET-QA-0242'], urgent=False,
  q='How can I manage horse anxiety, change the environment and use natural remedies?',
  title='Managing Horse Anxiety: Environment and Remedies',
  meta='Rule out pain first, then add turnout, enrichment, forage and a steady routine. Evidence for calming supplements is limited; ask your vet before using any.',
  short='Rule out pain, vision, tack and diet problems with your veterinarian first. Then regular exercise, more turnout, enrichment, herd contact and continuous forage can help. Evidence for calming supplements is limited, and many calming ingredients are on competition banned-substance lists.',
  body='''<h2>Start with the vet</h2>
<p>A thorough exam comes first to rule out pain, illness or poor tack fit (EQUUS; The Horse). Ulcers are a concern in stressed horses, and some pain medications can raise ulcer risk (The Horse).</p>
<h2>Environment and management</h2>
<ul>
<li>Regular exercise, more turnout, enrichment, herd living and continuous forage can help sedentary horses with limited social contact (The Horse).</li>
<li>Schedule stressful events such as vet visits for quiet times at the barn, choose familiar safe locations, and avoid sudden changes like a blanket draped on a fence (EQUUS).</li>
<li>Regular turnout helps hotter horses burn off energy, and a loose-rein walk at the start of a ride helps them settle (EQUUS).</li>
<li>For horses insecure when separated, use gradual exposure, a consistent routine, and separate stabling for bonded horses at shows (The Horse).</li>
<li>High-starch, high-sugar diets with little exercise may contribute to restlessness; a nutritionist may suggest changes, though diet alone may not fix the behavior (The Horse).</li>
</ul>
<h2>Natural remedies and supplements</h2>
<p>Evidence for calming supplements is limited, and many purported calming ingredients appear on competition banned-substance lists; pheromone products have shown some positive research results (The Horse). The sources give no recommended products or doses, and none are listed here. Ask your veterinarian before giving any supplement. See <a href="/qa/neurologic/behavior-techniques-and-common-behavior-issues/">behavior techniques</a>.</p>''',
  src=['horseanxious','equusnervous'], rel=['anxiety-signs-and-diagnosis','behavior-techniques-and-common-behavior-issues','travel-comfort-and-stress-reduction']),

 dict(slug='behavior-techniques-and-common-behavior-issues', ids=['VET-QA-0376','VET-QA-0377'], urgent=False,
  q='Are there behavioral techniques to reduce horse anxiety, and what behavioral issues are common?',
  title='Behavior Techniques for Nervous Horses',
  meta='Approach calmly, avoid punishment, introduce new things slowly and reward good behavior. Common problems include spooking, pulling back and refusing to stand.',
  short='Useful techniques include approaching calmly, avoiding punishment, introducing new things slowly, leaving the horse room to move, and rewarding good behavior with good timing. Common problems named in the sources include spooking, pulling back at cross ties, refusing to stand for the farrier and separation worry.',
  body='''<h2>Techniques (EQUUS)</h2>
<ul>
<li>Approach calmly: move slowly, come in from the side and pause before the horse reacts.</li>
<li>Avoid punishment; scolding confirms the horse's fear.</li>
<li>Introduce trailers, bridges and odd objects at the horse's own pace, ideally well before they are needed.</li>
<li>Do not trap the horse; leave room to move and keep the feet busy by circling or walking when he tenses.</li>
<li>Reward good behavior promptly; mistimed rewards can reinforce the wrong response.</li>
<li>Watch for early signs of tension and intervene before a blowup.</li>
</ul>
<h2>Common issues named in the sources</h2>
<p>Spooking and spinning, refusing to stand for the farrier, pulling back at cross ties, and bracing or sitting back (EQUUS); balking, bolting, and unsafe behavior when separated from companions (The Horse). The Horse notes that insufficient training can leave a horse unsettled and that a professional trainer can help establish consistent aids and routine. The sources reviewed give no complete list of behavior problems. Rule out pain first; see <a href="/qa/neurologic/anxiety-signs-and-diagnosis/">signs and veterinary check</a>.</p>''',
  src=['equusnervous','horseanxious'], rel=['anxiety-signs-and-diagnosis','anxiety-causes-and-management','travel-comfort-and-stress-reduction']),

 dict(slug='travel-comfort-and-stress-reduction', ids=['VET-QA-0238'], urgent=False,
  q='How can I help my horse feel more comfortable during travel?',
  title='Reducing Horse Travel Stress',
  meta='Train for calm loading, use a safe ventilated trailer, offer water and dust-free hay, allow head movement and watch for illness after arrival.',
  short='Train the horse to load and haul calmly, use a safe, well-ventilated trailer with non-slip footing and room to lower the head, offer water and dust-free hay, make regular stops, and watch for illness afterward. Contact your veterinarian for fever, nasal discharge, colic, diarrhea or refusal to eat.',
  body='''<p>These points come from UC Davis Center for Equine Health guidance reprinted in The Horse.</p>
<h2>Before travel</h2>
<ul>
<li>Train the horse to load, unload and ride calmly; loading is one of the most stressful parts of a trip.</li>
<li>Choose a vehicle that fits the horse's size and temperament, ideally with room to lower its head, and check it for safety and cleanliness.</li>
<li>Use a non-slip floor with absorbent bedding, good ventilation, a well-fitting leather halter, and feed and water brought from home.</li>
<li>Do not ship sick horses or those exposed to contagious respiratory disease. Use sedatives only under veterinary direction because they can affect temperature regulation.</li>
</ul>
<h2>During travel</h2>
<ul>
<li>Offer water regularly (every three to six hours, more often in heat), and use dust-free hay, low-hung.</li>
<li>Allow as much head movement as is safe; many horses travel better facing backward, though individual preference varies.</li>
<li>Keep exhaust away from vents, avoid long stops in traffic, and remove soiled bedding during stops on long trips.</li>
<li>Watch for injury, depression or severe agitation, and get help if a horse becomes very agitated.</li>
</ul>
<h2>After arrival</h2>
<p>Unload promptly and let the horse walk or graze; a healthy horse should be alert, drinking and eating within one to two hours. <strong>Contact your veterinarian</strong> for nasal discharge, refusal to eat, fever, reduced manure, colic or diarrhea, since some illnesses appear two to three days after transport. See <a href="/qa/respiratory/">respiratory questions</a>.</p>''',
  src=['horsetransport'], rel=['anxiety-causes-and-management','behavior-techniques-and-common-behavior-issues']),
]
