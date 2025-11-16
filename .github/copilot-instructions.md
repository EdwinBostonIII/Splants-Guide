# Splants Guide: AI Agent Instructions

## Project Overview
This repository contains the **Splants Automation Guide**, a comprehensive technical documentation project for building production-grade e-commerce automation systems. The guide teaches developers how to automate print-on-demand businesses using Stripe, Make.com, Printful/Printify, and Supabase.

**Current Status:** ~185,000 words across multiple files, consolidating to a single 120,000+ word production-ready guide.

## Critical Architecture Understanding

### The Three Essential Documents (Read These First)
1. **`MASTER_INTEGRATION_SPECIFICATION.md`** (7,700+ words) - Complete specification, requirements mapping, implementation roadmap
2. **`INTEGRATION_INDEX.md`** (2,000+ words) - Quick navigation, content completion tracker, week-by-week execution
3. **`CONSOLIDATION_COMPLETE.md`** (1,900+ words) - What was consolidated, how to use the master documents

These documents define the entire project structure. **Always consult them before making content changes.**

### Guide Structure (Parts 0-8)
The guide is divided into 9 main parts with specific word count targets:
- **Parts 0-1:** Architecture & Planning (~20,000 words each) - 75-85% complete
- **Part 2:** Core Implementation (~22,000 words) - 30% complete ⚠️ **High priority**
- **Parts 3-7:** Intelligence, Analytics, Customer Experience, Operations, Scaling (~8,000-12,000 words each) - 5-15% complete
- **Part 8:** Security & Compliance (~8,000 words) - Not started

Reference `INTEGRATION_INDEX.md` Section "Content Completion Tracker" for precise gaps.

## Strict Formatting Rules (Non-Negotiable)

### FORBIDDEN in Body Text
- **Em-dashes (—)** → Replace with: colon (:), comma (,), period (.), or parentheses ()
- **Standalone hyphens ( - )** surrounded by spaces → Replace with comma, colon, or period
- Vague statements without metrics → Always include specific numbers

### ALLOWED Hyphens (Only)
- Compound technical terms: `production-ready`, `real-time`, `server-side`
- Code blocks, URLs, file paths: `https://example.com/my-page`, `/path/to-file.txt`
- ASCII diagrams: `───`, `├──`, `└──`
- Ranges: `4-6 hours`, `10-15 minutes`

**Examples:**
```
❌ Wrong: "The system—which processes orders—handles webhooks"
✓ Right: "The system (which processes orders) handles webhooks"

❌ Wrong: "Make.com is powerful - it connects everything"  
✓ Right: "Make.com is powerful: it connects everything"
```

### Tool for Validation
Run `python format_cleaner.py <filename>` to detect and fix formatting violations. This script:
- Identifies em-dashes and body-text hyphens
- Generates before/after analysis
- Preserves appropriate hyphen usage (code, URLs, diagrams)

## Content Creation Patterns

### ASCII Diagrams (Minimum 1 per Major Section)
Copy from `ASCII_DIAGRAMS_LIBRARY.txt` (contains 8 complete diagrams). Use for:
- System architecture and data flows
- Decision trees and troubleshooting paths
- Comparisons and hierarchies

**Example pattern:**
```
┌─────────────────────────────────────────────────────┐
│  Stripe Webhook → Make.com → Printful API          │
│       ↓              ↓             ↓                │
│  Validation    Transform    Submit Order            │
└─────────────────────────────────────────────────────┘
```

### Production Reality Callouts (Need 75+ Total)
Real-world failure scenarios with specific metrics. Format:
```
╔═══════════════════════════════════════════════════════════╗
║ PRODUCTION REALITY: [Specific Scenario]                  ║
╠═══════════════════════════════════════════════════════════╣
║ Problem: [What went wrong]                                ║
║ Impact: [Time/money/customers affected - specific numbers]║
║ Solution: [How to prevent/fix]                            ║
╚═══════════════════════════════════════════════════════════╝
```

Reference `WAR_STORIES_COLLECTION.txt` for complete incident templates (2 fully documented, 8 templates).

### Code Blocks with Context
Always include:
- Purpose and when to use
- Prerequisites and dependencies  
- Expected output/behavior
- Common errors and troubleshooting

**Example from guide:**
```javascript
// Make.com webhook validation (prevents duplicate orders)
const orderId = webhook.data.id;
const existing = await supabase
  .from('orders')
  .select('id')
  .eq('stripe_order_id', orderId);
  
if (existing.data.length > 0) {
  return { status: 'duplicate', skipped: true };
}
```

## Key Workflows

