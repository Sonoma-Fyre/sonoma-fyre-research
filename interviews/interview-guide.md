# Interview guide: diagnosing wine demand for a Sonoma winery

Shared field instrument for Team Sonoma Fyre. Use it for every interview so five interviewers gather comparable evidence. The questions are not tied to any one interviewee: pick the module that matches who you are talking to. The goal is to diagnose what is actually failing (are wineries losing their old buyers or failing to win new ones, and is the problem foot traffic or spend per buyer) and to find which pivots have measurably worked. Each question names the hypothesis, contradiction, or lever it tests so you know why you are asking it. Hypotheses H1 to H3 and contradictions C5 and C6 are defined in `master-synthesis.md`.

## Interview rules (Mom-Test discipline, from CLAUDE.md)

- Ask about the past and about specifics, never about the future. Good: "when did you last, what did it cost, what happened after." Banned: "would you," "imagine," "if we offered."
- Never pitch our ideas. When you ask what a winery tried, do not read them our list of levers first.
- Chase numbers, not adjectives. Every question below has a capture line naming the figure to write down. Where a capture line lists more than one figure, treat it as a checklist and clear all of it before moving on.
- Do not lead. Several questions are open by design and you must not offer answer options on them: W4, W5, W7, W10, W12, CN2, CN4, and CN7. Ask, then wait.
- Write verbatim quotes in quotation marks. Keep what they said separate from what you think it means.

## Note metadata (put at the top of every note file)

Interviewee, role, date, place, teammate who ran it. File naming: kebab-case, date-prefixed, in `interviews/`, for example `2026-07-22-monte-rio-founder-notes.md`.

---

## Module 1: Winery operators

For owners, winemakers, and tasting-room or DTC managers. Aim for the ones you can get on the calendar before mid-August harvest.

### Trend: is it traffic or ticket

**W1. How do this year's total sales and cases sold compare with three years ago, and which moved more?**
Why we ask: W1 (H1, H2). Shows whether the problem is dollars or volume: if dollars held while cases fell, price or mix is masking a volume slide, which points to spend per buyer rather than lost buyers.
Capture: sales dollars and case volume for both years, which moved more, and in which direction.

**W2. Over those same three years, what happened to your tasting-room visits and to what an average visitor spends?**
Why we ask: W2 (H2). Splits traffic (how many come) from ticket (how much each spends) at the cellar door, the core diagnostic fork the desk data cannot make for a specific winery.
Capture: visits per year then versus now, and average spend per visit then versus now.

**W3. How has your wine club changed over three years, in both the number of members and the share who renew each year?**
Why we ask: W3 (H2, lean DTC lever). Club size and renewal are the survival metrics for the direct model; falling renewal signals the core itself pulling back.
Capture: member count then versus now, and annual renewal or retention rate then versus now.

### Who is buying, and who left

**W4. Who buys your wine today, and how is that different from three years ago?**
Why we ask: W4 (H2 falsifier). Tests whether the loss is the old core leaving or the young never arriving. Open on purpose: let them name the dimensions that matter before you probe age, local versus visitor, or club versus walk-in.
Capture: buyer mix now versus three years ago on whatever dimensions they raise, then probe the missing ones.

**W5. Have you had club members or regular buyers cancel or drift away recently? If so, what did they tell you when they left?**
Why we ask: W5 (H2 falsifier). H2 is wrong if the established older core is itself pulling back; their own words on leaving are the test. Do not assume there has been churn until they confirm it.
Capture: whether there is real churn, verbatim reasons, how many recently, and how long they had been buying.

### What moves volume

**W6. In the last two years, have you changed any prices, run discounts, or changed your tasting fee? For each change, what happened to volume or visits afterward?**
Why we ask: W6 (H1, price and value repositioning lever). No public source has a single winery's own price experiment, and firm-level demand is far more price-sensitive than the category, about -4.77 versus -0.53 (`chandra-2025-us-wine-demand-elasticity.pdf`). This closes our biggest field gap.
Capture: each price or fee change, its date and size, and the measured volume or visitation response.

**W7. What have you tried in the last three years to bring in sales or new customers? For each thing, roughly what did it cost, what happened, and are you still doing it?**
Why we ask: W7 (Act III, H3). A behavior inventory of every lever they actually pulled, with kept-or-killed outcomes. Open on purpose: do not read them our lever menu first.
Capture: each move (new varieties, formats, events, channel shifts, pricing), rough cost, measured result, kept or killed.

