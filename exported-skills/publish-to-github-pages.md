# Skill: publish-to-github-pages

**Trigger phrases:** "push my changes", "publish the site", "deploy to GitHub Pages", "commit and push", "update the live site"

---

# Publish to GitHub Pages

Follow these steps in order to stage, commit, push, and confirm deployment.

## Step 1 — Check current git status

Run `git status` to show the user what has changed:

```bash
git status
```

Summarise the output clearly:
- List modified files
- List untracked files
- Note the current branch

If there are **no changes** (clean working tree), tell the user there is nothing to commit and stop here.

## Step 2 — Ask for a commit message

Ask the user for a commit message. Suggest 2–3 options based on what you saw in `git status` — make them specific and descriptive (not "update files"). For example:

- "Add Episode 8 script and fix listen button alignment"
- "Fix episode card button alignment in index.html"
- "Add Episode 8 folder with script"

Always include an option for the user to provide their own message.

## Step 3 — Stage all changes

Run:
```bash
git add -A
```

Confirm it ran successfully before proceeding.

## Step 4 — Commit with the chosen message

Run:
```bash
git commit -m "<message from Step 2>"
```

Show the commit output to the user (the short hash and summary line).

## Step 5 — Push to main

Run:
```bash
git push origin main
```

If the push fails:
- If the error is "rejected" due to remote changes, tell the user to run `git pull --rebase origin main` first, then retry the push.
- If the error is an authentication failure, advise them to check their GitHub credentials or SSH key setup.
- For any other error, show the full error message and stop.

## Step 6 — Confirm deployment

After a successful push:
1. Tell the user the push succeeded and GitHub Pages will rebuild automatically (usually within 1–2 minutes).
2. Determine the live URL using this priority order:
   - **First**: check for a `CNAME` file in the repo root (`cat CNAME`). If it exists, the live URL is `https://<contents of CNAME>`. This is the canonical custom domain — always prefer it.
   - **Second**: if no `CNAME` exists, derive the URL from the remote: `git remote get-url origin`
     - Remote `https://github.com/username/repo.git` → `https://username.github.io/repo/`
     - Remote `git@github.com:username/repo.git` → `https://username.github.io/repo/`
     - If the repo name is `username.github.io`, the URL is `https://username.github.io/`
   - **Never** use the `og:url` meta tag value from `index.html` — it may be incorrect.
3. Display the live URL to the user and suggest opening it in 1–2 minutes to verify the changes are live.

## Notes

- Always run `git status` first — never assume what has changed.
- Never push without confirming the commit message with the user.
- If the user is on a branch other than `main`, warn them and ask if they want to proceed or switch branches first.
- Do not force-push (`--force`) under any circumstances.
