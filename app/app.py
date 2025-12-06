import streamlit as st
import joblib
import pandas as pd

# --- CONFIGURATION ---
MODEL_PATH = '../models/sentiment_model.pkl'  # Ensure this matches the file name you saved earlier

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        return None

pipeline = load_model()

# --- UI LAYOUT ---
st.set_page_config(page_title="Tunisian Sentiment Analyzer", page_icon="🇹🇳")

st.title("RT4 ML Mini project - Sentiment Analysis")
st.write("Type a review in derja, French, or Mixed dialect to test the AI.")

# --- INPUT SECTION ---
user_input = st.text_area("Enter your review here:", height=100, placeholder="e.g. Connexion khayba barcha...")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    elif pipeline is None:
        st.error(f"Error: Could not find '{MODEL_PATH}'. Make sure the file is in the same folder as this script.")
    else:
        # --- PREDICTION ---
        # The pipeline handles the vectorization automatically
        prediction = pipeline.predict([user_input])[0]
        probabilities = pipeline.predict_proba([user_input])[0]
        
        # --- DISPLAY RESULTS ---
        st.markdown("---")
        
        # Get confidence score (the highest probability)
        confidence = max(probabilities)
        
        if prediction == 'Positive':
            st.success(f"**Sentiment: POSITIVE** (Confidence: {confidence:.2%})")
            st.balloons()
        else:
            st.error(f"**Sentiment: NEGATIVE** (Confidence: {confidence:.2%})")
            
        # Optional: Show breakdown
        st.caption(f"Model Probability: Negative: {probabilities[0]:.2f} | Positive: {probabilities[1]:.2f}")