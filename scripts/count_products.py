#!/usr/bin/env python3
"""Count products per material category in index.html"""

import re
import sys
from pathlib import Path

def count_products():
    html_path = Path(__file__).parent.parent / 'index.html'
    
    with open(html_path, 'r') as f:
        content = f.read()
    
    # Find the affiliateProducts object
    match = re.search(r'const affiliateProducts = \{(.*?)\n        \};', content, re.DOTALL)
    if not match:
        print("Error: Could not find affiliateProducts")
        sys.exit(1)
    
    products_data = match.group(1)
    
    # Extract categories and count products
    category_blocks = re.finditer(
        r"'([^']+)':\s*\[(.*?)\](?=\s*,\s*'|\s*,\s*//|\s*$)",
        products_data,
        re.DOTALL
    )
    
    categories = {}
    for block_match in category_blocks:
        category_name = block_match.group(1)
        products_block = block_match.group(2)
        
        # Count ASINs in this category
        asin_count = len(re.findall(r'asin:', products_block))
        categories[category_name] = asin_count
    
    # Print results
    print("\n=== Product Count by Category ===\n")
    
    needs_more = []
    has_enough = []
    
    for cat, count in sorted(categories.items()):
        if cat.startswith('_'):
            print(f"  {cat}: {count} products (internal)")
        elif count < 2:
            print(f"  {cat}: {count} product(s) ⚠️  NEEDS MORE")
            needs_more.append(cat)
        else:
            print(f"  {cat}: {count} products ✓")
            has_enough.append(cat)
    
    print(f"\n=== Summary ===")
    print(f"Total categories: {len([c for c in categories if not c.startswith('_')])}")
    print(f"Categories with 2+ products: {len(has_enough)}")
    print(f"Categories needing more: {len(needs_more)}")
    
    if needs_more:
        print(f"\n⚠️  These categories need at least 1 more product:")
        for cat in needs_more:
            print(f"  - {cat}")

if __name__ == '__main__':
    count_products()