**W8. For any lesser-known grapes or unusual bottlings you make, how do their sell-through and margin compare with your flagship, and who buys them?**
Why we ask: W8 (alternative varieties lever, H3 differentiate falsifier). Sell-through and margin for non-benchmark varieties is missing from every public source we found, while benchmarked fruit is collapsing toward roughly $800 a ton on the spot market (`turrentine-2026-crush-report-2025.pdf`).
Capture: sell-through rate and margin for the alternative wines versus the flagship, and who buys the alternatives.

### The direct channel and the field

**W9. What share of your revenue is direct versus wholesale, how has that share moved over three years, and what happened to total revenue as it shifted?**
Why we ask: W9 (lean DTC lever, H3 direct). Direct sales carry about 70% of typical winery revenue, but the channel fell 15% by volume in 2025 (`sovos-2026-dtc-wine-shipping-report.pdf`), so the question is whether shifting toward direct actually held revenue up.
Capture: direct sales as a percent of revenue now and three years ago, and the direction of total revenue as the share moved.

**W10. Which wineries do you notice doing best right now, whatever their size, and what do you see them doing differently?**
Why we ask: W10 (H3 differentiate and go-small falsifier). In 2025 top-tier wineries grew revenue 22% while bottom-tier fell 13% in the same market (`napa-register-2026-svb-june-dtc-survey.pdf`). If the operators who are holding up are the larger, scaled ones, that cuts against the go-small thesis, so do not restrict the question to small peers.
Capture: named peers and their rough size, and the concrete tactics attributed to them (pricing, channels, events, service).

**W11. Since the 2025 crush, have you changed where you get your fruit, bought any grapes on the spot market, or renegotiated contracts?**
Why we ask: W11 (supply-correction enabler). The 2025 California crush was the lightest since 1999 and spot Sonoma Chardonnay ran near $800 a ton, making good fruit historically cheap for a lean buyer (`turrentine-2026-crush-report-2025.pdf`).
Capture: sourcing changes, spot purchases and their price, contracts dropped or renegotiated.

### The buyer's own words

**W12. When customers talk to you about their wine buying, what do they say? Tell me about the last few conversations.**
Why we ask: W12 (C5, C6). C5 (price versus health) and C6 (the weight of the competing drivers) are unresolved; offering options would fake a resolution. Open on purpose, and note it can only capture the reasons customers volunteer, not a full ranking.
Capture: verbatim customer reasons, unprompted, and what recurs across the last few conversations.

### Suggested run order (30 to 45 minutes)

W1, W2, W3 (warm up on the numbers), W4, W5 (who), W7 (what they tried, broad), then W6, W8, W9, W10, W11 (the economics), and close on W12 (open). Then the snowball ask below.

---

## Module 2: Ecosystem players

For growers, brokers, distributors, retailers, and trade or tourism organizations. These build the ecosystem map and ground-truth the supply story. Ask the ones that fit the person; not every question suits every role.

**E1. Compared with 2023, how much of your fruit is under contract versus sold on the spot market, what prices are you actually getting, and have you pulled any vines?** (growers and brokers)
Why we ask: E1 (supply-correction enabler). Turns the glut-and-correction narrative into realized grower economics.
Capture (checklist): contract versus spot mix in 2023 and now, realized dollars per ton, acres pulled.

**E2. Which price tiers and wine styles are you still taking on, and what have you delisted in the last year and at what price points?** (distributors and retailers)
Why we ask: E2 (the hourglass, `svb-2026-state-of-us-wine-industry.pdf`). Locates where trade demand still sits: under-$12 is deteriorating fastest while $20 to $29 and $100-plus hold up.
Capture: tiers and styles still moving, items delisted and their price points.

**E3. Have you seen any shared or regional marketing effort actually move visits or sales? If so, what were the numbers?** (associations and trade)
Why we ask: E3 (the parked Wine Improvement District lever). Generic-advertising studies claim 4:1 to 6:1 returns at industry level (`ward-2006-commodity-checkoff-generic-advertising.pdf`), but we have no winery-level outcome, so we want measured results, not adoption.
Capture: named efforts, the measured change in visits or sales, any hard figures.

**E4. For a small Sonoma winery, who actually decides whether its wine gets on a shelf, a wine list, or a visitor's itinerary?**
Why we ask: E4 (required ecosystem map). Names the gatekeepers and influencers between a winery and its buyer.
Capture: the roles and organizations that control shelf, list, and itinerary placement, and who influences the buyer before a visit.

