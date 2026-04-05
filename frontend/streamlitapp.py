import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="RAG Chat Assistant",
    page_icon="💬",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- STYLING ----------------
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}
.user-bubble {
    background-color: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 10px 0;
    text-align: right;
}
.assistant-bubble {
    background-color: #f1f5f9;
    color: #111827;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 10px 0;
    text-align: left;
}
.header {
    text-align: center;
    padding-bottom: 10px;
}
.clear-btn button {
    background-color: #ef4444 !important;
    color: white !important;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>💬 RAG Chat Assistant</h1>
    <p style="color:gray;">Ask questions about your uploaded research paper</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### 📄 Upload Document")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        with st.spinner("Processing PDF..."):
            response = requests.post(
                f"{API_BASE_URL}/ingest",
                files={"file": uploaded_file}
            )
        if response.status_code == 200:
            st.success("✅ Document ready!")
        else:
            st.error("❌ Upload failed")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- CHAT DISPLAY ----------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
query = st.chat_input("Ask something about your document...")

if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Thinking..."):
        response = requests.get(
            f"{API_BASE_URL}/query",
            params={"q": query}
        )

    if response.status_code == 200:
        answer = response.json()["answer"]
    else:
        answer = "❌ Failed to fetch answer from backend."

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    st.rerun()