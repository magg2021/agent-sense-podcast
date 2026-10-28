# Skill: publish-episode

**Trigger phrases:** "publish episode [N]", "add episode [N]", "new episode is out", "episode [N] is live"

---

# Publish a New Podcast Episode

Follow these steps in order to update the Agent Sense website for a new episode and push it live to GitHub Pages.

## Step 1 — Gather episode details

Ask the user for anything not already provided. You need:

- **Episode number** (e.g. 10)
- **Episode title** (full title as it should appear on the site)
- **Cover image path** (relative path to the cover PNG, e.g. `Episode 10-Ambient Agents/Podcast_cover_10.png`)
- **Spotify link** (direct episode link, e.g. `https://open.spotify.com/episode/...`)
- **Apple Podcasts link** (direct episode link with `?i=...`, e.g. `https://podcasts.apple.com/.../id1861925214?i=...`)
- **Guest name and role** — or confirm there is no guest
- **Arc theme label** — the one-word or short label for this episode's place in the Enterprise Arc (e.g. "Ambient Agents")
- **Arc breakdown sentence** — one sentence describing what this episode covers in the arc breakdown list
- **Key takeaway** — one punchy sentence
- **Episode description** — 2–3 sentences for the card and featured section
- **Tags** — 3–5 short topic tags (e.g. "Ambient Agents", "Event-Driven")
- **Publish date** — shown on the card (e.g. "Jul 31, 2025")

If the Apple Podcasts link is not yet available, proceed without it and note it as a follow-up. Do not block publishing for a missing Apple link.

## Step 2 — Read the current index.html

Locate and confirm the current state of each section you are about to edit. Specifically check:

1. The **Featured Episode** section (search for `featured-episode`)
2. The existing **episode card** for this episode number (it may already exist as "Coming Soon")
3. The **Enterprise Arc path** (`arc-path`) and **arc breakdown list**
4. The **hero CTA button** (`cta-primary`)
5. The **JS episodes array** at the bottom of the file (search for `episodes: [`)

Never assume the current content — always read first.

## Step 3 — Update index.html

Make all changes in a single pass using multiple find-and-replace operations. Update these five sections:

### 3a. Hero CTA button
Update the Spotify link in the `cta-primary` anchor to the new episode's Spotify URL.

### 3b. Featured Episode section
Replace the entire `<section class="featured-episode">` block:
- New cover image `src` and `alt`
- Episode number and publish date
- Full episode title
- Remove the guest line if there is no guest; update it if there is a guest
- New description
- New key takeaway
- Updated Spotify and Apple listen buttons (use `#` as placeholder for Apple if not yet available)

### 3c. Enterprise Arc
- Add the new arc theme label as a new `<div class="arc-step">` at the end of the `arc-path`, preceded by `<span class="arc-arrow">›</span>`
- Add a `<li>` entry in the arc breakdown `<details>` list

### 3d. Episode card
If the episode card already exists as "Coming Soon":
- Remove the `<span class="coming-soon">Coming Soon</span>` badge
- Add `<div class="episode-date">` with the publish date
- Update the title to the full title
- Expand the description
- Add `<div class="listen-links">` with Spotify and Apple buttons

If the card does not exist yet, insert a new `<!-- Episode N -->` card block after the previous episode's card, following the same HTML structure as the other cards.

### 3e. JS episodes array
Find the episode's entry in the `episodes: [` array (it may already exist with `comingSoon: true`). Update or add:
- `title` — full title
- `description` — 2–3 sentence description
- `spotify` — Spotify URL (without `?si=...` tracking params)
- `apple` — Apple Podcasts URL with `?i=...`
- Remove `comingSoon: true` if present
- `guest` — guest string or `null`

If there is a guest, also add them to the `guests: [` array following the same structure as existing guest entries.

## Step 4 — Commit and push

Run git commands:

```bash
git add index.html && git commit -m "Publish Episode [N] — [Title]" && git push origin main
```

Show the commit hash and confirm the push succeeded.

## Step 5 — Follow up on missing details

After pushing, check whether any details were skipped:
- If Apple Podcasts link was missing, remind the user to provide it so you can update the three Apple link locations (featured section, episode card, JS data).
- If any other field was missing, list what still needs to be added.

## Updating an existing episode tile

When the user asks to update any field on an episode (title, description, date, image, links, takeaway, guest, tags), **always update it in both tile locations**:

1. **Featured Episode section** (`<section class="featured-episode">`) — this large tile exists for the **latest** episode only. If the episode being updated is the current latest, update it here.
2. **Episode card** in the episodes grid (`<!-- Episode N -->` block inside `.episodes-grid`) — always update this card regardless of which episode is being changed.
3. **JS episodes array** (`AS_KB.episodes`) — always keep the data object in sync with the HTML tiles.

If the user says "update the tile" or "fix the episode", treat that as updating **all three** locations above. Never update only one location and leave the others stale.

**Checklist when updating any episode field:**
- [ ] Featured Episode section (if it is the latest episode)
- [ ] Episode card in the grid
- [ ] JS `AS_KB.episodes` entry

## Notes

- There are **five** places to update for every new episode: hero button, featured section, arc, episode card, JS data.
- New episodes that have a guest also appear in a third tile location: the **Guests section** (`<section class="guests-section" id="guests">`). If a guest name, role, or bio changes, update the guest card there too.
- The hero CTA button (`cta-primary`) is easy to miss — always check it.
- The JS `apple` field in the episodes array should use the URL **without** the `?si=` tracking suffix from Spotify (keep `?i=` for Apple).
- Show-level Apple Podcasts links (nav, footer, ratings badge) should **not** be changed — only the episode-specific links.
- Always read the file before editing — never assume the current content.
- If the episode card already exists as "Coming Soon", update it in place rather than adding a duplicate.
