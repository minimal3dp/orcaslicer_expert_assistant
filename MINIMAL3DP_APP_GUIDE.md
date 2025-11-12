# minimal3dp.com Application Development Guide

**Version:** 1.0  
**Last Updated:** November 12, 2025  
**Purpose:** Unified deployment, SEO, and monetization strategy for all minimal3dp.com applications

---

## 🎯 Mission Statement

Build a portfolio of high-quality, free 3D printing tools under the `minimal3dp.com` brand. Each tool should:
- Solve a specific user problem exceptionally well
- Generate passive revenue through Amazon affiliate links
- Drive traffic through SEO and YouTube integration
- Maintain consistent branding and cross-linking

---

## 📐 Architecture Standards

### Domain Strategy

**Root Domain:** `minimal3dp.com`
- **Purpose:** Main marketing site, portfolio page, blog
- **Hosting:** Vercel
- **Repository:** `minimal3dp/main-site`

**Subdomain Structure:** One app = One subdomain
```
minimal3dp.com                     → Main site/landing page
├── orcaslicer.minimal3dp.com     → OrcaSlicer Expert Assistant
├── filament.minimal3dp.com       → Filament Database (future)
├── calc.minimal3dp.com           → Print Calculator (future)
├── compare.minimal3dp.com        → Slicer Comparison (future)
├── guides.minimal3dp.com         → Guides Hub (future)
└── api.minimal3dp.com            → Shared API backend (future)
```

**Why Subdomains?**
- ✅ Shared brand identity and SEO authority
- ✅ Free unlimited subdomains
- ✅ Independent deployment per app
- ✅ Professional portfolio appearance
- ✅ Easy cross-linking between apps

### Technology Stack

**Frontend Options:**
- **Static HTML/JS:** Best for simple tools (Tailwind CSS recommended)
- **Next.js:** For complex apps needing SSR/SSG
- **Python + Flask:** For data-heavy tools
- **Vue/React:** For interactive calculators

**Hosting:** Vercel (Hobby - Free Tier)
- Automatic HTTPS
- GitHub auto-deploy
- Edge CDN (global performance)
- Unlimited bandwidth
- Zero configuration

**Backend (Future):**
- **Serverless Functions:** Python or Node.js on Vercel
- **Shared API:** `api.minimal3dp.com` for common services
- **Database:** PostgreSQL (Vercel Postgres) or MongoDB Atlas

### Repository Structure

**Option A: Monorepo** (Recommended for 5+ apps)
```
minimal3dp-apps/
├── apps/
│   ├── orcaslicer/
│   ├── filament/
│   └── calc/
├── packages/
│   ├── ui-components/
│   └── shared-utils/
└── turbo.json
```

**Option B: Individual Repos** (Current - Good for 1-3 apps)
```
minimal3dp/orcaslicer-assistant
minimal3dp/filament-database
minimal3dp/print-calculator
```

---

## 🚀 Deployment Checklist

Use this checklist for **every new app** you deploy.

### Phase 1: Initial Setup (30 minutes)

- [ ] **Create GitHub Repository**
  - Name: `<app-name>` (lowercase, hyphens)
  - Description: One-sentence summary
  - Add README.md with project overview
  - Initialize with main branch

- [ ] **Choose Subdomain Name**
  - Format: `<app>.minimal3dp.com`
  - Keep it short, descriptive, keyword-focused
  - Check DNS records to avoid conflicts
  - Examples: `orcaslicer`, `calc`, `filament`, `compare`

- [ ] **Deploy to Vercel**
  - Connect GitHub repository
  - Framework: Select appropriate preset (or "Other" for static)
  - Root directory: `./`
  - Build command: (depends on framework)
  - Output directory: (depends on framework)
  - Click "Deploy"

- [ ] **Configure Custom Domain**
  - In Vercel: Settings → Domains → Add domain
  - Enter: `<app>.minimal3dp.com`
  - Copy CNAME record: `cname.vercel-dns.com`
  - Add DNS record at domain registrar:
    ```
    Type:   CNAME
    Name:   <app>
    Value:  cname.vercel-dns.com.
    TTL:    3600
    ```
  - Wait 5-15 minutes for DNS propagation
  - Verify HTTPS certificate (auto-provisioned)

### Phase 2: SEO Foundation (60 minutes)

- [ ] **Optimize Page Title**
  - Format: `<Primary Keyword> - <Brand> | <Secondary Keyword>`
  - Example: `Best Slicer Settings for 3D Printing - OrcaSlicer Expert Assistant`
  - Include 1-2 target keywords
  - Keep under 60 characters

- [ ] **Write Meta Description**
  - Length: 150-160 characters
  - Include primary keyword in first 50 characters
  - List key features or benefits
  - Include call-to-action
  - Example: `Get expert 3D printing settings for 28 materials. Free tool optimized for strength, speed, quality, and accuracy. PLA, PETG, ABS, Nylon, PEEK, and more.`

