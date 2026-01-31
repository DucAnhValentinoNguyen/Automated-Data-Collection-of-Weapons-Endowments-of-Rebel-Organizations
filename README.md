# Automated Data Collection: Weapons Endowments of Rebel Organizations

![Python](https://img.shields.io/badge/Python-3.10-blue.svg) ![NLP](https://img.shields.io/badge/Area-NLP%20%26%20Conflict%20Research-green) ![Status](https://img.shields.io/badge/Status-Prototype-orange)

## 📄 Project Overview
This project implements an **automated end-to-end pipeline** to extract structured data on the armament of non-state actors (rebel groups) from unstructured text sources. 

Leveraging the **GDELT Project (Global Database of Events, Language, and Tone)** and **Large Language Models (LLMs)**, this system aims to enrich conflict datasets such as the *Rebels' Armament Dataset (RAD)* by identifying links between specific insurgent groups and weapon systems in real-time news streams.

> **Context:** Developed as a proof-of-concept for the application at the **Chair of Empirical Political Research (LMU Munich)**, demonstrating pipeline engineering and strategies for hallucination reduction in scientific data extraction.

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
    -
