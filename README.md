# Automated Data Collection: Weapons Endowments of Rebel Organizations

![Python](https://img.shields.io/badge/Python-3.10-blue.svg) ![NLP](https://img.shields.io/badge/Area-NLP%20%26%20Conflict%20Research-green) ![Status](https://img.shields.io/badge/Status-Prototype-orange)

## 📄 Project Overview
This project implements an **automated end-to-end pipeline** to extract structured data on the armament of non-state actors (rebel groups) from unstructured text sources. 

Leveraging the **GDELT Project (Global Database of Events, Language, and Tone)** and **Large Language Models (LLMs)**, this system aims to enrich conflict datasets such as the *Rebels' Armament Dataset (RAD)* by identifying links between specific insurgent groups and weapon systems in real-time news streams.


---

## 🚀 Key Features & Methodology

The pipeline addresses the challenge of extracting reliable data from noisy, unstructured text while minimizing LLM fabrications.

### 1. Data Ingestion (Pipeline Engineering)
- **Source:** Automated querying of the GDELT 2.0 API.
- **Filtering:** Targeting specific conflict keywords (e.g., "insurgents", "militia") combined with weaponry terms ("MANPADS", "drones", "assault rifles").
- **Handling:** Robust request handling (User-Agent rotation, rate limiting) to ensure continuous data flow.

### 2. Extraction & Hallucination Reduction (Optimization)
A critical requirement for political science research is data integrity. Standard LLM extraction often leads to hallucinations (inventing weapon transfers). This project implements a **Chain-of-Verification (CoVe)** approach:

1.  **Extraction Phase:** The model identifies potential `(Actor, Weapon)` tuples.
2.  **Verification Phase (Guardrail):** A secondary logic forces the model to provide an **exact quote** from the source text as evidence.
    - If no quote is found: The entry is flagged as `Hallucination` or `Unverified`.
    - If a quote exists: The entry is marked `Verified`.

---

## 🛠️ Project Structure

```bash
rebel-arms-pipeline/
├── data/
│   ├── raw/                   # Raw JSON responses from GDELT
│   └── processed/             # Structured extraction results (CSV/JSON)
├── src/
│   ├── ingestion.py           # API wrapper for GDELT
│   ├── extractor.py           # LLM logic including Verification Loop
│   └── main.py                # Pipeline orchestrator
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---


## 💻 Installation & Usage
Prerequisites
Python 3.8+

An OpenAI API Key (or local LLM setup)

### Setup

bash
````
# Clone the repository
git clone [https://github.com/YOUR-USERNAME/rebel-arms-pipeline.git](https://github.com/YOUR-USERNAME/rebel-arms-pipeline.git)
cd rebel-arms-pipeline

# Create virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
````

Running the Pipeline
To fetch the latest news on rebel weaponry and extract verified data

bash
````
python src/main.py
````

---


📊 Sample Output
The system outputs a JSON structure that explicitly flags the reliability of the extracted information. This allows researchers to filter out unreliable data points immediately.

JSON
````
[
  {
    "article_id": "123456789",
    "source_url": "[https://news-source.com/article](https://news-source.com/article)",
    "extracted_data": {
      "rebel_group": "Houthi Forces",
      "weapon_system": "Long-range Drones",
      "verification_status": "VERIFIED",
      "evidence_quote": "The Houthi forces claimed responsibility for the attack using long-range drones."
    }
  },
  {
    "article_id": "987654321",
    "source_url": "[https://news-source.com/opinion](https://news-source.com/opinion)",
    "extracted_data": {
      "rebel_group": "Unknown Militia",
      "weapon_system": "Nuclear Warheads",
      "verification_status": "HALLUCINATION_DETECTED",
      "evidence_quote": null
    }
  }
]
````

---

🔮 Future Improvements
Advanced RAG: Integration with official SIPRI reports to cross-reference extracted claims against known national inventories.

Scaling: Expanding the pipeline to process historical GDELT archives (2015-2025) for longitudinal studies.

Multilingual Support: Adding translation layers to analyze local news sources in Arabic and French.

---

Author: Duc-Anh Nguyen | January 2026
Contact: anh.ngyuyen1@campus.lmu.de
