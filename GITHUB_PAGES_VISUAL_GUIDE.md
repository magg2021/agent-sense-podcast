# GitHub Pages Setup - Visual Step-by-Step Guide

## Finding the "Source" Setting on GitHub Pages

### Step 1: Go to Your Repository
1. Open your browser
2. Go to: `https://github.com/magg2021/agent-sense-podcast`
3. Make sure you're logged into GitHub

### Step 2: Click on "Settings"
- Look at the **TOP menu bar** of your repository
- You'll see tabs: `< > Code`, `Issues`, `Pull requests`, `Actions`, `Projects`, `Wiki`, `Security`, `Insights`, **`Settings`**
- Click on **`Settings`** (it's the last tab on the right)

### Step 3: Click on "Pages" in the Left Sidebar
- On the left side, you'll see a menu with many options
- Scroll down until you see **`Pages`** (it has a 📄 icon)
- Click on **`Pages`**

### Step 4: Find the "Build and deployment" Section
Once you're on the Pages settings page, you'll see:

```
┌─────────────────────────────────────────────────────┐
│  Pages                                              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Build and deployment                              │
│                                                     │
│  Source                                            │
│  ┌─────────────────────────────────────┐          │
│  │ Deploy from a branch            ▼   │  ← Click this dropdown
│  └─────────────────────────────────────┘          │
│                                                     │
│  Branch                                            │
│  ┌──────────┐  ┌──────────┐                       │
│  │ main  ▼  │  │ /(root) ▼│  [Save]  ← Click Save │
│  └──────────┘  └──────────┘                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Step 5: Configure the Settings

**What you'll see:**

1. **Source dropdown:**
   - Should say "Deploy from a branch"
   - If it says something else, click the dropdown and select "Deploy from a branch"

2. **Branch dropdown (this is what you're looking for!):**
   - First dropdown: Select **`main`** (your branch name)
   - Second dropdown: Select **`/ (root)`** (the folder)

3. **Save button:**
   - Click the **`Save`** button

### Step 6: Wait for Deployment
After clicking Save, you'll see:
- A message saying "Your site is ready to be published"
- Then after 1-2 minutes: "Your site is live at https://magg2021.github.io/agent-sense-podcast/"

---

## Troubleshooting

### "I don't see the Settings tab"
- Make sure you're logged into GitHub
- Make sure you're the owner of the repository
- Try refreshing the page

### "I don't see the Pages option in the left sidebar"
- Scroll down in the left sidebar
- It's usually near the bottom, after "Secrets and variables"
- Make sure your repository is public (Pages doesn't work on private repos with free accounts)

### "The Branch dropdown is grayed out"
- Make sure "Deploy from a branch" is selected in the Source dropdown
- Make sure you have committed files to your repository

### "I don't see 'main' in the branch dropdown"
- Your default branch might be called "master" instead
- Select whatever branch name you see (likely "main" or "master")

---

## Alternative: Direct Link

Just click this link (replace with your username if different):
👉 **https://github.com/magg2021/agent-sense-podcast/settings/pages**

This takes you directly to the Pages settings!

---

## What Happens After You Click Save?

1. **Immediate:** GitHub starts building your site
2. **1-2 minutes:** Your site is deployed
3. **Result:** Your site is live at `https://magg2021.github.io/agent-sense-podcast/`

You'll see a green box at the top of the Pages settings with your live URL.

---

## Quick Checklist

- [ ] Go to repository: https://github.com/magg2021/agent-sense-podcast
- [ ] Click "Settings" tab (top menu)
- [ ] Click "Pages" in left sidebar
- [ ] Under "Source", select "Deploy from a branch"
- [ ] Under "Branch", select "main" and "/ (root)"
- [ ] Click "Save"
- [ ] Wait 2-3 minutes
- [ ] Visit your live site!

---

## Still Need Help?

If you're still having trouble finding it, you can:
1. Take a screenshot of what you see
2. Or describe what you see on the Settings page
3. I'll help you navigate to the right place!

The key is: **Settings (top) → Pages (left sidebar) → Branch dropdown (middle of page)**