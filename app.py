import streamlit as st

st.set_page_config(
    page_title="Voice2Query AI",
    page_icon="🎤",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0e1117;
    color: white;
}

/* Title styling */
h1 {
    color: #00ffcc;
    text-align: center;
}

/* Buttons */
.stButton > button {
    background-color: #00ffcc;
    color: black;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton > button:hover {
    background-color: #00bfa6;
    color: white;
}

/* Dataframe styling */
.dataframe {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)



import streamlit as st

from modules.record_audio import record_audio
from modules.speech_to_text import transcribe_audio
from modules.text_to_sql import generate_sql
from modules.sql_executor import execute_query

st.set_page_config(
    page_title="Voice2Query AI",
    page_icon="🎤",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

h1 {
    color: #00ffcc;
    text-align: center;
}

.stButton > button {
    background-color: #00ffcc;
    color: black;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton > button:hover {
    background-color: #00bfa6;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("🎤 Voice2Query AI Dashboard")

st.markdown("### Speak → SQL → Data Visualization")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎙️ Voice Input")

    if st.button("Start Recording"):
        record_audio()

        text = transcribe_audio("audio/input.wav")

        st.success("Speech Recognized")
        st.write(text)

        sql_query = generate_sql(text)

        st.info("Generated SQL Query")
        st.code(sql_query)

        results = execute_query(sql_query)

with col2:
    st.subheader("📊 Results Panel")

    try:
        st.dataframe(results)

        st.bar_chart(results.select_dtypes(include='number'))

    except:
        st.warning("No data to display yet")

st.sidebar.title("⚙️ Controls")
st.sidebar.info("Voice2Query System")

model = st.sidebar.selectbox(
    "Choose Mode",
    ["Movies DB"]
)

st.progress(0)
st.progress(5)
st.progress(15)
st.progress(20)
