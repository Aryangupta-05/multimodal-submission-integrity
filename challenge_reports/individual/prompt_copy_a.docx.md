# Integrity audit: prompt_copy_a.docx

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | 48.39 |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

35 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 152; excluded: 151.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**prompt_copy_b.docx**, cosine **1.0000**

`{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop


## Excluded material

- configured_common_prompt: 151 words. Exact excluded text and spans in JSON.

## Peer evidence

### 1. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

### 2. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances

### 3. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near

Source passage:

> while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near

### 4. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source passage:

> The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

### 5. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed

### 6. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales

### 7. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers

### 8. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

Source passage:

> The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

### 9. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> I propose a two colour chalkboard tally of early and late sales

Source passage:

> I propose a two colour chalkboard tally of early and late sales

### 10. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers

Source passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers

### 11. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

Source passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

### 12. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

Source passage:

> I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

### 13. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker can record loaves by product without linking purchases to individual customers

Source passage:

> The baker can record loaves by product without linking purchases to individual customers

### 14. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

Source passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

### 15. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

Source passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

### 16. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

Source passage:

> The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

### 17. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

Source passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged

### 18. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

Source passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

### 19. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

Source passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

### 20. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

Source passage:

> After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.
> 
> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

### 21. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

Source passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note

### 22. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

Source passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted

### 23. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

Source passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

### 24. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

Source passage:

> Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

### 25. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

Source passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

### 26. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

Source passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

### 27. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

Source passage:

> Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

### 28. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

Source passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction

### 29. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

Source passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing

### 30. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

Source passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

### 31. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source passage:

> A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

### 32. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

Source passage:

> The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter

### 33. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Feedback can come from a small basket of paper comments near the counter

Source passage:

> Feedback can come from a small basket of paper comments near the counter

### 34. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source passage:

> Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop

### 35. prompt_copy_b.docx | cosine 1.0000

Location: `{"query_paragraphs": [2], "query_sections": ["Document body"], "matched_paragraphs": [2], "matched_sections": ["Document body"]}`

Query passage:

> The proposed intervention is a production scheduling change that uses equipment already present in the shop

Source passage:

> The proposed intervention is a production scheduling change that uses equipment already present in the shop


## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": 48.39,
  "status": "heuristic_only",
  "calibrated": false,
  "features": {
    "sentence_length_cv": 0.235,
    "type_token_ratio": 0.7895,
    "transition_count": 0,
    "words": 152
  },
  "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity."
}
