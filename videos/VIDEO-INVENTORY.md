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
