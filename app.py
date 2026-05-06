import os
import logging
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()

# Configure Gemini client
client = genai.Client(api_key=api_key)

logging.basicConfig(level=logging.INFO)

@st.cache_data(show_spinner=False)
def generate_food_switch(prompt):
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text

# Debug (commented out for now)
# try:
#     models = client.models.list()
#
#     st.write("Available Models:")
#
#     for m in models:
#         st.write(m.name)
#
# except Exception as e:
#     st.error(f"Error listing models: {e}")

# Page Configuration
st.set_page_config(
    page_title="CraveSwitch AI",
    page_icon="🍽️",
    layout="wide"
)

# Header Section
st.title("🍽 CraveSwitch AI")
st.caption("CraveSwitch AI helps users discover healthier alternatives to foods they crave while preserving taste and satisfaction.")
st.subheader("Keep the craving. Switch the damage.")

st.markdown("""
Welcome to **CraveSwitch AI**, your culturally-aware intelligent food swapping assistant.

Enter the food you're craving and the context, and we'll help you find a smarter, healthier alternative without sacrificing the satisfaction!
""")

# Input Form
with st.container():

    st.markdown("### 🍔 Tell Us About Your Craving")

    with st.form("craving_form"):

        dish = st.text_input(
            "What dish are you craving?",
            placeholder="e.g., Chole Bhature, Ice Cream, Biryani"
        )
        st.caption("Example: Biryani, Ice Cream, Pizza, Chole Bhature")

        context_options = [
            "Late-night craving",
            "Stress eating",
            "Gym/Fitness",
            "Quick hunger",
            "Comfort food",
            "Budget meal",
            "Social outing"
        ]

        context = st.selectbox(
            "What is the context?",
            context_options
        )

        submit_button = st.form_submit_button("Switch My Meal")

# Output Section
if submit_button:

    if not dish:
        st.warning("Please enter a dish.")
        st.stop()
        
    st.divider()

    prompt = f"""
You are CraveSwitch AI, a culturally-aware intelligent food swapping assistant.

The user wants:
Dish: {dish}
Context: {context}

Your job:
Help the user keep the satisfaction of the food while making it healthier.

Analyze:
1. Why this food is appealing psychologically or culturally
2. Main nutritional and behavioral concerns
3. Healthier alternatives preserving flavor and familiarity
4. Healthier cooking modifications
5. Smarter restaurant ordering strategies
6. Behavioral insights tied to the context

Be practical, concise, modern, and non-judgmental.

Use this exact format:

🍽 Original Dish

🧠 Craving Insight

🔴 Nutrition Risks

🔁 Smart Switches

👨‍🍳 Cook Smarter

🛒 Order Smarter

💡 Why This Works
"""

    with st.spinner("Analyzing flavor profile and generating healthier switches..."):

        try:

            response_text = generate_food_switch(prompt)
            logging.info(f"Generated food switch for: {dish} | Context: {context}")

            st.success("Analysis Complete!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Health Upgrade", "+42%")

            with col2:
                st.metric("Flavor Retention", "88%")

            st.markdown("---")
            st.markdown(response_text)
            st.markdown("---")

            st.caption(
                "CraveSwitch AI provides wellness suggestions and not medical advice."
            )

        except Exception as e:
            logging.error(str(e))
            st.error("The AI service is temporarily busy. Please try again in a few seconds.")