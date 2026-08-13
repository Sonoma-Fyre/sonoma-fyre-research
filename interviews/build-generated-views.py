#!/usr/bin/env python3
"""Rebuild the generated views from the canonical tables. Run from interviews/.

Inputs (canonical, hand-maintained or one-time extracted):
  interview-data.csv
  ../consumer-field/2026-08-08-wine-consumption-survey-responses.csv (PII-stripped raw)
Outputs (generated, never hand-edited):
  interview-data-module-1-wide.csv
  interview-data-module-2-wide.csv
  ../consumer-field/consumer-survey-data.csv
"""
import csv
from collections import OrderedDict

def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))

def write(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

# ---- wide views from the tidy interview table ----
rows = read("interview-data.csv")
hdr, data = rows[0], rows[1:]
ix = {h: i for i, h in enumerate(hdr)}
interviews = OrderedDict()
for r in data:
    key = r[ix["interview_id"]]
    meta = (r[ix["org"]], r[ix["interview_date"]], r[ix["module"]], r[ix["ran_by"]])
    interviews.setdefault(key, {"meta": meta, "answers": {}})
    qid = r[ix["question_id"]]
    if qid in ("EXTRA",):
        continue  # unmapped material stays in the tidy table and the notes
    a = interviews[key]["answers"]
    a[qid] = (a[qid] + " || " if qid in a else "") + r[ix["answer_verbatim"]]

def wide(module, qids):
    out = [["interview_id", "org", "interview_date", "ran_by"] + qids]
    for key, v in interviews.items():
        if v["meta"][2] != module:
            continue
        org, date, _, ran = v["meta"]
        out.append([key, org, date, ran] + [v["answers"].get(q, "") for q in qids])
    return out

write("interview-data-module-1-wide.csv", wide("1", [f"W{i}" for i in range(1, 16)] + ["SNOW"]))
write("interview-data-module-2-wide.csv", wide("2", [f"E{i}" for i in range(1, 9)] + ["SNOW"]))

# ---- tidy survey from the stripped raw ----
raw = read("../consumer-field/2026-08-08-wine-consumption-survey-responses.csv")
shdr, sdata = raw[0], raw[1:]
out = [["respondent_id", "question_id", "question_text", "answer"]]
for n, r in enumerate(sdata, start=1):
    for i, (q, v) in enumerate(zip(shdr, r), start=1):
        if i == 41 or not v.strip():
            continue  # S41 is the contact column, kept local only; blanks are skipped
        out.append([f"R{n}", f"S{i}", q, v.strip()])
write("../consumer-field/consumer-survey-data.csv", out)
print("generated views rebuilt")
