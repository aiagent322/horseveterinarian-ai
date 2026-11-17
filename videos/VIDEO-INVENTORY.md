# HorseVeterinarian.ai — Video Library Inventory (Batch 001)

The CSV is the editorial inventory, **not** a list of 25 published or verified videos. Target: 25 topic slots across colic (6), hoof health (6), lameness (6), and laminitis (7).

## Status and publication gates
- `research_needed`: topic slot only; do not display a video card or fabricate a video ID.
- `source_identified`: a source/video was located; not necessarily clinically approved or currently playable.
- `source_verified`: URL/publisher/title, upload metadata, and working video confirmed at review time.
- `clinical_approved`: equine veterinary reviewer has checked the content for clinical safety and relevance.
- `published`: URL works and is embedded or linked on the live site after approval.
- `rejected`: inaccurate, unsafe, off-topic, promotional, or unavailable.

`publish_eligible` remains `no` until verified for clinical accuracy, direct URL and accessibility. Source screening alone is not a veterinary endorsement.

## Required checks before publication
1. Identify exact YouTube watch URL, publisher, original title, upload date, duration, thumbnail, and topic fit.
2. Verify that YouTube permits viewing/embedding and the URL points to the correct video.
3. Review actual content to exclude diagnosis presented as certainty, unsafe DIY interventions, dosage instructions, and claims that delay emergency veterinary care.
4. Record clinical reviewer and review date before labeling medically reviewed.
5. Deduplicate by YouTube ID, connect to a relevant existing KB topic/page, and add to cards **only when eligible**.
6. For emergency topics put contact-a-veterinarian guidance before the video.

CSV IDs are stable. Current website has one source-identified hoof abscess video; that card is not marked clinically approved. No other slots have been populated with fabricated URLs.


## Batch 002 — user-selected additions, October 27, 2026

`video-inventory-batch-002.json` records all 36 supplied links. YouTube oEmbed returned titles and publisher names for 35; these were added as externally produced educational selections, following the existing page's clinical-review-pending labeling. This metadata check does not establish clinical approval or successful playback. No videos are labeled medically reviewed.

The remaining link (`hTBsGh2k5F8`) returned HTTP 401 twice and is retained in the inventory without a public card. The new selections comprise 9 colic/surgery, 10 lameness, 2 neurological examination, and 14 dentistry videos. Two ColiCare-related selections are labeled as including program promotion. The supplied 15-second start for `ZTntWmehC4s` is retained. The page now contains 60 selections, and its filtered count is calculated from the cards.


## Batch 003 — Eye Health, October 27, 2026

All 11 user-supplied links returned titles and publisher names through YouTube oEmbed; none duplicated an existing YouTube ID. Added an Eye Health section and filter, bringing the page to 71 selections. The 184-second start for `QU1T23FpoQA` is preserved in both the embed and direct link. The Vetericyn publisher is identified as a commercial brand; UF Innovate's video is described as research. The section links to UC Davis and UF guidance about contacting a veterinarian for eye problems and consulting before applying anything to the eye. Metadata verification does not establish playback availability or clinical approval.


## Batch 004 — Tendons & Rehabilitation, October 27, 2026

The user supplied 11 links representing 10 unique videos; `629VEcIemsU` was submitted twice and appears once. All 10 unique links returned titles and publisher names through YouTube oEmbed, with no existing-library ID duplicates. Added a Tendons & Rehabilitation section and filter, bringing the page to 81 selections. The 70-second start for `_gFz8gZmXAU` is preserved in both the embed and direct link. Product presentations and owner experiences are identified in descriptions; recovery and treatment claims are not independently verified. Metadata verification does not establish playback availability or clinical approval.


## Q&A page videos — colic and digestive health, November 16, 2026

`tools/qa_videos_colic.json` (21 videos) and `tools/qa_videos_gi.json` (12 videos) record videos attached to `/qa/colic/` and `/qa/gi/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Videos from feed-company, podcast and similar publishers are flagged `commercial_note`. Candidates that failed oEmbed (`ev5-0-yZKtA`, `XD73GAHiFNw`) were dropped, not guessed.


## Q&A page videos — metabolic and endocrine, November 16, 2026

`tools/qa_videos_metabolic.json` (10 videos, 14 placements on 10 pages) records videos attached to `/qa/metabolic/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Podcast and creator channels are flagged `commercial_note`. Pharmaceutical-company and feed-product videos, and candidates older than about eight years, were not used. Pages with no topic-matched video were left blank.


## Q&A page videos — lameness, hooves and limbs, November 16, 2026

