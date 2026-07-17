# Setup: connect your Claude to this folder

Each of us runs our own Cowork project pointed at this one shared folder. Do this once.

## Step 1: Clone the repo to your computer
The team's shared copy is the GitHub repo `rldser1986/sonoma-fyre-research`. Get a local clone (ask Rodolfo for collaborator access first if you cannot push).

Option A, command line:
1. Install git (or the GitHub CLI, `gh`).
2. Run: `git clone https://github.com/rldser1986/sonoma-fyre-research.git`
3. Note the folder it creates, for example `~/sonoma-fyre-research`.

Option B, GitHub Desktop:
1. Install GitHub Desktop and sign in.
2. File, Clone repository, pick `rldser1986/sonoma-fyre-research`.
3. Note the local path it clones to.

This clone is a working copy. It does not update on its own; you keep it in step with `git pull` and `git push` (see the sync rule in the paste below and in `CLAUDE.md`).

## Step 2: Create the Cowork project
1. Open Claude.
2. On the Home page, select Cowork.
3. Click Projects.
4. Click New Project.
5. In the project setup window, choose Add Folder.
6. Select your local clone folder from Step 1 (for example `~/sonoma-fyre-research`).
7. Rename the project to `Sonoma Fyre Research`.
8. Copy the instructions below and paste them into the project instructions.

## Instructions to paste (Step 2.8)
> Purpose: research support for Team Sonoma Fyre on reversing declining wine demand in Sonoma. This folder is a git clone of the shared repo (github.com/rldser1986/sonoma-fyre-research).
> Sync rule (this repo does NOT auto-sync like Drive): at the start of every work session, run `git pull` to get teammates' latest changes. After making changes worth sharing, `git add`, `git commit` with a clear message, and `git push`. If a pull reports conflicts, stop and surface them rather than guessing.
> First rule: read `CLAUDE.md` in this folder at the start of every task and follow it exactly. It holds all team rules (source of truth, citations, naming, the AI-tools log, style, the master-synthesis protocol). If this paste ever disagrees with `CLAUDE.md`, follow `CLAUDE.md`; the file is maintained, this paste is not.
> Fallback, only if `CLAUDE.md` is unreadable: the shared folder beats general knowledge; name the file for any fact you use; cite the file for any figure headed into a deliverable; log every AI research task in `ai-tools-log.md` (graded); concise plain prose, no em-dashes; deliverables US Letter, Arial, black, minimal styling.

## Step 3: check it took
In the new project, ask: "What working rules apply in this folder?" The answer should come from `CLAUDE.md` (citations, naming, the AI-tools log). If it does not, check the folder connection from Step 2, then ask Claude to read `CLAUDE.md` directly.

Note: our projects and chats stay separate; the GitHub repo is our shared common knowledge. Push your work so teammates can pull it, and do not commit anything you would not want the whole team to have.
