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
