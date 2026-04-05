# SEO Fix Plan: Create Allied Health Services
**Based on:** SEO Audit, Schema Report & Competitor Analysis (4 April 2026)
**Current Score:** 38/100 | **Target Score:** 85/100

---

## Phase 1 — Critical Fixes (Week 1-2)
*Goal: Stop the bleeding. Fix what's actively hurting visibility.*
*Expected score: 38 → 55*

### Step 1: Unblock AI Search Crawlers
**Where:** Squarespace → Settings → SEO → Search Engine Indexing
**What to do:**
1. Go to Settings > SEO in the Squarespace admin
2. Look for crawler/bot blocking settings or robots.txt customisation
3. Remove blocks on the following crawlers: GPTBot (ChatGPT), Google-Extended (Gemini/AI Overviews), ClaudeBot (Claude), PerplexityBot
4. If Squarespace doesn't offer granular control, check Settings > Advanced > robots.txt and ensure no `Disallow` rules target these bots
5. Verify by visiting `www.createalliedhealth.com.au/robots.txt` after saving — confirm the AI crawlers are no longer blocked

**Why first:** Every day these are blocked, the site is invisible to AI-powered search (ChatGPT, Google AI Overviews, Perplexity). This is the single highest-impact fix.

---

### Step 2: Fix Broken Sitemap URLs (3 dead pages)
**Where:** Squarespace page manager
**What to do:**
1. Find and delete or unpublish these 3 pages that return 404:
   - `/ndis-access-requests`
   - `/case-consultation`
   - `/student-supervision`
2. If these pages should exist, recreate them with proper content, titles, and meta descriptions
3. Remove the `/home` duplicate URL — ensure the homepage only lives at `/`
4. Identify and redirect or delete the 6 legacy pages from the old site structure that are competing with current pages
5. After changes, go to Settings > SEO > verify sitemap regenerates cleanly
6. Submit the updated sitemap to Google Search Console (`/sitemap.xml`)

---

### Step 3: Fix the "Accommodation" URL Typo
**Where:** Squarespace → Pages → Accommodation Support page → Settings → URL Slug
**What to do:**
1. Current URL: `/accomodation-support` (missing a "c")
2. Change the URL slug to: `accommodation-support`
3. Squarespace should auto-create a 301 redirect from the old URL — verify this
4. If not, manually add a 301 redirect: `/accomodation-support` → `/accommodation-support`
5. Update any internal links pointing to the old URL

**Why:** "NDIS accommodation support Sydney" is a high-value keyword. The misspelled URL prevents Google from matching it.

---

### Step 4: Fix Multiple H1 Tags (6+ pages)
**Where:** Each page in Squarespace editor
**What to do:**
1. **Homepage:** Identify the 4 elements tagged as H1. Keep only the primary heading as H1 (should be the main value proposition). Change the other 3 to H2 or H3.
2. **Service pages:** The "Take your first step" CTA block is set as H1 on 6 pages. Change it to H2 or a styled paragraph on every page it appears.
3. Each page should have exactly ONE H1 that describes that page's primary topic.
4. Audit all pages:
   - Homepage: 1x H1 (e.g., "NDIS Allied Health & Clinical Social Work in Sydney")
   - Each service page: 1x H1 matching the service name
   - About page: 1x H1
   - Contact page: 1x H1
   - Blog posts: 1x H1 (the post title)

---

### Step 5: Fix Broken Internal Link (Housing → Mental Health)
**Where:** Homepage or Services page — Housing & Accommodation section
**What to do:**
1. Find the "Learn More" button in the Housing & Accommodation section
2. It currently links to `/mental-health-services` — change it to `/accommodation-support` (or the corrected URL from Step 3)
3. Check all other internal "Learn More" buttons across the site to ensure they point to the correct pages

---

### Step 6: Fix /student-placement Content Mismatch
**Where:** Squarespace → Pages → Student Placement page
**What to do:**
1. This page was cloned from another page and still has the wrong H1, title tag, and meta description
2. Update the page title to: "Student Placement — Create Allied Health"
3. Update the H1 heading to match the actual content (e.g., "Social Work Student Placements")
4. Write a unique meta description (140-155 chars)

