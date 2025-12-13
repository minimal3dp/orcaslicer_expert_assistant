# Railway.app Deployment Guide for OrcaSlicer Settings Recommender

**Last Updated:** December 12, 2025  
**Version:** 0.4  
**Platform:** Railway.app  
**Application Type:** Static HTML/JavaScript Single-Page App

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Pre-Deployment Checklist](#pre-deployment-checklist)
3. [Step-by-Step Deployment](#step-by-step-deployment)
4. [Post-Deployment Verification](#post-deployment-verification)
5. [Custom Domain Setup](#custom-domain-setup)
6. [Environment Variables](#environment-variables)
7. [Monitoring & Maintenance](#monitoring--maintenance)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Accounts & Tools
- ✅ Railway.app account (sign up at https://railway.app)
- ✅ GitHub account (for repository connection)
- ✅ Git installed locally (`git --version` to verify)
- ✅ Optional: Railway CLI (`npm install -g @railway/cli` for advanced features)

### Local Repository Setup
Ensure your local repository is clean and up to date:

```bash
# Navigate to project directory
cd /Users/wilsonm/development/m3dp_orcaslicer_settings_recommender

# Verify git status (should be clean)
git status

# Verify main branch is current
git branch -v
git log --oneline -5
```

---

## Pre-Deployment Checklist

Before deploying to Railway.app, complete these verification steps:

### Code Quality
- [ ] All code changes are committed to main branch
- [ ] No uncommitted changes (`git status` shows clean)
- [ ] Latest commits are pushed to GitHub
- [ ] index.html syntax is valid (no console errors locally)

### Application Verification
- [ ] Test locally by opening `index.html` in browser
- [ ] Verify all 28 materials load correctly
- [ ] Test warning system on 3-4 materials
- [ ] Verify feedback form works (should redirect to Formspree)
- [ ] Check Google Analytics tracking (GA4 events fire)
- [ ] Test affiliate links (should open Amazon)

### Configuration Files
- [ ] `index.html` exists and is optimized (3,248+ lines)
- [ ] `data/material_db.csv` exists (29 materials)
- [ ] `data/materials.json` exists
- [ ] `sitemap.xml` exists
- [ ] `robots.txt` exists
- [ ] Footer includes Railway referral link ✅

### Documentation
- [ ] `README.md` is current
- [ ] GitHub repository is public (for Railway connection)
- [ ] `.gitignore` excludes sensitive files

---

## Step-by-Step Deployment

### **Step 1: Prepare GitHub Repository**

#### 1.1 Ensure Latest Code is Pushed
```bash
# Verify main branch
git checkout main

# Pull any remote changes
git pull origin main

# Verify clean status
git status
# Expected output: "On branch main, your branch is up to date with 'origin/main'"
```

#### 1.2 Create a Deployment Tag (Optional but Recommended)
```bash
# Tag this version for reference
git tag -a v0.4-railway -m "Deploy to Railway.app - December 12, 2025"

# Push tag to GitHub
git push origin v0.4-railway
```

#### 1.3 Verify GitHub Visibility
- Navigate to: https://github.com/minimal3dp/orcaslicer_expert_assistant
- Ensure repository is **Public** (not Private)
- If Private, change to Public in GitHub Settings → Visibility

---

### **Step 2: Log in to Railway.app**

#### 2.1 Access Railway Dashboard
1. Go to https://railway.app
2. Click **"Login"** or **"Start Project"**
3. Choose authentication method:
   - GitHub (Recommended - allows direct repo connection)
   - Google
   - Email

#### 2.2 Create New Project
1. Click **"+ New Project"** or **"Start New"**
2. Select **"Deploy from GitHub"** (or "Empty Project" if not connecting repo yet)
3. Authorize Railway.app to access your GitHub account
4. Select the `orcaslicer_expert_assistant` repository

---

### **Step 3: Configure Railway Project**

#### 3.1 Select Deployment Source
1. **Repository:** `minimal3dp/orcaslicer_expert_assistant`
2. **Branch:** `main` (default)
3. **Auto-deploy:** Enable (redeploys on every push to main)

#### 3.2 Configure Build Settings
Since this is a static HTML app, minimal configuration is needed:

1. Click **"Settings"** in Railway dashboard
2. Under **"Build & Deploy":**
   - **Build Command:** (leave blank or use `echo "No build needed"`)
   - **Start Command:** (leave blank - Railway serves static files)
   - **Publish Directory:** `.` (root directory contains index.html)

#### 3.3 Add Root File Configuration
For proper static site serving:

1. Create file: `.railway/nixpacks.toml`
2. Add content:
```toml
[build]
packages = ["nginx"]

[start]
cmd = "nginx -g 'daemon off;' -c /etc/nginx/nginx.conf"
```

**Alternative: Use Nixpacks (Recommended for Static Sites)**

Create `.railway/Procfile`:
```
web: python3 -m http.server 8080
```

Or use Railway's built-in static site detection (no config needed).

---

### **Step 4: Set Environment Variables (If Needed)**

For this application, no sensitive environment variables are required (GA4 ID is public).

However, if you add backend functionality later:

1. Go to **"Variables"** tab in Railway dashboard
2. Add any needed variables:
   - `PAAPI_ACCESS_KEY` (if implementing Amazon PA-API)
   - `PAAPI_SECRET_KEY`
   - `NODE_ENV=production`

For now, skip this step.

---

### **Step 5: Deploy to Railway**

#### 5.1 Automatic Deployment (via GitHub)
1. **Best Practice:** Let Railway auto-deploy from GitHub
2. Every push to `main` branch triggers automatic deployment
3. Monitor deployment status in Railway dashboard

#### 5.2 Manual Deployment (via CLI)
If you prefer manual control:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Link to your project
railway link

# Deploy
railway up

# Check deployment status
railway status
```

#### 5.3 Watch Deployment Progress
1. In Railway dashboard, view **"Recent Deployments"**
2. Click on the latest deployment
3. Monitor logs for errors
4. Expected status: **"✓ Success"** (green checkmark)

---

### **Step 6: Verify Deployment**

#### 6.1 Get Deployment URL
1. In Railway dashboard, click on **"Settings"**
2. Look for **"Domain"** section
3. Railway assigns a temporary domain: `orcaslicer-expert-assistant-prod.up.railway.app` (example)
4. Click the domain to open your deployed app

#### 6.2 Test Application
Open the deployment URL and verify:

- [ ] Page loads without errors
- [ ] All 28 materials appear in dropdown
- [ ] Select a material and verify warning system works
- [ ] Google Analytics tracking fires (check GA4 Realtime)
- [ ] Feedback form loads (test by filling out and submitting)
- [ ] Affiliate links redirect to Amazon
- [ ] Footer shows Railway.app link with referral code
- [ ] Mobile responsiveness works (test on mobile browser or device inspector)

#### 6.3 Check Console for Errors
1. Open browser Developer Tools (F12)
2. Go to **"Console"** tab
3. Should see no red errors
4. May see GA4 tracking logs

---

## Custom Domain Setup

### **Step 7: Connect Custom Domain**

#### 7.1 Connect `settings.minimal3dp.com`

**Prerequisites:**
- Domain must be registered and accessible
- DNS provider access (GoDaddy, Namecheap, etc.)

**Railway Setup:**
1. Go to Railway project **Settings**
2. Click **"Domains"** or **"Custom Domain"**
3. Click **"+ Add Domain"**
4. Enter: `settings.minimal3dp.com`
5. Railway will provide CNAME record to add

#### 7.2 Update DNS Records

**With your domain registrar (e.g., GoDaddy, Namecheap):**
1. Access DNS management panel
2. Add CNAME record:
   - **Name:** `settings`
   - **Type:** `CNAME`
   - **Value:** Railway-provided CNAME (e.g., `cname.railway.app`)
   - **TTL:** 3600 (or default)
3. Save changes
4. Wait 5-30 minutes for DNS propagation

#### 7.3 Verify Domain
```bash
# Check DNS propagation
dig settings.minimal3dp.com CNAME

# Expected output: Should show Railway CNAME
```

1. Visit `https://settings.minimal3dp.com` in browser
2. Should load your app with SSL certificate
3. Verify certificate is valid (green lock icon)

---

## Environment Variables

### For Static Site
No environment variables needed for current deployment.

### For Future Backend Features
If you add Node.js/Python backend later, configure in Railway:

```
PAAPI_ACCESS_KEY=your_key
PAAPI_SECRET_KEY=your_secret
GA4_MEASUREMENT_ID=G-GERCPZ07KR
NODE_ENV=production
```

---

## Monitoring & Maintenance

### **Monitor Deployment**

#### 1. View Deployment Logs
- Dashboard: **"Logs"** tab
- Filter by date/time
- Check for errors or unusual activity

#### 2. Check Uptime
- Railway dashboard shows deployment status
- Green checkmark = healthy deployment
- Red X = deployment issue

#### 3. View Traffic
- Railway provides basic analytics
- Monitor for unusual spikes or errors

### **Update Application**

#### Deploy Updates
```bash
# Make code changes locally
git add .
git commit -m "Update: description"

# Push to GitHub (auto-deploys via Railway)
git push origin main

# Monitor deployment in Railway dashboard
```

#### Zero-Downtime Deployments
Railway automatically handles:
- ✅ Seamless redeployment (no downtime)
- ✅ Automatic rollback if health checks fail
- ✅ Load balancing during deployment

### **Rollback Deployment (If Needed)**

If a deployment breaks the app:

1. In Railway dashboard, go to **"Deployments"**
2. Find the previous working deployment
3. Click **"Redeploy"** on that version
4. App reverts to previous state
5. Investigate issue locally before pushing new fix

---

## Troubleshooting

### **Issue: Deployment Fails**

**Symptom:** Red X on deployment status

**Solution:**
1. Check logs: **"Logs"** tab in Railway
2. Look for error message (e.g., build failure, missing file)
3. Common issues:
   - **Missing `index.html`:** Ensure file exists in root
   - **Build command error:** Leave build command blank for static sites
   - **Wrong directory:** Ensure publish directory is `.`

### **Issue: App Loads Blank Page**

**Symptom:** White screen, no content

**Solution:**
1. Open browser console (F12 → Console tab)
2. Check for JavaScript errors
3. Verify `index.html` syntax locally
4. Check file paths (data/material_db.csv, etc.)
5. Redeploy with `git push origin main`

### **Issue: Materials Not Loading**

**Symptom:** Material dropdown is empty

**Solution:**
1. Verify `data/material_db.csv` exists in repository
2. Check that CSV is not in `.gitignore`
3. Verify CSV syntax (proper comma-separated format)
4. Redeploy: `git push origin main`

### **Issue: Google Analytics Not Tracking**

**Symptom:** No events in GA4 Realtime

**Solution:**
1. Verify GA4 measurement ID: `G-GERCPZ07KR`
2. Check browser console for GA4 errors
3. Wait 5-10 minutes (real-time lag)
4. Ensure you're not blocking analytics (browser extensions)

### **Issue: Feedback Form Not Working**

**Symptom:** Form doesn't submit or shows error

**Solution:**
1. Verify Formspree action: `action="https://formsubmit.co/minimal3dp@gmail.com"`
2. Check that form method is POST
3. Test locally first
4. Check spam/junk email for submissions
5. Verify Formspree account status at https://formsubmit.co

### **Issue: Custom Domain Not Working**

**Symptom:** Custom domain shows error or doesn't connect

**Solution:**
1. Verify DNS record was created correctly
2. Wait for DNS propagation (up to 48 hours, usually 5-30 min)
3. Check CNAME record: `dig settings.minimal3dp.com CNAME`
4. Verify domain is properly configured in Railway
5. Check SSL certificate (Railway auto-provides)

### **Issue: Affiliate Links Not Working**

**Symptom:** Amazon links return 404 or wrong product

**Solution:**
1. Verify ASINs in `data/material_db.csv`
2. Check that affiliate tag `mwf064-20` is in URLs
3. Test ASIN format: `https://amazon.com/dp/ASIN?tag=mwf064-20`
4. Verify affiliate account is still active

---

## Performance Optimization (Optional)

### Enable Caching
Railway automatically caches static assets. For additional optimization:

#### Add Cache Headers
Create `.railway/cache.headers` (if using Nginx):
```
# Cache static assets for 30 days
/*.js: max-age=2592000
/*.css: max-age=2592000
/*.png: max-age=2592000
/*.jpg: max-age=2592000

# Don't cache HTML (for updates)
/index.html: max-age=3600
```

#### Use CDN (Optional)
1. Cloudflare free tier for CDN
2. Add CNAME: `settings.minimal3dp.com`
3. Point to Railway domain
4. Caches assets globally

---

## Security Best Practices

### HTTPS/SSL
- ✅ Railway auto-enables HTTPS for custom domains
- ✅ Free SSL certificate (Let's Encrypt)
- ✅ Auto-renewal handled by Railway

### Secrets Management
- ✅ Never commit API keys to GitHub
- ✅ Use Railway **Variables** for sensitive data
- ✅ Current app has no secrets (GA4 ID is public)

### Repository Security
- ✅ `.gitignore` excludes sensitive files
- ✅ GitHub repo remains public (for Railway)
- ✅ No private data in public repository

---

## FAQ

### Q: How much does Railway cost?
**A:** Free tier includes:
- ✅ 5GB storage
- ✅ 100GB bandwidth/month
- ✅ Unlimited deployments
- Paid tier ($5/month) for additional resources

Your static site easily fits free tier.

### Q: Can I still use Vercel?
**A:** Yes, you can:
- Keep Vercel deployed (or remove it)
- Both platforms work fine
- Railway is now primary deployment
- Update DNS to point to Railway

### Q: How do I rollback a deployment?
**A:** In Railway dashboard → **Deployments** → Click older deployment → **Redeploy**

### Q: What if GitHub goes down?
**A:** Railway maintains your deployed app even if GitHub is down. Deployments are stored on Railway servers.

### Q: Can I add a backend later?
**A:** Yes! Railway supports:
- Node.js (Express)
- Python (Flask, Django)
- Database (PostgreSQL, MongoDB)
- Just add code and Railway auto-detects

---

## Next Steps After Deployment

1. **Update DNS:** Point `settings.minimal3dp.com` to Railway
2. **Update Social Links:** Update YouTube channel description with new URL
3. **Test Everything:** Verify all functionality works
4. **Monitor Analytics:** Track traffic in GA4
5. **Gather Feedback:** Use feedback form to collect user insights
6. **Plan Phase 5:** Integrate elongation data into material_db.csv

---

## Quick Reference

| Task | Command/Link |
|------|---|
| Railway Dashboard | https://railway.app/dashboard |
| GitHub Repository | https://github.com/minimal3dp/orcaslicer_expert_assistant |
| Production URL (Railway) | `https://orcaslicer-expert-assistant-prod.up.railway.app` |
| Custom Domain | `https://settings.minimal3dp.com` |
| GA4 Dashboard | https://analytics.google.com/analytics/web/#/p/[ID]/reports/dashboard |
| GitHub Issues | https://github.com/minimal3dp/orcaslicer_expert_assistant/issues |
| Feedback Form | minimal3dp@gmail.com |

---

## Support

### Issues During Deployment?
1. Check Railway docs: https://docs.railway.app
2. Review troubleshooting section above
3. Check GitHub issues: https://github.com/minimal3dp/orcaslicer_expert_assistant/issues
4. Contact Railway support in dashboard

### Questions About the App?
1. Review `README.md` in repository
2. Check `dev_docs/` folder for detailed guides
3. File GitHub issue for bugs or feature requests

---

**Deployment Guide Version:** 1.0  
**Last Updated:** December 12, 2025  
**Maintained By:** minimal3dp  
**Status:** Ready for Production
