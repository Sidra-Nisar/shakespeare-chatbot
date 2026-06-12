import streamlit as st
from generator import generate_response
from retrieve_quotes import search_quotes

st.set_page_config(page_title="Shakespeare Chatbot")

st.title("🎭 Shakespeare Chatbot")
st.write("Ask me anything about Shakespeare’s plays, characters, or themes.")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display full conversation
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"🟨 **You:** {message}")
    else:
        st.markdown(f"🟥 **{speaker}:** {message}")

# Create input form (so input is handled BEFORE rerun)
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("Ask The Bard...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Retrieve quote and generate response
    quotes = search_quotes(user_input)
    with st.spinner("Thinking in Shakespearean style..."):
        reply = generate_response(user_input, quotes)

    # Add messages to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Shakespeare Bot", reply))

    # Rerun after input
    st.rerun()
