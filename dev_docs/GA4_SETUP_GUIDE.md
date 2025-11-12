# Google Analytics 4 Setup Guide - OrcaSlicer Expert Assistant

**Last Updated:** November 12, 2025  
**Application:** settings.minimal3dp.com  
**GA4 Measurement ID:** G-GERCPZ07KR  
**Status:** Basic tracking active, custom events pending

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Phase 1: Add Custom Event Tracking for Affiliate Links](#phase-1-add-custom-event-tracking-for-affiliate-links)
4. [Phase 2: Set Up Conversion Goals in GA4 Dashboard](#phase-2-set-up-conversion-goals-in-ga4-dashboard)
5. [Phase 3: Add Custom Dimensions for YouTube Referral Tracking](#phase-3-add-custom-dimensions-for-youtube-referral-tracking)
6. [Phase 4: Test Events in GA4 Realtime View](#phase-4-test-events-in-ga4-realtime-view)
7. [Verification Checklist](#verification-checklist)
8. [Troubleshooting](#troubleshooting)

---

## Overview

This guide will help you implement advanced Google Analytics 4 tracking for your OrcaSlicer settings recommender application. You'll track:

- **Affiliate link clicks** (CTR measurement for revenue optimization)
- **Material selections** (user behavior patterns)
- **YouTube referral traffic** (measure video-to-app conversion)
- **Warning interactions** (educational content effectiveness)

**Expected Time:** 2-3 hours total
**Difficulty:** Medium (JavaScript + GA4 dashboard configuration)

---

## Prerequisites

✅ **Before you begin, verify:**

1. **GA4 tracking code is installed** (lines 62-68 in `index.html`)
   ```html
   <!-- Google tag (gtag.js) -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-GERCPZ07KR"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-GERCPZ07KR');
   </script>
   ```

2. **You have admin access to GA4 property** at [analytics.google.com](https://analytics.google.com)
3. **Browser console open** (for debugging during testing)
4. **Text editor ready** (VS Code or similar)

---

## Phase 1: Add Custom Event Tracking for Affiliate Links

**Time:** 45 minutes  
**Goal:** Track every affiliate link click with product details

### Step 1.1: Add Affiliate Click Tracking JavaScript

**Location:** `index.html`, after the existing `gtag` configuration (around line 70)

**Add this code block:**

```html
<script>
// ============================================================
// GOOGLE ANALYTICS 4 - CUSTOM EVENT TRACKING
// ============================================================

/**
 * Track affiliate link clicks
 * Fires when user clicks any Amazon affiliate link
 */
document.addEventListener('click', function(e) {
  const affiliateLink = e.target.closest('a[href*="amazon.com"]');
  
  if (affiliateLink) {
    // Extract product information from the link
    const href = affiliateLink.getAttribute('href');
    const productCard = affiliateLink.closest('.product-card');
    
    // Try to extract ASIN from URL (format: /dp/ASIN or /gp/product/ASIN)
    const asinMatch = href.match(/\/(?:dp|gp\/product)\/([A-Z0-9]{10})/);
    const asin = asinMatch ? asinMatch[1] : 'unknown';
    
    // Get product name from card if available
    let productName = 'Unknown Product';
    if (productCard) {
      const nameElement = productCard.querySelector('.product-name, h3, h4');
      if (nameElement) {
        productName = nameElement.textContent.trim();
      }
    }
    
    // Get currently selected material
    const materialSelect = document.getElementById('material');
    const currentMaterial = materialSelect ? materialSelect.value : 'unknown';
    
    // Send event to GA4
    gtag('event', 'affiliate_click', {
      'product_name': productName,
      'product_asin': asin,
      'material': currentMaterial,
      'link_url': href,
      'timestamp': new Date().toISOString()
    });
    
    console.log('📊 GA4 Event: affiliate_click', {
      product_name: productName,
      product_asin: asin,
      material: currentMaterial
    });
  }
});

/**
 * Track material selections
 * Fires when user selects a material from dropdown
 */
function trackMaterialSelection(materialKey, materialName) {
  gtag('event', 'material_selected', {
    'material_key': materialKey,
    'material_name': materialName,
    'timestamp': new Date().toISOString()
  });
  
  console.log('📊 GA4 Event: material_selected', {
    material_key: materialKey,
    material_name: materialName
  });
}

/**
 * Track warning dismissals
 * Fires when user dismisses a warning card
 */
function trackWarningDismissal(warningType, materialKey) {
  gtag('event', 'warning_dismissed', {
    'warning_type': warningType,
    'material': materialKey,
    'timestamp': new Date().toISOString()
  });
  
  console.log('📊 GA4 Event: warning_dismissed', {
    warning_type: warningType,
    material: materialKey
  });
}

/**
 * Track warning expansions/collapses
 * Fires when user interacts with collapsible warnings
 */
function trackWarningInteraction(action, warningType, materialKey) {
  gtag('event', 'warning_interaction', {
    'action': action, // 'expand' or 'collapse'
    'warning_type': warningType,
    'material': materialKey,
    'timestamp': new Date().toISOString()
  });
  
  console.log('📊 GA4 Event: warning_interaction', {
    action: action,
    warning_type: warningType,
    material: materialKey
  });
}

// Track page engagement (time on site)
let pageLoadTime = new Date();
let engagementTracked = false;

window.addEventListener('beforeunload', function() {
  if (!engagementTracked) {
    const timeOnSite = Math.round((new Date() - pageLoadTime) / 1000); // seconds
    
    gtag('event', 'page_engagement', {
      'time_on_site_seconds': timeOnSite,
      'timestamp': new Date().toISOString()
    });
    
    engagementTracked = true;
  }
});

// Track at 30-second intervals for longer sessions
setInterval(function() {
  const timeOnSite = Math.round((new Date() - pageLoadTime) / 1000);
  
  if (timeOnSite % 30 === 0 && timeOnSite > 0) {
    gtag('event', 'engagement_milestone', {
      'time_on_site_seconds': timeOnSite,
      'milestone': timeOnSite + 's',
      'timestamp': new Date().toISOString()
    });
  }
}, 1000);

console.log('✅ GA4 Custom Event Tracking Initialized');
</script>
```

### Step 1.2: Integrate with Existing Material Selection Function

**Location:** `index.html`, find the `handleMaterialSelection()` function (around line 1500-1600)

**Find this code:**
```javascript
function handleMaterialSelection() {
  const selectedMaterial = materialSelect.value;
  // ... existing code ...
```

**Add this line right after getting `selectedMaterial`:**
```javascript
function handleMaterialSelection() {
  const selectedMaterial = materialSelect.value;
  
  // Track material selection in GA4
  const materialData = materials.find(m => m.key === selectedMaterial);
  const materialName = materialData ? materialData.name : selectedMaterial;
  trackMaterialSelection(selectedMaterial, materialName);
  
  // ... rest of existing code ...
```

### Step 1.3: Integrate with Warning Dismissal Function

**Location:** `index.html`, find the `dismissWarning()` function (around line 1700-1800)

**Find this code:**
```javascript
function dismissWarning(warningType) {
  const warningElement = document.getElementById(`warning-${warningType}`);
  if (warningElement) {
    warningElement.remove();
    // ... existing code ...
```

**Add tracking before the element is removed:**
```javascript
function dismissWarning(warningType) {
  const warningElement = document.getElementById(`warning-${warningType}`);
  if (warningElement) {
    // Track warning dismissal in GA4
    const materialSelect = document.getElementById('material');
    const currentMaterial = materialSelect ? materialSelect.value : 'unknown';
    trackWarningDismissal(warningType, currentMaterial);
    
    warningElement.remove();
    // ... rest of existing code ...
```

### Step 1.4: Test Locally

**Before deploying, test in browser console:**

1. Open `index.html` in browser
2. Open Developer Console (F12 or Cmd+Option+I on Mac)
3. Select a material (e.g., "PLA")
4. Look for console message: `📊 GA4 Event: material_selected`
5. Click an affiliate link
6. Look for console message: `📊 GA4 Event: affiliate_click`

**Expected console output:**
```
✅ GA4 Custom Event Tracking Initialized
📊 GA4 Event: material_selected { material_key: 'PLA', material_name: 'PLA' }
📊 GA4 Event: affiliate_click { product_name: 'Overture PLA Filament', product_asin: 'B07PGZNM34', material: 'PLA' }
```

---

## Phase 2: Set Up Conversion Goals in GA4 Dashboard

**Time:** 30 minutes  
**Goal:** Mark affiliate clicks as conversions for revenue attribution

### Step 2.1: Access GA4 Admin Panel

1. Go to [analytics.google.com](https://analytics.google.com)
2. Select your property: **OrcaSlicer Expert Assistant** (or property with ID `G-GERCPZ07KR`)
3. Click **Admin** (gear icon, bottom left)
4. In the **Property** column, click **Events**

### Step 2.2: Mark Events as Conversions

**You should see these custom events after Phase 1 deployment:**
- `affiliate_click`
- `material_selected`
- `warning_dismissed`
- `warning_interaction`
- `page_engagement`

**To mark `affiliate_click` as a conversion:**

1. Find `affiliate_click` in the events list
2. Toggle the **Mark as conversion** switch to **ON**
3. Confirm the action

**Repeat for other key events:**
- ✅ Mark `affiliate_click` as conversion (CRITICAL for revenue)
- ✅ Mark `material_selected` as conversion (user intent signal)
- ⚪ Leave `warning_dismissed` as regular event
- ⚪ Leave `warning_interaction` as regular event
- ⚪ Leave `page_engagement` as regular event

### Step 2.3: Create Custom Conversion Goals

**If you want more specific goals:**

1. In **Admin** → **Property** → Click **Conversions**
2. Click **New conversion event**
3. Enter event name: `high_value_affiliate_click`
4. Click **Save**

**Then create a custom event in GA4:**

1. Go to **Admin** → **Property** → **Data display** → **Events**
2. Click **Create event**
3. Set up conditions:
   - **Event name:** `high_value_affiliate_click`
   - **Matching conditions:**
     - `event_name` equals `affiliate_click`
     - `material` matches regex `(PEEK|PEKK|Nylon|CF)` (high-value materials)
   - **Parameter modifications:** (optional)
     - Add parameter `value` = `5` (estimated affiliate value in USD)

### Step 2.4: Set Up Funnel Analysis (Optional)

**Track the user journey from material selection → affiliate click:**

1. Go to **Explore** → **Funnel exploration**
2. Click **Create new exploration**
3. Name: "Material to Affiliate Click Funnel"
4. Add steps:
   - **Step 1:** `page_view` (entry)
   - **Step 2:** `material_selected` (engagement)
   - **Step 3:** `affiliate_click` (conversion)
5. Save and monitor conversion rates

---

## Phase 3: Add Custom Dimensions for YouTube Referral Tracking

**Time:** 30 minutes  
**Goal:** Track which YouTube videos/channels drive traffic

### Step 3.1: Set Up UTM Parameters for YouTube Links

**When sharing your app link in YouTube:**

**Format:**
```
https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=settings_guide&utm_content={video_title}
```

**Example links for different videos:**

1. **General tutorial video:**
   ```
   https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=settings_guide&utm_content=best_orcaslicer_settings
   ```

2. **Material-specific video (e.g., PLA guide):**
   ```
   https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=pla_settings&utm_content=pla_ultimate_guide
   ```

3. **Troubleshooting video:**
   ```
   https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=troubleshooting&utm_content=fix_stringing
   ```

**Where to add these links:**
- ✅ YouTube video descriptions (first 3 lines)
- ✅ Pinned comments
- ✅ YouTube channel "About" section
- ✅ YouTube channel banner (if space allows)
- ✅ Video end screens (call-to-action cards)
- ✅ Video cards (mid-roll)

### Step 3.2: Create Custom Dimensions in GA4

**Track additional YouTube metadata:**

1. Go to **Admin** → **Property** → **Data display** → **Custom definitions**
2. Click **Create custom dimensions**
3. Create these dimensions:

**Dimension 1: Video Title**
- **Dimension name:** `video_title`
- **Scope:** Event
- **Description:** YouTube video that referred the user
- **Event parameter:** `utm_content`
- Click **Save**

**Dimension 2: YouTube Campaign**
- **Dimension name:** `youtube_campaign`
- **Scope:** Event
- **Description:** YouTube campaign type (settings_guide, pla_settings, etc.)
- **Event parameter:** `utm_campaign`
- Click **Save**

**Dimension 3: Referral Source**
- **Dimension name:** `referral_source`
- **Scope:** Event
- **Description:** Traffic source (youtube, organic, direct, etc.)
- **Event parameter:** `utm_source`
- Click **Save**

### Step 3.3: Add YouTube Referral Tracking JavaScript

**Location:** `index.html`, add this code after the GA4 event tracking code (around line 180):

```html
<script>
// ============================================================
// YOUTUBE REFERRAL TRACKING
// ============================================================

/**
 * Track YouTube referrals with UTM parameters
 * Automatically captures utm_source, utm_campaign, utm_content
 */
function trackYouTubeReferral() {
  const urlParams = new URLSearchParams(window.location.search);
  const utmSource = urlParams.get('utm_source');
  const utmMedium = urlParams.get('utm_medium');
  const utmCampaign = urlParams.get('utm_campaign');
  const utmContent = urlParams.get('utm_content');
  
  // Only track if coming from YouTube
  if (utmSource === 'youtube' || document.referrer.includes('youtube.com')) {
    gtag('event', 'youtube_referral', {
      'referral_source': utmSource || 'youtube',
      'referral_medium': utmMedium || 'referrer',
      'youtube_campaign': utmCampaign || 'unknown',
      'video_title': utmContent || 'unknown',
      'referrer_url': document.referrer,
      'timestamp': new Date().toISOString()
    });
    
    console.log('📊 GA4 Event: youtube_referral', {
      referral_source: utmSource,
      youtube_campaign: utmCampaign,
      video_title: utmContent
    });
    
    // Store in localStorage for attribution (optional)
    localStorage.setItem('youtube_referral', JSON.stringify({
      source: utmSource,
      campaign: utmCampaign,
      video: utmContent,
      timestamp: new Date().toISOString()
    }));
  }
}

// Track YouTube referrals on page load
window.addEventListener('DOMContentLoaded', trackYouTubeReferral);

console.log('✅ YouTube Referral Tracking Initialized');
</script>
```

### Step 3.4: Update YouTube Channel & Videos

**Action items:**

1. **Update channel description:**
   ```
   Get optimized slicer settings at settings.minimal3dp.com
   
   Best slicer settings for 3D printing - Free tool for OrcaSlicer, PrusaSlicer, and more!
   
   🔗 Settings Tool: https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=channel_description
   ```

2. **Update top 5 video descriptions** (add to first 3 lines):
   ```
   🔗 Get the best slicer settings: https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=settings_guide&utm_content={VIDEO_TITLE_HERE}
   ```

3. **Pin comment on popular videos:**
   ```
   📌 Want optimized settings for this material? Try my free tool: 
   https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign={VIDEO_TOPIC}&utm_content={VIDEO_TITLE}
   ```

4. **Update channel banner** (if possible):
   - Add text: "settings.minimal3dp.com - Free Settings Tool"

---

## Phase 4: Test Events in GA4 Realtime View

**Time:** 30 minutes  
**Goal:** Verify all events are firing correctly

### Step 4.1: Deploy Your Changes

**Before testing in production:**

1. Commit changes to `seo-amazon` branch:
   ```bash
   git add index.html
   git commit -m "feat: Add GA4 custom event tracking for affiliate clicks, material selections, and YouTube referrals"
   git push origin seo-amazon
   ```

2. Merge to `main` branch:
   ```bash
   git checkout main
   git merge seo-amazon
   git push origin main
   ```

3. Vercel will auto-deploy to production (2-3 minutes)

### Step 4.2: Access GA4 Realtime View

1. Go to [analytics.google.com](https://analytics.google.com)
2. Select your property: **OrcaSlicer Expert Assistant**
3. Click **Reports** (left sidebar)
4. Click **Realtime** (under Reports Overview)

**You should see:**
- **Users by Event Name** (chart)
- **Event count by Event name** (table)
- **Users in last 30 minutes** (counter)

### Step 4.3: Test Material Selection Event

**Steps:**

1. Open **settings.minimal3dp.com** in browser
2. Open **GA4 Realtime view** in another tab
3. On your app, select a material (e.g., "PLA")
4. Wait 5-10 seconds
5. Check GA4 Realtime → **Event count by Event name**
6. Look for: `material_selected` (event count should increment)

**Expected result:**
- ✅ Event `material_selected` appears in list
- ✅ Event count: 1
- ✅ Parameters visible (if you click the event): `material_key`, `material_name`

**Browser console check:**
```
📊 GA4 Event: material_selected { material_key: 'PLA', material_name: 'PLA' }
```

### Step 4.4: Test Affiliate Click Event

**Steps:**

1. With material selected (e.g., PLA), scroll to **Recommended Products**
2. Click any Amazon affiliate link
3. **DO NOT close the tab** - let it load Amazon, then come back
4. Wait 5-10 seconds
5. Check GA4 Realtime → **Event count by Event name**
6. Look for: `affiliate_click` (event count should increment)

**Expected result:**
- ✅ Event `affiliate_click` appears in list
- ✅ Event count: 1
- ✅ Parameters visible: `product_name`, `product_asin`, `material`, `link_url`

**Browser console check:**
```
📊 GA4 Event: affiliate_click { 
  product_name: 'Overture PLA Filament 1.75mm', 
  product_asin: 'B07PGZNM34', 
  material: 'PLA' 
}
```

### Step 4.5: Test YouTube Referral Event

**Steps:**

1. Open a **new incognito/private browser window**
2. Navigate to: 
   ```
   https://settings.minimal3dp.com/?utm_source=youtube&utm_medium=video&utm_campaign=test&utm_content=manual_test
   ```
3. Wait 5-10 seconds
4. Check GA4 Realtime → **Event count by Event name**
5. Look for: `youtube_referral` (event count should increment)

**Expected result:**
- ✅ Event `youtube_referral` appears in list
- ✅ Event count: 1
- ✅ Parameters visible: `referral_source`, `youtube_campaign`, `video_title`

**Browser console check:**
```
📊 GA4 Event: youtube_referral { 
  referral_source: 'youtube', 
  youtube_campaign: 'test', 
  video_title: 'manual_test' 
}
```

### Step 4.6: Test Warning Dismissal Event

**Steps:**

1. Select a material with warnings (e.g., "Nylon" - hygroscopic)
2. Click the **X** button on a warning card
3. Wait 5-10 seconds
4. Check GA4 Realtime → **Event count by Event name**
5. Look for: `warning_dismissed`

**Expected result:**
- ✅ Event `warning_dismissed` appears
- ✅ Parameters: `warning_type`, `material`

### Step 4.7: Document Test Results

**Create a simple test log:**

| Event Name | Status | Timestamp | Notes |
|------------|--------|-----------|-------|
| `material_selected` | ✅ Pass | 2025-11-12 14:30 | Material key and name captured |
| `affiliate_click` | ✅ Pass | 2025-11-12 14:32 | ASIN extracted correctly |
| `youtube_referral` | ✅ Pass | 2025-11-12 14:35 | UTM parameters captured |
| `warning_dismissed` | ✅ Pass | 2025-11-12 14:37 | Warning type tracked |

---

## Verification Checklist

**Before considering setup complete, verify:**

### Code Implementation
- [ ] GA4 custom event tracking code added to `index.html`
- [ ] `trackMaterialSelection()` function integrated
- [ ] `trackWarningDismissal()` function integrated
- [ ] Affiliate click tracking event listener added
- [ ] YouTube referral tracking code added
- [ ] Console logs show event tracking in browser

### GA4 Dashboard Configuration
- [ ] `affiliate_click` marked as conversion
- [ ] `material_selected` marked as conversion
- [ ] Custom dimensions created: `video_title`, `youtube_campaign`, `referral_source`
- [ ] Funnel exploration set up (optional)

### YouTube Integration
- [ ] UTM parameter links created for top 5 videos
- [ ] YouTube channel description updated with tool link
- [ ] Video descriptions updated with tool links
- [ ] Pinned comments added to popular videos

### Testing & Validation
- [ ] Material selection event fires in GA4 Realtime
- [ ] Affiliate click event fires in GA4 Realtime
- [ ] YouTube referral event fires in GA4 Realtime
- [ ] Warning dismissal event fires in GA4 Realtime
- [ ] All events show correct parameters in GA4
- [ ] Browser console shows event tracking logs

### Documentation
- [ ] Test results documented
- [ ] UTM parameter structure documented
- [ ] Custom dimensions documented
- [ ] Conversion goals documented

---

## Troubleshooting

### Events Not Showing in GA4 Realtime

**Problem:** Events fire in console but don't appear in GA4 Realtime

**Solutions:**

1. **Wait longer:** GA4 Realtime can have 5-30 second delay
2. **Check ad blockers:** Disable browser ad blockers (they block GA4)
3. **Verify GA4 ID:** Confirm `G-GERCPZ07KR` is correct in `gtag('config', ...)`
4. **Check browser console for errors:** Look for `gtag is not defined` errors
5. **Hard refresh:** Clear cache and reload (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)

### Affiliate Clicks Not Tracking

**Problem:** Clicking affiliate links doesn't fire `affiliate_click` event

**Solutions:**

1. **Verify link structure:** Affiliate links must contain `amazon.com` in href
2. **Check event listener:** Ensure code is after `gtag` initialization
3. **Test with console.log:** Look for `📊 GA4 Event: affiliate_click` message
4. **Check timing:** If link navigates away immediately, event may not send
   - **Fix:** Add short delay before navigation (100ms)
   ```javascript
   affiliateLink.addEventListener('click', function(e) {
     e.preventDefault();
     // Track event
     gtag('event', 'affiliate_click', {...});
     // Navigate after brief delay
     setTimeout(() => {
       window.location.href = affiliateLink.href;
     }, 100);
   });
   ```

### YouTube Referrals Not Tracking

**Problem:** YouTube traffic not showing `youtube_referral` event

**Solutions:**

1. **Test UTM parameters manually:** Use full URL with UTM params in incognito
2. **Check referrer policy:** Some browsers block `document.referrer`
3. **Verify UTM structure:** Ensure `utm_source=youtube` is in URL
4. **Check localStorage:** Event should save to localStorage for debugging

### Custom Dimensions Not Available

**Problem:** Custom dimensions don't appear in GA4 reports

**Solutions:**

1. **Wait 24-48 hours:** Custom dimensions can take time to populate
2. **Verify event parameter names match:** `utm_content` → `video_title` mapping
3. **Check data retention settings:** Ensure data retention is not too short
4. **Re-create dimension:** Delete and recreate with exact parameter name

### Conversion Goals Not Counting

**Problem:** Events fire but conversions don't increment

**Solutions:**

1. **Check conversion toggle:** Ensure toggle is **ON** in Admin → Events
2. **Wait for data processing:** Conversions can take 24-48 hours to show in reports
3. **Check in Realtime:** Conversions should show immediately in Realtime view
4. **Verify event name spelling:** Must match exactly (case-sensitive)

---

## Next Steps After Setup

### Week 1: Monitor & Validate
- [ ] Check GA4 daily for event counts
- [ ] Verify conversion goals are incrementing
- [ ] Monitor YouTube referral traffic
- [ ] Document baseline metrics (CTR, conversion rate)

### Week 2: Optimize Based on Data
- [ ] Identify top-performing materials (by affiliate clicks)
- [ ] Identify top-performing YouTube videos (by referrals)
- [ ] Adjust product recommendations for low-CTR materials
- [ ] Create content for high-traffic materials

### Week 3: Scale YouTube Integration
- [ ] Update remaining video descriptions with UTM links
- [ ] Create new videos for high-converting materials
- [ ] Pin comments on all videos
- [ ] Update channel banner with tool URL

### Month 2: Revenue Analysis
- [ ] Correlate GA4 events with Amazon Associates earnings
- [ ] Calculate actual CTR and conversion rates
- [ ] Identify most profitable traffic sources
- [ ] Optimize affiliate product selection based on data

---

## Success Metrics to Track

**After 1 Month:**
- **Affiliate click CTR:** Target 2-5% (clicks / product impressions)
- **Material-to-click conversion:** Target 10-20% (users who select material → click product)
- **YouTube referral rate:** Target 20-30% of traffic from YouTube
- **Top 3 materials by clicks:** Identify for content strategy
- **Top 3 YouTube videos by referrals:** Identify for cross-promotion

**After 3 Months:**
- **Affiliate revenue correlation:** $X revenue per 100 affiliate clicks
- **YouTube → Revenue path:** Track full funnel from video → site → affiliate → purchase
- **Seasonal patterns:** Identify material trends (summer: PETG, winter: ABS)
- **Warning effectiveness:** Do users who dismiss warnings still click affiliates?

---

## Resources

### GA4 Documentation
- [GA4 Event Reference](https://support.google.com/analytics/answer/9267735)
- [GA4 Custom Dimensions](https://support.google.com/analytics/answer/10075209)
- [GA4 Conversions](https://support.google.com/analytics/answer/9267568)

### UTM Parameter Builder
- [Google Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/)

### Testing Tools
- [GA4 DebugView](https://support.google.com/analytics/answer/7201382) (for detailed event debugging)
- Browser DevTools Console (for quick validation)

---

## Summary

You've now implemented:
- ✅ Custom event tracking for affiliate clicks
- ✅ Conversion goals in GA4 dashboard
- ✅ Custom dimensions for YouTube referrals
- ✅ Realtime event validation

**Expected Impact:**
- **Data-driven optimization:** Know which materials/products perform best
- **Revenue attribution:** Track YouTube → Site → Affiliate → Purchase path
- **Content strategy:** Create videos for high-converting materials
- **ROI measurement:** Calculate return on content investment

**Time Investment:** 2-3 hours setup → Ongoing revenue insights

Good luck with your analytics setup! 🚀📊
