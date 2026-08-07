# CLAUDE.md: Team Sonoma Fyre working rules

Instructions for Claude. Five teammates each point their own Claude at this one shared folder, so five separate Claude instances work on these files in parallel. These rules are what make the five behave as one team; follow them exactly. Read this file at the start of every task. Rules live here; findings and status live in `master-synthesis.md`.

This folder is the single source of truth. If a fact, decision, or interview is not written in this folder, the team does not have it. Decisions made in meetings or on WhatsApp count only once someone records them here.

The team's shared copy lives in the GitHub repo (Sonoma-Fyre/sonoma-fyre-research). Your Cowork folder is a local git clone of it, so "this folder" and "the repo" mean the same body of work, kept in step with git. See Syncing with the team below.

## Syncing with the team (git)
This folder is a git clone, not a Drive-synced folder, so nothing updates on its own. We never commit to `main` directly; every change lands through a reviewed pull request.
- Start of every session: `git checkout main` then `git pull` to get teammates' latest work.
- Start new work on a branch: `git checkout -b <type>/<short-topic>`, for example `research/two-shepherds-notes` or `docs/pr-workflow`.
- Commit small and often, one topic per commit, with a clear message that names the teammate and what changed.
- Share it: `git push -u origin <branch>`, then open a pull request on GitHub for a teammate to review.
- Merge only after at least one teammate approves. Delete the branch after it merges.
- If a pull or merge reports a conflict, stop and surface it to your teammate. Never resolve a conflict by guessing or by discarding someone's work.

### Working from a cloud Cowork session
A Cowork session running in the cloud cannot run git inside this folder: the device bridge has no network to GitHub and cannot delete files. Claude: never run git in this folder from a cloud session. The workflow instead, in order:
1. Teammate, terminal, session start: check `git status` is clean, then `git checkout main` and `git pull`, so the folder the session reads is current. If status shows uncommitted changes you do not recognize, stop and check whether another session left work there before touching anything.
2. Claude, in its cloud workspace: clone fresh `main` from GitHub (the cloud side can read the public repo) and do all work there, on a properly named branch, following every rule in this file.
3. Claude delivers one git bundle built from `main..<branch>` and names the branch. If the delivery-time pull (step 4) brings in commits newer than the bundle's base, say so in chat before pushing: Claude rebases onto the new `main` in the cloud, resolves any overlap (log rows appended by two branches are the usual case), and delivers a fresh bundle.
4. Teammate, terminal, on delivery:
   - `git checkout main` and `git pull` (required even after step 1: the bundle only applies if local `main` already contains the commit the branch was built on)
   - `git fetch <path-to-bundle> <branch>:<branch>`
   - `git switch <branch>` then `git push -u origin HEAD`
   - `gh pr create --base main --fill --reviewer <teammate-username>` (no spaces in a comma-separated reviewer list)
   - `git switch main`
5. After a teammate approves and the PR merges: `git checkout main`, `git pull`, then `git branch -d <branch>`.
Sessions running on the teammate's own computer have working git and use the normal branch-and-PR steps above instead.

### Cowork cloud sandbox gotchas
These bite only when a session runs in the Cowork cloud sandbox and reaches this folder through the device bridge. They do not happen when Cowork runs on your computer or when you use a normal Mac terminal, so the fix is usually to run the git step yourself in Terminal.
- No network to GitHub from the bridge: `git pull` and `git push` in this folder fail with "403 from proxy after CONNECT". Do the file work in the session, then run pull and push from your own Mac terminal, or start the task in on-your-computer mode.
- The bridge cannot delete files: `git checkout` fails partway with "unable to unlink ... Operation not permitted" on tracked files and leaves the working tree in a mixed state. No lock trick fixes this; do not switch branches in this folder from a cloud session.
- Stranded `index.lock`: git through the bridge cannot delete its own lock file, so a leftover `.git/index.lock` blocks the next command, and even a read-only `git status` can leave one. The bridge cannot `rm` it either; rename it (`mv .git/index.lock .git/index.lock.old`) and retry. This clears the lock only; it does not make checkout or pull work (previous bullets).
- `quote>` hang on commit: a commit message split across two lines inside one pair of quotes leaves the shell waiting at a `quote>` prompt. Keep each `-m` on one physical line, and press Control-C to escape a stuck prompt (nothing is committed).

## The project in five lines
- Course: Applied Innovation Immersion Week (AIIW) 2026, UC Berkeley Haas, XMBA 290P.1.
- Topic: reversing declining wine demand, told through one Sonoma winery as protagonist (pick pending, see Open decisions).
- Method: three-act story (Origin, Present tension, Future) per Riemer's Get Your Startup Story Straight. The hero is the wine buyer, not the winery.
- Required output: 10-minute team presentation, ecosystem map, 10+ field interviews (at least 2 per member), Initial Research Results due Aug 9, 2026.
- Calendar: winery interviews in July (harvest crush makes wineries hard to reach from mid-August), Aug 9 research gate, immersion week in Sonoma Aug 11 to 14.

