from dotenv import load_dotenv
from pipeline import generate_report_and_points
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

load_dotenv()

if "prev_mode" not in st.session_state:
    st.session_state.prev_mode = "💬 Chat"

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-live-preview",
    temperature=0.5
)

mode = st.sidebar.radio(
    "Select Mode (⚠️ changing mode will clear current chat)",
    ["💬 Chat", "📄 Report Generator"]
)

if mode != st.session_state.prev_mode:
    st.session_state.messages = []
    st.session_state.report_topic = ""
    st.session_state.report_output = None
    st.session_state.prev_mode = mode

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: #e5e7eb;
}
.block-container {
    max-width: 900px;
    padding-top: 3rem;
}
h1 {
    text-align: center;
    font-weight: 700;
    letter-spacing: 1px;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 2rem;
}
.stChatMessage {
    border-radius: 16px;
    padding: 8px;
}
[data-testid="stChatMessage-user"] {
    background-color: #1f2937;
}
[data-testid="stChatMessage-assistant"] {
    background-color: #020617;
    border: 1px solid #1f2937;
}
textarea {
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1>👾 BuddyAI</h1>
<p class="subtitle">Your friendly AI companion · Ask anything</p>
""", unsafe_allow_html=True)

if st.button("🗑 Clear chat"):
    st.session_state.messages = []
    st.rerun()

with st.container():
    st.markdown("### 💬 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    role = messages["role"]
    content = messages["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything")
History = []

if query:
    st.chat_message("user").markdown(query)

    if mode == "💬 Chat":
        st.session_state.messages.append({"role": "user", "content": query})

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                History.append(HumanMessage(content=msg["content"]))
            else:
                History.append(AIMessage(content=msg["content"]))

        def stream_response():
            for chunk in llm.stream(History):
                yield chunk.content

        try:
            with st.chat_message("ai"):
                full_response = st.write_stream(stream_response())

            st.session_state.messages.append({"role": "ai", "content": full_response})

        except Exception as e:
            st.error("⚠️ Something went wrong while calling the AI.")
            st.stop()

    elif mode == "📄 Report Generator":
        try:
            with st.spinner("Generating report..."):
                report, points = generate_report_and_points(query)

            report_output = f"""
### 📘 Report
{report}

---

### ✅ 5 Key Points
{points}
"""
            st.chat_message("ai").markdown(report_output)

        except Exception as e:
            st.error("⚠️ Something went wrong while generating the report.")
            st.stop()
