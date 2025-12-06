# Customers Review Analysis Mini Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](https://github.com/)

> **A Machine Learning project to analyze customer sentiment and churn drivers for Tunisian Telecom providers (Orange, Ooredoo, Tunisie Telecom) by processing mixed-language reviews (French, Arabic, and Tunisian Derja).**

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tech Stack & Methodology](#tech-stack--methodology)
3. [Repository Structure](#repository-structure)
4. [Getting Started](#getting-started)
5. [Key Challenges](#key-challenges)
6. [Results](#results)
7. [Authors](#authors)

---

## Project Overview
Telecommunications companies in Tunisia face high customer churn. Traditional metrics fail to capture the *why* behind customer dissatisfaction, especially when feedback is written in **Tunisian Derja** (a mix of Arabic dialects and French) or **Arabizi** (Latin characters for Arabic).

**Our Goal:**
1. **Scrape** real-time reviews from the Google Play Store.
2. **Translate & Clean** the unique Tunisian dialect/Arabizi into a standardized format.
3. **Analyze Sentiment** (Positive/Negative) to track brand health.
4. **Visualize** insights via an interactive Streamlit Dashboard.

---

## Tech Stack & Methodology

We followed the **CRISP-DM** (Cross-Industry Standard Process for Data Mining) lifecycle:

| Phase | Tools/Techniques | Description |
| :--- | :--- | :--- |
| **1. Business Understanding** | Problem Definition, KPI setup | Understanding churn drivers and sentiment analysis goals. |
| **2. Data Collection** | `google-play-scraper`, `tqdm` | Scraped 20,600 reviews from Google Play Store. |
| **3. Data Preparation** | `nltk`, `re` (Regex), Custom Dialect Mappers | Cleaned and normalized text data, including Arabizi transliteration. |
| **4. Modeling** | `TF-IDF`, `Logistic Regression` | Achieved 88% accuracy for binary sentiment classification. |
| **5. Evaluation** | Accuracy, F1-Score | Evaluated model performance with balanced metrics. |
| **6. Deployment** | `Streamlit` Web App | Deployed an interactive dashboard for real-time predictions. |

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

---

## Getting Started

1. **Clone & Install**
```bash
git clone https://github.com/yourusername/RT4-PROJET-ML.git
cd RT4-PROJET-ML
pip install -r requirements.txt
```

2. **Configure Environment**
Create a `.env` file in the root directory:

```ini
RAW_DATA_PATH="data/01_raw/tunisian_telco_reviews_raw.csv"
ORANGE_APP_ID="com.orange.myorange.otn"
```

3. **Run the Scraper**
Collect the latest data from the Play Store:
```bash
python src/scraper.py
```

4. **Run the Dashboard**
Launch the Streamlit app:
```bash
streamlit run app/app.py
```

---

## Key Challenges

- **Code-Switching**: Handling reviews that switch languages mid-sentence (e.g., "L'application est top mais reseau 7moum").
- **Derja Translation**: Converting 3 (Ain), 7 (Ha), and 5 (Kha) into standardized text.
- **Emoji Semantics**: Interpreting 😡 vs 🤣 in a sarcastic context.

---

## Results

- **Model Performance**:
  - Accuracy: **88%**
  - F1-Score: **0.91 (Positive)**, **0.85 (Negative)**
- **Deployment**:
  - A Streamlit dashboard for real-time sentiment predictions.

---

## Authors

**Youssef Hamdani**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-hamdani2)

*Created for Machine Learning course as a mini project - 12/2025*