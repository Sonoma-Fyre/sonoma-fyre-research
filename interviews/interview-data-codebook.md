# Interview data: codebook and provenance

2026-08-09, Rodolfo. How the interview and survey data is stored, what each table means, and the rules used to build it. Built per the extraction plan agreed 2026-08-09 (long/tidy storage, generated wide views, coded layer in the same pass). Analysis reads the tables; deliverable claims cite the note files per CLAUDE.md.

## The six interviews

| interview_id | Who | Module | Ran by | Canonical note |
|---|---|---|---|---|
| WM-2026-07-24 | Chuck, wine reseller, The Wine Mine, Oakland | 2 | Allison Leow, Alexa Kornau | 2026-07-24-wine-mine-chuck-notes.md |
| OH-2026-07-27 | Justine, operations manager, OneHope | 2 | unknown, confirm | 2026-07-27-onehope-justine-notes.md |
| H12-2026-07-29 | Tasting-room / DTC manager, Highway 12 | 1 | Alexa Kornau | 2026-07-29-highway-12-notes.md |
| GF-2026-08-04 | Winemaker, Greater Fool Wine | 1 | self-completed | 2026-08-04-greater-fool-wine-notes.md |
| GAL-2026-08-05 | Director of sales finance (western area), Gallo | 1 | Alexa Kornau | 2026-08-05-gallo-notes.md |
| JAY-2026-08-08 | Jay Boberg | 1 | unknown, confirm | 2026-08-08-jay-boberg-notes.md |

The Wine Mine interview has two raw artifacts (live notes docx plus a Module 2 form entry) merged into one note and counted once. SURVEY-2026-08-08 in the coded tables refers to the consumer survey (n=14), which is consumer-field data, not an interview.

## Files and provenance

Canonical, hand-maintained:
- One md note per interview (listed above): metadata header plus verbatim source text, typos preserved, nothing reworded. The docx and xlsx originals these were extracted from stay outside the repo; the CSVs below carry the raw record.
- Raw form exports, cell-for-cell as CSV: `2026-08-04-greater-fool-module-1-responses.csv`, `2026-08-08-highway-12-gallo-module-1-responses.csv`, `2026-07-24-wine-mine-module-2-responses.csv`, and `../consumer-field/2026-08-08-wine-consumption-survey-responses.csv` (PII-stripped, see privacy).
- `interview-data.csv`: the tidy interview table (schema below). Form rows were extracted mechanically; docx rows were block-mapped by hand one time (the mapping cannot be regenerated from the CSVs alone).
- `interview-data-coded.csv`: the coded layer (interpretation, schema below).
- `hypothesis-evidence.csv`: per-hypothesis stance per source (interpretation).

Generated, never hand-edited (rebuild with `python3 build-generated-views.py` from this folder):
- `interview-data-module-1-wide.csv`, `interview-data-module-2-wide.csv`: rows are interviews, columns are question ids, cells verbatim. EXTRA material is not in the wide views; it lives in the tidy table and the notes.
- `../consumer-field/consumer-survey-data.csv`: tidy survey, one row per respondent and question.

## Tidy interview table: interview-data.csv

One row per interview and answered question. Columns: `interview_id, interview_date, org, interviewee, role, module, ran_by, capture_mode, question_id, question_text, answer_verbatim, source_note, flags`.

- `capture_mode`: `live-notes` (typed during the conversation), `form-live` (form filled by a teammate during a live interview), `form-self` (self-completed by the interviewee).
- `question_id`: `W1..W12`, `E1..E4` are the shared guide (interviews/interview-guide.md). `W13..W15` and `E5..E8` were added on the Google Forms and are not in the guide file. `SNOW` is the snowball ask. `EXTRA` is material matching no guide question; its `question_text` holds the in-note question when one exists, otherwise a `[label]`.
- Blank form cells produce no row (question shown, no answer recorded); the notes list them explicitly.
- `flags` carries per-row cautions (cross-references, answer mismatches, pasted questions, timestamp-derived dates).

Mapping rules used: a docx passage maps to a question id only when the note contains the question or the match is unambiguous, otherwise EXTRA; `answer_verbatim` is untouched source text; unknown stays unknown, written as "unknown, confirm"; one interview, one note, one count.

## Coded layer: interview-data-coded.csv

One row per interview and coded variable. Columns: `interview_id, variable, code, basis_verbatim, source_note, hypotheses`. This table is interpretation: codes are kebab-case values (directions like `up/down/flat`, or short category lists joined with `;`), each anchored to a short verbatim basis and its note file. `hypotheses` tags relevance: `H1 H2 H3` (master-synthesis.md working hypotheses), `C5 C6` (its cross-source contradictions), `lever:<name>` (Act III levers: price-value, dtc, varieties, format, supply, regional-marketing, brand), `ecosystem-map`, `context`. Codes never replace the verbatim; disagreement between a code and the note resolves toward the note.

## Hypothesis evidence: hypothesis-evidence.csv

One row per hypothesis and source. Columns: `hypothesis, interview_id, stance, basis_short, source_note`. Stance vocabulary: `supports, supports-weak, opposes, mixed, silent`. This is a generated reading of the coded layer for the Aug 9 results. It is not a second synthesis: findings merge into `master-synthesis.md` under its protocol, and this table is the evidence trail for that merge, nothing more.

## Consumer survey

`consumer-field/2026-08-08-wine-consumption-survey-responses.csv` is a snapshot of a live form (14 responses as of 2026-08-08); a later download supersedes it, replace the content, never add a version suffix. Respondents are `R1..R14`, anonymous end to end. Question ids `S1..S41` are the column positions; the question text rides along in the tidy file. Sample caveat: n=14 convenience sample, 8 of 14 aged 40 to 49, mostly SF Bay Area; directional texture, not population evidence.

Privacy: the repo is public. `S41` (contact for follow-up) never enters the repo in any form; the stripped raw carries a placeholder marker, the tidy file omits S41 entirely, and the six volunteered contacts live in `consumer-field/contacts-local-DO-NOT-COMMIT.csv` on local machines only (gitignored). Treat every survey cell as text when exporting; Excel had stored two phone numbers as floats.

## Open items carried in the data

Ran-by and place unknown for OH-2026-07-27 and JAY-2026-08-08; Jay's winery and role unstated in his note ("Nickel and Nickel" appears twice where his own winery may be meant, unconfirmed, left verbatim). Highway 12 offered follow-up numbers. Chuck tariff research is an open action item. Field tally at extraction time: 6 interviews toward the 10-plus requirement.
