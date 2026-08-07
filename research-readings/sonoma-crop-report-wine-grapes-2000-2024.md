# Sonoma County crop report: wine grapes, 2000-2024

Desk research dataset. Wine grapes only (table grapes and raisin grapes excluded). Source: Sonoma County Department of Agriculture, Weights & Measures, annual Crop Reports (sonomacounty-crop-reports).

## What's here

Two CSVs, both in this folder:
- `sonoma-crop-report-wine-grapes-yearly-summary-2000-2024.csv`: one row per year, total tons, total value, price per ton, bearing/non-bearing/total acres, and a notes column flagging any judgment call or source inconsistency for that year.
- `sonoma-crop-report-wine-grapes-variety-detail-2000-2024.csv`: one row per year per variety (long format), with color (red/white), bearing/non-bearing/total acres, tons, price per ton, and value.

Two standalone HTML chart files, built from the CSVs above, open directly in a browser:
- `sonoma-wine-grapes-red-vs-white-trends-2000-2024.html`: total tons, price per ton (nominal and inflation-adjusted), and total acreage, red vs white.
- `sonoma-wine-grapes-by-variety-trends-2000-2024.html`: the same three metrics for the top 5 varieties by tons (Chardonnay, Pinot Noir, Cabernet Sauvignon, Merlot, Zinfandel).

Price-per-ton charts show both a nominal line and an inflation-adjusted line (CPI-U annual averages, 2000 = reference year; source: U.S. Bureau of Labor Statistics, https://www.bls.gov/cpi/tables/supplemental-files/historical-cpi-u-202412.pdf). Adjusted for inflation, red grape prices per ton fell about 15% from 2000 to 2024 and white fell about 26%; by variety, only Pinot Noir held its real value (roughly flat), while Chardonnay, Cabernet Sauvignon, Merlot, and Zinfandel all lost real value (down about 27%, 34%, 40%, and 17% respectively).

## Scope and why it starts at 2000

The county has published a Crop Report every year since 1928, but only 2000-2024 was extracted. Reports from 2000 on use a consistent "Winegrape Production" table (separate Reds and Whites, one row per variety, with bearing acres, non-bearing acres, total acres, tons, price per ton, and value). Before that:
- 1999's report is an image scan with no text layer, and no later report carries 1999 as a prior-year comparison column, so it's unrecoverable without OCR.
- 1998 and earlier: the per-variety red/white tables were laid out as charts/graphics rather than text, so only a lump wine-grape total is extractable, not the varietal breakdown this dataset is built around.

Per team decision, years before 2000 were left out entirely rather than mixed in at lower confidence.

The 2000 and 2001 report PDFs are themselves image scans; those two years were recovered from the "prior year" comparison columns printed in the 2001 and 2002 reports, respectively.

## Method

Each year's PDF was downloaded from the Crop Reports page and its Winegrape Production table (Reds and Whites) extracted via `pdftotext`, cross-checked wherever possible against the same figures reprinted as a "prior year" comparison column in the following year's report, and validated with two arithmetic checks: bearing acres + non-bearing acres = total acres, and tons x price per ton ≈ value. No figures came from memory or general knowledge; every number traces to a specific report PDF.

## Known inconsistencies in the source reports themselves

These aren't extraction errors; the county's own report vintages disagree internally or across years. Numbers are kept as the source printed them (per team style: copy numbers exactly, round only with "about"), and the conflict is flagged rather than silently resolved:

- **2005**: the Winegrape Production table's own printed total acreage (63,824.6) doesn't equal its own bearing + non-bearing figures. Used the Fruit & Nut Summary's reconciled total (62,146) instead.
- **2007, 2011**: each year's own Winegrape Production table disagrees with that same report's Fruit & Nut Summary page on bearing acres (off by about 37 acres in 2007, about 247 in 2011). Winegrape Production table used as primary (more granular source).
- **2010**: the 2011 report's comparison column shows 2010 tons/value revised downward, marked "*Revised from 2010." 2010's own contemporaneous report used as primary; the later revision is noted.
- **2012**: the 2012 report's own red-grape acreage differs materially from the 2013 report's comparison column for the same year; the 2014 report explicitly notes "All Acreage Information Revised for 2012." The later, revised figures are used as primary.
- **2015, 2017**: summing each year's TOTAL ALL REDS + TOTAL ALL WHITES component values exceeds the stated TOTAL WINEGRAPES total by roughly $3.3-3.4M, even though acreage and tonnage reconcile exactly. Likely a weighted-average rounding artifact in the source; the stated grand total is used as primary.
- **2020**: the Fruit & Nut Summary states wine grape value as $351,511,500 versus the Winegrape Production table's own $357,511,500 (repeated identically in the 2021 report's comparison column), a likely 5/7 digit transposition in the source PDF. Winegrape Production table figure used as primary.
- **2007 "Other Whites"** and **2014 Muscat Blanc**: printed bearing + non-bearing acreage doesn't equal the printed total for that row. Kept as printed in the variety-detail CSV, flagged here rather than silently corrected.

## Variety coverage changes over time (not missing data)

The named-variety list isn't constant across 2000-2024, which is why row counts differ by year:
- Chenin Blanc and Napa Gamay drop out after 2003.
- Malbec and Pinot Gris first appear in 2004.
- Grenache and Mataro/Mourvedre first appear intermittently from 2015, consistently from 2019 on.
- 2016 uniquely lists "Sauvignon Musque" and a combined "White Riesling/Johannisberg Riesling" line, and omits Carignane and Roussanne as named rows that year.
- 2009-2012 print no "Other Reds"/"Other Whites" catch-all row; 2019-2024 reports also don't itemize an "other" row (their totals are labeled "Top 13 reds"/"Top 10 whites including other reds/whites," so the residual is only in the yearly total, not broken out by variety).
- 2009 and 2010's "Other Reds"/"Other Whites" rows print tons and value but no price per ton; that field is blank in the CSV for those four rows.
- Variety spelling is preserved exactly as each year's report printed it (e.g. "Petite Verdot" vs. "Petit Verdot," "White Riesling" vs. "White Reisling," "Mataro/Mourvedere" vs. "Mataro/Mouvedere") rather than normalized.

## Citation

Sonoma County Department of Agriculture, Weights & Measures, Crop Reports, https://sonomacounty.gov/natural-resources/agriculture-weights-and-measures/crop-reports (2000-2024 report PDFs).
