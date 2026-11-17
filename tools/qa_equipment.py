# -*- coding: utf-8 -*-
"""Equipment (tack fit) Q&A. Same rules as qa_colic.py."""
import qa_colic as C
S = dict(C.S)
S.update({
 'smsaddle': ('Stable Management — How to Assess Equine Saddle Fit (2020 AAEP Convention discussion)', 'https://stablemanagement.com/?p=274'),
 'smsaddle2': ('Stable Management — How to Evaluate Saddle Fit Issues', 'https://stablemanagement.com/articles/how-to-evaluate-saddle-fit-issues/'),
})
HELD = {}
PAGES = [
 dict(slug='checking-saddle-and-tack-fit', ids=['VET-QA-0064'], urgent=False,
  q='What are the best ways to check if my tack is fitting correctly?',
  title='How to Check Saddle and Tack Fit on a Horse',
  meta='Check the saddle before and after saddling and girthing: level seat, even panel contact, gullet clearance. Recheck as the horse changes, and ask a professional.',
  short='Check the saddle before saddling, after saddling without a rider, and after girthing. Look for a level seat, even panel contact without bridging, and clearance along the spine and gullet. Recheck as the horse\'s muscle and weight change, and involve a saddle-fitting professional. Unexplained behavior can be a physical signal.',
  body='''<p>These points come from a 2020 AAEP Convention saddle-fit discussion reported by Stable Management.</p>
<h2>Before saddling</h2>
<ul><li>Check the flocking for even consistency and lumps, that the tree rails do not bulge past the panels, and that the saddle is symmetrical.</li></ul>
<h2>Saddled, no rider</h2>
<ul>
<li>The saddle's lowest point should line up with the lowest point of the horse's back, and the seat should be level with pommel and cantle balanced.</li>
<li>Slide a hand under the tree points and panels on each side to feel for pressure spots; the panels should sit evenly without bridging over any area.</li>
<li>Look for clearance along the spine and gullet.</li>
</ul>
<h2>After girthing</h2>
<ul>
<li>Repeat the checks and make sure the pad does not bunch in the gullet.</li>
<li>Saddles are often set too far forward, which can restrict shoulder movement; the source says tree points should sit well behind the shoulder blade.</li>
</ul>
<h2>Recheck and get help</h2>
<ul>
<li>A horse's back can change significantly within about two months with more work, time off, or weight change; the source advises checking young or training horses at least every three months.</li>
<li>Girthiness or abnormal behavior can point to fit, but can also come from gastric ulcers or musculoskeletal pain; check the saddle before assuming a training problem, and have a vet rule out other causes.</li>
<li>If shoulder muscles look asymmetric, a musculoskeletal problem should be evaluated before blaming the saddle.</li>
<li>Have a saddle-fitting professional help, since tree sizing standards vary, and no single saddle suits every horse.</li>
</ul>
<p>The sources give no checks for bridles, bits or cinches, and none are listed here. See <a href="/qa/gi/">gastrointestinal questions</a> for ulcer-related questions.</p>''',
  src=['smsaddle','smsaddle2'], rel=[]),
]
