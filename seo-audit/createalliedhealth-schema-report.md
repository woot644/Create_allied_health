# Schema.org Audit — Create Allied Health Services
**URL:** https://www.createalliedhealth.com.au  
**Date:** 2026-04-04  
**Auditor:** Arclight Digital (Claude Schema Agent)

---

## Schema Score: 9 / 100

The site has the bare minimum Squarespace auto-generated schema present, but both blocks contain critical errors that prevent Google from using them effectively. No rich result types are implemented.

---

## 1. Detection Results

### Formats Present

| Format | Present |
|--------|---------|
| JSON-LD | Yes — 2 blocks (Squarespace auto-generated, sitewide) |
| Microdata | Yes — 5 attributes (Squarespace image component, not structured) |
| RDFa | No |

### Existing JSON-LD Block 1 — WebSite

```json
{
  "url": "https://www.createalliedhealth.com.au",
  "name": "Create Allied Health Services",
  "image": "//images.squarespace-cdn.com/...",
  "@context": "http://schema.org",
  "@type": "WebSite"
}
```

### Existing JSON-LD Block 2 — LocalBusiness

```json
{
  "address": "",
  "image": "https://static1.squarespace.com/...",
  "openingHours": "",
  "@context": "http://schema.org",
  "@type": "LocalBusiness"
}
```

---

## 2. Validation Results

### Block 1 — WebSite

| Check | Result | Detail |
|-------|--------|--------|
| @context is https | FAIL | Uses `http://schema.org` — must be `https://schema.org` |
| @type is valid | PASS | WebSite is valid |
| name present | PASS | "Create Allied Health Services" |
| url present | PASS | Absolute URL present |
| image URL is absolute | FAIL | Protocol-relative URL `//images.squarespace-cdn.com/...` — not an absolute URL |
| potentialAction (SearchAction) | MISSING | Recommended for Sitelinks Searchbox eligibility |

**Block 1 Verdict: 2 failures — not spec-compliant**

---

### Block 2 — LocalBusiness

| Check | Result | Detail |
|-------|--------|--------|
| @context is https | FAIL | Uses `http://schema.org` — must be `https://schema.org` |
| @type is valid | PASS | LocalBusiness is valid |
| name present | FAIL | Property is entirely absent |
| address present + populated | FAIL | Present but empty string — Google requires a valid PostalAddress object |
| telephone present | FAIL | Missing |
| email present | FAIL | Missing |
| url present | FAIL | Missing |
| description present | FAIL | Missing |
| openingHours | WARN | Empty string — omit entirely if not applicable for a service business |
| image absolute URL | WARN | URL lacks explicit https scheme prefix |
| sameAs (social profiles) | MISSING | Missing all social profile links |

**Block 2 Verdict: 5 failures, 2 warnings — effectively unusable by Google**

---

## 3. Schema Score Breakdown

| Category | Max | Score | Reason |
|----------|-----|-------|--------|
| WebSite schema | 10 | 3 | Exists but http context + non-absolute image |
| LocalBusiness/MedicalBusiness | 20 | 2 | Exists but missing name, address, phone, email |
| Organization / sameAs | 10 | 0 | Not implemented |
| Person (founder E-E-A-T) | 10 | 0 | Not implemented |
| Service schema (per service) | 15 | 0 | Not implemented |
| BreadcrumbList | 10 | 0 | Not implemented |
| FAQPage (AI value) | 10 | 0 | Not implemented |
| WebPage per page | 10 | 0 | Not implemented |
| Sitewide correctness bonus | 5 | 4 | Site uses JSON-LD format (correct), Squarespace auto-generates |
| **Total** | **100** | **9** | |

---

## 4. Missing Schema Opportunities

### Priority: CRITICAL

These fix broken existing schema or add high-impact types with direct Google rich result eligibility.

1. **Fix LocalBusiness → upgrade to MedicalBusiness** — Add name, address, telephone, email, url, description, sameAs. Switch @type to MedicalBusiness (subtype of LocalBusiness, appropriate for allied health providers).
2. **Fix WebSite** — Fix @context to https, fix image to absolute URL, add SearchAction.

### Priority: HIGH

These add structured data with significant SEO and E-E-A-T signal value.

3. **Organization** — Adds legal entity details, sameAs social links, and legalName. Strengthens Knowledge Panel eligibility.
4. **Person (Kate Engledow)** — Founder schema with credentials, jobTitle, alumniOf, sameAs. Critical for E-E-A-T signals in YMYL (health) content.
5. **Service schema** — One block per service page (psychosocial assessment, hospital discharge, housing support, etc.) with serviceType, provider, areaServed, audience.

### Priority: MEDIUM

6. **BreadcrumbList** — On all service and blog subpages. Enables breadcrumb display in Google SERPs.
7. **WebPage / MedicalWebPage** — On service pages and blog posts. MedicalWebPage with `specialty` is appropriate for health content pages.

### Priority: LOW / INFORMATIONAL