## Team
Jiahan Ericsson and Rohit Mishra (slides and story), Allison Leow and Rodolfo Lagos (research and economics), Alexa Kornau (outreach and interview logistics). Interviews themselves are everyone's job: the syllabus requires at least 2 per member.

## At the start of every task
1. Run `git checkout main` then `git pull` to get the team's latest work, and start your change on a new branch before anything else (see Syncing with the team).
2. Read `readme-index.md` for the folder map, then `master-synthesis.md` for where findings stand. Do this before answering research questions or writing anything.
3. Know which teammate you are working for; ask once if unclear. Date and sign their name on everything you add (log rows, interview notes, changelog lines).
4. The folder beats your general knowledge. When they disagree on something material, say so explicitly.

## Where work goes
- Source and article analysis: `research-readings/`. Register every new source in `research-readings/sources.md` (file, title, outlet, exact date, author, URL).
- Interview guides and per-interview notes: `interviews/`.
- Conversations with actual drinkers (run clubs, tastings, friends): `consumer-field/`.
- Graded outputs only: `deliverables/`.
- Integrated findings: `master-synthesis.md` and nowhere else. Never create a second synthesis or summary file; merge into the one.

## Naming and versions
- kebab-case, lowercase, no spaces: `monte-rio-interview-notes.md`. Date-prefix time-sensitive files: `2026-07-15-two-shepherds-notes.md`. (`CLAUDE.md` is a platform convention and the one uppercase exception.)
- One canonical file per topic. Supersede by replacing the old file's content, never by adding `-v2`, `-final`, or a near-duplicate. Every duplicate makes five Claudes give five different answers.
- Do not commit sync-collision or scratch files (`Copy of ...`, names ending `(1)`, editor temp files). If a git merge leaves conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in a file, resolve them with your teammate before committing; never leave them in.
- If a `memory.md` or similar auto-memory file appears here, it belongs to one member's Claude, not to the team. Do not treat it as team truth; flag it so its owner can move it out.

## master-synthesis.md protocol
- Pull the latest `main` into your branch, then re-read the live file immediately before editing it; a teammate may have just merged a change.
- Merge, never overwrite. Integrate new findings into the existing text. Do not delete or rewrite a teammate's contribution unless new evidence supersedes it, and then record what was replaced and why in the changelog.
- No claim enters without a citation (next section).
- Evidence that contradicts the current text goes into Open questions as a named conflict. Never silently pick a side.
- Keep hypotheses falsifiable: each keeps its "we are wrong if" clause, with supporting or opposing evidence cited beside it.
- End every edit with one changelog line at the bottom of the file: date, member, what changed.

## Citations
- Desk claims cite the source file in `research-readings/` by name, for example (oiv-2025-state-of-world-wine-sector.pdf).
- Interview and field claims cite the note file, for example (2026-07-15-two-shepherds-notes.md).
- Copy numbers exactly as the source prints them; if you round, write "about".
- Always distinguish desk research from primary research (our interviews and field notes). The Aug 9 deliverable is graded on both.
- Nothing from memory or the open web enters a deliverable until the source is saved into `research-readings/` and registered in `sources.md`.

## AI-tools log (graded; cannot be rebuilt in August)
Any AI-assisted research or deliverable work gets a row in `ai-tools-log.md` in the same session: date, member, tool, exact prompt, purpose, where the output went. If you (Claude) did the work, append the row yourself before the session ends.

## Interviews and field notes
- Mom-Test discipline: ask about past behavior and specifics ("when did you last buy wine, what was it, what did it cost"), never pitch ideas or ask hypotheticals ("would you buy...").
- Every note opens with metadata: interviewee, role, date, place, which teammate ran it.
- Verbatim quotes go in quotation marks; everything else is paraphrase. Keep what they said separate from what we think it means.
- After each batch, merge the findings that matter into `master-synthesis.md` per the protocol.

## Style
- No em-dashes anywhere: prose, notes, exports. Use commas, periods, or parentheses.
- Concise, plain, collaborative prose that reads as written by the team. No filler, no generated-sounding boilerplate.
- Markdown is canonical in this folder. Exports: US Letter, Arial, black text, minimal styling.

## Settled decisions (do not reopen)
- Topic: reversing declining wine demand with one Sonoma winery as protagonist. The apple backup topic exists only if the whole team formally switches.
- Story method: Riemer three-act, customer-as-hero.
- This folder structure and these rules. Change them only by team agreement, then edit this file.

## Open decisions (flag, never decide unilaterally)
- Protagonist winery: Monte Rio Cellars vs Quivira Vineyards. Neither appears in our nine desk sources, so the pick needs founder outreach. When the team decides, record it here and in `master-synthesis.md`.

## Hard guardrails
- Never delete a teammate's file or wholesale-rewrite their notes; propose changes to that person instead.
- Never invent facts, figures, quotes, interviewees, or citations. Unknown stays written as unknown.
- When two files conflict, surface the conflict; do not silently pick one.
- When unsure where something goes or whether a decision is settled, ask the teammate instead of guessing.
