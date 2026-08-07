# California Grape Crush and Acreage Reports, 2000-2025

Two California-wide data artifacts, built alongside the Sonoma crop report dataset (`sonoma-crop-report-wine-grapes-2000-2024.md`). These are statewide, not Sonoma-specific, with one Sonoma-adjacent proxy noted below. Wine grapes only; table and raisin grapes excluded throughout.

## Files

- `california-crush-report-statewide-summary-2000-2025.csv`: California statewide crush totals by color (white/red), tons crushed, weighted average price per ton, and average Brix, one row per color per year.
- `california-crush-report-district3-sonoma-marin-2000-2025.csv`: Grape Crush District 3 (Sonoma and Marin Counties combined, the official CDFA/NASS pricing district) tons and price per ton by color, one row per color per year.
- `california-grape-acreage-estimated-2000-2025.csv`: California statewide estimated wine grape acreage (bearing, non-bearing, total), one year per row.
- `california-crush-report-trends-2000-2025.html`: standalone trend-chart dashboard for the two crush CSVs above (statewide and District 3 tons and price per ton, red vs white, price shown nominal and inflation-adjusted to 2000 dollars).
- `california-grape-acreage-trends-2000-2025.html`: standalone trend-chart dashboard for the acreage CSV above (bearing, non-bearing, total).
- `wine-grape-trends-combined-dashboard-2000-2025.html`: combined dashboard with every chart from the acreage, Sonoma crop, and crush datasets in one file, presented in that order (acreage, then crop, then crush) with each chart's geography and units labeled, since the three sources cover different geographies (see "Why California-wide, not Sonoma-specific" below).

## Source

California Grape Crush Report and California Grape Acreage Report, published by the California Department of Food and Agriculture (CDFA) in cooperation with USDA's National Agricultural Statistics Service (NASS), Pacific Regional Office. Reports fetched directly from nass.usda.gov; see `sources.md` for the registered listing pages. Where both a "Final" and later "Errata" report existed for a crop year, the Errata figures were used as authoritative wherever they reached the needed table; otherwise Final was used and is noted.

## Why California-wide, not Sonoma-specific

Unlike the Sonoma crop report, neither the Crush Report nor the Acreage Report is published at the Sonoma County level directly for the figures we could reliably extract. The closest available proxy:

- **Crush report**: Grape Crush District 3 is defined by CDFA/NASS as "Sonoma and Marin Counties" combined. This is the standard proxy used industry-wide for Sonoma crush activity, but it is not Sonoma alone.
- **Acreage report**: does publish true county-level acreage (Sonoma by name), but that table sits far enough into each report (past a large table-grape section we don't need) that it could not be reliably reached with our extraction tooling. This was tested across multiple years (2000, 2005, 2024) with the same result each time, so it's a structural limit, not a one-off failure. Only the California statewide "Estimated Grape Acreage" figure is included here.

## Known data gaps (crush report, District 3 price only)

Tons crushed and California statewide figures are complete for all 26 years (2000-2025), no gaps. District 3 price per ton, split by color, could not be reached in the source PDF text for:

- 2000, 2001, 2002, 2003, 2009 (both colors)
- 2020, 2021 (red only; white was recovered)
- 2023, 2024, 2025 (both colors)

This is a tool-side reach limit on very long PDF reports (some of these documents run 100+ pages, and the district-price table sits deep enough that it fell outside what could be extracted in a single pass), not evidence the figure doesn't exist in the source. Where available, a combined (not color-split) District 3 narrative price from the report's own summary text is noted in the CSV's `notes` column as a partial substitute. Do not interpolate across these gaps; treat them as missing data points when charting (see the changelog note in the crop-report trend files for the plotting convention we've used elsewhere on this project).

## Acreage report: two different "acreage" numbers

Every Acreage Report publishes two distinct figures that are easy to conflate:

1. **Estimated Grape Acreage** (what this dataset uses): a rounded, survey-extrapolated statewide estimate with an allowance for incomplete reporting, published in each report's RESULTS section. Rounded to the nearest 1,000 acres.
2. **Detail data**: unrounded figures built directly from the ~6,500-10,000 grower questionnaires actually returned that year, broken out by variety, county, and year planted. This is a narrower base (voluntary response, and it excludes acreage harvested and removed within the same year), and it runs 20-25% lower than the Estimated figure in every year checked.

These two series answer different questions and are not directly comparable. This dataset uses the Estimated figure only, since it is CDFA/NASS's own headline statewide number.

## Inflation adjustment and the 2025 CPI-U gap

The trend-chart HTML files adjust crush price per ton to 2000 dollars using the same BLS CPI-U annual-average series (1982-84=100) already used for the Sonoma crop report price charts, 2000-2024. BLS's December 2025 CPI News Release (released Jan 13, 2026; see `sources.md`) states the 2025 CPI-U series has a data gap for October and November 2025 from the 2025 federal lapse in appropriations, and no calendar-year 2025 annual average has been published as of this check. Rather than estimate one, the inflation-adjusted (real, 2000$) price lines stop at 2024 in every chart; 2025 is shown nominal-only. Do not interpolate or approximate a 2025 real value until BLS publishes the finalized annual figure.

## Citation

Cite the report listing pages registered in `sources.md`: the Grape Crush Reports listing and the Grape Acreage Reports listing, both at nass.usda.gov (California Field Office, Specialty and Other Releases). Individual report PDFs are not cited per-file, consistent with how the crop report source is registered.
