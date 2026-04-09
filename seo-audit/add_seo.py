"""
Add SEO infrastructure to all HTML pages:
- OG tags, Twitter Cards, canonical links
- Schema JSON-LD (sitewide + page-specific)
- Updated footer (copyright 2026, NDIS reg, privacy link)
- Favicon link
"""
import os
import re

BASE_URL = "https://www.createalliedhealth.com.au"
ROOT = r"C:\Users\zacen\Python\vibe_coding\allied_health"

# Page-specific SEO data
PAGES = {
    "index.html": {
        "title": "NDIS Allied Health & Clinical Social Work Sydney | Create Allied Health",
        "desc": "NDIS-registered allied health provider in Sydney. Psychosocial assessments, hospital discharge planning, housing support, and clinical supervision across Australia. Call 1800 930 350.",
        "canonical": f"{BASE_URL}/",
        "og_title": "Create Allied Health Services — Empower Your Journey",
        "schema_extra": "",
    },
    "about.html": {
        "title": "About Kate Engledow & Our Team | Create Allied Health Services",
        "desc": "Meet Kate Engledow, AASW-registered clinical social worker and PhD candidate. Learn about our person-centred approach to complex allied health cases in Sydney.",
        "canonical": f"{BASE_URL}/about.html",
        "og_title": "About Us — Create Allied Health Services",
        "schema_extra": "person",
    },
    "contact.html": {
        "title": "Contact Create Allied Health | Sydney NDIS Provider",
        "desc": "Get in touch with Create Allied Health Services. Call 1800 930 350 or email admin@createalliedhealth.com.au. Sydney-based, serving all of Australia.",
        "canonical": f"{BASE_URL}/contact.html",
        "og_title": "Contact Us — Create Allied Health Services",
        "schema_extra": "",
    },
    "referrals.html": {
        "title": "Refer a Client | Create Allied Health Services Sydney",
        "desc": "Refer a client to Create Allied Health Services. NDIS, iCare, WorkCover, and private referrals accepted. Simple online referral form for allied health professionals.",
        "canonical": f"{BASE_URL}/referrals.html",
        "og_title": "Refer a Client — Create Allied Health Services",
        "schema_extra": "",
    },
    "careers.html": {
        "title": "Careers in Allied Health | Join Create Allied Health Sydney",
        "desc": "Join our team of clinical social workers and allied health professionals in Sydney. Current openings for OTs, counsellors, and social workers.",
        "canonical": f"{BASE_URL}/careers.html",
        "og_title": "Careers — Create Allied Health Services",
        "schema_extra": "",
    },
    "blog.html": {
        "title": "Allied Health Insights & Resources | Create Allied Health Blog",
        "desc": "Expert insights on NDIS, psychosocial support, hospital discharge planning, and clinical social work from Create Allied Health Services in Sydney.",
        "canonical": f"{BASE_URL}/blog.html",
        "og_title": "Blog — Create Allied Health Services",
        "schema_extra": "",
    },
    "ndis-services.html": {
        "title": "NDIS Services Sydney | Registered Provider | Create Allied Health",
        "desc": "NDIS-registered allied health services in Sydney. Access requests, therapeutic supports, plan reviews, and coordinated care from qualified clinical social workers.",
        "canonical": f"{BASE_URL}/ndis-services.html",
        "og_title": "NDIS Services — Create Allied Health Services",
        "schema_extra": "service",
        "service_name": "NDIS Allied Health Services",
        "service_type": "NDIS Support Services",
        "service_desc": "NDIS-registered allied health services including access requests, therapeutic supports, plan reviews, and coordinated care across Sydney and Australia.",
    },
    "psychosocial-support.html": {
        "title": "Psychosocial Assessment Sydney | NDIS | Create Allied Health",
        "desc": "Comprehensive psychosocial assessments and therapeutic intervention for NDIS participants, iCare/WorkCover clients, and complex cases in Sydney. Trauma-informed approach.",
        "canonical": f"{BASE_URL}/psychosocial-support.html",
        "og_title": "Psychosocial Assessment & Support — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Psychosocial Assessment & Therapeutic Intervention",
        "service_type": "Psychosocial Assessment",
        "service_desc": "Comprehensive psychosocial assessments for NDIS participants and complex cases. Trauma-informed, strength-based therapeutic intervention by AASW-registered clinical social workers in Sydney.",
    },
    "hospital-discharge.html": {
        "title": "Hospital Discharge Planning Sydney | iCare | Create Allied Health",
        "desc": "Expert hospital discharge and rehabilitation planning in Sydney. iCare, WorkCover, and NDIS. Smooth transitions from hospital to home or community living.",
        "canonical": f"{BASE_URL}/hospital-discharge.html",
        "og_title": "Hospital Discharge & Rehabilitation — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Hospital Discharge & Rehabilitation Planning",
        "service_type": "Hospital Discharge Planning",
        "service_desc": "Specialist hospital discharge planning and rehabilitation coordination in Sydney. Supporting smooth transitions from hospital to home or community for iCare, WorkCover, and NDIS clients.",
    },
    "housing-support.html": {
        "title": "NDIS Housing & Accommodation Support Sydney | Create Allied Health",
        "desc": "NDIS housing navigation, SDA and SIL assessments, accommodation support, and NCAT applications in Sydney. Expert support for complex housing needs.",
        "canonical": f"{BASE_URL}/housing-support.html",
        "og_title": "Housing & Accommodation Support — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Housing & Accommodation Support",
        "service_type": "NDIS Accommodation Support",
        "service_desc": "NDIS housing and accommodation support in Sydney. SDA and SIL assessments, housing navigation, tenancy support, and NCAT housing applications for people with complex needs.",
    },
    "guardianship-ncat.html": {
        "title": "Guardianship & NCAT Social Work Sydney | Create Allied Health",
        "desc": "Expert guardianship and NCAT support in Sydney. Capacity assessments, tribunal reports, and legal navigation by experienced clinical social workers.",
        "canonical": f"{BASE_URL}/guardianship-ncat.html",
        "og_title": "Guardianship & NCAT Support — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Guardianship & NCAT Support",
        "service_type": "Guardianship and NCAT Support",
        "service_desc": "Specialist guardianship and NCAT support in Sydney. Capacity assessments, tribunal reports, advocacy, and legal system navigation by AASW-registered clinical social workers.",
    },
    "aged-care-transitions.html": {
        "title": "Aged Care Transitions Sydney | Hospital to Residential | Create Allied Health",
        "desc": "Aged care transition support in Sydney. Hospital-to-aged-care pathways, residential placement decisions, and family support by qualified clinical social workers.",
        "canonical": f"{BASE_URL}/aged-care-transitions.html",
        "og_title": "Aged Care Transitions — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Aged Care Transition Support",
        "service_type": "Aged Care Transition Support",
        "service_desc": "Aged care transition support in Sydney. Hospital-to-residential care pathways, placement assessments, family mediation, and My Aged Care navigation by experienced social workers.",
    },
    "mental-health-support.html": {
        "title": "Mental Health Support Sydney | NDIS Psychosocial | Create Allied Health",
        "desc": "Mental health support and psychosocial disability services in Sydney. Family mediation, substance use support, crisis intervention, and NDIS mental health navigation.",
        "canonical": f"{BASE_URL}/mental-health-support.html",
        "og_title": "Mental Health Support — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Mental Health Support & Navigation",
        "service_type": "Mental Health Social Work",
        "service_desc": "Mental health support and psychosocial disability services in Sydney. Family mediation, advocacy, crisis intervention, and NDIS mental health navigation by clinical social workers.",
    },
    "supervision.html": {
        "title": "Clinical Social Work Supervision Sydney | AASW | Create Allied Health",
        "desc": "AASW-accredited clinical supervision for social workers in Sydney. Individual and group supervision from experienced clinical social worker Kate Engledow.",
        "canonical": f"{BASE_URL}/supervision.html",
        "og_title": "Clinical Supervision — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Clinical Social Work Supervision",
        "service_type": "Clinical Supervision",
        "service_desc": "AASW-accredited clinical supervision for social workers in Sydney. Individual and group supervision, reflective practice, and professional development from Kate Engledow.",
    },
    "service-packages.html": {
        "title": "Student Placements & Case Consultation | Create Allied Health Sydney",
        "desc": "Social work student placements and professional case consultation services in Sydney. Field education and specialist consultation for allied health professionals.",
        "canonical": f"{BASE_URL}/service-packages.html",
        "og_title": "Service Packages — Create Allied Health",
        "schema_extra": "service",
        "service_name": "Student Placements & Case Consultation",
        "service_type": "Professional Consultation",
        "service_desc": "Social work student placements and case consultation services in Sydney. Field education placements and specialist case consultation for allied health professionals.",
    },
}


