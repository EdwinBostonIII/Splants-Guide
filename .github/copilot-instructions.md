# Splants Guide: AI Agent Instructions

## Project Overview
This repository contains the **Splants Automation Guide**, a comprehensive technical documentation project for building production-grade e-commerce automation systems. The guide teaches developers how to automate print-on-demand businesses using Stripe, Make.com, Printful/Printify, and Supabase.

**Current Status:** ~36,000 words in main guide, expanding to target 100,000+ words for complete production-ready guide.

## Critical Architecture Understanding

### The Three Essential Documents (Read These First)
1. **`Splants_Guide_COMPLETE_DRAFT.txt`** (36,000+ words) - Complete guide with Introduction, Part 0, Part 1, Part 2 (complete), and Part 3 (partial)
2. **`INTEGRATION_INDEX.md`** (2,000+ words) - Quick navigation, content completion tracker, week-by-week execution
3. **`CONSOLIDATION_COMPLETE.md`** (1,900+ words) - What was consolidated, how to use the master documents

These documents define the entire project structure. **Always consult them before making content changes.**

### Guide Structure (Parts 0-8)
The guide is divided into 9 main parts with specific completion status:
- **Introduction:** Complete (~5,500 words) - Emotional journey and prerequisites
- **Part 0:** Complete (~18,000 words) - Architecture and planning
- **Part 1:** Complete (~7,000 words) - Implementation plan and costs
- **Part 2:** Complete (~8,000 words) - Core implementation with all 5 sections ✅
- **Part 3:** Partial (~3,000 words) - Intelligence layer framework provided
- **Parts 4-7:** Framework only - Need full implementation ⚠️ **High priority**
- **Part 8:** Not started - Security and compliance

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
- Ranges: `4 to 6 hours`, `10 to 15 minutes` (prefer "to" over hyphen)

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

### Voice and Tone Requirements
**Required tone characteristics:**
- Welcoming yet professional (no emojis, but supportive language)
- Explanatory without condescension (assume intelligence, not expertise)
- Specific measurements everywhere (never "fast" but "3 to 5 seconds")
- Subdued confidence (not hyperbolic promises)
- Acknowledging difficulty while providing solutions

**Replace dramatic language:**
- "War Stories" → "Production Experience Reports"
- "You will fail" → "Common challenges include..."
- "This is critical!" → "This step prevents [specific problem]"
- "Amazing results" → "Measurable improvements of X%"

### Production Reality Callouts (Need 75+ Total, Currently ~25)
Real-world failure scenarios with specific metrics. Format:
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PRODUCTION REALITY: [Specific Scenario]                                     │
│                                                                             │
│ Problem: [What went wrong with numbers]                                     │
│ Impact: [Time/money/customers affected, specific metrics]                   │
│ Solution: [How to prevent/fix]                                              │
│ Financial impact: [Dollar amounts]                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

Reference `WAR_STORIES_COLLECTION.txt` for complete incident templates.

### ASCII Visual Elements (Minimum 1 per Major Section, Currently ~15)
**Required types of visual elements:**
- System architecture diagrams (flowcharts showing data movement)
- Decision trees (routing logic, troubleshooting paths)
- Quick reference boxes (time estimates, cost breakdowns)
- Milestone celebration boxes (achievement markers)
- Navigation menus (section jump links)

**Example pattern:**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Stripe Webhook → Make.com → Printful API → Database → Email               │
│       ↓              ↓             ↓           ↓         ↓                  │
│  Validation    Transform    Submit Order   Log Event   Notify              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Visual hierarchy patterns:**
```
═══ for major section breaks
─── for subsection dividers
┌─┐ boxes for callouts and diagrams
✓ for completed items
□ for checklist items
→ for process flows
```

### Code Blocks with Context
Always include:
- Purpose and when to use
- Prerequisites and dependencies  
- Expected output/behavior
- Common errors and troubleshooting
- **Time to implement**

**Example from guide:**
```javascript
// Make.com webhook validation (prevents duplicate orders)
// Time: 5 minutes to configure
// Prevents: $460/year in duplicate fulfillment costs

const orderId = webhook.data.id;
const existing = await supabase
  .from('orders')
  .select('id')
  .eq('stripe_order_id', orderId);
  
if (existing.data.length > 0) {
  return { status: 'duplicate', skipped: true };
}

// Expected: 2.3% of webhooks are duplicates (caught here)
// If this fails: Orders process twice, customer charged once
```

## Key Workflows

### Content Expansion Workflow
1. Check `INTEGRATION_INDEX.md` for section status and word count gap
2. **Review existing Parts 0-3** to understand established patterns and voice
3. **Follow Part 2's structure** as the blueprint (it works well and should be replicated)
4. Add Production Reality callouts from real scenarios
5. Include specific metrics and time estimates for every step
6. Add ASCII diagrams for complex concepts
7. Run `format_cleaner.py` before committing
8. Update completion tracker in `INTEGRATION_INDEX.md`

### Structure Each Part Like Part 2
Part 2's structure is the template for new content:
- Overview with time/cost reality check
- Quick jump navigation menu
- Step-by-step implementation
- Production Reality callouts
- Validation checkpoints
- Milestone celebration at completion

### When Editing Existing Content
- **Canonical file**: `Splants_Guide_COMPLETE_DRAFT.txt` (36,000+ words, most current)
- Also update: `Splants_Guide_FINAL.txt` (maintain sync)
- Cross-reference `MASTER_INTEGRATION_SPECIFICATION.md` for requirements