8. **FAQPage** — Restricted for Google rich results on commercial sites (August 2023). However, FAQPage schema is actively consumed by AI assistants and LLMs for citation. If GEO (Generative Engine Optimization) is a goal, implement on service pages that have FAQ sections. Do not expect a Google rich result from this on a commercial allied health site.

### Do NOT implement

- **HowTo** — Rich results removed September 2023
- **SpecialAnnouncement** — Deprecated July 31, 2025

---

## 5. Generated JSON-LD — Implementation Code

All blocks should be added via Squarespace's **Settings > Advanced > Code Injection > Header** section (for sitewide blocks) or via a **Code Block** on individual pages (for page-specific blocks).

---

### Block A — WebSite (replace existing, sitewide)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Create Allied Health Services",
  "url": "https://www.createalliedhealth.com.au",
  "description": "NDIS-registered allied health and clinical social work services in Sydney, Australia. Specialising in psychosocial assessment, hospital discharge planning, housing support, and mental health.",
  "image": {
    "@type": "ImageObject",
    "url": "https://images.squarespace-cdn.com/content/v1/6510f5d30064772b66aed216/4170c623-6c3a-4aa7-9025-5e288f2b625f/Create+Allied+Health+Logo.png"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.createalliedhealth.com.au/?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

---

### Block B — MedicalBusiness (replace existing LocalBusiness, sitewide)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "name": "Create Allied Health Services",
  "legalName": "Create Allied Health Services Pty Ltd",
  "url": "https://www.createalliedhealth.com.au",
  "logo": {
    "@type": "ImageObject",
    "url": "https://images.squarespace-cdn.com/content/v1/6510f5d30064772b66aed216/4170c623-6c3a-4aa7-9025-5e288f2b625f/Create+Allied+Health+Logo.png"
  },
  "image": "https://images.squarespace-cdn.com/content/v1/6510f5d30064772b66aed216/4170c623-6c3a-4aa7-9025-5e288f2b625f/Create+Allied+Health+Logo.png",
  "description": "NDIS-registered clinical social work and allied health provider. Specialising in psychosocial assessment, hospital discharge planning, housing support, guardianship and NCAT matters, mental health services, aged care transitions, and clinical supervision. Serving Sydney and nationally across Australia.",
  "telephone": "+611800930350",
  "email": "admin@createalliedhealth.com.au",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Sydney",
    "addressRegion": "NSW",
    "addressCountry": "AU"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Australia"
  },
  "medicalSpecialty": "MentalHealth",
  "hasMap": "https://www.google.com/maps/search/Create+Allied+Health+Services+Sydney",
  "sameAs": [
    "https://www.instagram.com/createalliedhealth",
    "https://www.tiktok.com/@createalliedhealth",
    "https://www.facebook.com/createalliedhealth",
    "https://www.youtube.com/@createalliedhealth"
  ],
  "founder": {
    "@type": "Person",
    "name": "Kate Engledow"
  },
  "priceRange": "$$"
}
</script>
```

> **Note:** Replace the `sameAs` social URLs with the exact profile URLs from the site. Replace `hasMap` with the actual Google Maps URL if a physical address is listed on the site.

---

### Block C — Organization (sitewide, complements MedicalBusiness)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Create Allied Health Services",
  "legalName": "Create Allied Health Services Pty Ltd",
  "url": "https://www.createalliedhealth.com.au",
  "logo": {
    "@type": "ImageObject",
    "url": "https://images.squarespace-cdn.com/content/v1/6510f5d30064772b66aed216/4170c623-6c3a-4aa7-9025-5e288f2b625f/Create+Allied+Health+Logo.png",
    "width": 300,
    "height": 100
  },
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+611800930350",
      "contactType": "customer service",
      "email": "admin@createalliedhealth.com.au",
      "areaServed": "AU",
      "availableLanguage": "English"
    },
    {
      "@type": "ContactPoint",
      "telephone": "+611800930350",
      "contactType": "referral",
      "areaServed": "AU",
      "availableLanguage": "English"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/createalliedhealth",
    "https://www.tiktok.com/@createalliedhealth",
    "https://www.facebook.com/createalliedhealth",
    "https://www.youtube.com/@createalliedhealth"
  ]
}
</script>
```

---

### Block D — Person: Kate Engledow (About page only)

