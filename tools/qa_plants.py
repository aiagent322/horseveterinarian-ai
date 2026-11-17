# -*- coding: utf-8 -*-
"""Toxic plants Q&A (source-first; no package records). Same rules as qa_colic.py. No plant amounts or doses."""
import qa_colic as C
S = dict(C.S)
S.update({
 'usefp1': ('US Equestrian / Hagyard Equine Medical Institute — Poisonous Plants: Five to Know (G. Tranquillo, DVM; May 16, 2017)', 'https://usef.org/media/press-releases/poisonous-plants-five-to-know'),
 'usefp2': ('US Equestrian / Hagyard Equine Medical Institute — Poisonous Plants: Five to Know, Part 2 (G. Tranquillo, DVM; May 22, 2017)', 'https://usef.org/media/press-releases/poisonous-plants-five-to-know-part-2'),
 'uconnplants': ('UConn Extension — Toxic Plants and Horses: Concerns and Prevention (J. Nadeau; EXT124, June 2025)', 'https://extension.uconn.edu/publication/toxic-plants-horses'),
 'ifasplants': ('University of Florida IFAS Extension — Toxic Plants of Florida for Horse Owners, VM247 (A. Schortinghouse, B. Sellers; no date shown)', 'https://ask.ifas.ufl.edu/publication/VM247'),
 'utplants': ('University of Tennessee Institute of Agriculture — Equine Toxicity Series: Poisonous Plants to Horses, W784-A (Kiningham, Ivey, Strickland; Oct 2018)', 'https://utia.tennessee.edu/publications/wp-content/uploads/sites/269/2023/10/W784-A.pdf'),
})
HELD = {}
PAGES = [
 dict(slug='what-to-do-if-a-horse-eats-a-poisonous-plant', ids=[], urgent=True,
  q='What should I do if my horse eats a poisonous plant?',
  title='What to Do If a Horse Eats a Poisonous Plant',
  meta='Call your veterinarian right away, remove the horse from the plant or hay, and save a sample or photos of the plant. Some poisonings cause permanent damage.',
  short='Call your veterinarian right away. Remove the horse from the plant or contaminated hay, save a sample or clear photos of the whole plant, and note how much the horse may have eaten. Treatment is usually supportive care, and some poisonings cause permanent damage even when treated.',
  body='''<h2>Steps from the sources</h2>
<ul>
<li>Call your veterinarian right away (Hagyard/US Equestrian; University of Florida IFAS).</li>
<li>Save a sample of the plant for identification and note how much the horse may have eaten (Hagyard/US Equestrian).</li>
<li>If you can, collect leaves, seeds, stems and flowers, and photograph the whole plant, bush or tree (University of Florida IFAS).</li>
<li>Remove the plant promptly so no more is eaten (Hagyard/US Equestrian).</li>
</ul>
<h2>What your veterinarian may do</h2>
<p>Hagyard says treatment is often supportive care to stabilize the horse, and severe cases may be referred to a hospital for 24-hour care. The University of Florida says the veterinarian can give the most accurate prognosis and may use medication to limit how much toxin enters the bloodstream. Hagyard adds that even after treatment some poisonings leave permanent or irreversible damage.</p>
<h2>Why speed matters</h2>
<p>Hagyard describes signs from some plants within an hour or two, such as nervousness, tremors and incoordination from hemlock, and from others only after months, such as yellow star thistle. Signs from wilted red maple leaves can appear within hours or as late as four to five days. Do not wait for signs if you know the horse ate a toxic plant.</p>
<h2>What the sources do not cover</h2>
<p>The sources give no home treatments, and they do not say what to do if you cannot identify the plant. Do not try to treat the horse yourself. See <a href="/qa/toxic-plants/most-common-poisonous-plants-for-horses/">common poisonous plants</a>, <a href="/qa/toxic-plants/preventing-plant-poisoning-in-horses/">prevention</a> and the <a href="/emergency/colic-emergency/">colic emergency guide</a>.</p>''',
  src=['usefp1','usefp2','ifasplants'], rel=['most-common-poisonous-plants-for-horses','preventing-plant-poisoning-in-horses','red-maple-poisoning-in-horses']),

 dict(slug='most-common-poisonous-plants-for-horses', ids=[], urgent=True,
  q='What are the most common poisonous plants for horses, and what signs do they cause?',
  title='Common Poisonous Plants for Horses and Their Signs',
  meta='Hagyard names 10 toxic pasture plants from an AAEP list, such as bracken fern, hemlock, oleander, red maple and yew, with signs for each. Ask local extension.',
  short='A Hagyard Equine Medical Institute series, based on an AAEP list, names ten toxic pasture plants: bracken fern, hemlock, water hemlock, tansy ragwort, Johnson and Sudan grass, locoweed, oleander, red maple, yellow star thistle and yew. Each causes different signs. Your veterinarian or county extension can name the ones in your area.',
  body='''<p>The list below comes from Dr. Gina Tranquillo of Hagyard Equine Medical Institute (US Equestrian, 2017), who based it on an AAEP list. It is not complete, and plants vary by region. Horses usually avoid these plants, but hunger can drive them to eat them.</p>
<h2>Signs by plant</h2>
<ul>
<li><strong>Bracken fern:</strong> depression, incoordination and blindness; it interferes with vitamin B1 absorption.</li>
<li><strong>Hemlock:</strong> nervousness, tremors and incoordination within an hour or two, then depression, colic and slowed heart and breathing.</li>
<li><strong>Water hemlock:</strong> drooling, dilated pupils, breathing difficulty and seizures; it grows in wet, low-lying areas and can progress quickly.</li>
<li><strong>Tansy ragwort:</strong> sun-sensitive skin, yellowing of the skin or eyes, incoordination, depression and weight loss, appearing only after severe liver damage. Cut plants stay toxic, so it is a risk in hay.</li>
<li><strong>Johnson grass and Sudan grass:</strong> rapid breathing, gasping, frequent urination and defecation, brick-red gums and convulsions. Sorghum hay carries a risk of lasting bladder nerve damage.</li>
<li><strong>Locoweed:</strong> exaggerated high-stepping gait, staggering, aimless wandering and falling; abortion in pregnant mares and birth defects.</li>
<li><strong>Oleander:</strong> colic, lying down and unable to rise, irregular heart rate and labored breathing. See <a href="/qa/toxic-plants/oleander-poisoning-in-horses/">oleander</a>.</li>
<li><strong>Red maple:</strong> fast breathing and heart rate, lethargy, poor appetite and dark red or brown urine. See <a href="/qa/toxic-plants/red-maple-poisoning-in-horses/">red maple</a>.</li>
<li><strong>Yellow star thistle:</strong> a tense face, inability to bite or chew, weight loss and incoordination, developing over months of eating it.</li>
<li><strong>Yew:</strong> sudden death is the typical sign; horses found alive may tremble, have colic, slowed pulse and difficulty breathing.</li>
</ul>
<h2>Outlook and limits</h2>
<p>Hagyard says several of these have no effective treatment once nerve or liver damage is advanced, so preventing access matters most. The articles are from 2017. Signs alone cannot tell you which plant is responsible, so a horse with these signs needs a veterinarian. See <a href="/qa/toxic-plants/what-to-do-if-a-horse-eats-a-poisonous-plant/">what to do</a>.</p>''',
  src=['usefp1','usefp2'], rel=['what-to-do-if-a-horse-eats-a-poisonous-plant','red-maple-poisoning-in-horses','oleander-poisoning-in-horses']),

 dict(slug='red-maple-poisoning-in-horses', ids=[], urgent=True,
  q='Are red maple leaves poisonous to horses?',
  title='Red Maple Leaf Poisoning in Horses',
  meta='Wilted or dried red maple leaves, often after storms or in fall, can be fatal to horses. Dark red urine and fast breathing mean call your vet now.',
  short='Yes. Wilted or dried red maple leaves are toxic to horses and damage red blood cells so they carry less oxygen. Fresh leaves seem to do little harm. Signs include dark red or brown urine and fast breathing. If a horse may have eaten wilted leaves, call your veterinarian immediately.',
  body='''<h2>What makes it dangerous</h2>
<ul>
<li>The University of Tennessee says wilted or dried leaves are the main danger. Fresh and red autumn leaves are less toxic but should still be avoided.</li>
<li>Hagyard says wilted leaves are most often eaten after storms or during autumn leaf fall.</li>
<li>The toxin damages the hemoglobin in red blood cells, which reduces oxygen delivery.</li>
</ul>
<h2>Signs and timing</h2>
<ul>
<li>Weakness, depression, poor appetite, faster breathing and heart rate, yellow or brown gums and dark red or brown urine (University of Tennessee; Hagyard).</li>
<li>Signs usually appear one to two days after eating (University of Tennessee); Hagyard says they can appear within hours or as late as four to five days.</li>
</ul>
<h2>Outlook</h2>
<p>The University of Tennessee says about three-quarters of cases are fatal and describes no specific treatment. Hagyard says recovery depends on how much was eaten and how quickly veterinary care starts, and it notes silver and sugar maples may contain similar but weaker toxins. The sources differ on how much leaf is dangerous, so this page gives no amounts.</p>
<h2>Prevention</h2>
<p>The University of Tennessee advises limiting access to red maple trees, checking pastures after storms or high winds, removing fallen leaves and providing enough forage. UConn Extension adds that dried or wilted maple leaves should be removed from pastures, especially after storms. See <a href="/qa/toxic-plants/what-to-do-if-a-horse-eats-a-poisonous-plant/">what to do</a>.</p>''',
  src=['utplants','usefp2','uconnplants'], rel=['what-to-do-if-a-horse-eats-a-poisonous-plant','most-common-poisonous-plants-for-horses','preventing-plant-poisoning-in-horses']),

 dict(slug='oleander-poisoning-in-horses', ids=[], urgent=True,
  q='Is oleander poisonous to horses, and what are the signs?',
  title='Oleander Poisoning in Horses',
  meta='Oleander is toxic to horses, and dried leaves and clippings stay toxic. Colic, trouble standing or an irregular pulse need a vet at once. Keep it from pasture.',
  short='Yes. Oleander is toxic to horses, and dried leaves stay toxic. Signs include colic, lying down and being unable to rise, an irregular heart rate, labored breathing and tremors, and they can start hours after eating. Call your veterinarian immediately; the outlook is better when poisoning is caught early.',
  body='''<h2>Signs and timing</h2>
<ul>
<li>Hagyard lists colic, lying down and being unable to rise, an irregular heart rate, labored breathing, tremors or death. Symptoms can start several hours after eating and last more than 24 hours.</li>
<li>The University of Tennessee lists colic, diarrhea, labored breathing, weakness, tremors, inability to stand and an irregular or weak pulse, with death often within 24 hours of symptoms.</li>
<li>UConn Extension ranks oleander as the most toxic plant among those it names, and UConn says some ornamentals are toxic in very small amounts.</li>
</ul>
<h2>Outlook and treatment</h2>
<p>Hagyard says supportive veterinary care is essential and the outlook is better when poisoning is caught early. The University of Florida says a veterinarian may use medication to limit how much toxin enters the bloodstream. The sources give no home treatment.</p>
<h2>Where it comes from</h2>
<p>Hagyard says dried leaves stay toxic and that clippings thrown into pastures are a common cause, so pruned material should be removed and disposed of promptly.</p>
<h2>What to do</h2>
<p>Call your veterinarian immediately and save a sample or photos of the plant. Do not plant oleander in or near pastures. See <a href="/qa/toxic-plants/what-to-do-if-a-horse-eats-a-poisonous-plant/">what to do</a> and <a href="/qa/toxic-plants/preventing-plant-poisoning-in-horses/">prevention</a>.</p>''',
  src=['usefp2','utplants','uconnplants','ifasplants'], rel=['what-to-do-if-a-horse-eats-a-poisonous-plant','most-common-poisonous-plants-for-horses','preventing-plant-poisoning-in-horses']),

 dict(slug='preventing-plant-poisoning-in-horses', ids=[], urgent=False,
  q='How can I prevent my horse from eating poisonous plants?',
  title='How to Prevent Plant Poisoning in Horses',
  meta='Keep plenty of forage, scout pastures and fence lines, remove toxic plants, buy hay from reputable sources and never feed yard clippings. Ask local extension.',
  short='Extension sources agree on these steps: keep plenty of grass and hay so hunger does not drive horses to weeds, inspect pastures and fence lines, remove toxic plants, buy hay from a reputable source, avoid yard clippings and toxic ornamentals, and ask your county extension office which plants grow in your area.',
  body='''<h2>Steps listed by the sources</h2>
<ul>
<li><strong>Feed enough:</strong> horses are more likely to eat weeds when forage is scarce (University of Florida IFAS). UConn suggests free-choice hay or slow feeders for easy keepers.</li>
<li><strong>Inspect regularly:</strong> check pastures and fence lines, since wind, birds and wildlife spread seeds (University of Florida IFAS).</li>
<li><strong>Remove toxic plants:</strong> by herbicide, pulling or digging them out, or fencing the area off. Mowing alone rarely removes weeds permanently (University of Florida IFAS).</li>
<li><strong>Follow herbicide labels:</strong> waiting periods before grazing are on the label, and herbicides can make toxic plants more appealing, so keeping horses off until plants have fully dried may be safest (University of Florida IFAS).</li>
<li><strong>Control what comes in:</strong> buy hay from a reputable farmer, ask neighbors not to feed clippings, know your bedding source and avoid black walnut shavings (UConn Extension).</li>
<li><strong>Plant carefully:</strong> research new plantings and avoid toxic ornamentals, especially along pasture borders (UConn Extension; University of Florida IFAS).</li>
<li><strong>Remove wilted maple leaves</strong> after storms (UConn Extension).</li>
</ul>
<h2>Know your region</h2>
<p>Hagyard recommends advice from your veterinarian or county extension office, and the plants that matter vary by region. UConn notes most toxic plants must be eaten in large amounts before signs appear, but a few ornamentals are toxic in small amounts. These sources do not list the plants of every state. See <a href="/qa/toxic-plants/most-common-poisonous-plants-for-horses/">common poisonous plants</a>.</p>''',
  src=['ifasplants','uconnplants','usefp1'], rel=['most-common-poisonous-plants-for-horses','what-to-do-if-a-horse-eats-a-poisonous-plant','oleander-poisoning-in-horses']),
]
