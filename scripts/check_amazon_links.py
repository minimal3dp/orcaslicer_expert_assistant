#!/usr/bin/env python3
"""
Check Amazon Product Links
===========================
This script extracts ASINs from index.html and checks if the Amazon product pages
are accessible. It focuses on checking the top 2 products in each category.

Usage:
    uv run scripts/check_amazon_links.py
    
Or with full details:
    uv run scripts/check_amazon_links.py --verbose
"""

import re
import sys
import time
import argparse
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from typing import List, Tuple, Dict

# ANSI color codes for pretty output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'


def extract_products_from_html(html_path: Path) -> Dict[str, List[Dict]]:
    """Extract product information from index.html."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the affiliateProducts object
    match = re.search(r'const affiliateProducts = \{(.*?)\n        \};', content, re.DOTALL)
    if not match:
        print(f"{Colors.RED}Error: Could not find affiliateProducts in HTML{Colors.END}")
        sys.exit(1)
    
    products_data = match.group(1)
    
    # Extract categories and their products
    categories = {}
    
    # Match each category and its products array
    # Pattern: 'CategoryName': [ ... products ... ]
    category_blocks = re.finditer(
        r"'([^']+)':\s*\[(.*?)\](?=\s*,\s*'|\s*,\s*//|\s*$)",
        products_data,
        re.DOTALL
    )
    
    for block_match in category_blocks:
        category_name = block_match.group(1)
        products_block = block_match.group(2)
        
        # Extract individual products from this category
        # Match product objects with all their fields
        product_matches = re.finditer(
            r'\{\s*'
            r'name:\s*[\'"]([^\'"]+)[\'"],\s*'
            r'brand:\s*[\'"]([^\'"]+)[\'"],\s*'
            r'price:\s*[\'"]([^\'"]+)[\'"],\s*'
            r'description:\s*[\'"]([^\'"]*)[\'"],\s*'
            r'asin:\s*[\'"]([^\'"]+)[\'"],\s*'
            r'tag:\s*[\'"]([^\'"]+)[\'"]',
            products_block,
            re.DOTALL
        )
        
        products = []
        for prod_match in product_matches:
            products.append({
                'name': prod_match.group(1),
                'brand': prod_match.group(2),
                'price': prod_match.group(3),
                'description': prod_match.group(4),
                'asin': prod_match.group(5),
                'tag': prod_match.group(6)
            })
        
        if products:
            categories[category_name] = products
    
    return categories


def check_amazon_url(asin: str, tag: str, retry_count: int = 2) -> Tuple[bool, int, str]:
    """
    Check if an Amazon product URL is accessible.
    
    Returns:
        Tuple of (success, status_code, message)
    """
    url = f"https://www.amazon.com/dp/{asin}?tag={tag}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    for attempt in range(retry_count + 1):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=10) as response:
                status_code = response.getcode()
                if status_code == 200:
                    return True, status_code, "OK"
                else:
                    return False, status_code, f"Unexpected status code: {status_code}"
        except HTTPError as e:
            if attempt < retry_count:
                time.sleep(1)  # Wait before retry
                continue
            return False, e.code, f"HTTP Error: {e.code}"
        except URLError as e:
            if attempt < retry_count:
                time.sleep(1)
                continue
            return False, 0, f"URL Error: {e.reason}"
        except Exception as e:
            if attempt < retry_count:
                time.sleep(1)
                continue
            return False, 0, f"Error: {str(e)}"
    
    return False, 0, "All retries failed"


def check_products(categories: Dict[str, List[Dict]], top_n: int = 2, verbose: bool = False):
    """Check the top N products in each category."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}=== Amazon Product Link Checker ==={Colors.END}\n")
    print(f"Checking top {top_n} products in each category...\n")
    
    total_checked = 0
    total_working = 0
    total_broken = 0
    broken_products = []
    
    for category, products in categories.items():
        # Skip internal categories
        if category.startswith('_'):
            continue
        
        print(f"{Colors.BOLD}{Colors.BLUE}Category: {category}{Colors.END}")
        
        # Check top N products
        products_to_check = products[:top_n]
        
        for i, product in enumerate(products_to_check, 1):
            total_checked += 1
            asin = product['asin']
            name = product['name']
            brand = product['brand']
            
            print(f"  [{i}] {brand} - {name[:50]}..." if len(name) > 50 else f"  [{i}] {brand} - {name}")
            print(f"      ASIN: {asin}", end=" ... ")
            
            # Check the URL
            success, status_code, message = check_amazon_url(asin, product['tag'])
            
            if success:
                total_working += 1
                print(f"{Colors.GREEN}✓ Working{Colors.END}")
                if verbose:
                    print(f"      Status: {status_code}")
            else:
                total_broken += 1
                print(f"{Colors.RED}✗ Broken{Colors.END}")
                print(f"      {Colors.YELLOW}Error: {message}{Colors.END}")
                broken_products.append({
                    'category': category,
                    'name': name,
                    'brand': brand,
                    'asin': asin,
                    'error': message
                })
            
            # Be nice to Amazon's servers
            time.sleep(0.5)
        
        print()  # Empty line between categories
    
    # Print summary
    print(f"\n{Colors.BOLD}{Colors.CYAN}=== Summary ==={Colors.END}")
    print(f"Total products checked: {total_checked}")
    print(f"{Colors.GREEN}Working links: {total_working}{Colors.END}")
    print(f"{Colors.RED}Broken links: {total_broken}{Colors.END}")
    
    if broken_products:
        print(f"\n{Colors.BOLD}{Colors.RED}⚠️  Broken Products:{Colors.END}")
        for product in broken_products:
            print(f"\n  Category: {product['category']}")
            print(f"  Product: {product['brand']} - {product['name']}")
            print(f"  ASIN: {product['asin']}")
            print(f"  Error: {product['error']}")
    
    # Exit with error code if any links are broken
    if total_broken > 0:
        print(f"\n{Colors.YELLOW}⚠️  Some links are broken. Please update them in index.html{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✓ All checked links are working!{Colors.END}")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description='Check Amazon product links in index.html',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Check top 2 products per category (default):
    uv run scripts/check_amazon_links.py
  
  Check top 3 products per category:
    uv run scripts/check_amazon_links.py --top 3
  
  Verbose output with status codes:
    uv run scripts/check_amazon_links.py --verbose
        """
    )
    parser.add_argument(
        '--top',
        type=int,
        default=2,
        help='Number of top products to check per category (default: 2)'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show detailed output including HTTP status codes'
    )
    
    args = parser.parse_args()
    
    # Find index.html
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    html_path = repo_root / 'index.html'
    
    if not html_path.exists():
        print(f"{Colors.RED}Error: index.html not found at {html_path}{Colors.END}")
        sys.exit(1)
    
    print(f"{Colors.CYAN}Reading products from: {html_path}{Colors.END}")
    
    # Extract products
    categories = extract_products_from_html(html_path)
    
    # Check products
    check_products(categories, top_n=args.top, verbose=args.verbose)


if __name__ == '__main__':
    main()
