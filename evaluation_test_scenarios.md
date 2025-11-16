# SPLANTS GUIDE: EVALUATION TEST SCENARIOS

## Purpose
This document provides detailed test scenarios for evaluating the Splants Automation Guide. Each scenario simulates realistic reader experiences and measures guide effectiveness.

---

## SCENARIO SET 1: FIRST TIME IMPLEMENTATION

### Scenario 1.1: Complete Beginner Journey

**Test Profile:**
- **Reader Type:** Solo entrepreneur, no coding experience
- **Starting Point:** Manual order processing, 30 to 50 orders/month
- **Technical Skills:** Can use Shopify/WordPress, no API experience
- **Available Time:** 2 to 3 hours daily, weeknights and weekends
- **Budget Constraint:** Under $50/month operational costs

**Test Procedure:**

**Day 1 (2 hours):**
1. Read introduction and mandatory sections
2. Assess emotional response to manual operations story
3. Evaluate understanding of system capabilities
4. Complete prerequisites checklist
5. **Log:** Clarity rating, motivation level, concerns raised

**Day 2 (3 hours):**
6. Read Part 0: Architecture Blueprint (if guide restructured per enhancement plan)
7. Attempt to draw system architecture from memory
8. Rate understanding of each component's purpose
9. **Log:** Architectural comprehension score, confusion points

**Day 3 to 5 (8 hours):**
10. Create Stripe account following guide
11. Set up test product and payment link
12. Complete test transaction
13. **Log:** Time per step, errors encountered, external resources needed

**Day 6 to 10 (12 hours):**
14. Create Make.com account
15. Build webhook receiver scenario
16. Configure webhook signature validation
17. Test webhook with Stripe
18. **Log:** Configuration challenges, Make.com operations consumed, success/failure

**Day 11 to 15 (15 hours):**
19. Create Printful account
20. Map product variants
21. Build order submission flow in Make.com
22. Test end to end order flow
23. **Log:** Variant mapping issues, API errors, order processing time

**Day 16 to 20 (10 hours):**
24. Set up Supabase database
25. Implement order logging
26. Build reconciliation query
27. Test data persistence
28. **Log:** Database schema clarity, SQL query challenges

**Day 21 to 25 (8 hours):**
29. Configure monitoring (Better Uptime, Discord)
30. Set up email notifications
31. Implement error alerting
32. Test all notification channels
33. **Log:** Alert configuration complexity, false positive rate

**Day 26 to 30 (5 hours):**
34. Deploy to production
35. Process first 10 real orders
36. Monitor system performance
37. Handle first production error
38. **Log:** Production deployment anxiety, error recovery success

