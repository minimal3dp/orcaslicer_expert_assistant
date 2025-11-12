# Vercel Deployment Guide - OrcaSlicer Expert Assistant

**Last Updated:** November 12, 2025  
**Deployment Target:** Vercel Hobby (Free Tier)  
**Estimated Time:** 15-30 minutes  
**Domain Strategy:** Subdomain deployment on existing root domain

---

## ⚡ Quick Start (Your Specific Setup)

**Your Configuration:**
- **Root Domain:** `minimal3dp.com` (owned)
- **Subdomain for this app:** `orcaslicer.minimal3dp.com` (recommended)
- **Alternative names:** `assistant.minimal3dp.com` or `settings.minimal3dp.com`
- **Deployment:** Vercel (free tier)
- **DNS Setup:** CNAME record only (simple!)
- **YouTube Channel:** youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw
- **Target Keyword:** "best slicer settings for 3d printing" (from YouTube Analytics Trends)

**SEO Strategy:** ✅ Already Optimized!
- ✅ Title tag optimized for target keyword
- ✅ Meta descriptions with material keywords
- ✅ Schema.org structured data (WebApplication)
- ✅ Open Graph tags for social sharing
- ✅ YouTube channel link in header
- ⏳ Pending: OG image, sitemap.xml, robots.txt

**Why Subdomains? ✅ Highly Recommended**
- ✅ One domain → unlimited apps (free subdomains)
- ✅ Shared brand identity (`minimal3dp.com`)
- ✅ Easy cross-linking between apps
- ✅ SEO boost for root domain
- ✅ Professional appearance
- ✅ Independent deployments per app

**Multi-App Portfolio Example:**
```
minimal3dp.com                     → Main site/landing page
├── orcaslicer.minimal3dp.com     → This app (OrcaSlicer Assistant)
├── filament.minimal3dp.com       → Future: Filament database
├── calc.minimal3dp.com           → Future: Print calculator
└── docs.minimal3dp.com           → Future: Documentation
```

