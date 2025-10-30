import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import nltk
import sys

# --- NLTK Tokenizer Download ---
# We do this once at the start
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    st.info("Downloading NLTK 'punkt' tokenizer... (This runs only once)")
    nltk.download('punkt')
    st.experimental_rerun() # Rerun the script after download

# --- Page Configuration ---
st.set_page_config(page_title="Sentiment Analysis", layout="wide")

# --- Main Application ---
st.title("Sentiment Analysis Tool 📊")
st.write("Enter text below to analyze its sentiment. The app will classify each sentence as Positive, Negative, or Neutral.")

# --- Input Area ---
st.subheader("Enter Your Text")
user_text = st.text_area("Paste your text here:", height=200, placeholder="Example: I love Streamlit! It's so easy to use. But sometimes I get errors.")

if st.button("Analyze Sentiment"):
    if user_text:
        # --- Analysis Logic ---
        blob = TextBlob(user_text)
        
        positive = 0
        negative = 0
        neutral = 0
        
        # Store detailed results for the table
        results = []
        
        for sentence in blob.sentences:
            polarity = sentence.sentiment.polarity  # Range: -1 (neg) to 1 (pos)
            
            if polarity > 0:
                sentiment = "Positive"
                positive += 1
            elif polarity < 0:
                sentiment = "Negative"
                negative += 1
            else:
                sentiment = "Neutral"
                neutral += 1
            
            # Append detailed info
            results.append({
                "Sentence": str(sentence),
                "Polarity": f"{polarity:.2f}",
                "Sentiment": sentiment
            })
        
        total = positive + negative + neutral

        if total > 0:
            st.write("---")
            st.subheader("Analysis Results")

            # --- Layout with Columns ---
            col1, col2 = st.columns(2)

            with col1:
                # --- Summary Metrics ---
                st.subheader("Summary")
                st.metric("Total Sentences", total)
                st.metric("Positive Sentences", positive, f"{positive/total:.1%}")
                st.metric("Negative Sentences", negative, f"{negative/total:.1%}")
                st.metric("Neutral Sentences", neutral, f"{neutral/total:.1%}")

            with col2:
                # --- Matplotlib Bar Chart ---
                st.subheader("Sentiment Distribution")
                
                labels = ['Positive', 'Negative', 'Neutral']
                values = [positive, negative, neutral]
                colors = ['#28a745', '#dc3545', '#6c757d'] # Green, Red, Gray

                # Create figure and axis
                fig, ax = plt.subplots(figsize=(7, 5))
                bars = ax.bar(labels, values, color=colors)
                
                ax.set_title("Sentiment Analysis Results", fontsize=14, fontweight='bold')
                ax.set_ylabel("Number of Sentences", fontsize=12)
                ax.grid(axis='y', linestyle='--', alpha=0.7)
                
                # Add labels on top of bars
                for bar in bars:
                    yval = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.05, str(yval), ha='center', va='bottom', fontweight='bold')

                plt.tight_layout()
                
                # Display plot in Streamlit
                st.pyplot(fig)

            # --- Detailed Results Table ---
            st.write("---")
            st.subheader("Detailed Sentence-by-Sentence Analysis")
            if results:
                # Use Pandas for a nice dataframe display
                df = pd.DataFrame(results)
                st.dataframe(df)
            
        else:
            st.info("No sentences were detected. Please enter some valid text.")

    else:
        st.warning("Please enter some text to analyze.")

# --- Sidebar Info ---
st.sidebar.header("About")
st.sidebar.info("This app uses **TextBlob** for sentiment analysis and **Streamlit** to create the user interface. The bar chart is generated using **Matplotlib**.")