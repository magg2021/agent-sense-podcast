# Agent Sense Podcast Website - Deployment Guide

## Quick Deployment Options

### Option 1: GitHub Pages (Recommended - Free & Easy)

**Steps:**
1. Create a GitHub account if you don't have one (github.com)
2. Create a new repository named `agent-sense-podcast`
3. Upload only these files to the repository:
   - `index.html`
   - All episode folders (Episode 3, Episode 4, Episode 5, Episode 6, Episode 7) - **cover images only**
   - All image files (agent_sense_cover.png, etc.)
   - **NO audio files** - visitors will click through to Spotify/Apple for analytics
4. Go to repository Settings → Pages
5. Under "Source", select "main" branch
6. Click Save
7. Your site will be live at: `https://yourusername.github.io/agent-sense-podcast/`

**Time to deploy:** 5-10 minutes  
**Cost:** Free  
**Custom domain:** Yes (optional)

---

### Option 2: Netlify (Easy Drag & Drop)

**Steps:**
1. Go to netlify.com and sign up (free)
2. Click "Add new site" → "Deploy manually"
3. Drag and drop your entire project folder
4. Your site goes live instantly!
5. You'll get a URL like: `https://random-name.netlify.app`
6. You can customize the subdomain or add your own domain

**Time to deploy:** 2-3 minutes  
**Cost:** Free  
**Custom domain:** Yes (optional)

---

### Option 3: Vercel (Fast & Professional)

**Steps:**
1. Go to vercel.com and sign up (free)
2. Click "Add New Project"
3. Import from GitHub or upload files directly
4. Click Deploy
5. Your site will be live at: `https://your-project.vercel.app`

**Time to deploy:** 3-5 minutes  
**Cost:** Free  
**Custom domain:** Yes (optional)

---

### Option 4: AWS S3 + CloudFront (Enterprise Option)

**Steps:**
1. Create an AWS account
2. Create an S3 bucket with static website hosting enabled
3. Upload all files to the bucket
4. Set bucket policy for public read access
5. (Optional) Set up CloudFront for CDN and HTTPS
6. (Optional) Configure Route 53 for custom domain

**Time to deploy:** 15-30 minutes  
**Cost:** ~$1-5/month (depending on traffic)  
**Custom domain:** Yes

---

## Recommended: GitHub Pages

**Why GitHub Pages?**
- ✅ Completely free
- ✅ Easy to update (just push changes)
- ✅ Automatic HTTPS
- ✅ Custom domain support
- ✅ Version control included
- ✅ No credit card required

---

## Quick Start with GitHub Pages

### Using GitHub Desktop (Easiest):

1. **Install GitHub Desktop**
   - Download from: desktop.github.com
   - Sign in with your GitHub account

2. **Create Repository**
   - File → New Repository
   - Name: `agent-sense-podcast`
   - Local Path: Choose this folder
   - Click "Create Repository"

3. **Publish to GitHub**
   - Click "Publish repository"
   - Uncheck "Keep this code private" (for free GitHub Pages)
   - Click "Publish repository"

4. **Enable GitHub Pages**
   - Go to github.com and open your repository
   - Click Settings → Pages
   - Source: Deploy from branch "main"
   - Click Save

5. **Your site is live!**
   - URL: `https://yourusername.github.io/agent-sense-podcast/`
   - Updates automatically when you commit changes

---

### Using Command Line (For Developers):

```bash
# Navigate to your project folder
cd "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense"

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Agent Sense Podcast website"

# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/agent-sense-podcast.git

# Push to GitHub
git branch -M main
git push -u origin main

# Enable GitHub Pages in repository settings
```

---

## Custom Domain Setup (Optional)

If you want to use your own domain (e.g., agentsense.com):

1. **Purchase domain** from:
   - Namecheap
   - GoDaddy
   - Google Domains
   - Cloudflare

2. **Configure DNS:**
   - Add CNAME record pointing to: `yourusername.github.io`
   - Or add A records for GitHub Pages IPs

3. **Update GitHub Pages settings:**
   - Go to Settings → Pages
   - Enter your custom domain
   - Enable "Enforce HTTPS"

---

## File Structure for Deployment

Make sure only these files are uploaded (NO AUDIO FILES):

```
agent-sense-podcast/
├── index.html
├── agent_sense_cover.png
├── agent_sense_ep02_cover.png
├── Episode 3/
│   └── Podcast_cover _ep3_2.png
├── Episode 4/
│   └── Podcast_cover_ep4_2.png
├── Episode 5/
│   └── image.png
├── Episode 6/
│   └── Podcast_cover (1).jpg
└── Episode 7/
    └── 11.png
```

**Total: 8 files (images and HTML only)**

**Why no audio files?**
- ✅ Faster upload and smaller repository
- ✅ Better analytics - all plays tracked on Spotify/Apple
- ✅ Visitors click "Listen on Spotify/Apple" buttons
- ✅ You get full analytics from podcast platforms

---

## Updating Your Website

After initial deployment, to update content:

**GitHub Pages:**
1. Edit files locally
2. Commit changes in GitHub Desktop
3. Push to GitHub
4. Site updates automatically in 1-2 minutes

**Netlify/Vercel:**
1. Drag and drop updated files
2. Or connect to GitHub for automatic deployments

---

## Need Help?

- GitHub Pages docs: docs.github.com/pages
- Netlify docs: docs.netlify.com
- Vercel docs: vercel.com/docs

---

## Recommended Next Steps

1. ✅ Deploy to GitHub Pages (free, easy)
2. ✅ Test on mobile devices
3. ✅ Share the URL on LinkedIn
4. ✅ Consider custom domain (optional)
5. ✅ Add Google Analytics (optional)
6. ✅ Submit to podcast directories with website link

Your website is ready to go live! 🚀