---

### Step 7: Update Copyright & Attribution
**Where:** Squarespace → Footer section
**What to do:**
1. Change "© 2023 by Liddy Creative Studio" to "© 2026 Create Allied Health Services"
2. If crediting the designer, use: "Website by Liddy Creative Studio" in small text, not in the copyright line

---

### Step 8: Fix Geographic Coordinates
**Where:** Squarespace → Settings → Business Information (or Location settings)
**What to do:**
1. The geo coordinates are currently set to New York City (Squarespace default)
2. Update to Sydney coordinates: Latitude: -33.8688, Longitude: 151.2093
3. Or enter the actual business address if there is one

---

## Phase 2 — Foundation Building (Weeks 3-6)
*Goal: Build the SEO infrastructure that enables ranking.*
*Expected score: 55 → 70*

### Step 9: Claim & Optimise Google Business Profile
**Where:** business.google.com
**What to do:**
1. Go to Google Business Profile and search for "Create Allied Health Services"
2. If unclaimed, claim it. If it doesn't exist, create it.
3. Complete ALL fields:
   - Business name: Create Allied Health Services
   - Category: Primary = "Allied Health Service" or "Social Worker" | Secondary = "Health Service", "NDIS Provider"
   - Address: Enter the business address (even if it's a service-area business, you need a verified address)
   - Service area: Sydney, Greater Sydney, NSW, Australia
   - Phone: 1800 930 350
   - Website: www.createalliedhealth.com.au
   - Hours: Set business hours
   - Description: Write a keyword-rich 750-character description mentioning NDIS, social work, psychosocial assessment, hospital discharge, Sydney
4. Upload 10+ photos: office, team, logo, branded images
5. Create a Google Business post introducing the practice
6. Set up the messaging and Q&A features

**Why critical:** No GBP = invisible in Google Maps and the Local Pack. Competitors have GBPs with 20+ reviews.

---

### Step 10: Implement Schema Markup (7 blocks)
**Where:** Squarespace → Settings → Advanced → Code Injection → Header (sitewide blocks) and individual page Code Blocks (page-specific blocks)

**What to do — follow this exact order:**

**Sitewide (paste in Header Code Injection):**
1. **Block A — WebSite schema** (replace Squarespace's broken auto-generated one) — fixes the http→https context error and protocol-relative image URL
2. **Block B — MedicalBusiness schema** (replace Squarespace's empty LocalBusiness) — adds business name, phone, email, address, services, founder
3. **Block C — Organization schema** — adds contact points, social profiles, logo

**Page-specific (paste in Code Blocks on each page):**
4. **Block D — Person schema for Kate Engledow** — add to the /about page only. Includes AASW credentials, PhD candidacy, expertise areas
5. **Block E — Service schema** — one per service page (6 total):
   - `/psychosocial-support` → "Psychosocial Assessment"
   - `/hospital-discharge` → "Hospital Discharge Planning"
   - `/accommodation-support` → "Accommodation Support"
   - `/guardianship-ncat` → "Guardianship and NCAT Support"
   - `/mental-health-services` → "Mental Health Services"
   - `/aged-care-transitions` → "Aged Care Transitions"
   - `/socialwork-supervision` → "Clinical Supervision"
6. **Block F — BreadcrumbList** — add to all service pages and blog posts
7. **Block G — FAQPage** — add to service pages after FAQ content is added (Phase 3)

All JSON-LD code is ready to copy-paste from the Schema Report document.

**Validation:** After adding each block, test at https://validator.schema.org and https://search.google.com/test/rich-results

---

### Step 11: Rewrite All Title Tags
**Where:** Squarespace → Pages → each page → Settings → SEO Title
**What to do — rewrite every page title under 60 characters:**

| Page | Current Title (truncated) | New Title |
|------|--------------------------|-----------|
| Homepage | Create Allied Health Services / Empower Your Journey | NDIS Allied Health & Social Work Sydney |
| /psychosocial-support | Psychosocial Assessment & Therapy... | Psychosocial Assessment Sydney - NDIS |
| /hospital-discharge | Hospital Discharge Planning Sydney... | Hospital Discharge Planning Sydney |
| /accommodation-support | Accommodation Support... | NDIS Accommodation Support Sydney |
| /guardianship-ncat | Guardianship and NCAT Support... | Guardianship & NCAT Social Work Sydney |
| /mental-health-services | Mental Health Support & Navigation... | Mental Health Services Sydney - NDIS |
| /aged-care-transitions | Aged Care Transitions... | Aged Care Transition Support Sydney |
| /socialwork-supervision | Clinical Supervision... | Clinical Social Work Supervision Sydney |
| /disability-services | Disability Services / Enhance Your... | NDIS Disability Services Sydney |
| /ndis-access-requests | Create Allied Health Services | NDIS Access Request Support Sydney |
| /about | About... | About - Kate Engledow, Clinical Social Worker |
| /contact | Contact... | Contact Create Allied Health - Sydney |

**Rules:**
- Under 60 characters
- Include primary keyword + "Sydney"
- Don't append " - Create Allied Health Services" (wastes characters)
- Front-load the keyword

---

### Step 12: Rewrite All Meta Descriptions
**Where:** Squarespace → Pages → each page → Settings → SEO Description
**What to do:**
1. Write unique, 140-155 character descriptions for every page
2. Include: primary keyword, "Sydney" or "Australia", a call-to-action
3. Fix the homepage duplicate description (same text appears twice)
4. Fill in empty blog post descriptions
5. Template: "[Service name] in Sydney by NDIS-registered clinical social workers. [Key benefit]. Call 1800 930 350."

---

### Step 13: Create Privacy Policy Page
**Where:** Squarespace → Pages → Create new page
**What to do:**
1. Create a new page at `/privacy-policy`
2. Write or use a template covering Australian Privacy Principles
3. Must cover: what data is collected, how it's used, how to request access, complaint procedures
4. For a healthcare provider this should reference the Privacy Act 1988 and Health Records
5. Add a link to the privacy policy in the footer
6. Also create a basic Terms of Service page at `/terms` if one doesn't exist

---

### Step 14: Add NDIS Registration Number
**Where:** Squarespace → Footer section + /ndis-services or equivalent page
**What to do:**
1. Add the NDIS registration number to the site footer (e.g., "NDIS Registered Provider #XXXXXXX")
2. Also display it prominently on the main NDIS services page
3. If there's an NDIS logo/badge, add it to the footer as well

---

### Step 15: Create Proper OG Social Sharing Image
**Where:** Squarespace → Settings → Social Sharing / Marketing → Social Image
**What to do:**
1. Create a 1200x630px image with:
   - Brand name "Create Allied Health Services"
   - Tagline "Empower Your Journey"
   - Professional photo or branded graphic
   - Not just the logo (current square logo gets cropped badly)
2. Set as the default OG image in Squarespace settings
3. Also set page-specific OG images for key service pages if possible

---

### Step 16: Add Geographic Keywords Throughout Content
**Where:** All pages — body content
**What to do:**
1. **Homepage:** Add "Sydney" at least 3-5 more times naturally. Mention "Greater Sydney", "NSW", "Australia"
2. **Service pages:** Add specific suburb and hospital references:
   - Westmead Hospital, Royal Prince Alfred (RPA), Liverpool Hospital, Concord Hospital
   - Inner West, Western Sydney, Eastern Suburbs, Northern Beaches
3. **About page:** Mention Sydney, the university (University of Sydney)
4. Don't keyword-stuff — weave naturally into sentences like "serving NDIS participants across Sydney's Inner West and Greater Western Sydney"

---

### Step 17: Create llms.txt File
**Where:** Squarespace doesn't natively support this — use Code Injection or a workaround
**What to do:**
1. Create an `llms.txt` file with a structured description of the business for AI crawlers
2. Content should include:
   - Business name, what it does, who it serves
   - Key services list
   - Founder credentials
   - Location and service area
   - How to describe the business (prevents AI hallucination)
3. If Squarespace can't serve a `.txt` file at the root, create a `/llms` page with the same content as a fallback

---

## Phase 3 — Growth & Authority (Months 2-6)
*Goal: Build the content engine and earn trust signals.*
*Expected score: 70 → 85*

### Step 18: Launch a Monthly Blog (Target: 12 posts in 6 months)
**Where:** Squarespace → Blog
**What to do:**
1. Publish 2 posts per month minimum, authored by Kate Engledow
2. Every post must have: author byline with credentials, publication date, category, meta description, OG image

**Suggested first 12 topics (keyword-targeted):**
1. "What Is a Psychosocial Assessment for NDIS?" (how-to, high search volume)
2. "Hospital Discharge Planning: What Families Need to Know" (guide)
3. "Understanding Guardianship and NCAT in NSW" (explainer)
4. "How NDIS Accommodation Support Works" (guide)
5. "When to Seek a Clinical Social Worker for NDIS" (decision guide)
6. "Navigating Aged Care Transitions: A Step-by-Step Guide" (guide)
7. "iCare and WorkCover: How Social Workers Can Help" (niche, low competition)
8. "Mental Health and the NDIS: What's Covered?" (FAQ-style)
9. "The Role of Allied Health in Hospital Discharge" (authority piece)
10. "NDIS Plan Reviews: How to Prepare" (practical guide)
11. "Trauma-Informed Practice in Social Work" (thought leadership)
12. "Clinical Supervision for Social Workers: What to Expect" (targeting supervision clients)

**Each post should:**
- Target a specific long-tail keyword
- Be 800-1500 words
- Include internal links to relevant service pages
- Have FAQ sections at the bottom (for Step 19)
- Mention Sydney/NSW where relevant

---

### Step 19: Add FAQ Sections to All Service Pages
**Where:** Each service page in Squarespace
**What to do:**
1. Add 3-5 FAQs to the bottom of every service page
2. Use question-based H2 or H3 headings (e.g., "What is a psychosocial assessment for NDIS?")
3. Write clear, concise answers (2-4 sentences each)
4. After adding the content, add FAQPage schema (Block G from Schema Report) to each page
5. These make content citable by AI search engines

**Example FAQs per page:**
- **Psychosocial Assessment:** What is it? Who needs one? How long does it take? What does it cost under NDIS? What happens after the assessment?
- **Hospital Discharge:** When should I contact a social worker? What does discharge planning include? Can NDIS fund this? How far in advance should I plan?
- **Accommodation Support:** What is SDA vs SIL? How do I apply for housing support? What does the assessment involve?

---

### Step 20: Build Google Reviews (Target: 10 in 3 months)
**Where:** Google Business Profile
**What to do:**
1. Create a direct review link from GBP and shorten it
2. Send the link to existing satisfied clients (with consent)
3. Add the review link to:
   - Email signatures
   - Post-service follow-up emails
   - The website footer or contact page
4. Respond to every review (positive or negative) within 48 hours
5. Target: 2-3 reviews per month

---

### Step 21: Submit to Healthcare Directories
**Where:** External sites
**What to do — create profiles on these directories:**
1. **HealthEngine** (healthengine.com.au) — major Australian health directory
2. **HotDoc** (hotdoc.com.au) — if applicable for bookings
3. **AASW Find a Social Worker** directory
4. **MyCareSpace** (mycarespace.com.au) — NDIS provider directory
5. **Clickability** (clickability.com.au) — NDIS provider directory
6. **Provider Choice** (providerchoice.com.au) — NDIS comparison
7. **Care & Ageing Well** directory — for aged care services

**For each directory:**
- Use the EXACT same business name, address, and phone (NAP consistency)
- Link back to the website
- Use the same business description
- Upload the logo and photos

---

### Step 22: Create Service Areas Page
**Where:** Squarespace → Pages → Create new page at `/service-areas`
**What to do:**
1. Create a dedicated page listing all areas served
2. Include:
   - Sydney suburbs by region (Inner West, Western Sydney, Eastern Suburbs, etc.)
   - Named hospitals served (Westmead, RPA, Liverpool, Concord)
   - Regional NSW via telehealth
   - National coverage note
3. Add internal links to relevant service pages from each area
4. This captures "near me" and suburb-specific search queries

---

### Step 23: Add Kate Engledow's Credentials to Blog Bylines
**Where:** Blog posts — author section
**What to do:**
1. Set up a detailed author bio for Kate that appears on every blog post
2. Include: "Kate Engledow, AASW-Registered Clinical Social Worker, PhD Candidate (University of Sydney), Founder of Create Allied Health Services"
3. Link the author bio to the /about page
4. For E-E-A-T, Google needs to see that health content is written by a qualified professional

---

### Step 24: Create Dedicated Landing Pages per Referral Source
**Where:** Squarespace → Pages
**What to do — create these new pages:**
1. `/ndis-social-worker-sydney` — targets the high-value "NDIS social worker Sydney" keyword
2. `/ndis-registered-provider` — targets "NDIS registered provider Sydney" comparison traffic
3. `/icare-social-work` — dedicated page for iCare/WorkCover referrals
4. Each page should have unique content, proper H1, title tag, meta description, and service schema

---

### Step 25: Add Case Studies / Anonymised Outcomes
**Where:** New section on service pages or a dedicated `/case-studies` page
**What to do:**
1. Create 3-5 anonymised case studies showing:
   - The situation/challenge
   - What Create Allied Health did
   - The outcome
2. These demonstrate "Experience" in E-E-A-T
3. Use real scenarios (with client consent and full anonymisation)
4. Format: short (300-500 words each), with clear headings

---

## Tracking & Measurement

### Set up these tools (if not already):
1. **Google Search Console** — monitor indexing, sitemap health, search queries
2. **Google Analytics 4** — track traffic sources, page performance
3. **Google Business Profile Insights** — track local search impressions

### Monthly check-ins:
- [ ] Sitemap: 0 errors in Search Console
- [ ] Schema: passes Rich Results Test for all pages
- [ ] Title tags: none truncated in SERP
- [ ] Blog: 2+ new posts published
- [ ] Reviews: 2-3 new Google reviews
- [ ] Rankings: check target keywords in incognito search

---

## Summary Checklist

| # | Task | Phase | Priority | Est. Time |
|---|------|-------|----------|-----------|
| 1 | Unblock AI crawlers | 1 | Critical | 15 min |
| 2 | Fix broken sitemap URLs | 1 | Critical | 30 min |
| 3 | Fix "accommodation" URL typo | 1 | Critical | 10 min |
| 4 | Fix multiple H1 tags | 1 | Critical | 1 hour |
| 5 | Fix broken internal link (housing) | 1 | Critical | 10 min |
| 6 | Fix /student-placement mismatch | 1 | High | 20 min |
| 7 | Update copyright & attribution | 1 | High | 5 min |
| 8 | Fix geo coordinates | 1 | High | 5 min |
| 9 | Claim Google Business Profile | 2 | Critical | 1-2 hours |
| 10 | Implement schema markup (7 blocks) | 2 | High | 2-3 hours |
| 11 | Rewrite all title tags | 2 | High | 1 hour |
| 12 | Rewrite all meta descriptions | 2 | High | 1 hour |
| 13 | Create privacy policy | 2 | High | 1-2 hours |
| 14 | Add NDIS registration number | 2 | High | 10 min |
| 15 | Create OG social sharing image | 2 | Medium | 30 min |
| 16 | Add geographic keywords to content | 2 | Medium | 2 hours |
| 17 | Create llms.txt file | 2 | Medium | 30 min |
| 18 | Launch monthly blog | 3 | High | Ongoing |
| 19 | Add FAQ sections + schema | 3 | High | 3-4 hours |
| 20 | Build Google reviews | 3 | High | Ongoing |
| 21 | Submit to healthcare directories | 3 | Medium | 2-3 hours |
| 22 | Create service areas page | 3 | Medium | 1-2 hours |
| 23 | Add credentials to blog bylines | 3 | Medium | 30 min |
| 24 | Create referral-source landing pages | 3 | Medium | 3-4 hours |
| 25 | Add case studies | 3 | Medium | 3-4 hours |

---

*Phase 1 (Steps 1-8): ~3 hours of work → Score 38 → 55*
*Phase 2 (Steps 9-17): ~10-12 hours of work → Score 55 → 70*
*Phase 3 (Steps 18-25): Ongoing over 2-6 months → Score 70 → 85*
