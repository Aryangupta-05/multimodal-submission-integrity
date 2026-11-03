# Integrity audit: 04_clinic_paraphrase.docx

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | 45.2 |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

10 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 172; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**03_clinic.docx**, cosine **0.8816**

`{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query:

> Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications

Source:

> Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages


## Excluded material


## Peer evidence

### 1. 03_clinic.docx | cosine 0.8816

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications

Source passage:

> Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages

### 2. 03_clinic.docx | cosine 0.8795

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications. The proposal fixes a mismatch with the bus timetable, instead of blaming residents for insufficient commitment to treatment

Source passage:

> Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 3. 03_clinic.docx | cosine 0.8607

Location: `{"query_paragraphs": [1, 2], "query_sections": ["Document body"], "matched_paragraphs": [1, 2], "matched_sections": ["Document body"]}`

Query passage:

> For a countryside health centre, the earliest consultations ought to be set aside for people arriving on the single local bus. Public transport reaches the building before reception starts taking bookings, leaving those visitors stuck in the daily rush. A modest allocation of protected slots could prevent fruitless trips without hiring additional clinicians. During a six week trial, compare the nonattendance rate of public transport users against that of neighbours living close by. Urgent cases must retain priority, and access cannot depend on having a mobile telephone
> Each Thursday the community store could distribute numbered paper cards specifying consultation times, with no medical condition written down. Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications. The proposal fixes a mismatch with the bus timetable, instead of blaming residents for insufficient commitment to treatment

Source passage:

> A rural clinic should reserve its first morning appointments for patients travelling on the only village bus. That bus arrives before the normal booking desk opens, so visitors currently wait through the busiest part of the day. Keeping a small protected block would reduce wasted journeys without expanding the medical staff. The clinic should compare missed appointments for bus passengers with missed appointments for nearby residents over six weeks. The experiment must not displace emergencies or create a preference for people who own phones
> Reception staff can issue paper appointment cards through the village shop each Thursday. A numbered card holds the visit time without recording a diagnosis. Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 4. 03_clinic.docx | cosine 0.8493

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications. The proposal fixes a mismatch with the bus timetable, instead of blaming residents for insufficient commitment to treatment

Source passage:

> a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 5. 03_clinic.docx | cosine 0.8462

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence

Source passage:

> Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages

### 6. 03_clinic.docx | cosine 0.8246

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Each Thursday the community store could distribute numbered paper cards specifying consultation times, with no medical condition written down. Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications

Source passage:

> A numbered card holds the visit time without recording a diagnosis. Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages

### 7. 03_clinic.docx | cosine 0.8230

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications. The proposal fixes a mismatch with the bus timetable, instead of blaming residents for insufficient commitment to treatment

Source passage:

> Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 8. 03_clinic.docx | cosine 0.8154

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications

Source passage:

> Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 9. 03_clinic.docx | cosine 0.8089

Location: `{"query_paragraphs": [1, 2], "query_sections": ["Document body"], "matched_paragraphs": [1, 2], "matched_sections": ["Document body"]}`

Query passage:

> Urgent cases must retain priority, and access cannot depend on having a mobile telephone
> Each Thursday the community store could distribute numbered paper cards specifying consultation times, with no medical condition written down. Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence

Source passage:

> A rural clinic should reserve its first morning appointments for patients travelling on the only village bus. That bus arrives before the normal booking desk opens, so visitors currently wait through the busiest part of the day. Keeping a small protected block would reduce wasted journeys without expanding the medical staff. The clinic should compare missed appointments for bus passengers with missed appointments for nearby residents over six weeks. The experiment must not displace emergencies or create a preference for people who own phones
> Reception staff can issue paper appointment cards through the village shop each Thursday. A numbered card holds the visit time without recording a diagnosis. Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation

### 10. 03_clinic.docx | cosine 0.8070

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Each Thursday the community store could distribute numbered paper cards specifying consultation times, with no medical condition written down. Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence

Source passage:

> A numbered card holds the visit time without recording a diagnosis. Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages


## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": 45.2,
  "status": "heuristic_only",
  "calibrated": false,
  "features": {
    "sentence_length_cv": 0.2923,
    "type_token_ratio": 0.7907,
    "transition_count": 0,
    "words": 172
  },
  "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity."
}