### Quality Checklist (Before Any Commit)
- [ ] Zero em-dashes in body text
- [ ] Body hyphens only in allowed contexts
- [ ] Specific numbers (not "several," "many," "quickly")
- [ ] Time estimates for all tasks (e.g., "2 to 4 hours" not "short time")
- [ ] ASCII diagrams for complex concepts
- [ ] Production Reality callouts for failure modes
- [ ] Code blocks with troubleshooting notes and time estimates
- [ ] Milestone celebration boxes for achievements

## Critical Project Conventions

### Word Count Targets Are Guidelines
Each section should be comprehensive while remaining actionable. **Depth matters more than raw word count.** Example targets:
- Part 4 (Data Infrastructure): ~8,000 words
- Part 5 (Customer Experience): ~10,000 words
- Part 6 (Monitoring): ~8,000 words
- Part 7 (Scaling): ~12,000 words

### Tone: Experienced Developer to Developer
- Write in second person ("you check Stripe," not "developers check Stripe")
- Include production experience reports with specific failure scenarios
- Provide exact time/cost estimates with ROI calculations
- Assume reader knows programming but not this specific tech stack
- **Maintain welcoming, specific, professional voice** - no hyperbole or drama

### Visual Engagement Priority
The guide emphasizes visual learning:
- Minimum 1 ASCII diagram per major section (e.g., 2.1, 2.2, 2.3)
- Use boxes for warnings, separators for sections (see `ASCII_DIAGRAMS_LIBRARY.txt`)
- Decision matrices for comparisons (Printful vs Printify vs Gooten)
- Milestone celebration boxes to acknowledge achievements

## Integration Points & Dependencies

### External Services Documented
- **Stripe API** (v2024.10) - Payment webhooks, order data
- **Make.com** (current) - Workflow automation, API orchestration  
- **Printful/Printify/Gooten APIs** (v1) - Print-on-demand fulfillment with failover
- **Supabase** - PostgreSQL database, real-time features
- **Resend** - Transactional email service
- **Better Uptime** - Monitoring and alerting
- **Discord** - Team notifications

### Testing Approach
Each implementation section must include:
- Prerequisites validation
- Step-by-step testing procedures
- Expected outcomes with specific metrics
- Common failure modes and solutions
- Validation checkpoints

See `evaluation_framework.md`, `evaluation_quickstart.md`, `evaluation_test_scenarios.md` for:
- Assessment criteria for guide quality
- Quick start evaluation protocols
- 50+ test scenarios for validating automation logic

## Quick Commands

```bash
# Analyze formatting issues
python format_cleaner.py Splants_Guide_COMPLETE_DRAFT.txt

# Check word count for a section
wc -w <filename>

# Search for formatting violations
grep -n "—" Splants_Guide_COMPLETE_DRAFT.txt  # Find em-dashes
grep -n " - " Splants_Guide_COMPLETE_DRAFT.txt  # Find body hyphens
```

## When Creating New Content

1. **Identify the section** in `INTEGRATION_INDEX.md` (shows word count gap and priority)
2. **Read the template** in `PART_2_EXPANSION_TEMPLATE.txt` (demonstrates proper structure)
3. **Check existing content** in `Splants_Guide_COMPLETE_DRAFT.txt` (avoid duplication)
4. **Reference war stories** in `WAR_STORIES_COLLECTION.txt` (real failure scenarios with metrics)
5. **Apply formatting rules** from `STYLE_AND_FORMATTING_GUIDE.txt` (punctuation, diagrams, callouts)
6. **Validate before commit** using `format_cleaner.py`

## Files to Never Directly Edit
- `__azurite_db_blob__.json`, `__azurite_db_blob_extent__.json` - Azure storage emulator files
- Backup files: `Splants_Guide_REVISED.txt.backup`
- Historical versions: Only edit `Splants_Guide_COMPLETE_DRAFT.txt` as the canonical guide

## Current Gaps (Priority Order)

1. **Part 4:** Data and Analytics Infrastructure (0% complete, needs ~8,000 words)
2. **Part 5:** Customer Experience Automation (0% complete, needs ~10,000 words)
3. **Part 6:** Monitoring and Operations (0% complete, needs ~8,000 words)
4. **Part 7:** Scaling and Optimization (0% complete, needs ~12,000 words)
5. **Part 8:** Security and Compliance (0% complete, needs ~6,000 words)
6. **Appendices A-G:** (0% complete, needs ~8,000 words total)

## Success Metrics (From Specification)
- ✅ 100,000+ words total (currently ~36,000 in main guide)
- ✅ 75+ Production Reality callouts (currently ~25)
- ✅ 30+ ASCII diagrams (currently ~15)
- ✅ 100+ code blocks with context (currently ~40)
- ✅ 100+ error scenarios documented (currently ~35)
- ✅ Zero formatting violations (em-dashes, body hyphens)
- ✅ Complete implementation instructions that a beginner could follow

Reference `MASTER_INTEGRATION_SPECIFICATION.md` Section 15 for complete completion criteria.

## AI Agent Specific Guidance

When continuing the guide:
1. **Read existing Parts 0-3** to understand established patterns and voice
2. **Match the voice exactly**: welcoming, specific, professional (no hyperbole)
3. **Build on Part 2's success**: that structure clearly works
4. Avoid adding complexity that isn't justified by real needs
5. Include failure scenarios with specific costs and recovery times
6. Make every instruction actionable with exact steps
7. Test your formatting with the validation rules

**The goal is a guide that helps real people build real systems that process real money reliably.**