def build_sitewide_schema():
    """WebSite + MedicalBusiness + Organization — injected on every page."""
    return '''
    <!-- Schema: WebSite -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Create Allied Health Services",
      "url": "https://www.createalliedhealth.com.au",
      "description": "NDIS-registered allied health and clinical social work services in Sydney, Australia.",
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
    <!-- Schema: MedicalBusiness -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "MedicalBusiness",
      "name": "Create Allied Health Services",
      "legalName": "Create Allied Health Services Pty Ltd",
      "url": "https://www.createalliedhealth.com.au",
      "description": "NDIS-registered clinical social work and allied health provider specialising in psychosocial assessment, hospital discharge planning, housing support, guardianship, aged care transitions, and mental health services in Sydney and nationally across Australia.",
      "telephone": "1800 930 350",
      "email": "admin@createalliedhealth.com.au",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Sydney",
        "addressRegion": "NSW",
        "addressCountry": "AU"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": -33.8688,
        "longitude": 151.2093
      },
      "areaServed": {
        "@type": "Country",
        "name": "Australia"
      },
      "medicalSpecialty": "MentalHealth",
      "founder": {
        "@type": "Person",
        "name": "Kate Engledow"
      },
      "sameAs": [
        "https://www.instagram.com/createalliedhealth",
        "https://www.facebook.com/createalliedhealth"
      ],
      "priceRange": "$$"
    }
    </script>
    <!-- Schema: Organization -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Create Allied Health Services",
      "legalName": "Create Allied Health Services Pty Ltd",
      "url": "https://www.createalliedhealth.com.au",
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "1800 930 350",
        "contactType": "customer service",
        "email": "admin@createalliedhealth.com.au",
        "areaServed": "AU",
        "availableLanguage": "English"
      },
      "sameAs": [
        "https://www.instagram.com/createalliedhealth",
        "https://www.facebook.com/createalliedhealth"
      ]
    }
    </script>'''


