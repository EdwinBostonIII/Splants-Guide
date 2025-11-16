#!/usr/bin/env python3
"""
Splants Guide Format Cleaner
Removes em-dashes and body-text hyphens per style requirements

Rules:
1. Remove all em-dashes (—) from body text
2. Remove hyphens surrounded by spaces (body text hyphens)
3. Keep hyphens in code blocks, URLs, and compound words
4. Replace with appropriate punctuation (colons, commas, periods)
"""

import re
import sys

def clean_em_dashes(text):
    """Replace em-dashes with appropriate punctuation"""
    # Replace em-dash with colon, comma, or period based on context
    # For now, simple replacement with colon
    text = text.replace('—', ':')
    return text

def clean_body_hyphens(text):
    """
    Remove hyphens that are clearly body text (surrounded by spaces)
    Keep hyphens that are part of compound words or code
    """
    # Pattern: space-hyphen-space (body text usage)
    # Replace with appropriate punctuation
    
    # First, handle " - " (space hyphen space) replacements
    # Context-aware replacement would be ideal, but for now use comma
    
    # Don't replace in code blocks (lines starting with spaces/tabs or between ```)
    lines = text.split('\n')
    cleaned_lines = []
    in_code_block = False
    
    for line in lines:
        # Check if we're entering/exiting a code block
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
            continue
        
        # Check if line looks like code (starts with significant whitespace)
        if line.startswith('    ') or line.startswith('\t'):
            cleaned_lines.append(line)
            continue
        
        # Skip lines with URLs or file paths
        if 'http://' in line or 'https://' in line or '.com' in line or '/' in line and line.count('/') > 2:
            cleaned_lines.append(line)
            continue
        
        # If not in code block, clean body text hyphens
        if not in_code_block:
            # Replace " - " with ", " in body text
            line = re.sub(r' \- ', ', ', line)
            # Replace " -- " with ": " 
            line = re.sub(r' \-\- ', ': ', line)
        
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def analyze_file(filepath):
    """Analyze file for formatting issues"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    em_dash_count = content.count('—')
    body_hyphen_count = len(re.findall(r' \- ', content))
    double_hyphen_count = len(re.findall(r' \-\- ', content))
    
    print(f"Analysis of {filepath}:")
    print(f"  Em-dashes (—): {em_dash_count}")
    print(f"  Body hyphens ( - ): {body_hyphen_count}")
    print(f"  Double hyphens ( -- ): {double_hyphen_count}")
    print(f"  Total issues: {em_dash_count + body_hyphen_count + double_hyphen_count}")
    
    return content

def clean_file(filepath, output_path=None):
    """Clean formatting issues from file"""
    content = analyze_file(filepath)
    
    print("\nCleaning...")
    cleaned = clean_em_dashes(content)
    cleaned = clean_body_hyphens(cleaned)
    
    if output_path is None:
        output_path = filepath + '.cleaned'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print(f"Cleaned file written to: {output_path}")
    
    # Re-analyze cleaned file
    print("\nRe-analyzing cleaned file...")
    with open(output_path, 'r', encoding='utf-8') as f:
        cleaned_content = f.read()
    
    em_dash_count = cleaned_content.count('—')
    body_hyphen_count = len(re.findall(r' \- ', cleaned_content))
    double_hyphen_count = len(re.findall(r' \-\- ', cleaned_content))
    
    print(f"  Em-dashes (—): {em_dash_count}")
    print(f"  Body hyphens ( - ): {body_hyphen_count}")
    print(f"  Double hyphens ( -- ): {double_hyphen_count}")
    print(f"  Total remaining: {em_dash_count + body_hyphen_count + double_hyphen_count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python format_cleaner.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    clean_file(input_file, output_file)
