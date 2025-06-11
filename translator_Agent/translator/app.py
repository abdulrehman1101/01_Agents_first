import streamlit as st
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig

# Load .env variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Setup Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Config for run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define agent
agent = Agent(
    name="Sindhi Translator",
    instructions="You are a translator. Always translate English sentences into clear and simple Sindhi.",
)

# Async function to get translation
async def get_translation(text):
    return await Runner.run(agent, input=text, run_config=config)

# --- Streamlit App ---

# Page config
st.set_page_config(
    page_title="🌐 English to Sindhi Translator",
    page_icon="🔤",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }

    .stTextArea textarea {
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
        min-height: 150px;
        background-color: #f9f9f9;
    }

    .stButton>button {
        background-color: #0066cc;
        color: white;
        font-weight: 600;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        border: none;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #004a99;
    }

    .translation-box {
        background-color: #f0f4f8;
        border-left: 6px solid #0066cc;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🌐 English to Sindhi Translator")
st.markdown("Translate English sentences into simple **Sindhi**.")

# Input
user_input = st.text_area("✍️ Enter English sentence")

# Button + Result
if st.button("🔁 Translate"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                result = asyncio.run(get_translation(user_input))
                sindhi_translation = getattr(result, "final_output", "").strip()
                if sindhi_translation:
                    st.markdown(
                        f"<div class='translation-box'><b>Sindhi Translation:</b><br>{sindhi_translation}</div>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("❌ No translation received.")
            except Exception as e:
                st.error(f"Translation failed: {e}")

st.markdown("</div>", unsafe_allow_html=True)