**Jump to Your Section:**
- [Part 1: Deploy to Vercel](#-part-1-initial-deployment-static-html) (15 min)
- [Part 2: Configure Subdomain](#-part-2-set-up-custom-domain-recommended-for-production) (10 min)
- [Part 2B: Link from Main Site](#-part-2b-linking-from-your-main-site) (strategy)
- [Part 2C: Multi-App Architecture](#-part-2c-multi-app-architecture-best-practices) (best practices)
- [Part 3: Google Analytics Setup](#-part-3-set-up-google-analytics-4-revenue-tracking) (15 min)
- [Part 4: SEO Setup](#-part-4-seo-optimization-get-found-on-google) (30 min) **NEW!**
- [Part 5: YouTube Integration](#-part-5-youtube-integration-drive-traffic-from-videos) (15 min) **NEW!**

---

## 📋 Prerequisites

Before you begin, ensure you have:

- [ ] A GitHub account with this repository pushed
- [ ] A Vercel account (sign up at https://vercel.com - free)
- [ ] Git installed locally
- [ ] Amazon Associates affiliate tag (`mwf064-20` is already configured in the HTML)

---

## 🚀 Part 1: Initial Deployment (Static HTML)

### Step 1: Connect GitHub to Vercel

1. **Log in to Vercel:**
   - Go to https://vercel.com
   - Click "Continue with GitHub"
   - Authorize Vercel to access your GitHub account

2. **Import Your Repository:**
   - Click "Add New..." → "Project"
   - Find `orcaslicer_expert_assistant` repository
   - Click "Import"

### Step 2: Configure Project Settings

**Project Name:** `orcaslicer-expert-assistant` (or your preferred name)

**Framework Preset:** Select "Other" (static HTML)

**Root Directory:** `./` (leave as default)

**Build Settings:**
- **Build Command:** Leave empty (static site, no build needed)
- **Output Directory:** `./` (leave as default)
- **Install Command:** Leave empty

**Environment Variables:** None needed for initial deployment

### Step 3: Deploy!

1. Click "Deploy"
2. Wait 30-60 seconds for deployment to complete
3. Click "Visit" to see your live site!

**Your site will be live at:**
```
https://orcaslicer-expert-assistant-<random>.vercel.app
```

✅ **Congratulations!** Your static HTML application is now live and generating revenue potential.

---

## 🎯 Part 2: Set Up Custom Domain (Recommended for Production)

### Why Use a Custom Domain?
- Professional appearance
- Better SEO
- Easier to remember and share
- Builds brand trust
- Consistent branding across multiple apps

### Multi-App Subdomain Strategy (RECOMMENDED)

**If you own a root domain like `minimal3dp.com`:**

✅ **Use subdomains for each app** (Highly Recommended)

**Benefits:**
1. **Shared Brand Identity:** All apps under `minimal3dp.com` reinforce your brand
2. **SEO Boost:** Subdomains contribute to root domain authority
3. **Easy Cross-Linking:** Link between apps naturally
4. **Cost Effective:** One domain, unlimited subdomains (free)
5. **Flexible Deployment:** Each app is independent but connected
6. **Professional Appearance:** Shows you have a portfolio of tools

**Recommended Subdomain Structure:**
```
minimal3dp.com                    → Main marketing site (landing page)
├── orcaslicer.minimal3dp.com    → OrcaSlicer Expert Assistant (this app)
├── filament.minimal3dp.com      → Filament calculator/database (future)
├── slicer.minimal3dp.com        → Slicer comparison tool (future)
├── bed.minimal3dp.com           → Bed leveling assistant (future)
└── docs.minimal3dp.com          → Documentation hub (future)
```

**Alternative Naming (Shorter URLs):**
```
minimal3dp.com                    → Main site
├── assistant.minimal3dp.com     → OrcaSlicer Expert Assistant
├── calc.minimal3dp.com          → Calculators/tools
├── compare.minimal3dp.com       → Comparison tools
└── guides.minimal3dp.com        → Guides and tutorials
```

**Why NOT to use separate root domains:**
- ❌ Higher cost ($10-15/year per domain)
- ❌ Split SEO authority (dilutes your ranking)
- ❌ Harder to maintain branding consistency
- ❌ More DNS management overhead
- ❌ Confuses users with multiple brand identities

### Step 1: Choose Your Subdomain

**For this app, we recommend:**
- `orcaslicer.minimal3dp.com` (clear, descriptive)
- `assistant.minimal3dp.com` (shorter, easier to type)
- `settings.minimal3dp.com` (keyword-focused for SEO)

**Pick one and stick with it!** For this guide, we'll use `orcaslicer.minimal3dp.com`

### Step 2: Add Subdomain to Vercel

### Step 2: Add Subdomain to Vercel

1. In Vercel dashboard, go to your project (`orcaslicer-expert-assistant`)
2. Click "Settings" → "Domains"
3. Enter your subdomain: `orcaslicer.minimal3dp.com`
4. Click "Add"

**Vercel will show you the DNS configuration needed.**

### Step 3: Configure DNS at Your Domain Registrar

**For subdomains, you only need a CNAME record** (much simpler than root domains!)

#### Option A: CNAME Record Method (RECOMMENDED for Subdomains)

Go to your domain registrar (where you purchased `minimal3dp.com`) and add:

```
Type:   CNAME
Name:   orcaslicer (or full: orcaslicer.minimal3dp.com)
Value:  cname.vercel-dns.com.
TTL:    3600 (or "Automatic")
```

**Common Registrars:**

**Namecheap:**
1. Log in → Domain List → Manage
2. Advanced DNS → Add New Record
3. Type: CNAME, Host: `orcaslicer`, Value: `cname.vercel-dns.com`, TTL: Automatic
4. Save

**Cloudflare:**
1. Log in → Select `minimal3dp.com`
2. DNS → Add Record
3. Type: CNAME, Name: `orcaslicer`, Target: `cname.vercel-dns.com`, Proxy: Off (DNS only)
4. Save

**Google Domains:**
1. Log in → My Domains → Manage
2. DNS → Custom Records
3. Host: `orcaslicer`, Type: CNAME, Data: `cname.vercel-dns.com`, TTL: 1H
4. Save

**GoDaddy:**
1. Log in → My Products → DNS
2. Add → Type: CNAME, Name: `orcaslicer`, Value: `cname.vercel-dns.com`, TTL: 1 Hour
3. Save

**Important Notes:**
- ✅ For the "Name" field, use just `orcaslicer` (not the full subdomain)
- ✅ Some registrars auto-append `.minimal3dp.com` to the name
- ✅ Make sure to include the trailing dot: `cname.vercel-dns.com.` (some require it)
- ✅ DNS propagation typically takes 5-15 minutes for CNAME records (much faster than A records!)

#### Option B: Vercel Nameservers (Alternative - For Root Domain Management)

**Only use this if you want Vercel to manage ALL DNS for `minimal3dp.com`**

⚠️ **Not recommended if you have other services on `minimal3dp.com`** (email, other subdomains, etc.)

If you choose this route:
1. Vercel will show you nameservers: `ns1.vercel-dns.com`, `ns2.vercel-dns.com`
2. Go to your registrar and replace ALL nameservers with Vercel's
3. Wait 24-48 hours for propagation

**We recommend Option A (CNAME) for subdomains** - it's simpler and doesn't affect your main domain.

### Step 4: Verify DNS Configuration

**Check DNS Propagation:**
1. Visit https://www.whatsmydns.net/
2. Enter: `orcaslicer.minimal3dp.com`
3. Select "CNAME" from dropdown
4. Should show: `cname.vercel-dns.com`
5. Green checkmarks = propagated globally

**Typical propagation times:**
- 5-15 minutes: Most locations see the change
- 1-2 hours: Global propagation complete
- 24-48 hours: Maximum (rare for CNAME records)

### Step 5: Verify HTTPS

Once DNS is configured:
1. Vercel automatically provisions SSL certificate (5-10 minutes)
2. Visit `https://orcaslicer.minimal3dp.com`
3. Verify padlock icon in browser
4. Certificate is auto-renewed every 90 days (no action needed)

✅ **Custom subdomain configured!** Your app is now live at `orcaslicer.minimal3dp.com`

---

## 🔗 Part 2B: Linking from Your Main Site

### Create a Portfolio/App Directory on minimal3dp.com

**Recommended Structure for Your Main Site:**

```html
<!-- On minimal3dp.com - Tools/Apps Section -->
<section class="tools-portfolio">
  <h2>3D Printing Tools & Calculators</h2>
  
  <div class="tool-grid">
    <!-- OrcaSlicer Assistant -->
    <a href="https://orcaslicer.minimal3dp.com" class="tool-card">
      <h3>🎯 OrcaSlicer Expert Assistant</h3>
      <p>Get intelligent slicer settings recommendations based on material and print goals</p>
      <span class="badge">Free Tool</span>
    </a>
    
    <!-- Future App Placeholders -->
    <a href="https://filament.minimal3dp.com" class="tool-card coming-soon">
      <h3>📊 Filament Database</h3>
      <p>Comprehensive database of 100+ filament specifications</p>
      <span class="badge">Coming Soon</span>
    </a>
    
    <a href="https://calc.minimal3dp.com" class="tool-card coming-soon">
      <h3>🧮 Print Calculator</h3>
      <p>Calculate print time, material cost, and weight</p>
      <span class="badge">Coming Soon</span>
    </a>
  </div>
</section>
```

### SEO Benefits of Cross-Linking

**1. Add Navigation Bar on All Apps:**
```html
<!-- Add to orcaslicer.minimal3dp.com header -->
<nav class="main-nav">
  <a href="https://minimal3dp.com">← Back to minimal3dp</a>
  <a href="https://minimal3dp.com/tools">All Tools</a>
</nav>
```

**2. Add Footer Links:**
```html
<footer>
  <div class="footer-links">
    <div>
      <h4>minimal3dp Tools</h4>
      <ul>
        <li><a href="https://orcaslicer.minimal3dp.com">OrcaSlicer Assistant</a></li>
        <li><a href="https://filament.minimal3dp.com">Filament Database</a></li>
        <li><a href="https://minimal3dp.com">Main Site</a></li>
      </ul>
    </div>
  </div>
</footer>
```

**3. Add Canonical Tags (Important for SEO):**
```html
<!-- In <head> of orcaslicer.minimal3dp.com -->
<link rel="canonical" href="https://orcaslicer.minimal3dp.com">

<!-- Also add -->
<meta name="description" content="Free OrcaSlicer settings recommendations for 28 materials. Expert guidance on strength, speed, quality, and accuracy.">
<meta name="keywords" content="orcaslicer, 3d printing, slicer settings, bambu lab, filament settings">
```

### Analytics - Track Cross-Site Traffic

**In Google Analytics 4, set up Cross-Domain Tracking:**

```javascript
// In both minimal3dp.com AND orcaslicer.minimal3dp.com
gtag('config', 'G-XXXXXXXXXX', {
  'linker': {
    'domains': ['minimal3dp.com', 'orcaslicer.minimal3dp.com']
  }
});
```

This ensures you can track:
- Users coming from main site → subdomain
- User journey across your app portfolio
- Which apps drive the most engagement

### Marketing Strategy

**1. Main Site (minimal3dp.com) as Hub:**
- Showcase all your tools
- About page explaining your mission
- Blog posts driving traffic to tools
- Newsletter signup

**2. Each Subdomain as Specialized Tool:**
- Deep functionality
- Tool-specific landing page
- Call-to-action to other tools
- Links back to main site

**3. Social Media Strategy:**
- Share main site in bio: `minimal3dp.com`
- Share specific tools in posts: `orcaslicer.minimal3dp.com`
- Builds recognition for your brand

**Example Twitter Bio:**
```
3D Printing Tools & Guides
🔧 Free calculators & assistants
🎯 orcaslicer.minimal3dp.com
🌐 minimal3dp.com
```

---

## 🏗️ Part 2C: Multi-App Architecture Best Practices

### Subdomain Strategy: One App = One Subdomain ✅

**Why This Works:**

1. **Independent Deployment:**
   - Each app has its own Vercel project
   - Deploy/update apps without affecting others
   - Different frameworks per app (HTML, Next.js, Python, etc.)
   - Isolated environments and configs

2. **Scalability:**
   - Add new apps easily (just add CNAME record)
   - No limit on number of subdomains (Vercel free tier supports unlimited)
   - Each app can have different resource requirements

3. **Clear Separation of Concerns:**
   - OrcaSlicer Assistant: `orcaslicer.minimal3dp.com`
   - Filament Database: `filament.minimal3dp.com`
   - Print Calculator: `calc.minimal3dp.com`
   - Each app is focused and maintainable

4. **SEO Benefits:**
   - Each subdomain can rank independently
   - Specific keywords per subdomain
   - All subdomains boost `minimal3dp.com` authority

5. **Analytics:**
   - Track each app separately
   - Compare performance across apps
   - Identify which tools drive most engagement

### Vercel Project Organization

**Recommended Setup:**

```
Your Vercel Account
├── orcaslicer-expert-assistant      → orcaslicer.minimal3dp.com
├── filament-database                → filament.minimal3dp.com
├── print-calculator                 → calc.minimal3dp.com
├── minimal3dp-main                  → minimal3dp.com (root domain)
└── minimal3dp-docs                  → docs.minimal3dp.com
```

**Each Project Gets:**
- Own GitHub repository (or monorepo with separate folders)
- Own environment variables
- Own deployment pipeline
- Own domain configuration

### Shared Components Across Apps

**Option 1: Shared UI Library (Recommended for Consistency)**
```
GitHub: minimal3dp/ui-components
├── components/
│   ├── Header.js        → Consistent header across all apps
│   ├── Footer.js        → Consistent footer
│   ├── Navigation.js    → Cross-app navigation
│   └── Analytics.js     → Shared GA4 setup
├── styles/
│   └── theme.css        → Shared Tailwind config
└── package.json
```

Install in each app:
```bash
npm install @minimal3dp/ui-components
```

**Option 2: Copy-Paste Approach (Simpler for Now)**
- Copy header/footer HTML across apps
- Maintain consistency manually
- Good for early stage (2-3 apps)
- Migrate to shared library later (5+ apps)

### DNS Management Tips

**Keep a DNS Record Spreadsheet:**
```
Subdomain              | Type  | Value                | App
-----------------------|-------|----------------------|------------------
orcaslicer             | CNAME | cname.vercel-dns.com | OrcaSlicer Assistant
filament               | CNAME | cname.vercel-dns.com | Filament Database
calc                   | CNAME | cname.vercel-dns.com | Print Calculator
docs                   | CNAME | cname.vercel-dns.com | Documentation
@                      | A     | <IP>                 | Main Site
www                    | CNAME | cname.vercel-dns.com | Main Site (www)
```

**Why This Matters:**
- Easy to see all your subdomains at a glance
- Documentation for future you
- Helps debug DNS issues
- Onboarding new team members

### Root Domain (minimal3dp.com) Options

**Option A: Main Site on Vercel** (Recommended)
- Deploy your marketing/portfolio site to Vercel
- Configure as root domain: `minimal3dp.com`
- Consistent deployment pipeline for all apps
- Free Vercel hosting

**Option B: Main Site Elsewhere** (Traditional Hosting)
- Host main site on traditional hosting (Bluehost, SiteGround, etc.)
- Subdomains point to Vercel
- Good if you already have hosting
- Mixed deployment pipeline

**Option C: Main Site as Simple Redirect**
- `minimal3dp.com` → redirects to primary tool
- Simplest approach for single-focus brand
- Example: `minimal3dp.com` → `orcaslicer.minimal3dp.com`

### Future-Proofing Your Architecture

**When You Hit 5+ Apps:**
1. Consider a monorepo structure (Turborepo, Nx)
2. Implement shared component library
3. Unified CI/CD pipeline
4. Centralized analytics dashboard

**When You Need API Backend:**
1. Create `api.minimal3dp.com` subdomain
2. Shared API for all apps (Phase 11-14 PA-API work)
3. Centralized authentication if needed
4. Shared database access

**Example Future Architecture:**
```
minimal3dp.com              → Main marketing site
api.minimal3dp.com          → Shared API backend
auth.minimal3dp.com         → Authentication service
├── orcaslicer.minimal3dp.com
├── filament.minimal3dp.com
├── calc.minimal3dp.com
├── compare.minimal3dp.com
└── guides.minimal3dp.com
```

---

## 📊 Part 3: Set Up Google Analytics 4 (Revenue Tracking)

### Step 1: Create Google Analytics Account

1. Go to https://analytics.google.com
2. Click "Start measuring"
3. Create account: "OrcaSlicer Assistant"
4. Create property: "OrcaSlicer Expert Assistant"
5. Select industry: "Internet & Telecom" or "Technology"
6. Configure business size and objectives

### Step 2: Get Measurement ID

1. In GA4, go to "Admin" (bottom left)
2. Under "Property", click "Data Streams"
3. Click "Add stream" → "Web"
4. Enter your website URL (Vercel URL or custom domain)
5. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 3: Add GA4 to Your HTML

Edit `orcaslicer_assistant.html` and add this in the `<head>` section (after line 48):

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

### Step 4: Track Affiliate Link Clicks

Add this JavaScript function before the closing `</script>` tag in your HTML (around line 2190):

```javascript
// Track affiliate link clicks
document.addEventListener('click', function(e) {
    if (e.target.closest('a[rel*="sponsored"]')) {
        const link = e.target.closest('a');
        const productName = link.getAttribute('data-product-name') || 'Unknown Product';
        const materialKey = link.getAttribute('data-material') || 'Unknown Material';
        
        gtag('event', 'affiliate_click', {
            'event_category': 'Affiliate',
            'event_label': `${materialKey} - ${productName}`,
            'value': 1
        });
    }
});
```

Also update the `createAffiliateProductCard()` function to add tracking attributes (around line 2075):

```javascript
// Add data attributes for tracking
<a href="${amazonLink}" 
   target="_blank" 
   rel="noopener noreferrer sponsored"
   data-product-name="${product.name}"
   data-material="${materialKey}"
   class="inline-flex items-center...">
```

### Step 5: Track Material Selections

Add this code in the material selection event listener (around line 1725):

```javascript
materialSelect.addEventListener('change', (e) => {
    const materialKey = e.target.value;
    if (materialKey && materialsData[materialKey]) {
        displayMaterialWarnings(materialKey);
        displayAffiliateLinks(materialKey);
        
        // Track material selection
        gtag('event', 'material_selected', {
            'event_category': 'Material',
            'event_label': materialKey,
            'value': 1
        });
    } else {
        hideMaterialWarnings();
        hideAffiliateLinks();
    }
});
```

### Step 6: Deploy Updated Code

```bash
git add orcaslicer_assistant.html
git commit -m "Add Google Analytics 4 tracking"
git push origin amazon
```

Vercel will automatically redeploy (takes ~30 seconds).

### Step 7: Verify Tracking Works

1. Go to GA4 → Reports → Realtime
2. Visit your website
3. Select a material and click an affiliate link
4. Confirm events appear in GA4 Realtime dashboard

✅ **Analytics configured!** You can now track user behavior and affiliate performance.

---

## � Part 4: SEO Optimization (Get Found on Google)

**Goal:** Rank for "best slicer settings for 3d printing" and drive organic traffic

### Step 1: Verify SEO Meta Tags (Already Done ✅)

Your HTML has been optimized with:
- ✅ **Title tag:** "Best Slicer Settings for 3D Printing - OrcaSlicer Expert Assistant"
- ✅ **Meta description:** Keyword-rich description with 28 materials listed
- ✅ **Schema.org structured data:** WebApplication with keywords
- ✅ **Open Graph tags:** Social sharing optimization
- ✅ **H1 heading:** "Best Slicer Settings for 3D Printing"
- ✅ **YouTube link:** Prominent in header for cross-promotion

**No action needed** - These are already in your HTML!

### Step 2: Create OG Image for Social Sharing (30 min)

**Why This Matters:**
When someone shares your link on Facebook, Twitter, LinkedIn, or Discord, a preview image will appear. This increases click-through rates by 30-40%.

**Specifications:**
- **Dimensions:** 1200x630 pixels
- **Format:** PNG (preferred) or JPG
- **File Size:** <300KB (ideally <200KB)
- **File Name:** `og-image.png`

**Design Content:**
```
Headline: "Best Slicer Settings for 3D Printing"
Subheadline: "Free Expert Tool - 28 Materials"
Visual: Screenshot of your app or 3D printing imagery
Branding: "minimal3dp" logo (if you have one)
Call-to-action: "orcaslicer.minimal3dp.com"
```

**Tools to Create:**
1. **Canva** (Easiest - Free)
   - Go to canva.com
   - Search for "Facebook Post" template (1200x630)
   - Use "3D Printing" or "Technology" theme
   - Add your text and branding
   - Download as PNG

2. **Figma** (More Control - Free)
   - Create 1200x630 frame
   - Design from scratch
   - Export as PNG

3. **Use AI Image Generator** (Quick)
   - Prompt: "Professional banner image for '3D printing slicer settings tool', technology theme, blue gradient, modern minimalist design"
   - Add text overlay in Canva

**Where to Save:**
- Save as `/og-image.png` in your project root
- Vercel will serve it at `https://orcaslicer.minimal3dp.com/og-image.png`
- Your HTML already references this file (meta tags updated)

**Deploy:**
```bash
git add og-image.png
git commit -m "Add OG image for social sharing"
git push origin amazon
```

### Step 3: Create Sitemap.xml (10 min)

**Why This Matters:**
A sitemap tells Google about all the pages on your site, helping them index faster.

**Create `sitemap.xml` in project root:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://orcaslicer.minimal3dp.com/</loc>
    <lastmod>2025-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- Add more URLs here when you create material pages -->
  <!--
  <url>
    <loc>https://orcaslicer.minimal3dp.com/materials/pla</loc>
    <lastmod>2025-11-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  -->
</urlset>
```

**Deploy:**
```bash
git add sitemap.xml
git commit -m "Add sitemap.xml for SEO"
git push origin amazon
```

### Step 4: Create Robots.txt (5 min)

**Why This Matters:**
Tells search engines what they can and cannot crawl.

**Create `robots.txt` in project root:**
```
User-agent: *
Allow: /

Sitemap: https://orcaslicer.minimal3dp.com/sitemap.xml
```

**Deploy:**
```bash
git add robots.txt
git commit -m "Add robots.txt for search engines"
git push origin amazon
```

### Step 5: Submit to Google Search Console (15 min)

**Why This Matters:**
This is THE tool for tracking your SEO performance. You'll see:
- How many people search for your keywords
- How many click through to your site
- What position you rank for each keyword
- Any indexing issues

**Setup Steps:**
1. Go to https://search.google.com/search-console
2. Click "Add Property"
3. Choose "URL prefix" (not "Domain")
4. Enter: `https://orcaslicer.minimal3dp.com`
5. Verify ownership using one of these methods:
   - **HTML file upload** (easiest for Vercel):
     - Download verification file (`google123abc.html`)
     - Add to project root
     - Deploy to Vercel
     - Click "Verify" in Search Console
   - **Meta tag** (also easy):
     - Copy meta tag from Search Console
     - Add to `<head>` in HTML
     - Deploy to Vercel
     - Click "Verify"
6. Once verified, submit your sitemap:
   - Go to "Sitemaps" in left menu
   - Enter: `sitemap.xml`
   - Click "Submit"

**What to Monitor (Weekly):**
- **Performance Tab:**
  - Total clicks (goal: growing each week)
  - Total impressions (how many times you appear in search)
  - Average CTR (goal: 5%+)
  - Average position (goal: top 10, then top 3)
- **Top Queries:**
  - Are you ranking for "best slicer settings for 3d printing"?
  - What other keywords are working?
- **Pages:**
  - Which pages get the most traffic?
  - Are there any indexing errors?

### Step 6: Add FAQ Section to HTML (30 min)

**Why This Matters:**
FAQ sections help you rank for question-based queries like "what are the best slicer settings for 3d printing?" and can appear as featured snippets in Google.

**Add this section before the closing `</main>` tag in your HTML (around line 2100):**

```html
<!-- FAQ Section for SEO -->
<section class="mt-8 bg-gray-800 rounded-lg p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-200">Frequently Asked Questions</h2>
    
    <div class="space-y-4">
        <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-2">What are the best slicer settings for 3D printing?</h3>
            <p class="text-gray-300">The best slicer settings depend on your material and print goals. For PLA, use 200-220°C hotend, 20-40mm/s speed, 20% infill. For PETG, use 230-250°C, slower speeds, and higher bed temperature. Use our tool above to get personalized recommendations for 28 materials.</p>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-2">What are the best OrcaSlicer settings for PLA?</h3>
            <p class="text-gray-300">For PLA in OrcaSlicer: 210°C hotend, 60°C bed, 50-60mm/s speed, 20% infill, 0.2mm layer height. Adjust based on your printer and priorities (strength, speed, quality). Our tool provides optimized recommendations.</p>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-2">How do I optimize 3D print strength?</h3>
            <p class="text-gray-300">To maximize strength: increase wall thickness (3-4 perimeters), use 40%+ infill, slow print speed to 30-40mm/s, increase temperature slightly, and consider engineering materials like Nylon or carbon fiber composites.</p>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-2">What materials does this tool support?</h3>
            <p class="text-gray-300">We support 28 materials including PLA, PETG, ABS, ASA, Nylon, TPU, PC, PEEK, PEKK, and more. Each material includes temperature recommendations, speed settings, and special requirements (enclosure, hardened nozzle, etc.).</p>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold text-blue-400 mb-2">Is this tool free to use?</h3>
            <p class="text-gray-300">Yes! This tool is completely free. We earn a small commission if you purchase recommended products through our Amazon affiliate links, which helps us keep the tool free and updated.</p>
        </div>
    </div>
</section>
```

**Deploy:**
```bash
git add orcaslicer_assistant.html
git commit -m "Add FAQ section for SEO"
git push origin amazon
```

**Expected Results:**
- ✅ Better rankings for question-based queries
- ✅ Potential featured snippets in Google
- ✅ Improved user experience (answers common questions)

---

## 📺 Part 5: YouTube Integration (Drive Traffic from Videos)

**Goal:** Leverage your YouTube channel to drive traffic and build SEO authority

### Step 1: Update YouTube Channel Description (5 min)

**Current Channel:** youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw

**New Channel Description:**
```
Free 3D printing tools and guides! 

�🔧 BEST SLICER SETTINGS TOOL (FREE): https://orcaslicer.minimal3dp.com
Get personalized settings for 28 materials (PLA, PETG, ABS, Nylon, PEEK, and more)

🌐 Main Site: https://minimal3dp.com

Subscribe for:
• Slicer settings guides
• Material reviews & comparisons
• 3D printing tips & tricks
• Project walkthroughs
• Troubleshooting help

New video every week!
```

**Where to Update:**
1. Go to YouTube Studio
2. Customization → Basic Info
3. Paste new description
4. Click "Publish"

### Step 2: Update YouTube Channel Banner (10 min)

**Add Text to Banner:**
- "Free Tool: orcaslicer.minimal3dp.com"
- "Best Slicer Settings for 3D Printing"

**Banner Specifications:**
- **Dimensions:** 2560x1440 pixels
- **Safe area (always visible):** 1546x423 pixels (center)
- **Format:** JPG or PNG

**Quick Option:**
Use Canva's "YouTube Channel Art" template and add your text overlay.

### Step 3: Add Custom Links to Channel (5 min)

**In YouTube Studio:**
1. Go to Customization → Basic Info
2. Scroll to "Links"
3. Add these custom links:
   - **Title:** "Free Settings Tool"
     **URL:** https://orcaslicer.minimal3dp.com
   - **Title:** "Main Site"
     **URL:** https://minimal3dp.com

**These links appear:**
- On your channel banner
- In your About page
- Hover over your channel name

### Step 4: Update Video Descriptions (30 min)

**Add this section to ALL your video descriptions:**

```
━━━━━━━━━━━━━━━━━━━━━
🔧 FREE TOOL: BEST SLICER SETTINGS
━━━━━━━━━━━━━━━━━━━━━

Get personalized OrcaSlicer settings for 28 materials:
👉 https://orcaslicer.minimal3dp.com

Optimize for:
✅ Strength
✅ Speed
✅ Quality
✅ Accuracy

Perfect for PLA, PETG, ABS, Nylon, Carbon Fiber, PEEK, and more!

━━━━━━━━━━━━━━━━━━━━━
```

**Place this:**
- At the top of the description (after your intro)
- OR in a "Resources" section
- Make it prominent and easy to find

### Step 5: Pin Comments on Popular Videos (10 min)

**For each video with 1000+ views:**

**Pin this comment:**
```
📌 BEST SLICER SETTINGS TOOL (FREE)

Want to know the PERFECT settings for your material?
👉 https://orcaslicer.minimal3dp.com

28 materials | Expert recommendations | Optimized for your goals

Whether you're printing PLA, PETG, ABS, Nylon, or high-temp materials like PEEK, this free tool gives you personalized settings in seconds!
```

**Why Pin Comments?**
- They stay at the top (even with 1000+ comments)
- Mobile users see them immediately
- Increases click-through rate by 20-30%

### Step 6: Plan Companion Video (Long-Term)

**Video Idea:** "Best Slicer Settings for 3D Printing - Complete Guide 2025"

**Script Outline:**
- **Hook (0-15s):** "Struggling with slicer settings? Here's the BEST settings for any material."
- **Problem (15s-1min):** Common issues (warping, stringing, weak prints)
- **Solution (1-2min):** Show your tool in action
- **Material Examples (2-8min):** PLA, PETG, ABS, Nylon settings
- **Optimization Goals (8-10min):** Strength vs Speed vs Quality
- **CTA (10min):** "Use the free tool at orcaslicer.minimal3dp.com"

**SEO Optimization:**
- **Title:** "Best Slicer Settings for 3D Printing - Complete Guide 2025 (OrcaSlicer, PLA, PETG, ABS)"
- **Thumbnail:** Bold text "BEST SLICER SETTINGS" with material comparison
- **Tags:** 3d printing, orcaslicer, slicer settings, bambu lab, pla settings, petg settings

**See `SEO_STRATEGY.md` for full video production guide.**

---

## 🔧 Part 6: Environment Variables (For Future PA-API Integration)

When you're ready to add the Python backend (Phases 11-14), you'll need to configure environment variables.

### How to Add Environment Variables in Vercel

1. Go to your project in Vercel dashboard
2. Click "Settings" → "Environment Variables"
3. Add each variable:

**For PA-API (Future - Phase 12):**
```
PAAPI_ACCESS_KEY = <Your Amazon PA-API Access Key>
PAAPI_SECRET_KEY = <Your Amazon PA-API Secret Key>
PAAPI_ASSOCIATE_TAG = mwf064-20
PAAPI_REGION = us-east-1
PAAPI_HOST = webservices.amazon.com
CACHE_TTL = 3600
CACHE_ENABLED = true
```

**For each variable:**
- Name: (e.g., `PAAPI_ACCESS_KEY`)
- Value: (paste your key)
- Environment: Select "Production", "Preview", "Development"
- Click "Save"

⚠️ **Important:** Never commit API keys to GitHub! Always use environment variables.

---

## 🎨 Part 5: Optimize for Production

### Performance Optimizations

1. **Enable Vercel Analytics (Optional - $10/month):**
   - Project Settings → Analytics → Enable
   - Get detailed performance metrics
   - Track Core Web Vitals

2. **Add Security Headers:**
   Create `vercel.json` in project root:
   ```json
   {
     "headers": [
       {
         "source": "/(.*)",
         "headers": [
           {
             "key": "X-Content-Type-Options",
             "value": "nosniff"
           },
           {
             "key": "X-Frame-Options",
             "value": "DENY"
           },
           {
             "key": "X-XSS-Protection",
             "value": "1; mode=block"
           },
           {
             "key": "Referrer-Policy",
             "value": "strict-origin-when-cross-origin"
           }
         ]
       }
     ]
   }
   ```

3. **Add Favicon:**
   - Create a `favicon.ico` file (16x16 or 32x32 PNG converted to ICO)
   - Place in project root
   - Vercel will serve it automatically

4. **Add Open Graph Meta Tags:**
   Add these in the `<head>` section of `orcaslicer_assistant.html`:
   ```html
   <!-- Open Graph / Facebook -->
   <meta property="og:type" content="website">
   <meta property="og:url" content="https://your-domain.com/">
   <meta property="og:title" content="OrcaSlicer Expert Assistant">
   <meta property="og:description" content="Get personalized 3D printing settings recommendations for any material">
   <meta property="og:image" content="https://your-domain.com/og-image.png">

   <!-- Twitter -->
   <meta property="twitter:card" content="summary_large_image">
   <meta property="twitter:url" content="https://your-domain.com/">
   <meta property="twitter:title" content="OrcaSlicer Expert Assistant">
   <meta property="twitter:description" content="Get personalized 3D printing settings recommendations for any material">
   <meta property="twitter:image" content="https://your-domain.com/og-image.png">
   ```

---

## 📈 Part 6: Monitor & Maintain

### Daily Checks (2 minutes)

1. **Check Site Health:**
   - Visit your site to ensure it's loading
   - Test material selection and affiliate links
   - Check mobile responsiveness

2. **Check Analytics:**
   - GA4 → Realtime (are users visiting?)
   - Check affiliate click events
   - Monitor material selection patterns

### Weekly Checks (15 minutes)

1. **Review GA4 Reports:**
   - Reports → Engagement → Pages and screens
   - Reports → Engagement → Events (affiliate clicks)
   - Reports → User → Demographics (where are users from?)

2. **Check Amazon Associates Dashboard:**
   - Log in to https://affiliate-program.amazon.com
   - Check clicks, conversions, earnings
   - Note which products are performing best

3. **Update Products (if needed):**
   - Replace low-performing products
   - Add new popular products
   - Update prices if they've changed significantly

### Monthly Checks (30 minutes)

1. **Review Performance:**
   - Total visitors, page views, session duration
   - Affiliate CTR (clicks / impressions)
   - Conversion rate (orders / clicks)
   - Revenue (commissions earned)

2. **Optimize Based on Data:**
   - Which materials are most popular? Feature them.
   - Which products get the most clicks? Promote them.
   - Which materials have zero clicks? Improve product selection.
   - Are mobile users converting? Optimize mobile UX.

3. **Deploy Updates:**
   - Commit and push improvements
   - Vercel auto-deploys in ~30 seconds

---

## 🐛 Troubleshooting

### Deployment Failed

**Error: "No Output Directory"**
- Solution: Make sure `orcaslicer_assistant.html` is in the root directory
- Check that "Output Directory" is set to `./` in project settings

**Error: "Build Command Failed"**
- Solution: Set "Build Command" to empty (static site needs no build)

### Site Not Loading

**Error: "404 - Not Found"**
- Check that `orcaslicer_assistant.html` is named correctly (not `index.html`)
- Vercel serves `index.html` by default; rename if needed

**Workaround:** Rename `orcaslicer_assistant.html` to `index.html`

### Custom Domain Not Working

**DNS Propagation Takes Time:**
- Wait 24-48 hours for nameserver changes
- Wait 1-4 hours for A/CNAME record changes
- Use https://www.whatsmydns.net/ to check propagation

**HTTPS Not Working:**
- Vercel auto-provisions SSL certificates
- This can take 5-10 minutes after DNS is configured
- Check project settings → Domains → SSL status

### Analytics Not Tracking

**No Events in GA4:**
- Check that Measurement ID is correct (`G-XXXXXXXXXX`)
- Ensure GA4 script is in `<head>` section
- Check browser console for errors
- Use GA4 Realtime view and visit your own site

**Affiliate Clicks Not Tracked:**
- Verify click event listener is added correctly
- Check browser console for JavaScript errors
- Test: Right-click affiliate link → Inspect → Console

---

## 🎯 Success Checklist

After completing this guide, you should have:

- [x] ✅ Live website accessible 24/7 on Vercel
- [x] ✅ Custom domain configured (optional but recommended)
- [x] ✅ HTTPS enabled automatically
- [x] ✅ Google Analytics 4 tracking visitors and events
- [x] ✅ Affiliate link clicks tracked in GA4
- [x] ✅ Material selections tracked in GA4
- [x] ✅ Amazon Associates account linked
- [x] ✅ Ready to generate revenue!

---

## 🚀 Next Steps

Once deployed, proceed to:

1. **Phase 10:** Expand affiliate products to all 28 materials (see TODO.md)
2. **Phase 10B:** Optimize product presentation and seasonal rotation
3. **Phase 7A:** Add material search/filter to increase engagement
4. **Monitor & Iterate:** Use GA4 data to guide improvements

**Estimated Timeline:**
- **Today:** Deploy (30 min)
- **This Week:** Basic affiliate expansion (2 hours) → $5-10/month
- **Next Week:** Complete static enhancements (8 hours) → $15-25/month
- **Month 2:** PA-API integration (20 hours) → $50-100/month

---

## 📚 Additional Resources

### Vercel Documentation
- **Getting Started:** https://vercel.com/docs
- **Custom Domains:** https://vercel.com/docs/concepts/projects/domains
- **Environment Variables:** https://vercel.com/docs/concepts/projects/environment-variables
- **CLI Reference:** https://vercel.com/docs/cli

### Google Analytics 4
- **GA4 Setup Guide:** https://support.google.com/analytics/answer/9304153
- **Event Tracking:** https://support.google.com/analytics/answer/9267735
- **Realtime Reports:** https://support.google.com/analytics/answer/9271392

### Amazon Associates
- **Associates Central:** https://affiliate-program.amazon.com
- **Program Policies:** https://affiliate-program.amazon.com/help/operating/agreement
- **Product Linking:** https://affiliate-program.amazon.com/help/node/topic/GP38PJ6EUR6PFBEC

### Performance Monitoring
- **Vercel Analytics:** https://vercel.com/docs/concepts/analytics
- **Core Web Vitals:** https://web.dev/vitals/
- **Lighthouse CI:** https://github.com/GoogleChrome/lighthouse-ci

---

## ❓ Need Help?

**Vercel Support:**
- Docs: https://vercel.com/docs
- Community: https://github.com/vercel/vercel/discussions
- Status: https://vercel-status.com

**GitHub Issues:**
- Report bugs or request features at: https://github.com/minimal3dp/orcaslicer_expert_assistant/issues

**Contact:**
- Ko-fi: https://ko-fi.com/J3J41MTJUB (support the developer!)

---

**Last Updated:** November 12, 2025  
**Guide Version:** 1.0  
**Deployment Target:** Vercel Hobby (Free Tier)  

🎉 **Happy Deploying!** Your OrcaSlicer Expert Assistant is ready to help the 3D printing community and generate revenue!
