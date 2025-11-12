# Vercel Deployment Guide - OrcaSlicer Expert Assistant

**Last Updated:** November 12, 2025  
**Deployment Target:** Vercel Hobby (Free Tier)  
**Estimated Time:** 15-30 minutes  

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

## 🎯 Part 2: Set Up Custom Domain (Optional but Recommended)

### Why Use a Custom Domain?
- Professional appearance
- Better SEO
- Easier to remember and share
- Builds brand trust

### Step 1: Purchase a Domain (if you don't have one)

**Recommended Registrars:**
- **Namecheap:** https://www.namecheap.com (~$10-15/year)
- **Google Domains:** https://domains.google (~$12/year)
- **Cloudflare:** https://www.cloudflare.com/products/registrar/ (~$8-10/year)

**Suggested Domain Names:**
- `orcaslicer-assistant.com`
- `orcaslicer-expert.com`
- `3dprint-settings.com`
- `orcaslicer-helper.com`

### Step 2: Add Domain to Vercel

1. In Vercel dashboard, go to your project
2. Click "Settings" → "Domains"
3. Enter your domain (e.g., `orcaslicer-assistant.com`)
4. Click "Add"

### Step 3: Configure DNS

Vercel will show you DNS records to add. You have two options:

**Option A: Nameserver Method (Recommended)**
1. Copy the nameservers shown by Vercel
2. Go to your domain registrar
3. Replace existing nameservers with Vercel's nameservers
4. Wait 24-48 hours for DNS propagation

**Option B: A/CNAME Records Method**
1. Add these records at your domain registrar:
   ```
   Type: A
   Name: @
   Value: 76.76.21.21

   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```
2. Wait 1-4 hours for DNS propagation

✅ **Custom domain configured!** Your site is now accessible at your chosen domain.

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

## 🔧 Part 4: Environment Variables (For Future PA-API Integration)

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
