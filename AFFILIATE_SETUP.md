# Amazon Affiliate Links Setup Guide

## Overview
The OrcaSlicer Expert Assistant now includes Amazon affiliate product recommendations that display when users select a material. This feature can generate income through the Amazon Associates program.

## Setup Instructions

### 1. Join Amazon Associates
1. Go to [Amazon Associates](https://affiliate-program.amazon.com/)
2. Sign up for an account (it's free)
3. Complete the application process
4. Once approved, you'll receive your unique Associate Tag (tracking ID)

### 2. Update Your Affiliate Tag
In `orcaslicer_assistant.html`, find the `affiliateProducts` object (around line 1311) and replace `'YOUR_AFFILIATE_TAG'` with your actual Amazon Associates tag:

```javascript
const affiliateProducts = {
    'PLA': [
        {
            name: 'Overture PLA Filament 1.75mm',
            brand: 'Overture',
            price: '$19.99',
            description: 'Premium PLA with excellent layer adhesion',
            asin: 'B07PGZNM34',
            tag: 'yourtag-20'  // ← Replace 'YOUR_AFFILIATE_TAG' with this
        },
        // ... more products
    ],
    // ... more materials
};
```

**Find & Replace:** Use your code editor to find all instances of `'YOUR_AFFILIATE_TAG'` and replace with your actual tag.

### 3. Customize Product Recommendations (Optional)

#### Add More Products
You can add more products to any material by adding entries to the array:

```javascript
'PLA': [
    {
        name: 'Product Name',
        brand: 'Brand Name',
        price: '$XX.XX',
        description: 'Brief product description',
        asin: 'B0XXXXXXXX',  // Amazon product ASIN
        tag: 'yourtag-20'
    },
    // Add more products here
],
```

#### Find Product ASINs
1. Go to the product page on Amazon
2. Look in the URL: `amazon.com/dp/B07PGZNM34` - the ASIN is `B07PGZNM34`
3. Or scroll down to "Product Information" section on the product page

#### Add New Materials
If a material doesn't have products yet, add a new entry:

```javascript
'MaterialName': [
    {
        name: 'Product Name',
        brand: 'Brand',
        price: '$XX.XX',
        description: 'Description',
        asin: 'B0XXXXXXXX',
        tag: 'yourtag-20'
    }
],
```

## How It Works

### User Experience
1. User selects a material from the dropdown
2. Material warnings display (if applicable)
3. **NEW:** Product recommendations appear below warnings
4. Each product card shows:
   - Product name and brand
   - Brief description
   - Price estimate
   - "View on Amazon" button with your affiliate link

### Affiliate Link Structure
Links are automatically generated in this format:
```
https://www.amazon.com/dp/{ASIN}?tag={YOUR_TAG}
```

### Default Products
Materials without specific products show the `_default` items (filament storage, hardened nozzles, etc.).

## Best Practices

### 1. Choose Quality Products
- Only recommend products you trust or have researched
- Prioritize products with high ratings (4+ stars)
- Include popular brands users recognize

### 2. Keep Descriptions Honest
- Be accurate about product benefits
- Don't oversell or make false claims
- Mention any limitations

### 3. Update Prices Regularly
- Prices shown are estimates
- Check Amazon occasionally and update
- Consider removing specific prices and using "Check Price" instead

### 4. Disclosure Requirements
The app already includes the required disclosure:
> "As an Amazon Associate, I earn from qualifying purchases."

**Keep this visible** - it's required by Amazon Associates terms.

## Current Product Coverage

### Materials with Products
- ✅ PLA (3 products)
- ✅ PLA Plus (2 products)
- ✅ HTPLA (1 product)
- ✅ PLA Carbon Fiber (2 products)
- ✅ PETG (3 products)
- ✅ PETG Carbon Fiber (1 product)
- ✅ ABS (2 products)
- ✅ ASA (1 product)
- ✅ Nylon (2 products)
- ✅ Nylon Carbon Fiber (2 products)
- ✅ TPU 95A (2 products)
- ✅ TPU 85A (1 product)
- ✅ Polycarbonate (1 product)
- ✅ PVA (1 product)

### Materials Needing Products
Add products for these materials to increase coverage:
- PET
- HIPS
- PC-ABS Blend
- Nylon Glass Fiber
- PP (Polypropylene)
- PVB
- PLA variants (Wood, Metal, Silk, Glow-in-the-dark)
- PEEK, PEKK, PPSU, ULTEM (high-performance materials)

## Compliance Notes

### Amazon Associates Program Policies
- ✅ Disclosure is included
- ✅ Links open in new tab (`target="_blank"`)
- ✅ Links include `rel="noopener noreferrer sponsored"`
- ✅ You must disclose material connection to Amazon

### What You Must Do
1. Maintain at least 3 qualifying sales within 180 days of approval
2. Don't click your own affiliate links
3. Don't share links via email or offline methods
4. Keep your website content appropriate and legal

### What You Can't Do
- No price comparisons stating Amazon is cheaper
- No claiming to be Amazon or creating confusion
- No trademark violations
- No promoting illegal, obscene, or offensive content

## Revenue Potential

### Commission Rates (as of 2025)
Amazon's commission structure varies by category:
- **3D Printer Filament**: Typically 3-4% commission
- **3D Printers/Equipment**: Typically 2-3% commission
- **Prime benefits**: Can increase conversion rates

### Realistic Expectations
- **Low traffic (100 clicks/month)**: $10-30/month
- **Medium traffic (500 clicks/month)**: $50-150/month
- **High traffic (2000+ clicks/month)**: $200-600+/month

**Note:** These are estimates. Actual earnings depend on:
- Click-through rate (CTR)
- Conversion rate
- Average order value
- Product category
- User intent

## Testing Your Setup

### Quick Test
1. Open `orcaslicer_assistant.html` in a browser
2. Select "PLA" from the material dropdown
3. Verify product recommendations appear
4. Click a "View on Amazon" button
5. Check the URL includes your affiliate tag: `?tag=yourtag-20`

### Verify Each Link
Test a few products to ensure:
- Links go to correct products
- Your affiliate tag is present
- Products are still available on Amazon

## Troubleshooting

### Products Not Showing
- Check browser console for JavaScript errors
- Verify material key matches exactly (case-sensitive)
- Ensure affiliate container has correct ID: `affiliate-links`

### Wrong Products Displaying
- Verify ASIN is correct (10 characters)
- Check material key spelling
- Clear browser cache

### Links Not Working
- Ensure ASIN format is correct: `B0XXXXXXXX`
- Verify no extra spaces in tag
- Check Amazon product is still active

## Support

For questions about:
- **Amazon Associates**: [Amazon Associates Help](https://affiliate-program.amazon.com/help)
- **This Implementation**: Review the code comments in `orcaslicer_assistant.html`
- **Commission Issues**: Contact Amazon Associates support

## Future Enhancements

Potential improvements you could add:
- Product images from Amazon Product Advertising API
- Real-time prices via API
- User reviews/ratings
- "Add to Cart" direct integration
- More sophisticated product matching
- A/B testing different products
- Analytics tracking for click-through rates

---

**Remember**: Quality content that helps users should be your priority. Affiliate links are a bonus that funds your work, not the primary purpose of the tool.
