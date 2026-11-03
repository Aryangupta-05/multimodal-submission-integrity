# Integrity audit: 01_harbor.pdf

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | 45.33 |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

97 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 305; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**02_harbor_copy.pdf**, cosine **1.0000**

`{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect

Source:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect

**11_harbor_pitch.mp4**, cosine **1.0000**

`{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:00.000 - 00:00:04.720", "matched_start_seconds": 0.0, "matched_end_seconds": 4.72}`

Query:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source:

> The harbor cooperative should repair its cold storage before buying another delivery truck


## Excluded material


## Peer evidence

### 1. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect

### 2. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 3. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The

### 4. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process

Source passage:

> at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process

### 5. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning

Source passage:

> reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning

### 6. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four

Source passage:

> spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four

### 7. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 8. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight

### 9. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment

### 10. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

### 11. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

Source passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

### 12. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment

Source passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment

### 13. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

Source passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

### 14. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

Source passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

### 15. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

Source passage:

> The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

### 16. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

Source passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish

### 17. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

Source passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site

### 18. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

Source passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

### 19. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

Source passage:

> Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

### 20. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The first investment should therefore address the temperature failure at the landing site

Source passage:

> The first investment should therefore address the temperature failure at the landing site

### 21. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

Source passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

### 22. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

Source passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

### 23. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

Source passage:

> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

### 24. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

Source passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative

### 25. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

Source passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening

### 26. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

Source passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

### 27. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

Source passage:

> This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

### 28. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening

Source passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening

### 29. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

Source passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening

### 30. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

Source passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

### 31. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

Source passage:

> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

### 32. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

Source passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

### 33. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

Source passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

### 34. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

Source passage:

> A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

### 35. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

Source passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan

### 36. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

Source passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

### 37. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

Source passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

### 38. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

### 39. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

Source passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful

### 40. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

Source passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

### 41. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

### 42. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

### 43. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_page": 1, "matched_pages": [1]}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

Source passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle

### 44. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

### 45. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

### 46. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_page": 1, "matched_pages": [1, 2]}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 47. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

### 48. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

### 49. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 50. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 51. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 52. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 53. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

### 54. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 55. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

### 56. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

Source passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

### 57. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 58. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

### 59. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

### 60. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

### 61. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

### 62. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

Source passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

### 63. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

Source passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

### 64. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

Source passage:

> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

### 65. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Every participating vessel would receive
> the same access to crates during the trial

Source passage:

> Every participating vessel would receive
> the same access to crates during the trial

### 66. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

Source passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings

### 67. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

Source passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

### 68. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

Source passage:

> Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

### 69. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

Source passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

### 70. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

Source passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

### 71. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 72. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

Source passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection

### 73. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

Source passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

### 74. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 75. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

Source passage:

> The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve

### 76. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 77. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_page": 2, "matched_pages": [2]}`

Query passage:

> These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> These checks distinguish the operational claim from a generic recommendation to
> expand distribution

### 78. 11_harbor_pitch.mp4 | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:00.000 - 00:00:04.720", "matched_start_seconds": 0.0, "matched_end_seconds": 4.72}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

### 79. 11_harbor_pitch.mp4 | cosine 1.0000

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:16.700", "matched_start_seconds": 5.8, "matched_end_seconds": 16.7}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 80. 11_harbor_pitch.mp4 | cosine 0.9968

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 81. 11_harbor_pitch.mp4 | cosine 0.9965

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 82. 11_harbor_pitch.mp4 | cosine 0.9918

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:11.540 - 00:00:20.140", "matched_start_seconds": 11.54, "matched_end_seconds": 20.14}`

Query passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 83. 11_harbor_pitch.mp4 | cosine 0.9894

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:00.000 - 00:00:11.540", "matched_start_seconds": 0.0, "matched_end_seconds": 11.54}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice

### 84. 11_harbor_pitch.mp4 | cosine 0.9847

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:00.000 - 00:00:20.140", "matched_start_seconds": 0.0, "matched_end_seconds": 20.14}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 85. 11_harbor_pitch.mp4 | cosine 0.9827

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:00.000 - 00:00:16.700", "matched_start_seconds": 0.0, "matched_end_seconds": 16.7}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 86. 11_harbor_pitch.mp4 | cosine 0.9288

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 87. 11_harbor_pitch.mp4 | cosine 0.9174

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:16.700", "matched_start_seconds": 0.0, "matched_end_seconds": 16.7}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 88. 11_harbor_pitch.mp4 | cosine 0.9038

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:16.700", "matched_start_seconds": 0.0, "matched_end_seconds": 16.7}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 89. 11_harbor_pitch.mp4 | cosine 0.8632

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply

Source passage:

> A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 90. 11_harbor_pitch.mp4 | cosine 0.8484

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial

Source passage:

> A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 91. 11_harbor_pitch.mp4 | cosine 0.8443

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:16.700", "matched_start_seconds": 0.0, "matched_end_seconds": 16.7}`

Query passage:

> Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 92. 11_harbor_pitch.mp4 | cosine 0.8408

Location: `{"query_page": 2, "query_pages": [2], "matched_timestamp": "00:00:05.800 - 00:00:20.140", "matched_start_seconds": 5.8, "matched_end_seconds": 20.14}`

Query passage:

> spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four

Source passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 93. 11_harbor_pitch.mp4 | cosine 0.8350

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:16.700", "matched_start_seconds": 0.0, "matched_end_seconds": 16.7}`

Query passage:

> A coastal fish cooperative is losing income because its storage rooms warm overnight. The
> members have proposed purchasing another delivery truck, yet dispatch records show that
> vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding
> transport before stabilizing storage would increase idle capacity rather than preserve more fish.
> The first investment should therefore address the temperature failure at the landing site. This is a
> synthetic business case; the quantities below are illustrative rather than observations from a real
> cooperative.
> The pilot would assign two members to inspect seals and clean condenser coils every evening. A
> paper log would record room temperature at closing and opening. Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

### 94. 11_harbor_pitch.mp4 | cosine 0.8183

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:20.140", "matched_start_seconds": 0.0, "matched_end_seconds": 20.14}`

Query passage:

> reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 95. 11_harbor_pitch.mp4 | cosine 0.8125

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:20.140", "matched_start_seconds": 0.0, "matched_end_seconds": 20.14}`

Query passage:

> to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks.
> The decision rule should use the fraction of landed fish discarded, not revenue alone, because
> auction prices change with weather and seasonal supply. Every participating vessel would receive
> the same access to crates during the trial. A rotating committee would publish aggregate totals
> without disclosing individual earnings. A four week reduction in waste would justify extending the
> maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The
> cooperative should stop the pilot if contamination incidents increase, even if transport margins
> improve. These checks distinguish the operational claim from a generic recommendation to
> expand distribution

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

### 96. 11_harbor_pitch.mp4 | cosine 0.8085

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:04.720", "matched_start_seconds": 0.0, "matched_end_seconds": 4.72}`

Query passage:

> If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

### 97. 11_harbor_pitch.mp4 | cosine 0.8061

Location: `{"query_page": 1, "query_pages": [1, 2], "matched_timestamp": "00:00:00.000 - 00:00:04.720", "matched_start_seconds": 0.0, "matched_end_seconds": 4.72}`

Query passage:

> Repairs would be funded from
> a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare
> spoilage during similar landing volumes, since a small catch can make a weak process appear
> successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer
> without committing the group to a new vehicle
> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck


## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": 45.33,
  "status": "heuristic_only",
  "calibrated": false,
  "features": {
    "sentence_length_cv": 0.3456,
    "type_token_ratio": 0.6885,
    "transition_count": 0,
    "words": 305
  },
  "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity."
}