### Suggested run order (30 minutes)

Open with the person's own role and E1 or E2 depending on where they sit, then E3, then E4 to map the wider field. Then the snowball ask below.

---

## Module 3: Consumers and buyers

For run clubs, tastings, and conversations with actual drinkers. Mom-Test discipline is strictest here: anchor every answer to a real, recent, specific occasion, and never offer the reason for them. Notes go in `consumer-field/`.

**CN1. When did you last buy a bottle of wine? What was it, where did you buy it, and what did it cost?**
Why we ask: CN1 (baseline). Anchors the conversation in a real purchase before anything else.
Capture: date, product, channel, price, occasion.

**CN2. Tell me about the last time you picked something other than wine to drink. What did you choose and what was going on?**
Why we ask: CN2 (C6, substitution). Captures real substitution (ready-to-drink, non-alcoholic beer, cannabis, or simply nothing) without leading them to it.
Capture: the alternative chosen, the occasion, and the reason in their own words.

**CN3. How does your wine drinking and buying now compare with two years ago? Which changed more, how often you drink it or how much you spend per bottle?**
Why we ask: CN3 (H1, C5). Splits frequency from spend at the buyer level. The split maps onto C5: the synthesis finds price tends to bind on spend per bottle while health and moderation bind on how often people drink.
Capture: direction of frequency versus spend, which moved more, rough magnitudes.

**CN4. Think of a recent time you decided not to buy or drink wine when you otherwise might have. What was going on?**
Why we ask: CN4 (C5, C6). Open on purpose: this is where price, health, moderation, or a substitute can surface in the buyer's own words, without us naming any of them. It can only capture what they volunteer, which is the honest limit of what an interview can weigh.
Capture: the occasion, the reason in their own words, and whether it points to cost, health, moderation, or something else.

**CN5. When did you last visit a winery or tasting room? What did you spend, and have you ever joined or left a wine club?**
Why we ask: CN5 (H2). The buyer-side read on tasting-room and club behavior.
Capture (checklist): last visit date, spend that visit, club history, and the reason for leaving if it lapsed.

**CN6. When did you last buy a bottle over $30? What was the occasion?**
Why we ask: CN6 (the hourglass, `drinks-business-2026-wine-opinions-value-survey.pdf`). 54% of respondents buy under-$15 wine regularly versus 28% for $30-plus; this finds the premium-occasion split.
Capture: the last purchase over $30, the occasion, and their normal price band.

**CN7. When did you last have wine, and what did you make of it? What do you usually reach for instead?** (younger drinkers)
Why we ask: CN7 (taste and image barrier, `wmc-2025-millennials-largest-cohort.pdf`). Among millennials who skip wine, 35% dislike the taste and 39% prefer other drinks; anchoring to the last time they actually had wine surfaces the entry barrier through a real occasion rather than an opinion.
Capture: when they last had wine and their reaction to it in their words, and their usual go-to drink instead.

### Suggested run order (20 to 30 minutes)

CN1 (baseline), CN3 (change over time), CN4 (a recent cutback, open), CN2 (substitution), CN5 and CN6 (visits and price), and CN7 for anyone under about 40. Then the snowball ask below.

---

## Adapting the guide to each interview

This file is the shared core, kept generic on purpose. Two kinds of question get added around it per interview, and neither belongs in this file.

- Interviewee-specific questions: once we lock the target list, prepare a short block for each interviewee from public sources (their winery, varieties, recent press) before you sit down. Keep them past-behavior and specific, slot them in after the module warm-up, and write them in that interview's note file, not here.
- On-the-go follow-ups: the capture lines are the floor, not the ceiling. When someone says something surprising, or something that cuts against the synthesis, chase it: "tell me more about that," "when was the last time," "what did that cost," "what happened next." Keep following past behavior and do not drift into pitching.

In the note, mark which questions were core, interviewee-specific, or improvised, so the synthesis can weight the answers.

## Close every interview with the snowball ask

"Who else should we talk to?" Ask for a name and an introduction. This is how we reach 10-plus interviews before harvest, and every name a winery or trade contact gives also feeds the ecosystem map.

## After each interview

Write the note the same day with the metadata header, verbatim quotes in quotation marks, and your read kept separate. After a batch, merge what matters into `master-synthesis.md` per the protocol in CLAUDE.md, and add your AI-tools log row if you used a tool.