**Success Metrics:**
- ✅ System deployed and processing orders
- ✅ Total time: 60 to 80 hours (within 2x of guide's 40 hour speed path)
- ✅ Total cost: $100 to $300 (within guide's projections)
- ✅ Order processing: 30 to 90 seconds average
- ✅ Error resolution: 70%+ resolved using guide
- ✅ Satisfaction: 4+/5
- ✅ Would continue using: Yes

**Failure Indicators:**
- ❌ Abandonment before deployment
- ❌ Major blocker requiring paid consulting
- ❌ System cannot process orders reliably
- ❌ Costs exceed $500
- ❌ Time exceeds 120 hours
- ❌ Satisfaction below 3/5

---

### Scenario 1.2: Technical Reader Sprint

**Test Profile:**
- **Reader Type:** Software developer building side project
- **Starting Point:** Validating product idea, expect 10 to 100 orders/month
- **Technical Skills:** Full stack developer, API/webhook experience
- **Available Time:** 30 hours concentrated over 1 week
- **Budget Constraint:** Under $200/month acceptable

**Test Procedure:**

**Day 1 (6 hours):**
1. Skim introduction for system overview
2. Deep read Part 0: Architecture (evaluate technical soundness)
3. Review service choices, consider alternatives
4. Critique architectural decisions
5. **Log:** Technical accuracy assessment, architectural concerns

**Day 2 (8 hours):**
6. Set up all service accounts (Stripe, Make.com, Printful, Supabase)
7. Configure development environment
8. Build payment flow with test mode
9. Implement webhook with signature validation
10. **Log:** Setup friction points, security implementation quality

**Day 3 (6 hours):**
11. Build Make.com orchestration scenario
12. Implement Printful integration with error handling
13. Add idempotency checking
14. Build database schema with proper indexes
15. **Log:** Schema design quality, performance considerations

**Day 4 (5 hours):**
16. Implement failover logic (Printful → Printify → Gooten)
17. Add retry mechanisms with exponential backoff
18. Configure monitoring and alerting
19. Build admin dashboard queries
20. **Log:** Redundancy implementation complexity, monitoring completeness

**Day 5 (5 hours):**
21. Write test suite (manual test cases)
22. Load test with simulated traffic
23. Deploy to production
24. Document architecture decisions
25. **Log:** Testing adequacy, production readiness, documentation gaps

**Success Metrics:**
- ✅ Production system deployed in under 40 hours
- ✅ All redundancy layers functional
- ✅ Performance meets or exceeds guide benchmarks (under 47s avg)
- ✅ Security best practices implemented
- ✅ System handles 100+ orders/day without manual intervention
- ✅ Technical architecture assessment: 4+/5

**Failure Indicators:**
- ❌ Significant architectural flaws discovered
- ❌ Security vulnerabilities in guide recommendations
- ❌ Performance below acceptable thresholds
- ❌ Scaling issues at low volumes
- ❌ Technical credibility concerns

---

## SCENARIO SET 2: ERROR RECOVERY TESTING

### Scenario 2.1: Common Integration Failures

**Objective:** Verify troubleshooting guidance resolves typical errors

**Pre-Condition:** Reader has basic system implemented (payment + fulfillment)

**Induced Errors:**

**Error 1: Webhook Signature Validation Failure**
- **Trigger:** Misconfigure webhook secret in Make.com
- **Expected Outcome:** Webhook calls rejected with 401
- **Test:** Can reader diagnose and fix using guide alone?
- **Time Limit:** 30 minutes
- **Success:** Fix applied, webhooks processing correctly
- **Log:** Troubleshooting path taken, time to resolution, guide section helpfulness

**Error 2: Printful Rate Limiting (429)**
- **Trigger:** Submit 10 orders rapidly to trigger rate limit
- **Expected Outcome:** API returns "Rate limit exceeded, retry after 60s"
- **Test:** Can reader identify cause and implement delay solution?
- **Time Limit:** 45 minutes
- **Success:** Rate limiting handled gracefully with retries
- **Log:** Error recognition speed, solution implementation quality

**Error 3: Duplicate Order Submission**
- **Trigger:** Stripe webhook fires twice for single payment
- **Expected Outcome:** Two orders sent to Printful without idempotency
- **Test:** Can reader recognize problem and implement idempotency check?
- **Time Limit:** 60 minutes
- **Success:** Idempotency key system prevents duplicates
- **Log:** Problem detection method, solution approach, prevention quality

**Error 4: Database Connection Pool Exhaustion**
- **Trigger:** Configure Supabase with minimal connections, spike traffic
- **Expected Outcome:** "Connection pool exhausted" errors
- **Test:** Can reader diagnose database issue and increase pool size?
- **Time Limit:** 30 minutes
- **Success:** Connection limits increased, no more pool errors
- **Log:** Diagnostic process, Supabase configuration clarity

**Error 5: Make.com Operations Limit Exceeded**
- **Trigger:** Approach 10K operations/month on free tier
- **Expected Outcome:** Scenarios stop executing, orders fail silently
- **Test:** Can reader identify limit, upgrade tier, recover lost orders?
- **Time Limit:** 45 minutes
- **Success:** Upgraded to Pro, identified and processed missed orders
- **Log:** Detection method (proactive monitoring vs reactive discovery), recovery completeness

**Aggregate Success Criteria:**
- ✅ 4 of 5 errors resolved without external help
- ✅ Average resolution time under 45 minutes
- ✅ All errors detected within 10 minutes (via monitoring or customer contact)
- ✅ No data loss or customer impact lasting over 1 hour

---

### Scenario 2.2: Production Crisis Simulation

**Objective:** Test incident response guidance under pressure

**Setup:** System in production, processing 20 to 50 orders/day

**Crisis Event:** Printful Unplanned Outage (simulate 4 hour downtime)

**Timeline:**

**T+0 minutes (Outage Begins):**
- Printful API returns 503 Service Unavailable
- Orders start queueing or failing
- **Test:** Does monitoring detect outage within 5 minutes?

**T+5 minutes (Detection):**
- Reader becomes aware via monitoring alert
- **Test:** Does guide provide clear incident response steps?
- **Expected Actions:** 
  1. Verify outage (check Printful status page)
  2. Activate failover to Printify
  3. Notify customers of potential delays
  4. Log incident details

**T+15 minutes (Response):**
- Reader implements failover routing
- **Test:** Can failover be activated without losing queued orders?
- **Success:** All orders route to Printify automatically

**T+30 minutes (Communication):**
- Reader sends customer communications
- **Test:** Does guide provide email templates for delays?
- **Success:** Professional delay notifications sent

**T+240 minutes (Recovery):**
- Printful comes back online
- **Test:** Can reader safely switch back to Printful?
- **Success:** Gradual rollback without duplicate orders

**T+24 hours (Post-Mortem):**
- Reader documents incident and improvements
- **Test:** Does guide provide post-mortem framework?
- **Success:** Lessons learned documented, system hardened

**Success Metrics:**
- ✅ Outage detected within 5 minutes
- ✅ Failover activated within 20 minutes
- ✅ Zero orders lost
- ✅ Customer communication sent within 30 minutes
- ✅ Post-mortem completed with action items

---

## SCENARIO SET 3: SCALING VALIDATION

### Scenario 3.1: Growth Progression

**Objective:** Verify guide prepares readers for each scaling breakpoint

**Test Procedure:**

**Phase 1: Low Volume (10 orders/day)**
- Implement basic system on free tiers
- Monitor costs and performance
- **Metrics:** $0/month operational, under 50s processing avg
- **Validation:** System stable, no optimization needed

**Phase 2: Approach First Breakpoint (40 to 47 orders/day)**
- Gradually increase volume
- **Expected Event:** Rate limiting errors appear
- **Test Questions:**
  - Does guide predict this breakpoint accurately?
  - Is solution (2s delay between calls) documented?
  - Can reader implement preventatively before crisis?
- **Success:** Delay implemented, no customer impact

**Phase 3: Service Tier Exhaustion (200 to 218 orders/day)**
- Continue volume growth
- **Expected Event:** Make.com free tier exhausted mid-month
- **Test Questions:**
  - Does guide recommend proactive upgrade threshold?
  - Is cost increase ($0 → $16/month) clearly communicated?
  - Can reader detect usage approaching limit?
- **Success:** Upgraded at 80% capacity, no service interruption

**Phase 4: Reconciliation Breakdown (450 to 500 orders/day)**
- Reach high volume
- **Expected Event:** Manual Friday reconciliation takes 4+ hours
- **Test Questions:**
  - Does guide recommend automated reconciliation before this point?
  - Are SQL queries or scripts provided?
  - Can reader implement without disrupting operations?
- **Success:** Automated reconciliation running, Friday check under 15 minutes

**Phase 5: Database Limits (1,000 to 1,100 orders/day)**
- Push to max free tier capacity
- **Expected Event:** Supabase connection pool exhaustion
- **Test Questions:**
  - Is this limit documented in advance?
  - Is migration to paid tier ($0 → $25/month) explained?
  - Is downtime minimized during upgrade?
- **Success:** Migrated to paid tier with under 10 minutes downtime

**Success Criteria:**
- ✅ All 4 breakpoints predicted within 10% of actual volume
- ✅ Solutions documented before crises occur
- ✅ Reader implements 3 of 4 proactively (not reactively)
- ✅ Total unplanned downtime under 30 minutes across all scaling
- ✅ Costs align with guide projections (within 20%)

---

## SCENARIO SET 4: ALTERNATIVE PATHS

### Scenario 4.1: Speed Build Path (MVO)

**Reader Goal:** Deploy minimal viable system in 40 hours

**Allowed Scope:**
- Stripe payment capture
- Single fulfillment provider (Printful only)
- Basic email confirmation
- Minimal error handling
- No redundancy
- No monitoring (beyond service dashboards)

**Test Procedure:**
1. Skip Part 0 (architecture theory)
2. Skip service comparison analysis
3. Implement fastest path from guide
4. Deploy to production at minimum viable
5. Track: Time, costs, stability, technical debt

**Success Metrics:**
- ✅ Deployed in under 40 hours
- ✅ Costs under $100 (mostly mistake budget)
- ✅ Processes orders successfully 90%+ of time
- ✅ Reader understands limitations accepted
- ✅ Clear path to enhance later documented

**Known Tradeoffs:**
- ⚠️ No failover (Printful outage = business down)
- ⚠️ Limited error handling (manual recovery needed)
- ⚠️ No automated monitoring (reactive not proactive)
- ⚠️ Will need enhancements within 2 to 3 months

---

### Scenario 4.2: Complete Build Path (Production Stable)

**Reader Goal:** Deploy production-ready system with all redundancy in 100 hours

**Required Scope:**
- Comprehensive architecture understanding
- Multi-provider failover (Printful, Printify, Gooten)
- Complete error handling and retries
- Idempotency checking
- Monitoring and alerting
- Database with proper schema
- Automated reconciliation
- Email templates for all scenarios

**Test Procedure:**
1. Read all theoretical sections (Part 0)
2. Evaluate all service choices
3. Implement complete system with redundancy
4. Thorough testing before production
5. Track: Time, costs, stability, confidence

**Success Metrics:**
- ✅ Deployed in 80 to 120 hours
- ✅ Costs under $300 total implementation
- ✅ Processes orders successfully 98%+ of time
- ✅ Survives first provider outage with zero customer impact
- ✅ Monitoring catches all errors within 5 minutes
- ✅ Reader highly confident in system

**Expected Outcomes:**
- ✅ System stable for 6+ months without major changes
- ✅ Handles scale to 500+ orders/day without modifications
- ✅ Fewer than 2 critical incidents in first quarter
- ✅ Reader becomes resource for others

---

### Scenario 4.3: Progressive Build Path (Learning Focused)

**Reader Goal:** Build understanding through staged implementation over 150 hours

**Staged Approach:**

**Stage 1 (Week 1-2, 30 hours): Payment Only**
- Deep understanding of payment flow
- Stripe setup with test mode
- Webhook fundamentals
- Manual fulfillment still
- **Outcome:** Can explain payment capture architecture

**Stage 2 (Week 3-4, 40 hours): Add Fulfillment**
- Printful integration
- Order data mapping
- Error handling basics
- **Outcome:** End-to-end automation for happy path

**Stage 3 (Week 5-6, 30 hours): Add Redundancy**
- Failover logic
- Printify and Gooten setup
- Provider health checking
- **Outcome:** Resilient to single provider failure

**Stage 4 (Week 7-10, 50 hours): Add Intelligence**
- Monitoring and alerting
- Analytics and reporting
- Automated reconciliation
- Performance optimization
- **Outcome:** Observable, optimized, maintainable system

**Test Procedure:**
1. Complete each stage fully before proceeding
2. Test thoroughly at each stage
3. Document learnings in personal notes
4. Optional: Small production traffic at each stage

**Success Metrics:**
- ✅ Highest comprehension scores across all paths
- ✅ Lowest stress and anxiety reported
- ✅ Best able to explain system to others
- ✅ Most prepared for future modifications
- ✅ Builds correct mental models of distributed systems

**Tradeoff:**
- ⚠️ Longest time to full production (10 weeks vs 4 weeks)
- ⚠️ Most total hours invested (150 vs 100 vs 40)

---

## SCENARIO SET 5: EDGE CASES AND STRESS TESTS

### Scenario 5.1: Payment Edge Cases

**Test Cases:**

1. **Disputed Charge After Fulfillment**
   - Customer initiates chargeback 3 days after receiving product
   - **Test:** Does guide address dispute handling?
   - **Expected:** Clear process for handling Stripe disputes, Printful can't retrieve product

2. **Failed Payment After Submission**
   - Payment authorized but capture fails
   - **Test:** Does system prevent fulfillment?
   - **Expected:** Order not sent to Printful, customer notified

3. **Partial Refund Request**
   - Customer wants refund for 1 item in 3 item order
   - **Test:** Does guide cover partial refunds?
   - **Expected:** Process documented or acknowledged as manual

4. **Currency Conversion Issues**
   - International customer, payment in EUR, costs in USD
   - **Test:** Are currency considerations addressed?
   - **Expected:** Stripe handling explained, or flagged as complexity

---

### Scenario 5.2: Fulfillment Edge Cases

**Test Cases:**

1. **Out of Stock Variant**
   - Customer orders product, Printful shows variant unavailable
   - **Test:** Does system detect and handle gracefully?
   - **Expected:** Customer notified, alternatives offered or refund processed

2. **All Providers Simultaneously Down**
   - Printful, Printify, and Gooten all experiencing outages (rare but possible)
   - **Test:** Does guide provide guidance for total failover failure?
   - **Expected:** Queuing strategy, customer communication templates

3. **Address Validation Failure**
   - Customer provides invalid or incomplete shipping address
   - **Test:** Does system catch before submission or handle rejection?
   - **Expected:** Validation logic or error recovery process

4. **International Shipping Restrictions**
   - Order to country not supported by provider
   - **Test:** Are geographic restrictions addressed?
   - **Expected:** Pre-order validation or fallback to manual handling

---

### Scenario 5.3: High Volume Stress Test

**Setup:** Simulate Black Friday or viral product launch

**Scenario Parameters:**
- Normal volume: 30 orders/day
- Spike volume: 500 orders in 4 hours (125/hour, 2/minute)
- Duration: 4 to 6 hours
- Return to normal after spike

**Test Questions:**
1. Does guide prepare reader for traffic spikes?
2. Will system handle 10x volume without manual intervention?
3. What breaks first? (API rate limits, database, Make.com capacity)
4. Can reader recover quickly?
5. Is cost spike ($25/month → $100/month) predictable?

**Success Criteria:**
- ✅ All orders processed successfully (possibly with delays)
- ✅ No orders lost or duplicated
- ✅ System recovers automatically after spike
- ✅ Reader aware of spike handling before it happens
- ✅ Costs increase explained in guide

---

## SCENARIO SET 6: LONG TERM MAINTENANCE

### Scenario 6.1: 6 Month Check-In

**Setup:** Reader has system running 6 months, processing 100 to 300 orders/month

**Test Areas:**

1. **System Stability:**
   - Uptime over 6 months: Target 99%+
   - Critical incidents: Target fewer than 3
   - Manual interventions: Target fewer than 5/month

2. **Cost Accuracy:**
   - Actual costs vs guide projections
   - Unexpected cost creep identified
   - Optimization opportunities realized

3. **Time Savings:**
   - Hours saved weekly: Target 15+
   - Time spent on maintenance: Target under 2 hours/week
   - ROI realized vs projected

4. **Technical Debt:**
   - Issues from shortcuts taken
   - Need for refactoring or upgrades
   - Guide preparation for maintenance phase

**Success Indicators:**
- ✅ System still operational without major overhauls
- ✅ Reader satisfied with time/cost savings
- ✅ Confidence to modify and optimize independently
- ✅ Would repeat implementation decision

---

### Scenario 6.2: Service Migration Necessity

**Trigger Event:** Major service changes requiring migration

**Examples:**
- Stripe raises fees by 30%
- Make.com discontinues free tier
- Printful changes TOS or pricing structure
- Supabase requires database migration

**Test Questions:**
1. Does guide acknowledge vendor lock-in risks?
2. Are exit strategies documented?
3. Can reader migrate with minimal disruption?
4. Is data exportable and portable?

**Success Criteria:**
- ✅ Reader aware of migration complexity before starting
- ✅ Data can be exported from all services
- ✅ Alternative services identified in guide
- ✅ Migration possible within 20 to 40 hours

---

## EVALUATION SCORING GUIDE

### For Each Scenario:

**Pass:** All success criteria met, no failure indicators triggered  
**Conditional Pass:** Most success criteria met, minor issues recoverable  
**Fail:** One or more failure indicators triggered, success criteria not met  

### Overall Guide Assessment:

| Pass Rate | Guide Status | Action Required |
|-----------|--------------|-----------------|
| 90%+ scenarios pass | Excellent | Minor refinements only |
| 75-89% pass | Good | Address failing scenarios |
| 60-74% pass | Needs Work | Significant improvements needed |
| Below 60% pass | Poor | Major revision required |

---

## APPENDIX: DATA COLLECTION TEMPLATES

### Template A: Scenario Test Report

```
SCENARIO: [ID and Name]
TESTER: [Persona type]
DATE: [Test date]

PRE-TEST:
- Technical skill level: [1-10]
- Time available: [Hours]
- Budget: $[Amount]
- Starting confidence: [1-10]

EXECUTION LOG:
[Timestamped actions, decisions, blockers]

09:00 - Started scenario
09:15 - Completed step 1, no issues
09:45 - Stuck on step 2, guide unclear about [specific issue]
10:30 - Resolved via external resource: [link]
[Continue...]

METRICS ACHIEVED:
- Time spent: [Hours] (vs expected: [Hours])
- Cost incurred: $[Amount]
- Success: [Yes/No/Partial]
- External resources needed: [Count]

GUIDE FEEDBACK:
Helpful sections: [List]
Confusing sections: [List]
Missing information: [List]
Errors found: [List]

SATISFACTION:
- Overall: [1-5]
- Would recommend: [Yes/No]
- Confidence after: [1-10]

PASS/FAIL: [Assessment]
NOTES: [Additional context]
```

---

**Document Version:** 1.0  
**Last Updated:** November 16, 2025  
**Purpose:** Structured testing scenarios for Splants Guide evaluation  
**Usage:** Select scenarios matching evaluation goals, execute with target personas, aggregate results
