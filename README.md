# Customers Review Analysis Mini Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)](https://github.com/)

> **A Machine Learning project to analyze customer sentiment and churn drivers for Tunisian Telecom providers (Orange, Ooredoo, Tunisie Telecom) by processing mixed-language reviews (French, Arabic, and Tunisian Derja).**

## Table of Contents
1. [Project Overview (Business Understanding)](#project-overview-business-understanding)
2. [Tech Stack & Methodology (CRISP-DM)](#tech-stack--methodology-crisp-dm)
3. [Repository Structure](#repository-structure)
4. [Getting Started](#getting-started)
5. [Key Challenges](#key-challenges)
6. [Authors](#authors)
---

## Project Overview (Business Understanding)
Telecommunications companies in Tunisia face high customer churn. Traditional metrics fail to capture the *why* behind customer dissatisfaction, especially when feedback is written in **Tunisian Derja** (a mix of Arabic dialects and French) or **Arabizi** (Latin characters for Arabic).

**Our Goal:**
1. **Scrape** real-time reviews from the Google Play Store.
2. **Translate & Clean** the unique Tunisian dialect/Arabizi into a standardized format.
3. **Analyze Sentiment** (Positive/Negative) to track brand health.
4. **Topic Modeling** to identify specific pain points (e.g., "Reseau taya7", "Solde masrou9").
5. **Visualize** insights via an interactive Streamlit Dashboard.

---

## Tech Stack & Methodology (CRISP-DM)

We follow the **CRISP-DM** (Cross-Industry Standard Process for Data Mining) lifecycle:

| Phase | Status | Tools/Techniques |
| :--- | :--- | :--- |
| **1. Business Understanding** | ✅ Complete | Problem Definition, KPI setup |
| **2. Data Collection** | 🔄 In Progress | `google-play-scraper`, `tqdm` |
| **3. Data Preparation** | ⏳ Pending | `nltk`, `re` (Regex), Custom Dialect Mappers |
| **4. Modeling** | ⏳ Pending | `TF-IDF`, `Logistic Regression`, `LDA` (Topic Modeling) |
| **5. Evaluation** | ⏳ Pending | Accuracy, F1-Score, Coherence Score |
| **6. Deployment** | ⏳ Pending | `Streamlit` Web App |

---

## Repository Structure

```text
RT4-PROJET-ML/
│
├── data/                   # Data Storage (GitIgnored)
│   ├── 01_raw/             # Original scraped reviews
│   ├── 02_intermediate/    # Cleaned/Translated data
│   └── 03_primary/         # Final dataset for modeling
│
├── notebooks/              # Jupyter Notebooks for experimentation
│   ├── 01_data_scraping.ipynb
│   ├── 02_eda_visuals.ipynb
│   ├── 03_preprocessing.ipynb
│   └── 04_modeling.ipynb
│
├── src/                    # Production-ready Source Code
│   ├── scraper.py          # Data collection logic
│   ├── preprocessing.py    # Text cleaning (Derja/Arabizi logic)
│   └── model.py            # Training & Inference
│
├── app/                    # Dashboard Application
│   └── app.py              # Streamlit Main App
│
├── models/                 # Serialized Models (.pkl)
└── requirements.txt        # Python Dependencies
```

## Getting Started
1. **Clone & Install**
```Bash
git clone [https://github.com/yourusername/RT4-PROJET-ML.git](https://github.com/yourusername/RT4-PROJET-ML.git)
cd RT4-PROJET-ML
pip install -r requirements.txt
```

2. **Configure Environment**
Create a `.env` file in the root directory:

```Ini, TOML
RAW_DATA_PATH="data/01_raw/tunisian_telco_reviews_raw.csv"
ORANGE_APP_ID="com.orange.myorange.otn"
```

3. **Run the Scraper**
Collect the latest data from the Play Store:

```Bash
# Run the notebook notebooks/01_data_scraping.ipynb
# OR (once implemented)
python src/scraper.py
```

## Key Challenges
- **Code-Switching**: Handling reviews that switch languages mid-sentence (e.g., "L'application est top mais reseau 7moum").

- **Derja Translation**: Converting 3 (Ain) and 7 (Ha) and 5 (Kha) into standardized text.

- **Emoji Semantics**: Interpreting 😡 vs 🤣 in a sarcastic context.

## Authors
**Youssef Hamdani**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-hamdani2)

*Created for Machine learning course as a mini project - 12/2025*