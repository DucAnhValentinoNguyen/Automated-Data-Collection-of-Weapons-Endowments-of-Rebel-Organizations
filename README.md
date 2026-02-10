# Automated Rebel Arms Tracker (ARAT)

## Project Overview
This pipeline automates the collection and analysis of non-state armed group weapon endowments. It leverages the **GDELT 2.0 API** for real-time global news ingestion and uses **Large Language Models (Meta-Llama-3-8B)** via the **Hugging Face Inference API** to extract structured conflict data.

## Features
- **Data Ingestion**: Targeted GDELT queries for "rebel," "insurgent," and "militia" activities.
- **NLP Extraction**: Automated identification of Rebel Groups, Weapon Systems, and Evidence Quotes.
- **Verification Logic**: Categorizes data into `VERIFIED` (explicit mentions) or `INFERRED` (contextual deduction).
- **Reproducibility**: Environment-based configuration and structured JSON/CSV output.

---

## Technical Architecture



1. **Ingestion (`src/ingestion.py`)**: Fetches the last 10 relevant global news articles via GDELT.
2. **Analysis (`src/extractor.py`)**: Processes text using Llama-3-8B-Instruct to generate structured JSON.
3. **Pipeline Control (`src/main.py`)**: Orchestrates the flow from raw news to processed data.
4. **Reporting (`src/report.py`)**: Generates a human-readable summary of findings.

---

## Prerequisites
- Python 3.8+
- Conda or Virtualenv (recommended)
- A Hugging Face API Token (Free tier)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Automated-Data-Collection-of-Weapons-Endowments-of-Rebel-Organizations
   ```

2. **Install dependencies**:

```
Bash
pip install -r requirements.txt
```

Configure Environment: Create a .env file in the root directory and add your Hugging Face token:


```
Plaintext
HF_TOKEN=hf_your_token_here
```

---



## Usage
1. **Run the Data Pipeline**
This will fetch news, perform NLP extraction, and save the results to data/processed/verified_events.json.

```
Bash
python src/main.py
```

2. **Generate Summary Report**
To view a structured table of the results in your terminal:

```Bash
python src/report.py
```

Data Structure
The output verified_events.json follows this schema:


```
JSON
{
  "source_url": "URL of the news article",
  "timestamp": "Date found",
  "nlp_analysis": {
    "rebel_group": "Group Name",
    "weapon": "Weapon System/Category",
    "verification_status": "VERIFIED/INFERRED",
    "evidence_quote": "Excerpt from text"
  }
}
```

--- 


Contact: Duc-Anh Nguyen anh.nguyen1@camous.lmu.de