`tools/qa_videos_lameness.json` (12 videos, 16 placements on 12 pages) records videos attached to `/qa/lameness/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Supplement-company, retailer, subscription, creator and veterinarian-audience channels are flagged in `commercial_note`. Pages with no topic-matched video were left blank; videos older than about eight years and treatment demonstrations by non-veterinarians were not used.


## Q&A page videos — infectious disease and fever, November 16, 2026

`tools/qa_videos_infectious.json` (8 videos, 8 placements on 6 pages) records videos attached to `/qa/infectious/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Podcast, veterinary-practice and breed-association channels are flagged in `commercial_note`. Pages with no topic-matched video were left blank; videos older than about eight years and news clips were not used. Candidates that failed oEmbed (`pugVjrzUPXU`, `0ziJEg8coAs`) were dropped, not guessed.


## Q&A page videos — skin, allergy and hives, November 16, 2026

`tools/qa_videos_skin.json` (9 videos, 9 placements on 9 pages) records videos attached to `/qa/skin/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Podcast, veterinary-practice and breed-association channels are flagged in `commercial_note`. Product-sponsored, home-remedy, retailer and non-equine videos, and candidates older than about eight years, were not used. Mange and several other pages were left blank for lack of a topic-matched video.


## Q&A page videos — respiratory, November 16, 2026

`tools/qa_videos_respiratory.json` (9 videos, 9 placements on 8 pages) records videos attached to `/qa/respiratory/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Podcast, veterinary-practice, media and charity channels are flagged in `commercial_note`. Non-equine, owner-case-diary and feed-company videos, and candidates older than about eight years, were not used. Candidate `TYNpOXn_dio` failed oEmbed and was dropped, not guessed.


## Q&A page videos — hoof care and farrier, November 16, 2026

`tools/qa_videos_hoof.json` (3 videos, 3 placements on 3 pages) records videos attached to `/qa/hoof/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Grooming-service and media channels are flagged in `commercial_note`. Product-sponsored, supplement-promotion, general-channel how-to, barefoot-trimming and non-equine videos, a laminitis video contradicting veterinary sources, and candidates older than about eight years were not used. Six pages were left blank for lack of a topic-matched video.


## Q&A page videos — dental and oral, November 16, 2026

`tools/qa_videos_dental.json` (5 videos, 5 placements on 5 pages) records videos attached to `/qa/dental/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Practice, education-platform and equestrian-centre channels are flagged in `commercial_note`. Feed-company-presented, media-blog, non-English, non-equine and surgical-extraction videos, and candidates older than about eight years, were not used. Five pages were left blank for lack of a topic-matched video.


## Q&A page videos — eye, November 16, 2026

`tools/qa_videos_eye.json` (5 videos, 5 placements on 5 pages) records videos attached to `/qa/eye/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Practice, hospital, education-company and podcast channels are flagged in `commercial_note`. Personal-channel, vet-CPD technical, research-promotion, non-equine and Italian-language videos, and candidates older than about eight years, were not used. Seven pages were left blank for lack of a topic-matched video.


## Q&A page videos — wounds and trauma, November 16, 2026

`tools/qa_videos_wounds.json` (5 videos, 5 placements on 5 pages) records videos attached to `/qa/wounds/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Practice, individual-veterinarian and information-site channels are flagged in `commercial_note`. Product-review, owner-case, insurer-promotion, non-equine and research-lab videos, and candidates older than about eight years, were not used. Two pages were left blank for lack of a topic-matched video.


## Q&A page videos — neurologic and behavior, November 16, 2026

`tools/qa_videos_neurologic.json` (4 videos, 4 placements on 2 pages) records videos attached to `/qa/neurologic/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. Practice, university and magazine channels are flagged in `commercial_note`. Trainer, product-program, non-equine, vet-audience and general fitness videos were not used. Four pages (rehabilitation, anxiety signs, anxiety management, behavior) were left blank for lack of a topic-matched veterinary video.


## Q&A page videos — exercise, hydration and urinary, November 16, 2026

`tools/qa_videos_exercise.json` (4 videos, 4 placements on 3 pages) records videos attached to `/qa/exercise/` pages. Each was resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. All carry `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and none may be labeled medically reviewed or `clinical_approved`. University, extension and practice channels are flagged in `commercial_note`. Podcast, feed-product, trainer, human-medicine and older-than-eight-year candidates were not used; one ulcer-prevention short failed oEmbed and was dropped. Three pages (urgent signs, urinary, ulcer routine) were left blank.


## Q&A page videos — parasites and equipment, November 16, 2026

`tools/qa_videos_parasites.json` (1 video, 1 placement) records the video attached to `/qa/parasites/` pages, resolved through YouTube oEmbed (title and publisher) and chosen for topic fit; no video is used on more than two pages site-wide. It carries `status: source_verified` and `clinical_review: not_performed`: content has not been watched or reviewed by a veterinarian, and it may not be labeled medically reviewed or `clinical_approved`. Product-sponsored, extension-agent technique, podcast, kit-review and older-than-eight-year candidates were not used. The other four parasite pages and the equipment page were left blank; saddle-fit candidates were saddle-business or retailer videos.


