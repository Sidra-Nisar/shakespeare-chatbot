# 🎭 Shakespeare Chatbot

This is an AI-powered chatbot that responds in Shakespearean style. Built using HuggingFace Transformers, FAISS, and Streamlit.

## 🚀 How to Run

1. Extract this folder.
2. Open terminal and navigate to project folder.
3. Install dependencies:
   pip install -r requirements.txt
4. Run chatbot:
   streamlit run streamlit_app.py

## 📁 File Structure

- streamlit_app.py — Main user interface
- generator.py — GPT-based response generator
- retrieve_quotes.py — Searches relevant Shakespeare quotes
- quotes.pkl, shakespeare_index.faiss — Vector data files