- [ ] **Add Meta Keywords**
  - 5-10 targeted keywords
  - Include variations and long-tail phrases
  - Example: `3d printing, slicer settings, orcaslicer, pla settings, petg settings, bambu lab`

- [ ] **Add Schema.org Structured Data**
  - Type: `WebApplication` (for tools) or `Article` (for guides)
  - Include: name, description, keywords, applicationCategory
  - JSON-LD format in `<head>` section
  ```json
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "OrcaSlicer Expert Assistant",
    "description": "Free tool for 3D printing slicer settings",
    "applicationCategory": "UtilitiesApplication",
    "keywords": "3d printing, slicer settings, orcaslicer"
  }
  ```

- [ ] **Add Open Graph Tags** (Social Sharing)
  ```html
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://<app>.minimal3dp.com/">
  <meta property="og:title" content="<App Name>">
  <meta property="og:description" content="<Description>">
  <meta property="og:image" content="https://<app>.minimal3dp.com/og-image.png">
  ```

- [ ] **Add Twitter Card Tags**
  ```html
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://<app>.minimal3dp.com/">
  <meta name="twitter:title" content="<App Name>">
  <meta name="twitter:description" content="<Description>">
  <meta name="twitter:image" content="https://<app>.minimal3dp.com/og-image.png">
  ```

- [ ] **Create OG Image**
  - Dimensions: 1200x630 pixels
  - Format: PNG (preferred) or JPG
  - File size: <300KB
  - Content: App name, key benefit, branding
  - Tool: Canva (use "Facebook Post" template)
  - Save as: `/og-image.png` in project root

- [ ] **Create sitemap.xml**
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://<app>.minimal3dp.com/</loc>
      <lastmod>2025-11-12</lastmod>
      <changefreq>weekly</changefreq>
      <priority>1.0</priority>
    </url>
  </urlset>
  ```

- [ ] **Create robots.txt**
  ```
  User-agent: *
  Allow: /
  
  Sitemap: https://<app>.minimal3dp.com/sitemap.xml
  ```

- [ ] **Submit to Google Search Console**
  - Go to: https://search.google.com/search-console
  - Add property: `https://<app>.minimal3dp.com`
  - Verify ownership (HTML file or meta tag)
  - Submit sitemap: `sitemap.xml`
  - Monitor weekly: impressions, clicks, position

- [ ] **Add FAQ Section**
  - 5-10 common questions related to your target keyword
  - Answer format: conversational, helpful, 2-3 sentences
  - Include Schema.org FAQ markup for rich snippets
  - Place prominently on page (not hidden in footer)

### Phase 3: Branding & Navigation (30 minutes)

- [ ] **Add Header Navigation**
  ```html
  <nav class="main-nav">
    <a href="https://minimal3dp.com">← minimal3dp</a>
    <a href="https://minimal3dp.com/tools">All Tools</a>
    <a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube</a>
  </nav>
  ```

- [ ] **Add Footer Links**
  - Link to main site: `minimal3dp.com`
  - Link to other apps (once launched)
  - Social media links (YouTube, Twitter, GitHub)
  - Ko-fi or donation link
  - Privacy policy (if collecting data)

- [ ] **Add YouTube Channel Link**
  - Prominent placement in header
  - Text: "Watch on YouTube" or "Video Guide"
  - Link: `https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw`

- [ ] **Add Canonical URL**
  ```html
  <link rel="canonical" href="https://<app>.minimal3dp.com">
  ```

### Phase 4: Analytics Setup (30 minutes)

- [ ] **Set Up Google Analytics 4**
  - Create GA4 property: `<App Name>`
  - Get Measurement ID: `G-XXXXXXXXXX`
  - Add GA4 script to `<head>`:
  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
  ```

- [ ] **Configure Cross-Domain Tracking** (if linking to other apps)
  ```javascript
  gtag('config', 'G-XXXXXXXXXX', {
    'linker': {
      'domains': ['minimal3dp.com', '<app>.minimal3dp.com']
    }
  });
  ```

- [ ] **Track Custom Events**
  - Button clicks
  - Form submissions
  - Tool usage (calculations, selections, etc.)
  - Affiliate link clicks
  - External link clicks

- [ ] **Set Up Conversions**
  - Define primary conversion (tool usage, download, etc.)
  - Mark event as "Key Event" in GA4
  - Track conversion funnel

### Phase 5: YouTube Integration (30 minutes)

- [ ] **Update YouTube Channel Description**
  - Add link to new app
  - Format: `🔧 <APP NAME>: https://<app>.minimal3dp.com`
  - Brief description of app's purpose