## Q&A video relevance cleanup, November 16, 2026

Fourteen placements (eleven videos) were removed from `tools/qa_videos_*.json` because they did not match the question they were attached to, or conflicted with the exclusion rules (feed, supplement or retailer channels; vet-audience; case stories). Removed: IU4K3EyE8GY, Ac6qnVrUNjQ, IYugRveVek4, u4cU6jg67u8 (feed companies); vrrxQ8RFAMI (supplement company); 5whQPnmlEoA (retailer); oFzztNZKMcI (aimed at veterinarians); tcJF19u7FxM and wMigaFwVTY0 (case stories); FtIf8PIuu90 (floating check, not risks or aftercare); gf75JVj63nM (heart pulse, not digital pulse); and Ghv4rFutUCA from the GI diarrhea page (dehydration check, not diarrhea). Affected pages now have fewer or no videos.


## Q&A video relevance cleanup, second pass, November 16, 2026

YouTube pages cannot be fetched from this workspace, so this pass checked each remaining placement against its oEmbed title, publisher and `commercial_note` only; video descriptions and content were not read. Ten videos were removed: Mad Barn (nbYeTmWp9DA, KfQ1yQiFBCc; feed company), v9MLQ9EMJTg (presenter employed by an ulcer-drug maker), uaNVcDBEsE8 (personal channel), QiONaR-eOa8 (title is about treating an abscess, page is about signs; subscription channel), PMNwf9L3WOk and 7QZ1DA5A9kQ (aimed at veterinarians), CPCOLtkLmzc (veterinarian lecture on a subscription platform), f-9rSPjmmYk (may mention products), and D_l_dcPW-sI (grooming-service channel, not a veterinary or farrier source). Content review by a veterinarian is still required for every remaining video.

## Video pass on lameness and GI additions — 2026-11-16
Judged by title, publisher and note only (YouTube watch pages cannot be opened here). All ids passed oEmbed. No clinical review.
- arthritis-causes-treatment-and-outlook: xLv9KHnjafg (OSUHorse), kxpF6MeDfqI (World Horse Welfare Education)
- ligament-injury-treatment-and-healing-time: KxfPAYSZNgU (World Horse Welfare Education), Xh6IORjasuo (Dr. Sue Dyson, hosted on a training education channel)
- stifle-injury-signs-and-diagnosis: xxmahbnzv_8 (The Equine Institute, locked stifle)
- preventing-splints-in-horses: kyLAgcgmQo4 (StreamZ Global)
- omeprazole-use-rebound-and-treatment-cautions: HGDatdXR5sg (World Horse Welfare Education, general ulcer management)
- long-term-effects-of-untreated-gastric-ulcers: HGDatdXR5sg, F63HbUV4rp4 (Starwood Equine)
- stifle-injury-treatment-recovery-and-surgery: blank, no relevant non-product video found.
- Excluded: Mad Barn (feed retailer), Arthramid and omeprazole product videos, Boehringer presentation, a personal channel on splints, NatGeo TV clip, vet-only CPD, videos older than ~8 years, Pet Food Science Podcast, CVS Equine ulcer video (already at 2 uses).

## Scratches / cracked heels merge — 2026-11-16
Records 0163, 0179 added to `preventing-scratches` and 0191 to `scratches-treatment-and-recovery-time` (UC Davis lists cracked heels as another name for scratches). `preventing-scratches` stays blank: the only matching prevention videos came from Professional Equine Grooms, an affiliate retail channel, so they were excluded.

## Scratches video added — 2026-11-16
Zy0oKksngmg (OSU Small Farms Program, Dr. Dawn Sherwood) added to `preventing-scratches` and `scratches-treatment-and-recovery-time`. Second search for `stifle-injury-treatment-recovery-and-surgery` found only product (Ice Horse, Arthramid), TV (NatGeo) and clinic case-tracking videos, so it stays blank. Professional Equine Grooms videos remain excluded (affiliate retail channel).

## Lethargy pages — 2026-11-16
- when-to-call-the-vet-for-a-lethargic-horse: 2u-LmAxc9JE (Starwood Equine Veterinary Services, TPR how-to), wbGapOskTVE (Troy Equine Services, TPR how-to). Matches the page's check-vitals step; neither is about lethargy itself. Judged by title and publisher only.
- common-causes-of-lethargy-in-horses: blank. Search found a news clip on equine depression, general illness-sign videos from unnamed channels and vet-audience content; none matched.

## Malnutrition signs — 2026-11-16
signs-of-malnutrition-in-horses: 6DwaWTAhWn0 (RanchTV at Texas A&M AgriLife Extension, body condition scoring), _o1gH9poeHM (Maine State Society for the Protection of Animals with Dr. Tom Judd, scoring starved horses). Excluded: DengieHorseFeeds (feed brand), videos older than ~8 years, a #ad rib-check video. Judged by title and publisher only.
