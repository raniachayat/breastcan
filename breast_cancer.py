
mutation_therapies = {
    "BRCA1": {
        "preferred_therapy": "Olaparib",
        "price": "Approx. €2,647.75 per pack (Spain retail price)",
        "coverage": (
            "Reimbursed by SNS for high-risk early-stage HER2- breast cancer with BRCA1/2 mutations, "
            "treatment up to 12 months after chemotherapy."
        ),
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/olaparib.html",
        "preferred_therapy_side_effect": (
            "May cause fatigue, nausea, blood disorders (e.g., anemia, leukemia), or blood clots; avoid during pregnancy."
        ),
        "alternative_after_progression": "Carboplatin",
        "alternative_therapy_price": "Approximately €68.8 per 450 mg vial (based on 2015 catalog prices)",
        "alternative_therapy_coverage": "Hospital-administered chemotherapy fully covered by the SNS (general public health system).",
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/carboplatin.html",
        "alternative_therapy_side_effect": (
            "May cause severe bone marrow suppression (risk of infection/bleeding), cumulative anemia, vomiting, and rare but serious anaphylactic reactions."
        ),
        "evidence_level": "Category 1",
        "use_stage": ["II", "III", "IV"],
        "priority": 1,
        "notes": "Also used in high-risk early breast cancer after chemo"
    },
    "BRCA2": {
        "preferred_therapy": "Olaparib",
        "price": "Approx. €2,647.75 per pack (Spain retail price)",
        "coverage": (
            "Reimbursed by SNS for high-risk early-stage HER2- breast cancer with BRCA1/2 mutations, "
            "treatment up to 12 months after chemotherapy."
        ),
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/olaparib.html",
        "preferred_therapy_side_effect": (
            "May cause fatigue, nausea, blood disorders (e.g., anemia, leukemia), or blood clots; avoid during pregnancy."
        ),
        "alternative_after_progression": "Carboplatin",
        "alternative_therapy_price": "Approximately €68.8 per 450 mg vial (based on 2015 catalog prices)",
        "alternative_therapy_coverage": "Hospital-administered chemotherapy fully covered by the SNS (general public health system).",
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/carboplatin.html",
        "alternative_therapy_side_effect": (
            "May cause severe bone marrow suppression (risk of infection/bleeding), cumulative anemia, vomiting, and rare but serious anaphylactic reactions."
        ),
        "evidence_level": "Category 1",
        "use_stage": ["II", "III", "IV"],
        "priority": 1,
        "notes": "Same as BRCA1"
    },
    "PALB2": {
        "preferred_therapy": "Olaparib",
        "price": "Approx. €2,647.75 per pack (Spain retail price)",
        "coverage": (
            "Reimbursed by SNS for high-risk early-stage HER2- breast cancer with BRCA1/2 mutations, "
            "treatment up to 12 months after chemotherapy."
        ),
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/olaparib.html",
        "preferred_therapy_side_effect": (
            "May cause fatigue, nausea, blood disorders (e.g., anemia, leukemia), or blood clots; avoid during pregnancy."
        ),
        "alternative_after_progression": "Carboplatin",
        "alternative_therapy_price": "Approximately €68.8 per 450 mg vial (based on 2015 catalog prices)",
        "alternative_therapy_coverage": "Hospital-administered chemotherapy fully covered by the SNS (general public health system).",
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/carboplatin.html",
        "alternative_therapy_side_effect": (
            "May cause severe bone marrow suppression (risk of infection/bleeding), cumulative anemia, vomiting, and rare but serious anaphylactic reactions."
        ),
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 2,
        "notes": "Same logic as BRCA, less data"
    },
    "PIK3CA": {
        "preferred_therapy": "Alpelisib + Fulvestrant",
        "price": (
            "Fulvestrant: €225.70 (1 syringe) or €408.86 (2‑syringe pack); "
            "Alpelisib: negotiated public price (not publicly listed)"
        ),
        "coverage": (
            "Reimbursed by SNS for PIK3CA‑mutated HR+ metastatic breast cancer after prior endocrine therapy."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/alpelisib.html",
            "https://www.drugs.com/drug-interactions/fulvestrant.html"
        ],
        "preferred_therapy_side_effect": (
            "May cause hyperglycemia, GI symptoms (nausea, vomiting, diarrhea), fatigue, and risk of infections or bleeding."
        ),
        "alternative_after_progression": "Capivasertib + Fulvestrant",
        "alternative_therapy_price": (
            "Fulvestrant: €225.70 per syringe or €408.86 for 2‑syringe pack (Spain PVP); "
            "Alpelisib: price subject to internal SNS negotiation (not publicly listed)"
        ),
        "alternative_therapy_coverage": (
            "Fulvestrant: reimbursable by SNS for metastatic HR+ breast cancer (standard oncology use). "
            "Alpelisib + Fulvestrant: EMA‑approved for PIK3CA‑mutated HR+ metastatic disease; "
            "Spanish SNS reimbursement pending pricing negotiation and formal inclusion."
        ),
        "alternative_therapy_urls": [
            "https://www.drugs.com/drug-interactions/capivasertib.html",
            "https://www.drugs.com/drug-interactions/fulvestrant.html"
        ],
        "alternative_therapy_side_effect": (
            "Common effects include diarrhea, skin reactions, fatigue, high glucose, low blood cells, and potential bleeding or breathing issues."
        ),
        "evidence_level": "Category 1",
        "use_stage": ["IV"],
        "priority": 2,
        "notes": "HR+/HER2– only"
    },
    "AKT1": {
        "preferred_therapy": "Capivasertib + Fulvestrant",
        "price": (
            "Fulvestrant: €225.70 per syringe or €408.86 for 2‑syringe pack (Spain PVP); "
            "Alpelisib: price subject to internal SNS negotiation (not publicly listed)"
        ),
        "coverage": (
            "Fulvestrant: reimbursable by SNS for metastatic HR+ breast cancer (standard oncology use). "
            "Alpelisib + Fulvestrant: EMA‑approved for PIK3CA‑mutated HR+ metastatic disease; "
            "Spanish SNS reimbursement pending pricing negotiation and formal inclusion."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/capivasertib.html",
            "https://www.drugs.com/drug-interactions/fulvestrant.html"
        ],
        "preferred_therapy_side_effect": (
            "Common effects include diarrhea, skin reactions, fatigue, high glucose, low blood cells, and potential bleeding or breathing issues."
        ),
        "alternative_after_progression": "Everolimus + Exemestane",
        "alternative_therapy_price": (
            "Everolimus: hospital-use, price not publicly listed; "
            "Exemestane: generic, variable retail price."
        ),
        "alternative_therapy_coverage": (
            "Used in public hospitals for HR+ metastatic breast cancer; "
            "commonly financed as hospital-administered therapy rather than outpatient prescription."
        ),
        "alternative_therapy_urls": [
            "https://www.drugs.com/drug-interactions/everolimus.html",
            "https://www.drugs.com/drug-interactions/exemestane.html"
        ],
        "alternative_therapy_side_effect": (
            "⚠️ Increases risk of serious infections, cancers (e.g., lymphoma, skin), and kidney thrombosis. "
            "Not recommended in heart transplant due to high early mortality risk. Requires cyclosporine dose adjustment and monitoring to prevent nephrotoxicity."
        ),
        "evidence_level": "Category 1",
        "use_stage": ["IV"],
        "priority": 3,
        "notes": "Same strategy for PTEN"
    },
    "PTEN": {
        "preferred_therapy": "Capivasertib + Fulvestrant",
        "price": (
            "Fulvestrant: €225.70 per syringe or €408.86 for 2‑syringe pack (Spain PVP); "
            "Alpelisib: price subject to internal SNS negotiation (not publicly listed)"
        ),
        "coverage": (
            "Fulvestrant: reimbursable by SNS for metastatic HR+ breast cancer (standard oncology use). "
            "Alpelisib + Fulvestrant: EMA‑approved for PIK3CA‑mutated HR+ metastatic disease; "
            "Spanish SNS reimbursement pending pricing negotiation and formal inclusion."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/capivasertib.html",
            "https://www.drugs.com/drug-interactions/fulvestrant.html"
        ],
        "preferred_therapy_side_effect": (
            "Common effects include diarrhea, skin reactions, fatigue, high glucose, low blood cells, and potential bleeding or breathing issues."
        ),
        "alternative_after_progression": "Everolimus ± endocrine",
        "alternative_therapy_price": (
            "Everolimus: laboratory price €1,733 or public price €1,860.47 (30 tablets of 10 mg); "
            "hospital-use only (SNS financing, not outpatient pharmacy)."
        ),
        "alternative_therapy_coverage": (
            "Everolimus is financed by the SNS as a hospital-administered oncology drug (not billed in community pharmacies)."
        ),
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/everolimus.html",
        "alternative_therapy_side_effect": (
            "⚠️ Increases risk of serious infections, cancers (e.g., lymphoma, skin), and kidney thrombosis. "
            "Not recommended in heart transplant due to high early mortality risk. Requires cyclosporine dose adjustment and monitoring to prevent nephrotoxicity."
        ),
        "evidence_level": "Category 1",
        "use_stage": ["IV"],
        "priority": 3,
        "notes": "Same strategy as AKT1"
    },
    "ESR1": {
        "preferred_therapy": "Elacestrant",
        "price": "Price in Spain not publicly listed (likely hospital-negotiated)",
        "coverage": "EMA-approved (Sept 2023) for ESR1‑mutated metastatic HR+/HER2– breast cancer; SNS coverage in Spain not yet confirmed.",
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/elacestrant.html",
        "preferred_therapy_side_effect": (
            "⚠️ Common effects: GI discomfort (diarrhea, constipation, indigestion), appetite loss, hot flushes, headache, and musculoskeletal pain."
        ),
        "alternative_after_progression": "Fulvestrant ± CDK4/6i",
        "alternative_therapy_price": "Fulvestrant: €225.70 per syringe or €408.86 for 2‑syringe pack (Spain PVP).",
        "alternative_therapy_coverage": "Fulvestrant: reimbursable by SNS for metastatic HR+ breast cancer (standard oncology use).",
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/fulvestrant.html",
        "alternative_therapy_side_effect": (
            "⚠️ Serious effects: internal bleeding (black stools, bleeding gums, hematuria), neuropathy (tingling, numbness), cardiopulmonary symptoms (chest pain, difficulty breathing, fainting), and signs of infection (chills, cough, cloudy urine)."
        ),
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 4,
        "notes": "Do not reuse Elacestrant"
    },
    "HER2 mutation": {
        "preferred_therapy": "Neratinib + Trastuzumab",
        "price": (
            "Neratinib 40 mg ×180 tablets: PVL €5,040 / PVP €5,299.75; "
            "Trastuzumab 600 mg vial: PVL €1,572.28 / PVP €1,693.32."
        ),
        "coverage": (
            "Neratinib: hospital-use, limited SNS funding for certain indications (Facturable SNS: NO). "
            "Trastuzumab: fully financed by SNS as hospital-administered biologic."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/neratinib.html",
            "https://www.drugs.com/drug-interactions/trastuzumab.html"
        ],
        "preferred_therapy_side_effect": (
            "⚠️ May cause dehydration (dry mouth, thirst, sunken eyes, decreased urination), cardiovascular symptoms (chest pain, rapid heartbeat, dizziness, fainting), "
            "internal bleeding (black stools, bleeding gums, hematuria), and general infection or systemic symptoms (body aches, swelling)."
        ),
        "alternative_after_progression": "Trastuzumab + endocrine therapy",
        "alternative_therapy_price": "Trastuzumab 600 mg vial: PVL €1,572.28 / PVP €1,693.32.",
        "alternative_therapy_coverage": "Trastuzumab: fully financed by SNS as hospital-administered biologic.",
        "alternative_therapy_url": "https://www.drugs.com/drug-interactions/trastuzumab.html",
        "alternative_therapy_side_effect": (
            "⚠️ May include signs of internal bleeding (black stools, bleeding gums, hematuria), swelling, body aches, and chest pain—monitor for serious complications."
        ),
        "evidence_level": "Category 2A–2B",
        "use_stage": ["IV"],
        "priority": 4,
        "notes": "For HER2-mutant, non-amplified"
    },
    "MSI-H": {
        "preferred_therapy": "Pembrolizumab or Dostarlimab",
        "price": (
            "Pembrolizumab (Keytruda) 100 mg vial: PVP €4,702.46 (Vademecum España); "
            "Dostarlimab (Jemperli) 500 mg vial: PVP €1,820.39 (Vademecum España)."
        ),
        "coverage": (
            "Pembrolizumab: publicly funded by SNS for approved oncology indications (hospital-use). "
            "Dostarlimab: financed by SNS for endometrial cancer with specific molecular profiles (hospital-use)."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/pembrolizumab.html",
            "https://www.drugs.com/drug-interactions/dostarlimab.html"
        ],
        "preferred_therapy_side_effect": (
            "⚠️ May cause internal bleeding signs (black stools, bloody urine), neurotoxicity (confusion, blurred vision, tingling), mood changes (depression), and swelling—requires monitoring."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 5,
        "notes": "Use after all standard options fail"
    },
    "dMMR": {
        "preferred_therapy": "Pembrolizumab or Dostarlimab",
        "price": (
            "Pembrolizumab (Keytruda) 100 mg vial: PVP €4,702.46 (Vademecum España); "
            "Dostarlimab (Jemperli) 500 mg vial: PVP €1,820.39 (Vademecum España)."
        ),
        "coverage": (
            "Pembrolizumab: publicly funded by SNS for approved oncology indications (hospital-use). "
            "Dostarlimab: financed by SNS for endometrial cancer with specific molecular profiles (hospital-use)."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/pembrolizumab.html",
            "https://www.drugs.com/drug-interactions/dostarlimab.html"
        ],
        "preferred_therapy_side_effect": (
            "⚠️ May cause internal bleeding signs (black stools, bloody urine), neurotoxicity (confusion, blurred vision, tingling), mood changes (depression), and swelling—requires monitoring."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 5,
        "notes": "Same as MSI-H"
    },
    "TMB-H": {
        "preferred_therapy": "Pembrolizumab",
        "price": "Pembrolizumab (Keytruda) 100 mg vial: PVP €4,702.46 (Vademecum España).",
        "coverage": "Pembrolizumab: publicly funded by SNS for approved oncology indications (hospital-use).",
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/pembrolizumab.html",
        "preferred_therapy_side_effect": (
            "⚠️ Watch for signs of bleeding or liver/kidney issues (black/clay-colored/dark urine/stools, cloudy urine)."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 6,
        "notes": "If ≥10 mut/Mb and no other options"
    },
    "NTRK fusion": {
        "preferred_therapy": "Larotrectinib or Entrectinib",
        "price": (
            "Larotrectinib (Vitrakvi): PVL €2,000 (56×25 mg) or €7,000 (56×100 mg); "
            "Entrectinib (Rozlytrek): no public price available in Spain."
        ),
        "coverage": (
            "Larotrectinib: hospital-use, SNS-financed per CIPM Resolution 236; "
            "Entrectinib: hospital-use, EMA-approved; SNS coverage presumed but confirm with hospital pharmacy."
        ),
        "preferred_therapy_urls": [
            "https://www.drugs.com/drug-interactions/larotrectinib.html",
            "https://www.drugs.com/drug-interactions/entrectinib.html"
        ],
        "preferred_therapy_side_effect": (
            "⚠️ May cause bleeding (black stools, bloody/cloudy urine), neurocognitive and sensory issues (confusion, forgetfulness, vision/color changes, tingling) "
            "and organ warning signs (dark/clay-colored urine/stools, appetite loss, swelling, painful urination)."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2A/2B",
        "use_stage": ["IV"],
        "priority": 6,
        "notes": "For rare fusion-driven tumors"
    },
    "RET fusion": {
        "preferred_therapy": "Selpercatinib",
        "price": (
            "Selpercatinib 40 mg (56 caps): PVL €5,576 / PVP €5,857.19; "
            "same pricing for 80 mg capsules."
        ),
        "coverage": (
            "Selpercatinib: hospital-use only, limited SNS funding for RET‑fusion tumors (Facturable SNS: NO)."
        ),
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/selpercatinib.html",
        "preferred_therapy_side_effect": (
            "⚠️ Watch for bleeding (gums, blood in stool/urine, coughing blood), neurological and mood changes (confusion, dizziness, depression), "
            "organ/sensory issues (blurred vision, chest tightness, breathing/swallowing trouble, constipation/diarrhea)."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2A",
        "use_stage": ["IV"],
        "priority": 6,
        "notes": "No reuse guidance in NCCN"
    },
    "FGFR1–3 fusion": {
        "preferred_therapy": "Erdafitinib",
        "price": "No public PVL/PVP listed in Spain; hospital-use only.",
        "coverage": "Hospital-use only; limited SNS funding for FGFR‑altered urothelial carcinoma (Facturable SNS: NO).",
        "preferred_therapy_url": "https://www.drugs.com/drug-interactions/erdafitinib.html",
        "preferred_therapy_side_effect": (
            "⚠️ Possible urinary issues (bladder pain, painful urination, discharge, bloody/cloudy urine), eye problems (blurred vision, burning, dryness, excessive tearing), "
            "and respiratory symptoms (chest tightness, labored breathing), along with confusion and nail discoloration."
        ),
        "alternative_after_progression": None,
        "evidence_level": "Category 2B",
        "use_stage": ["IV"],
        "priority": 6,
        "notes": "Investigational"
    },
}
# --- Utility functions ---
def determine_subtype(er, pr, her2):
    if her2 == "positive":
        return "HER2+"
    elif er == "negative" and pr == "negative" and her2 == "negative":
        return "TNBC"
    else:
        return "HR+/HER2–"

def is_high_risk(tumor_size, node_status, grade, ki67, lvi):
    return (
        tumor_size >= 2 or
        node_status == "positive" or
        grade == 3 or
        ki67 == "high" or
        lvi
    )

def oncotype_decision(score, age, high_risk):
    if score < 18:
        return "No chemotherapy"
    elif 18 <= score <= 30:
        return "Consider chemotherapy" if age < 50 or high_risk else "Endocrine therapy only"
    elif score > 30:
        return "Add chemotherapy"
    return "Unknown"

# --- Helper function to format therapy details ---
def format_therapy_details(mutation, therapy_name):
    m_info = mutation_therapies.get(mutation, {})
    details = []

    if therapy_name == m_info.get("preferred_therapy"):
        details.append(f"ℹ️ Details for preferred therapy {therapy_name} ({mutation} mutation):")

        price = m_info.get("price")
        if price:
            details.append(f"💰 Price: {price}")

        coverage = m_info.get("coverage")
        if coverage:
            details.append(f"🏥 Coverage: {coverage}")

        side_effects = m_info.get("preferred_therapy_side_effect")
        if side_effects:
            details.append(f"⚠️ Side Effects: {side_effects}")

        url = m_info.get("preferred_therapy_url") or m_info.get("preferred_therapy_urls")
        if url:
            if isinstance(url, list):
                for u in url:
                    details.append(f"🔗 Info: {u}")
            else:
                details.append(f"🔗 Info: {url}")

    elif therapy_name == m_info.get("alternative_after_progression"):
        details.append(f"ℹ️ Details for alternative therapy {therapy_name} ({mutation} mutation):")

        alt_price = m_info.get("alternative_therapy_price")
        if alt_price:
            details.append(f"💰 Price: {alt_price}")

        alt_coverage = m_info.get("alternative_therapy_coverage")
        if alt_coverage:
            details.append(f"🏥 Coverage: {alt_coverage}")

        alt_side_effects = m_info.get("alternative_therapy_side_effect")
        if alt_side_effects:
            details.append(f"⚠️ Side Effects: {alt_side_effects}")

        alt_url = m_info.get("alternative_therapy_url") or m_info.get("alternative_therapy_urls")
        if alt_url:
            if isinstance(alt_url, list):
                for u in alt_url:
                    details.append(f"🔗 Info: {u}")
            else:
                details.append(f"🔗 Info: {alt_url}")

    else:
        details.append(f"ℹ️ No detailed info available for {therapy_name} under {mutation} mutation.")

    return "\n".join(details)

# --- Main rule-based selector ---
def select_breast_therapy(inputs):
    subtype = determine_subtype(
        inputs["receptor_status"]["ER"],
        inputs["receptor_status"]["PR"],
        inputs["receptor_status"]["HER2"]
    )
    stage = inputs["stage"]
    node_status = inputs["tumor_characteristics"]["node_status"]
    high_risk = is_high_risk(
        inputs["tumor_characteristics"]["tumor_size_cm"],
        node_status,
        inputs["tumor_characteristics"]["tumor_grade"],
        inputs["tumor_characteristics"]["ki67"],
        inputs["tumor_characteristics"]["lvi"]
    )
    oncotype_applicable = (
        subtype == "HR+/HER2–" and
        stage in ["I", "II"] and
        node_status in ["N0", "N1"]
    )

    performance = inputs["patient_context"]["performance_status"]
    pregnant = inputs["patient_context"]["pregnant"]
    menopausal_status = inputs["patient_context"].get("menopausal_status", None)
    age = inputs["patient_context"]["age"]
    prior_therapies = inputs.get("prior_therapies", [])
    mutations = inputs.get("mutations", [])

    pregnancy_notes = []
    if pregnant:
        pregnancy_notes.append("⚠️ Avoid tamoxifen, PARP inhibitors, HER2-targeted therapies, and chemo in 1st trimester.")

    if performance > 2:
        if subtype == "HR+/HER2–":
            return "🧘‍♀️ Recommend: Endocrine therapy only due to ECOG >2"
        else:
            return "🤝 Recommend: Supportive care only due to ECOG >2"

    if stage in ["I", "II", "III"]:
        surgery_note = (
            "🩺 Recommend: Surgery followed by systemic therapy based on subtype"
            if inputs.get("surgery_possible", True)
            else "🧪 Non-surgical: Systemic therapy based on subtype"
        )

        therapy_plan = ""
        menopause_note = ""
        if subtype == "HER2+":
            therapy_plan = "based on HER2+ subtype we recommend HER2-targeted therapy + chemotherapy"
        elif subtype == "TNBC":
            therapy_plan = "based on TNBC subtype we recommend Chemotherapy ± immunotherapy"
        elif subtype == "HR+/HER2–":
            if oncotype_applicable:
                score = inputs["genomic_score"].get("oncotype_dx_score", 0)
                oncotype_result = oncotype_decision(score, age, high_risk)
                if menopausal_status == "postmenopausal":
                    therapy_plan = f"{oncotype_result} + Aromatase Inhibitor"
                elif menopausal_status == "premenopausal":
                    therapy_plan = f"{oncotype_result} + Tamoxifen"
                else:
                    therapy_plan = f"{oncotype_result} + Endocrine therapy"
            else:
                if menopausal_status == "postmenopausal":
                    therapy_plan = "Endocrine ± chemotherapy (AI preferred)"
                elif menopausal_status == "premenopausal":
                    therapy_plan = "Endocrine ± chemotherapy (Tamoxifen ± ovarian suppression)"
                else:
                    therapy_plan = "Endocrine ± chemotherapy"

            if menopausal_status == "postmenopausal":
                menopause_note = "📝 NCCN: Aromatase inhibitors preferred in postmenopausal women."
            elif menopausal_status == "premenopausal":
                menopause_note = "📝 NCCN: Tamoxifen ± ovarian suppression recommended for premenopausal patients."

        recommendation = ""
        valid_mut = []
        for m in mutations:
            m_info = mutation_therapies.get(m)
            if m_info and stage in m_info["use_stage"]:
                if m_info["preferred_therapy"] not in prior_therapies:
                    valid_mut.append((m_info["priority"], m, m_info["preferred_therapy"]))
                else:
                    alt_therapy = m_info.get("alternative_after_progression")
                    if alt_therapy and alt_therapy.lower() != "none":
                        valid_mut.append((m_info["priority"], m, alt_therapy))

        valid_mut.sort()
        mutation_output = []
        details_output = []
        if valid_mut:
            top = valid_mut[0]
            mutation_name = top[1]
            therapy_name = top[2]
            m_info = mutation_therapies.get(mutation_name)
            is_alt = (therapy_name != m_info["preferred_therapy"])

            if mutation_name in ["BRCA1", "BRCA2"] and not high_risk:
                pass

            if len(valid_mut) > 1 and valid_mut[1][0] == top[0]:
                m2 = valid_mut[1]
                if top[2] != m2[2]:
                    lines = [
                        f"⚠️ Both {top[1]} and {m2[1]} have equal priority.",
                        "💡 Check VAF (variant allele frequency) to guide therapy.",
                        f"If {top[1]} VAF > {m2[1]} → use {top[2]}",
                        f"If {m2[1]} VAF > {top[1]} → use {m2[2]}"
                    ]
                    recommendation += "\n".join(lines) + "\n"
                else:
                    recommendation += f"✅ Recommend: {top[2]} based on mutations {top[1]} and {m2[1]}\n"
            else:
                recommendation += f"✅ Recommend: {top[2]} based on mutation {top[1]}\n"

        final_note = "\n".join(pregnancy_notes) if pregnancy_notes else ""
        mutation_section = "\n".join(mutation_output) if mutation_output else ""
        details_section = "\n\n".join(details_output) if details_output else ""

        output = (
            f"{surgery_note}\n"
            f"🔬 Subtype: {subtype}\n"
            f"✅ Subtype-Based Recommendation: {therapy_plan}\n"
            f"{recommendation}\n"
            f"{details_section}\n"
            f"{final_note}"
        ).strip()

        if menopause_note:
            output += f"\n\n{menopause_note}"

        return output

    if stage == "IV":
        therapy_plan = ""
        menopause_note = ""
        if subtype == "HER2+":
            therapy_plan = "based on HER2+ subtype we recommend HER2-targeted therapy + chemotherapy"
        elif subtype == "TNBC":
            therapy_plan = "based on TNBC subtype we recommend Chemotherapy ± immunotherapy"
        elif subtype == "HR+/HER2–":
            if oncotype_applicable:
                score = inputs["genomic_score"].get("oncotype_dx_score", 0)
                oncotype_result = oncotype_decision(score, age, high_risk)
                if menopausal_status == "postmenopausal":
                    therapy_plan = f"{oncotype_result} + Aromatase Inhibitor"
                elif menopausal_status == "premenopausal":
                    therapy_plan = f"{oncotype_result} + Tamoxifen"
                else:
                    therapy_plan = f"{oncotype_result} + Endocrine therapy"
            else:
                if menopausal_status == "postmenopausal":
                    therapy_plan = "Endocrine ± chemotherapy (AI preferred)"
                elif menopausal_status == "premenopausal":
                    therapy_plan = "Endocrine ± chemotherapy (Tamoxifen ± ovarian suppression)"
                else:
                    therapy_plan = "Endocrine ± chemotherapy"

            if menopausal_status == "postmenopausal":
                menopause_note = "📝 NCCN: Aromatase inhibitors preferred in postmenopausal women."
            elif menopausal_status == "premenopausal":
                menopause_note = "📝 NCCN: Tamoxifen ± ovarian suppression recommended for premenopausal patients."

        recommendation = ""
        valid_mut = []
        for m in mutations:
            m_info = mutation_therapies.get(m)
            if m_info and stage in m_info["use_stage"]:
                if m == "PIK3CA" and subtype != "HR+/HER2–":
                    continue
                if m_info["preferred_therapy"] not in prior_therapies:
                    valid_mut.append((m_info["priority"], m, m_info["preferred_therapy"]))
                else:
                    alt_therapy = m_info.get("alternative_after_progression")
                    if alt_therapy and alt_therapy.lower() != "none":
                        valid_mut.append((m_info["priority"], m, alt_therapy))

        valid_mut.sort()
        mutation_output = []
        details_output = []
        if valid_mut:
            top = valid_mut[0]
            mutation_name = top[1]
            therapy_name = top[2]
            m_info = mutation_therapies.get(mutation_name)
            is_alt = (therapy_name != m_info["preferred_therapy"])
            details_output.append(format_therapy_details(mutation_name, therapy_name))

            if len(valid_mut) > 1 and valid_mut[1][0] == top[0]:
                m2 = valid_mut[1]
                if top[2] != m2[2]:
                    lines = [
                        f"⚠️ Both {top[1]} and {m2[1]} have equal priority.",
                        "💡 Check VAF (variant allele frequency) to guide therapy.",
                        f"If {top[1]} VAF > {m2[1]} → use {top[2]}",
                        f"If {m2[1]} VAF > {top[1]} → use {m2[2]}"
                    ]
                    recommendation += "\n".join(lines) + "\n"
                else:
                    recommendation += f"✅ Recommend: {top[2]} based on mutations {top[1]} and {m2[1]}\n"
            else:
                recommendation += f"✅ Recommend: {top[2]} based on mutation {top[1]}\n"

        if pregnancy_notes:
            recommendation += "\n" + "\n".join(pregnancy_notes)

        mutation_section = "\n".join(mutation_output) if mutation_output else ""
        details_section = "\n\n".join(details_output) if details_output else ""

        output = (
            f"🔬 Subtype: {subtype}\n"
            f"✅ Subtype-Based Recommendation: {therapy_plan}\n"
            f"{mutation_section}\n"
            f"{recommendation}\n"
            f"{details_section}"
        ).strip()

        if menopause_note:
            output += f"\n\n{menopause_note}"

        return output

    return "⚠️ Insufficient data or unsupported scenario."