- [ ] **Update YouTube Channel Links**
  - YouTube Studio → Customization → Basic Info → Links
  - Add custom link: Title: `<App Name>`, URL: `https://<app>.minimal3dp.com`

- [ ] **Update Video Descriptions**
  - Add tool section to ALL video descriptions
  - Template:
  ```
  ━━━━━━━━━━━━━━━━━━━━━
  🔧 FREE TOOLS
  ━━━━━━━━━━━━━━━━━━━━━
  
  <App Name>: https://<app>.minimal3dp.com
  <Description of tool>
  
  All Tools: https://minimal3dp.com/tools
  ```

- [ ] **Plan Companion Video**
  - Create video demonstrating the tool
  - Title format: `<Target Keyword> - <Tool Name> Tutorial`
  - Optimize for target SEO keyword
  - Link to tool in description, pinned comment, and cards

---

## 💰 Monetization Strategy

### Amazon Affiliate Implementation

**Prerequisites:**
- Amazon Associates account (sign up at https://affiliate-program.amazon.com)
- Affiliate tag: `mwf064-20` (use this across ALL apps)

#### Static Product Recommendations (Phase 1 - Quick Win)

**Use Case:** Simple tools with known product recommendations

**Implementation:**
1. Create JSON file with product data:
```json
{
  "material_name": {
    "products": [
      {
        "name": "Product Name",
        "asin": "B0XXXXXXXX",
        "price": "$25.99",
        "reason": "Why this product is recommended"
      }
    ]
  }
}
```

2. Generate affiliate links:
```
https://www.amazon.com/dp/<ASIN>?tag=mwf064-20
```

3. Display recommendations contextually:
   - After user makes a selection
   - Related to user's inputs
   - Sidebar or bottom section

**Tracking Static Links:**
```javascript
// Track affiliate link clicks in GA4
document.addEventListener('click', function(e) {
    if (e.target.closest('a[rel*="sponsored"]')) {
        const link = e.target.closest('a');
        const productName = link.getAttribute('data-product-name');
        
        gtag('event', 'affiliate_click', {
            'event_category': 'Affiliate',
            'event_label': productName,
            'value': 1
        });
    }
});
```

#### Dynamic PA-API Integration (Phase 2 - Advanced)

**Use Case:** Tools needing real-time pricing, reviews, or product search

**Requirements:**
- Amazon Product Advertising API (PA-API) credentials
- Python serverless function on Vercel
- Redis or in-memory caching

**API Endpoints:**
```
GET /api/products?keyword=<keyword>&category=<category>
GET /api/product/<asin>
```

**Environment Variables (Vercel):**
```
PAAPI_ACCESS_KEY = <Your PA-API Access Key>
PAAPI_SECRET_KEY = <Your PA-API Secret Key>
PAAPI_ASSOCIATE_TAG = mwf064-20
PAAPI_REGION = us-east-1
PAAPI_HOST = webservices.amazon.com
CACHE_TTL = 3600
```

**Caching Strategy:**
- Cache product data for 1 hour
- Fallback to static data if API fails
- Rate limit: 1 request/second (PA-API limit)

**Implementation:** See `TODO.md` Phases 11-14 in OrcaSlicer Assistant for full PA-API roadmap

### Revenue Expectations

**Static Affiliate System:**
- Week 1: $5-10/month
- Month 1: $15-25/month
- Month 3: $40-60/month
- Month 6: $80-120/month

**With PA-API (Dynamic):**
- More products → More clicks → Higher revenue
- Expected: 1.5-2× static system revenue
- Month 6: $120-200/month
- Month 12: $200-400/month

**Revenue Multiplier Per App:**
- Each app = additional revenue stream
- 3 apps = 3× revenue potential
- Cross-linking boosts all apps' traffic

### Best Practices

✅ **Do:**
- Recommend products you genuinely believe in
- Explain WHY you recommend each product
- Disclose affiliate relationship: "As an Amazon Associate, I earn from qualifying purchases"
- Use `rel="noopener noreferrer sponsored"` on links
- Test products before recommending (if possible)

❌ **Don't:**
- Recommend products just for commissions
- Use deceptive practices (fake urgency, false claims)
- Hide affiliate disclosure
- Spam users with excessive ads
- Violate Amazon Associates terms

**Compliance:**
- Add disclosure: "This site contains affiliate links. We may earn a commission if you purchase through these links at no extra cost to you."
- Use `rel="sponsored"` attribute on affiliate links
- Follow FTC guidelines for affiliate marketing
- Comply with Amazon Associates Program Policies

---

## 🎯 SEO Strategy Template

### Keyword Research Process

**For Each New App:**

1. **Identify Primary Keyword** (1-3 keywords)
   - What problem does your tool solve?
   - What would users search for?
   - Use Google Autocomplete for ideas
   - Check YouTube Analytics "Trends" tab

2. **Find Secondary Keywords** (5-10 keywords)
   - Variations of primary keyword
   - Related questions
   - Long-tail phrases
   - Tool: Ubersuggest, Google Keyword Planner (free)

3. **Analyze Competition**
   - Google your primary keyword
   - Check top 10 results
   - Identify gaps: What are they missing?
   - Your advantage: Free tool, interactive, comprehensive

**Example: OrcaSlicer Assistant**
- **Primary:** "best slicer settings for 3d printing"
- **Secondary:** "orcaslicer settings", "pla settings 3d printing", "petg settings", "slicer settings guide", "3d print optimization"
- **Advantage:** Interactive tool vs static blog posts, 28 materials vs 5-10 materials

### Content Strategy

**On-Page Content:**
- H1: Primary keyword (exact match or close variation)
- H2-H3: Secondary keywords, questions
- First paragraph: Primary keyword in first 50 words
- Body: Natural keyword usage (don't stuff)
- Alt text: Describe images with keywords
- Internal links: Link to related tools/pages

**FAQ Section:**
- Answer 5-10 common questions
- Use question format in H3 tags: "What are the best..."
- Natural, helpful answers
- Include Schema.org FAQ markup

**Material/Topic Landing Pages:** (For content-heavy tools)
- Create dedicated pages for high-traffic topics
- Example: `/materials/pla`, `/materials/petg`
- Optimize each page for specific keyword
- Internal linking between related pages

### Link Building Strategy

**Internal Linking:**
- Link from main site (`minimal3dp.com`) to all apps
- Link between related apps
- Breadcrumb navigation
- Footer links on all pages

**External Backlinks:**
- **Reddit:** Share tool in r/3Dprinting, r/BambuLab, r/ender3 (helpful, not spammy)
- **Forums:** 3DPrintBoardPro, Prusa forums, Bambu forum
- **YouTube:** Video descriptions, pinned comments
- **Guest Posts:** Write for All3DP, 3DPrintBeginner
- **Open Source:** Contribute to OrcaSlicer, link to tool in discussions

**Social Media:**
- Twitter: Share tool launches, updates
- Reddit: Helpful responses with tool link
- Facebook Groups: 3D printing communities
- Discord: Bambu Lab, OrcaSlicer servers

### Technical SEO

- [ ] **Mobile-Friendly:** Test with Google Mobile-Friendly Test
- [ ] **Fast Loading:** Optimize images, minimize JS/CSS
- [ ] **HTTPS:** Auto-configured with Vercel
- [ ] **Structured Data:** Schema.org markup for rich snippets
- [ ] **Sitemap:** Auto-generated or manual XML
- [ ] **Canonical URLs:** Prevent duplicate content issues
- [ ] **Internal Linking:** Logical site structure
- [ ] **Image Optimization:** Compress images, use WebP
- [ ] **Core Web Vitals:** Monitor in Google Search Console

### SEO Success Metrics

**Week 1:**
- Site indexed in Google
- 100-200 impressions

**Month 1:**
- 1,000+ impressions
- 50+ clicks
- Page 3-5 ranking for primary keyword

**Month 2:**
- 5,000+ impressions
- 250+ clicks
- Page 2-3 ranking

**Month 3:**
- 10,000+ impressions
- 500+ clicks
- Page 1 (top 10) ranking

**Month 6:**
- 25,000+ impressions
- 1,500+ clicks
- Top 3 ranking

**Month 12:**
- 50,000+ impressions
- 5,000+ clicks
- #1 or #2 ranking

---

## 📺 YouTube Integration Strategy

### Channel Structure

**Main Channel:** youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw

**Content Types:**
1. **Tool Tutorials:** How to use each minimal3dp tool
2. **Material Guides:** "Best settings for PLA", "Best settings for PETG"
3. **Comparison Videos:** "Cura vs OrcaSlicer vs PrusaSlicer"
4. **Project Walkthroughs:** Using tools in real projects
5. **Tips & Tricks:** Quick wins for 3D printing

### Video SEO

**Title Format:**
```
<Target Keyword> - <Secondary Keyword> (<Year>)
```
Example: `Best Slicer Settings for 3D Printing - PLA, PETG, ABS Guide (2025)`

**Description Template:**
```
<Hook - What viewer will learn>

<Chapters/Timestamps>
0:00 - Intro
1:00 - PLA Settings
5:00 - PETG Settings
...

━━━━━━━━━━━━━━━━━━━━━
🔧 FREE TOOL: <APP NAME>
━━━━━━━━━━━━━━━━━━━━━

Get personalized settings: https://<app>.minimal3dp.com

<Brief description of tool benefits>

All Tools: https://minimal3dp.com/tools

━━━━━━━━━━━━━━━━━━━━━

<Full video description, tips, links>

#3dprinting #orcaslicer #slicersettings
```

**Tags (10-15):**
- Primary keyword
- Secondary keywords
- Material names (PLA, PETG, ABS)
- Slicer names (OrcaSlicer, Cura, PrusaSlicer)
- Brand names (Bambu Lab, Prusa, Creality)

**Thumbnail:**
- Bold text: Primary keyword or benefit
- High contrast colors
- Include branding element
- Face (if applicable) for higher CTR
- 1280x720 pixels

### Cross-Promotion

**In Videos:**
- Mention tool in intro: "Link in description"
- Show tool on screen while explaining
- End screen: Add link to tool (custom URL)
- Cards: Link to tool at relevant moments

**Pinned Comments:**
```
📌 FREE TOOL: <APP NAME>

👉 https://<app>.minimal3dp.com

<Brief description of what tool does>

Perfect for <use cases>!
```

**Video Series Ideas:**

1. **"Best Settings" Series** - One video per material
2. **"Tool Tutorial" Series** - Deep dive on each minimal3dp tool
3. **"Common Problems" Series** - Troubleshooting guides
4. **"Project Showcase" Series** - Using tools in real projects
5. **"Comparison" Series** - Compare materials, slicers, printers

---

## 🔄 Cross-Linking Strategy

### Main Site (`minimal3dp.com`)

**Tools/Apps Page:**
```html
<section class="tools-portfolio">
  <h2>Free 3D Printing Tools</h2>
  
  <div class="tool-grid">
    <a href="https://orcaslicer.minimal3dp.com" class="tool-card">
      <h3>🎯 OrcaSlicer Expert Assistant</h3>
      <p>Get intelligent slicer settings for 28 materials</p>
      <span class="badge">Live</span>
    </a>
    
    <a href="https://filament.minimal3dp.com" class="tool-card">
      <h3>📊 Filament Database</h3>
      <p>Comprehensive specs for 100+ filaments</p>
      <span class="badge">Coming Soon</span>
    </a>
    
    <!-- More tools... -->
  </div>
</section>
```

### App Header Navigation

**Standard Header (All Apps):**
```html
<nav class="main-nav">
  <a href="https://minimal3dp.com" class="logo">minimal3dp</a>
  
  <div class="nav-links">
    <a href="https://minimal3dp.com/tools">All Tools</a>
    <a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube</a>
    <a href="https://github.com/minimal3dp">GitHub</a>
  </div>
</nav>
```

### App Footer Links

**Standard Footer (All Apps):**
```html
<footer>
  <div class="footer-content">
    <div class="footer-section">
      <h4>minimal3dp Tools</h4>
      <ul>
        <li><a href="https://orcaslicer.minimal3dp.com">OrcaSlicer Assistant</a></li>
        <li><a href="https://filament.minimal3dp.com">Filament Database</a></li>
        <li><a href="https://calc.minimal3dp.com">Print Calculator</a></li>
        <li><a href="https://minimal3dp.com/tools">All Tools</a></li>
      </ul>
    </div>
    
    <div class="footer-section">
      <h4>Resources</h4>
      <ul>
        <li><a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube Channel</a></li>
        <li><a href="https://minimal3dp.com/blog">Blog</a></li>
        <li><a href="https://minimal3dp.com/guides">Guides</a></li>
      </ul>
    </div>
    
    <div class="footer-section">
      <h4>Connect</h4>
      <ul>
        <li><a href="https://github.com/minimal3dp">GitHub</a></li>
        <li><a href="https://ko-fi.com/J3J41MTJUB">Support Us</a></li>
      </ul>
    </div>
  </div>
  
  <div class="footer-disclaimer">
    <p>As an Amazon Associate, we earn from qualifying purchases.</p>
    <p>&copy; 2025 minimal3dp. All rights reserved.</p>
  </div>
</footer>
```

### Related Tools Section

**Within App Content:**
```html
<section class="related-tools">
  <h3>You Might Also Like</h3>
  
  <div class="tool-cards">
    <a href="https://filament.minimal3dp.com">
      <strong>Filament Database</strong>
      <span>Compare 100+ filament specs</span>
    </a>
    
    <a href="https://calc.minimal3dp.com">
      <strong>Print Calculator</strong>
      <span>Estimate time, cost, and material</span>
    </a>
  </div>
</section>
```

---

## 📊 Analytics & Monitoring

### Weekly Review (15 minutes)

**Google Analytics 4:**
- [ ] Check total users, sessions, pageviews
- [ ] Review top pages
- [ ] Check affiliate click events
- [ ] Identify traffic sources (organic, YouTube, social)
- [ ] Monitor bounce rate (goal: <60%)
- [ ] Check average session duration (goal: >2 min)

**Google Search Console:**
- [ ] Total impressions (trending up?)
- [ ] Total clicks (trending up?)
- [ ] Average CTR (goal: 5%+)
- [ ] Average position (goal: improving)
- [ ] Top queries (ranking for target keywords?)
- [ ] Any indexing errors?

**Amazon Associates:**
- [ ] Total clicks
- [ ] Conversion rate (orders / clicks)
- [ ] Earnings this week
- [ ] Best-performing products

### Monthly Review (30 minutes)

**Performance Analysis:**
- [ ] Compare to last month: Users, sessions, revenue
- [ ] Identify growth trends
- [ ] Top-performing content
- [ ] Best traffic sources
- [ ] Conversion funnel analysis

**SEO Progress:**
- [ ] Keyword rankings: Improved or declined?
- [ ] New keywords ranking (unintended benefits)
- [ ] Backlinks gained (use Google Search Console)
- [ ] Domain authority (use Moz or Ahrefs free tools)

**Content Optimization:**
- [ ] Which pages have high bounce rate? (Improve content)
- [ ] Which pages have low CTR? (Improve title/description)
- [ ] Which products get clicks but no sales? (Replace products)
- [ ] Which tools get most usage? (Prioritize improvements)

**Competitive Analysis:**
- [ ] Google your primary keyword: Where do you rank?
- [ ] Check top 3 competitors: What are they doing well?
- [ ] Identify content gaps: What can you add?

### Key Performance Indicators (KPIs)

**Traffic Metrics:**
- Monthly unique users
- Monthly pageviews
- Average session duration
- Pages per session
- Bounce rate

**SEO Metrics:**
- Keyword rankings (top 3 keywords)
- Organic search traffic %
- Impressions in Google Search
- Click-through rate (CTR)

**Revenue Metrics:**
- Affiliate clicks
- Affiliate conversion rate
- Monthly earnings
- Revenue per 1000 visitors (RPM)

**Engagement Metrics:**
- Tool usage rate (% of visitors who use tool)
- Return visitor rate
- Social shares
- YouTube referral traffic

---

## 🚀 Launch Checklist

Use this checklist for **every new app launch**.

### Pre-Launch (1 week before)

- [ ] **Feature Complete:** Core functionality works flawlessly
- [ ] **Mobile Tested:** Responsive on phone, tablet, desktop
- [ ] **Browser Tested:** Chrome, Safari, Firefox, Edge
- [ ] **SEO Complete:** All meta tags, Schema.org, OG image
- [ ] **Analytics Installed:** GA4 tracking verified
- [ ] **Affiliate Links Ready:** Products selected, links tested
- [ ] **Cross-Links Added:** Header, footer navigation
- [ ] **Performance Optimized:** Images compressed, fast loading
- [ ] **Vercel Deployed:** Custom domain configured, HTTPS working

### Launch Day

- [ ] **Deploy to Production:** Final commit, Vercel auto-deploys
- [ ] **Submit to Google Search Console:** Sitemap submitted
- [ ] **Update Main Site:** Add tool to portfolio page
- [ ] **Update YouTube:** Channel description, links
- [ ] **Social Media Announcement:**
  - Twitter: "Launching <Tool Name>! Free 3D printing tool..."
  - Reddit: r/3Dprinting, r/BambuLab (helpful post, not spammy)
  - Discord: OrcaSlicer, Bambu Lab servers
- [ ] **Update Video Descriptions:** Add tool link to relevant videos
- [ ] **Pin Comment:** Pin comment with tool link on popular videos
- [ ] **Verify GA4 Tracking:** Check Realtime reports

### Post-Launch (First Week)

- [ ] **Monitor Daily:** Check for errors, user feedback
- [ ] **Fix Bugs:** Address any issues quickly
- [ ] **Gather Feedback:** Reddit comments, YouTube comments, Discord
- [ ] **Iterate:** Small improvements based on feedback
- [ ] **Create Content:** Blog post, video tutorial (if planned)
- [ ] **Monitor Rankings:** Check Google Search Console daily
- [ ] **Engage Community:** Respond to comments, questions

### First Month

- [ ] **Analyze Data:** GA4 reports, Search Console, Amazon Associates
- [ ] **Optimize Content:** Improve based on user behavior
- [ ] **Expand Features:** Add nice-to-haves based on feedback
- [ ] **Create More Content:** Additional blog posts, videos
- [ ] **Build Backlinks:** Reddit, forums, guest posts
- [ ] **Plan Next App:** Start developing next tool in portfolio

---

## 🎨 Branding Guidelines

### Visual Identity

**Logo/Brand:**
- Brand name: `minimal3dp`
- Tagline: "Free 3D Printing Tools" or "Tools for Makers"
- Design style: Clean, minimal, technical
- Color palette: Blue/teal (tech), white/gray (minimal)

**Typography:**
- Headings: Bold, sans-serif (Inter, Roboto, Tailwind default)
- Body: Regular, readable (system fonts)
- Code: Monospace (for technical content)

**Color Scheme:**
- Primary: Blue (#3B82F6) - action, links
- Secondary: Teal (#14B8A6) - accents
- Background: Dark gray (#1F2937) or white
- Text: Light gray (#E5E7EB) on dark, dark on light
- Success: Green (#10B981)
- Warning: Yellow (#F59E0B)
- Error: Red (#EF4444)

### Voice & Tone

**Brand Voice:**
- Helpful, not condescending
- Technical but accessible
- Enthusiastic about 3D printing
- Honest about trade-offs
- Community-focused

**Writing Style:**
- Short sentences (10-15 words average)
- Active voice: "Select your material" not "Material should be selected"
- Second person: "You can..." not "Users can..."
- Conversational but professional
- Use examples, not just theory

**Examples:**

✅ **Good:**
> "Select your material and print goal. We'll recommend the perfect settings for your project."

❌ **Bad:**
> "The user should proceed to select the material type and desired optimization parameters to receive algorithmically-determined configuration values."

### User Experience Principles

1. **Clarity:** Make it obvious what the tool does
2. **Simplicity:** Minimal clicks to get value
3. **Speed:** Fast loading, instant results
4. **Mobile-First:** Design for phones, enhance for desktop
5. **Accessibility:** Readable text, good contrast, keyboard navigation
6. **Consistency:** Same patterns across all apps
7. **Helpful:** Explain WHY, not just WHAT
8. **Trust:** Disclose affiliates, be honest about limitations

---

## 🛠️ Development Best Practices

### Code Quality

- [ ] **DRY (Don't Repeat Yourself):** Extract shared components
- [ ] **Comments:** Explain WHY, not WHAT
- [ ] **Naming:** Descriptive variable/function names
- [ ] **Error Handling:** Graceful failures, user-friendly messages
- [ ] **Validation:** Client-side and server-side (if applicable)
- [ ] **Security:** Sanitize inputs, use HTTPS, environment variables for secrets

### Performance

- [ ] **Image Optimization:** Compress, lazy load, WebP format
- [ ] **Code Splitting:** Load only what's needed
- [ ] **Caching:** Browser caching, CDN, API response caching
- [ ] **Minification:** Minify CSS/JS for production
- [ ] **Lazy Loading:** Defer non-critical resources

### Testing

- [ ] **Manual Testing:** Click every button, test every input
- [ ] **Mobile Testing:** Real devices, not just browser DevTools
- [ ] **Browser Testing:** Chrome, Safari, Firefox, Edge
- [ ] **Error Scenarios:** What happens if API fails? No internet?
- [ ] **Accessibility Testing:** Screen reader, keyboard navigation

### Git Workflow

**Branch Strategy:**
- `main`: Production-ready code
- `develop`: Development branch
- `feature/<name>`: New features
- `bugfix/<name>`: Bug fixes

**Commit Messages:**
```
<type>: <short summary>

<longer description if needed>

Examples:
feat: Add material search filter
fix: Resolve mobile navigation bug
docs: Update deployment guide
style: Improve button hover states
```

**Deployment:**
- Push to `main` → Auto-deploy to Vercel
- Preview deployments for feature branches
- Test on preview URL before merging

---

## 📈 Growth Strategy

### Months 1-3: Foundation

**Focus:** Launch, SEO foundation, initial traffic

- [ ] Deploy first 1-2 apps
- [ ] Optimize for target keywords
- [ ] Submit to Google Search Console
- [ ] Create 5-10 YouTube videos
- [ ] Build initial backlinks (Reddit, forums)
- [ ] Monitor analytics weekly
- [ ] Iterate based on feedback

**Goals:**
- 1,000+ monthly visitors per app
- Page 2-3 ranking for primary keyword
- $40-60/month revenue per app

### Months 4-6: Growth

**Focus:** More apps, more content, better rankings

- [ ] Deploy 2-3 additional apps
- [ ] Create material landing pages
- [ ] Publish 10-20 YouTube videos
- [ ] Guest post on 3D printing blogs
- [ ] Expand affiliate products
- [ ] Optimize conversion funnels

**Goals:**
- 5,000+ monthly visitors per app
- Page 1 (top 10) ranking for primary keywords
- $80-120/month revenue per app

### Months 7-12: Scale

**Focus:** Dominate keywords, expand portfolio, maximize revenue

- [ ] Deploy 5+ apps total
- [ ] Rank #1-3 for primary keywords
- [ ] 20,000+ monthly visitors per app
- [ ] Dynamic PA-API integration
- [ ] Premium features (optional)
- [ ] Partnerships with filament brands

**Goals:**
- 20,000+ monthly visitors per app
- Top 3 ranking for multiple keywords
- $200-400/month revenue per app
- $1,000-2,000/month total revenue

### Year 2+: Monetization Expansion

**Additional Revenue Streams:**
- Sponsored content (filament brand partnerships)
- Premium features ($5-10/month subscriptions)
- Consulting/coaching services
- Merchandise (branded tools, accessories)
- Affiliate expansion (printers, accessories, not just filament)

---

## 🆘 Common Issues & Solutions

### DNS/Deployment Issues

**Problem:** DNS not propagating
- **Solution:** Wait 15 minutes for CNAME, 24 hours for nameservers. Check https://www.whatsmydns.net/

**Problem:** HTTPS not working
- **Solution:** Vercel auto-provisions SSL, wait 5-10 minutes after DNS is verified

**Problem:** Site showing 404
- **Solution:** Check that `index.html` exists in root (or rename your HTML file)

### SEO Issues

**Problem:** Not appearing in Google after 1 week
- **Solution:** Submit sitemap in Google Search Console, verify indexing

**Problem:** Low CTR (<2%)
- **Solution:** Improve meta description, make it compelling and keyword-rich

**Problem:** High bounce rate (>70%)
- **Solution:** Improve page speed, make value proposition clearer, improve UX

### Analytics Issues

**Problem:** GA4 not tracking
- **Solution:** Check Measurement ID, verify script in `<head>`, test in Realtime view

**Problem:** Affiliate clicks not tracked
- **Solution:** Check event listener code, verify `gtag` function exists, test manually

### Revenue Issues

**Problem:** Clicks but no conversions
- **Solution:** Review product selection (wrong products?), check link format, verify tag `mwf064-20`

**Problem:** Low click-through rate on affiliate links
- **Solution:** Improve product presentation, add more context (WHY recommend), better placement

---

## 📚 Resources & References

### Vercel Documentation
- **Getting Started:** https://vercel.com/docs
- **Custom Domains:** https://vercel.com/docs/concepts/projects/domains
- **Environment Variables:** https://vercel.com/docs/concepts/projects/environment-variables

### SEO Resources
- **Google Search Console:** https://search.google.com/search-console
- **Google Keyword Planner:** https://ads.google.com/home/tools/keyword-planner/
- **Ubersuggest (Free):** https://neilpatel.com/ubersuggest/
- **Schema.org Documentation:** https://schema.org/

### Amazon Associates
- **Associates Central:** https://affiliate-program.amazon.com
- **Program Policies:** https://affiliate-program.amazon.com/help/operating/agreement
- **Product Linking:** https://affiliate-program.amazon.com/help/node/topic/GP38PJ6EUR6PFBEC

### Analytics
- **Google Analytics 4:** https://analytics.google.com
- **GA4 Documentation:** https://support.google.com/analytics/answer/9304153

### YouTube
- **YouTube Studio:** https://studio.youtube.com
- **YouTube SEO Guide:** https://backlinko.com/youtube-seo

### Development Tools
- **Tailwind CSS:** https://tailwindcss.com
- **Canva (Free):** https://canva.com
- **Figma (Free):** https://figma.com

---

## 🎯 AI Agent Instructions

**When using this guide to help develop a new minimal3dp.com application:**

1. **Read this entire document first** to understand the architecture, strategy, and standards.

2. **Follow the checklist sequentially:**
   - Phase 1: Deployment
   - Phase 2: SEO
   - Phase 3: Branding
   - Phase 4: Analytics
   - Phase 5: YouTube

3. **Customize for the specific app:**
   - Research target keywords for this app's niche
   - Identify appropriate affiliate products
   - Create app-specific content (FAQ, descriptions)

4. **Maintain consistency:**
   - Use same affiliate tag: `mwf064-20`
   - Follow subdomain naming convention
   - Use standard header/footer templates
   - Match branding guidelines

5. **Verify integrations:**
   - GA4 Measurement ID is correct
   - Affiliate links include tag
   - Cross-links point to correct URLs
   - DNS records are accurate

6. **Test thoroughly:**
   - Mobile responsiveness
   - All interactive features
   - Analytics tracking (use Realtime view)
   - Affiliate link tracking

7. **Document app-specific details:**
   - Create app README with specific features
   - Update TODO.md with app roadmap
   - Note any deviations from standard template

8. **Launch following checklist:**
   - Pre-launch verification
   - Launch day tasks
   - Post-launch monitoring

**Key Principle:** This guide is a starting point. Adapt as needed, but maintain consistency across the minimal3dp.com portfolio.

---

## 📝 Version History

- **v1.0 (2025-11-12):** Initial guide created based on OrcaSlicer Assistant deployment experience

---

**This is a living document.** Update it as you learn best practices, encounter new scenarios, or optimize the workflow.

**Questions?** Review the Resources section above or consult the specific app's documentation (README.md, TODO.md, SEO_STRATEGY.md).

🚀 **Happy Building!**
