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
The Cowork project loads this whole folder into context, so `CLAUDE.md` is always available. The paste is therefore just a pointer to it, not a copy of the rules (that keeps the two from drifting).

> Read `CLAUDE.md` in this folder and follow it exactly. It is the single source of truth for all team working rules: git sync and the branch/PR flow, citations, naming, the AI-tools log, style, and the master-synthesis protocol.

## Step 3: check it took
In the new project, ask: "What working rules apply in this folder?" The answer should come from `CLAUDE.md` (citations, naming, the AI-tools log). If it does not, check the folder connection from Step 2, then ask Claude to read `CLAUDE.md` directly.

Note: our projects and chats stay separate; the GitHub repo is our shared common knowledge. Push your work so teammates can pull it, and do not commit anything you would not want the whole team to have.