Add this to the /about page via a Code Block.

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Kate Engledow",
  "url": "https://www.createalliedhealth.com.au/about",
  "jobTitle": "Founder & Clinical Social Worker",
  "description": "Kate Engledow is an AASW-registered clinical social worker and PhD candidate. She is the founder of Create Allied Health Services, an NDIS-registered allied health provider specialising in psychosocial assessment, hospital discharge planning, and social work practice in Sydney, Australia.",
  "worksFor": {
    "@type": "MedicalBusiness",
    "name": "Create Allied Health Services",
    "url": "https://www.createalliedhealth.com.au"
  },
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "credentialCategory": "Professional Membership",
      "recognizedBy": {
        "@type": "Organization",
        "name": "Australian Association of Social Workers (AASW)",
        "url": "https://www.aasw.asn.au"
      }
    }
  ],
  "knowsAbout": [
    "Clinical Social Work",
    "NDIS",
    "Psychosocial Assessment",
    "Hospital Discharge Planning",
    "Mental Health",
    "Guardianship and NCAT"
  ],
  "sameAs": [
    "https://www.instagram.com/createalliedhealth",
    "https://www.linkedin.com/in/kate-engledow"
  ]
}
</script>
```

> **Note:** Replace the LinkedIn URL with Kate's actual LinkedIn profile URL. Add or remove sameAs entries as appropriate.

---

### Block E — Service schema examples (one per service page)

Add the relevant block to each service page via a Code Block. Example for the Psychosocial Assessment page (`/psychosocial-support`):

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Psychosocial Assessment",
  "serviceType": "Psychosocial Assessment",
  "description": "Comprehensive psychosocial assessments for NDIS participants to identify functional capacity, support needs, and goals. Conducted by AASW-registered clinical social workers.",
  "provider": {
    "@type": "MedicalBusiness",
    "name": "Create Allied Health Services",
    "url": "https://www.createalliedhealth.com.au"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Australia"
  },
  "audience": {
    "@type": "Audience",
    "audienceType": "NDIS participants, people with disability, carers"
  },
  "url": "https://www.createalliedhealth.com.au/psychosocial-support"
}
</script>
```

Replicate this pattern for each service page, adjusting `name`, `serviceType`, `description`, and `url`:

| Page | name | serviceType |
|------|------|-------------|
| /hospital-discharge | Hospital Discharge Planning | Hospital Discharge Planning |
| /accomodation-support | Accommodation Support | NDIS Accommodation Support |
| /guardianship-ncat | Guardianship and NCAT Support | Guardianship and NCAT |
| /mental-health-services | Mental Health Services | Mental Health Social Work |
| /aged-care-transitions | Aged Care Transitions | Aged Care Transition Support |
| /socialwork-supervision | Clinical Supervision | Clinical Social Work Supervision |

---

### Block F — BreadcrumbList (service and blog subpages)

Add to each subpage. Example for `/hospital-discharge`:

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.createalliedhealth.com.au"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "NDIS Services",
      "item": "https://www.createalliedhealth.com.au/ndis-services"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Hospital Discharge Planning",
      "item": "https://www.createalliedhealth.com.au/hospital-discharge"
    }
  ]
}
</script>
```

---

### Block G — FAQPage (informational, AI/GEO value only)

**Important context:** Google restricted FAQPage rich results to government and health authority sites in August 2023. This schema will NOT produce a rich result in Google Search for this site. However, FAQPage markup is read by AI assistants (ChatGPT, Gemini, Perplexity) for cited answers and improves GEO (Generative Engine Optimization) discoverability. Implement only if AI citation is a priority for this client.

Example for a service page FAQ section:

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a psychosocial assessment for NDIS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A psychosocial assessment for NDIS is a detailed evaluation conducted by a qualified social worker or allied health professional to identify how a person's mental health condition affects their daily functioning and support needs. The assessment informs the NDIS planning process and supports funding decisions."
      }
    },
    {
      "@type": "Question",
      "name": "Is Create Allied Health Services an NDIS registered provider?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Create Allied Health Services is a registered NDIS provider offering clinical social work, psychosocial assessment, hospital discharge planning, and other allied health services across Australia."
      }
    },
    {
      "@type": "Question",
      "name": "Do you provide services outside of Sydney?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. While Create Allied Health Services is based in Sydney, NSW, we provide services nationally across Australia, including telehealth options for clients in regional and remote areas."
      }
    }
  ]
}
</script>
```

---

## 6. Implementation Notes for Squarespace

Squarespace does not allow direct editing of its auto-generated JSON-LD blocks (WebSite and LocalBusiness). The recommended approach is:

1. Go to **Settings > Advanced > Code Injection > Header**
2. Paste Blocks A, B, C (sitewide blocks) there — these will appear on every page
3. The Squarespace-generated blocks will still be present but your new, correct blocks will take precedence for Google's parser when both are present (Google uses the most complete/valid block)
4. For page-specific blocks (D, E, F, G): use a **Code Block** widget on the individual page and paste the JSON-LD inside `<script type="application/ld+json">` tags

**Squarespace limitation:** The built-in LocalBusiness block cannot be fully controlled. If Squarespace adds a feature to disable auto-schema in future, disable the built-in blocks and rely solely on your injected blocks to avoid duplicate @type conflicts.

---

## 7. Final Scoring Summary

| Before | After Implementation |
|--------|---------------------|
| 9 / 100 | Estimated 78–85 / 100 |

**What moves the needle most:**
1. Fix WebSite + MedicalBusiness (Blocks A + B) — highest Google impact
2. Add Organization sameAs (Block C) — Knowledge Panel eligibility
3. Add Person schema for Kate (Block D) — E-E-A-T in YMYL health niche
4. Add Service schema per page (Block E) — topical authority signals
5. Add BreadcrumbList (Block F) — SERP appearance enhancement