### Content Expansion Workflow
1. Check `INTEGRATION_INDEX.md` for section status and word count gap
2. Review `PART_2_EXPANSION_TEMPLATE.txt` for structure blueprint (shows complete Section 2.2 example)
3. Follow `STYLE_AND_FORMATTING_GUIDE.txt` for tone, punctuation, and visual elements
4. Add ASCII diagrams from library or create new ones matching existing style
5. Run `format_cleaner.py` before committing
6. Update completion tracker in `INTEGRATION_INDEX.md`

### When Editing Existing Content
- **Multiple versions exist**: `Splants_Guide_FINAL.txt` (308 KB, most recent), `Splants_Guide_COMPREHENSIVE.txt` (221 KB), etc.
- Always edit **`Splants_Guide_FINAL.txt`** as the canonical version
- Cross-reference `MASTER_INTEGRATION_SPECIFICATION.md` Section 1.1 for file inventory

### Quality Checklist (Before Any Commit)
- [ ] Zero em-dashes in body text
- [ ] Body hyphens only in allowed contexts
- [ ] Specific numbers (not "several," "many," "quickly")
- [ ] Time estimates for all tasks (e.g., "2-4 hours" not "short time")
- [ ] ASCII diagrams for complex concepts
- [ ] Production Reality callouts for failure modes
- [ ] Code blocks with troubleshooting notes

## Critical Project Conventions

### Word Count Targets Are Mandatory
Each section has specific word count requirements tracked in `INTEGRATION_INDEX.md`. These are not suggestions—they define content depth. Example:
- Section 2.2.3 (Order Processing Pipeline): 2,000 words required, ~600 written → need 1,400 more

### Tone: Experienced Developer to Developer
- Write in second person ("you check Stripe," not "developers check Stripe")
- Include production war stories with specific failure scenarios
- Provide exact time/cost estimates with ROI calculations
- Assume reader knows programming but not this specific tech stack

### Visual Engagement Priority
The guide emphasizes visual learning:
- Minimum 1 ASCII diagram per major section (e.g., 2.1, 2.2, 2.3)
- Use boxes for warnings, separators for sections (see `ASCII_DIAGRAMS_LIBRARY.txt`)
- Decision matrices for comparisons (Printful vs Printify vs Gooten)

## Integration Points & Dependencies

### External Services Documented
- **Stripe API** (v2024.10) - Payment webhooks, order data
- **Make.com** (current) - Workflow automation, API orchestration  
- **Printful/Printify/Gooten APIs** (v1) - Print-on-demand fulfillment with failover
- **Supabase** - PostgreSQL database, real-time features

### Testing Approach
See `evaluation_framework.md`, `evaluation_quickstart.md`, `evaluation_test_scenarios.md` for:
- Assessment criteria for guide quality
- Quick start evaluation protocols
- 50+ test scenarios for validating automation logic

## Quick Commands

```bash
# Analyze formatting issues
python format_cleaner.py Splants_Guide_FINAL.txt

# Check word count for a section
wc -w <filename>

# Search for formatting violations
grep -n "—" Splants_Guide_FINAL.txt  # Find em-dashes
grep -n " - " Splants_Guide_FINAL.txt  # Find body hyphens
```

## When Creating New Content

1. **Identify the section** in `INTEGRATION_INDEX.md` (shows word count gap and priority)
2. **Read the template** in `PART_2_EXPANSION_TEMPLATE.txt` (demonstrates proper structure)
3. **Check existing content** in `Splants_Guide_FINAL.txt` (avoid duplication)
4. **Reference war stories** in `WAR_STORIES_COLLECTION.txt` (real failure scenarios with metrics)
5. **Apply formatting rules** from `STYLE_AND_FORMATTING_GUIDE.txt` (punctuation, diagrams, callouts)
6. **Validate before commit** using `format_cleaner.py`

## Files to Never Directly Edit
- `__azurite_db_blob__.json`, `__azurite_db_blob_extent__.json` - Azure storage emulator files
- Backup files: `Splants_Guide_REVISED.txt.backup`
- Historical versions: Only edit `Splants_Guide_FINAL.txt` as the canonical guide

## Success Metrics (From Specification)
- ✅ 120,000+ words total (currently ~51,000 in main guide)
- ✅ 75+ Production Reality callouts (currently ~20)
- ✅ 19+ ASCII diagrams (8 complete in library)
- ✅ 50+ code implementations (currently ~35)
- ✅ 100+ error scenarios documented (currently ~30)
- ✅ Zero formatting violations (em-dashes, body hyphens)

Reference `MASTER_INTEGRATION_SPECIFICATION.md` Section 15 for complete completion criteria.