def build_person_schema():
    """Kate Engledow — about page only."""
    return '''
    <!-- Schema: Person (Kate Engledow) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Kate Engledow",
      "url": "https://www.createalliedhealth.com.au/about.html",
      "jobTitle": "Founder & Clinical Social Worker",
      "description": "Kate Engledow is an AASW-registered clinical social worker, PhD candidate at the University of Sydney, and founder of Create Allied Health Services.",
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
      "knowsAbout": ["Clinical Social Work", "NDIS", "Psychosocial Assessment", "Hospital Discharge Planning", "Mental Health", "Guardianship and NCAT", "Aged Care Transitions"]
    }
    </script>'''


def build_service_schema(page_data, filename):
    """Service schema for each service page."""
    return f'''
    <!-- Schema: Service -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "{page_data['service_name']}",
      "serviceType": "{page_data['service_type']}",
      "description": "{page_data['service_desc']}",
      "provider": {{
        "@type": "MedicalBusiness",
        "name": "Create Allied Health Services",
        "url": "https://www.createalliedhealth.com.au"
      }},
      "areaServed": {{
        "@type": "Country",
        "name": "Australia"
      }},
      "url": "{BASE_URL}/{filename}"
    }}
    </script>'''


def build_breadcrumb_schema(page_title, filename):
    """BreadcrumbList for subpages."""
    return f'''
    <!-- Schema: BreadcrumbList -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.createalliedhealth.com.au"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{page_title}",
          "item": "{BASE_URL}/{filename}"
        }}
      ]
    }}
    </script>'''


def build_meta_block(page_data, filename):
    """Build OG, Twitter, canonical, and schema for a page."""
    og_title = page_data.get("og_title", page_data["title"])
    lines = []

    # Canonical
    lines.append(f'    <link rel="canonical" href="{page_data["canonical"]}">')

    # OG tags
    lines.append(f'    <meta property="og:title" content="{og_title}">')
    lines.append(f'    <meta property="og:description" content="{page_data["desc"]}">')
    lines.append(f'    <meta property="og:url" content="{page_data["canonical"]}">')
    lines.append(f'    <meta property="og:type" content="website">')
    lines.append(f'    <meta property="og:site_name" content="Create Allied Health Services">')
    lines.append(f'    <meta property="og:locale" content="en_AU">')

    # Twitter
    lines.append(f'    <meta name="twitter:card" content="summary_large_image">')
    lines.append(f'    <meta name="twitter:title" content="{og_title}">')
    lines.append(f'    <meta name="twitter:description" content="{page_data["desc"]}">')

    # Geo
    lines.append(f'    <meta name="geo.region" content="AU-NSW">')
    lines.append(f'    <meta name="geo.placename" content="Sydney">')
    lines.append(f'    <meta name="geo.position" content="-33.8688;151.2093">')
    lines.append(f'    <meta name="ICBM" content="-33.8688, 151.2093">')

    result = "\n".join(lines)

    # Schema — sitewide on every page
    result += build_sitewide_schema()

    # Page-specific schema
    if page_data.get("schema_extra") == "person":
        result += build_person_schema()

    if page_data.get("schema_extra") == "service":
        result += build_service_schema(page_data, filename)

    # Breadcrumbs for all subpages (not homepage)
    if filename != "index.html":
        clean_title = og_title.split(" — ")[0] if " — " in og_title else page_data["title"].split(" | ")[0]
        result += build_breadcrumb_schema(clean_title, filename)

    return result


def process_page(filename, page_data):
    filepath = os.path.join(ROOT, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update <title>
    html = re.sub(
        r"<title>.*?</title>",
        f'<title>{page_data["title"]}</title>',
        html
    )

    # 2. Update <meta name="description">
    html = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{page_data["desc"]}">',
        html
    )

    # 3. Insert meta block before </head>
    meta_block = build_meta_block(page_data, filename)
    html = html.replace("</head>", f"{meta_block}\n</head>")

    # 4. Update footer — copyright + privacy link
    old_footer_legal = '<p>&copy; 2025 Create Allied Health Services Pty Ltd. All rights reserved. NDIS Registered Provider.</p>'
    new_footer_legal = '<p>&copy; 2026 Create Allied Health Services Pty Ltd. All rights reserved. NDIS Registered Provider. <a href="privacy-policy.html">Privacy Policy</a></p>'
    html = html.replace(old_footer_legal, new_footer_legal)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  Updated: {filename}")


def main():
    print("Adding SEO infrastructure to all pages...\n")
    for filename, page_data in PAGES.items():
        process_page(filename, page_data)
    print(f"\nDone! Updated {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
