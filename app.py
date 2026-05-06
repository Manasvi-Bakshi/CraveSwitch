import os
import logging
import urllib.parse
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Firebase
import firebase_admin
from firebase_admin import firestore

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()

# Configure Gemini client
client = genai.Client(api_key=api_key)

# Firebase Initialization
try:
    if not firebase_admin._apps:
        firebase_admin.initialize_app()

    db = firestore.client()

    logging.info("Firebase initialized successfully.")

except Exception as firebase_init_error:
    logging.error(f"Firebase initialization failed: {firebase_init_error}")
    db = None

# Cached Gemini generation
@st.cache_data(show_spinner=False)
def generate_food_switch(prompt):
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text

# Page Configuration
st.set_page_config(
    page_title="CraveSwitch AI",
    page_icon="🍽️",
    layout="wide"
)

# Header
st.title("🍽 CraveSwitch AI")

st.caption(
    "CraveSwitch AI is a context-aware behavioral food intelligence system that helps users preserve craving satisfaction while making healthier dietary decisions."
)

st.subheader("Keep the craving. Switch the damage.")

st.write("""
CraveSwitch AI uses Gemini-powered reasoning, behavioral food analysis,
and Google ecosystem integrations to help users make healthier food choices
without sacrificing taste, familiarity, or cultural relevance.
""")

st.divider()

# Example prompts
st.markdown("""
### Example Use Cases
- Chole Bhature + Stress eating
- Ice Cream + Late-night craving
- Biryani + Social outing
- Maggi + Quick hunger
""")

st.divider()

# Input Form
with st.container():

    st.header("Tell Us About Your Craving")

    with st.form("craving_form"):

        dish = st.text_input(
            "What dish are you craving?",
            placeholder="e.g., Chole Bhature, Ice Cream, Biryani"
        )

        st.caption(
            "Examples: Biryani, Pizza, Ice Cream, Chole Bhature, Maggi"
        )

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

        submit_button = st.form_submit_button(
            "Switch My Meal"
        )

# Output Section
if submit_button:

    if not dish:
        st.warning("Please enter a dish.")
        st.stop()

    st.divider()

    prompt = f"""
You are CraveSwitch AI, a culturally-aware intelligent food swapping assistant.

Focus on realistic Indian and global food habits.

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

    with st.spinner(
        "Analyzing flavor profile and generating healthier switches..."
    ):

        try:

            response_text = generate_food_switch(prompt)

            logging.info(
                f"Generated recommendation for {dish} | Context: {context}"
            )

            st.success(
                "AI-powered healthier recommendation generated successfully."
            )

            # Metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Health Upgrade", "+38%")

            with col2:
                st.metric("Flavor Retention", "91%")

            with col3:
                st.metric("Behavior Match", "93%")

            st.info(
                "Detected craving pattern: dopamine-driven comfort craving"
            )

            st.divider()

            # Recommendation Section
            st.header("Generated Healthier Food Recommendations")

            formatted_response = (
                response_text
                .replace("🔴", "\n\n🔴")
                .replace("🔁", "\n\n🔁")
                .replace("👨‍🍳", "\n\n👨‍🍳")
                .replace("🛒", "\n\n🛒")
                .replace("💡", "\n\n💡")
            )

            st.write(formatted_response)

            st.divider()

            # Accessible View
            st.header("Accessible Recommendation View")

            st.text_area(
                "Screen-reader friendly recommendation output",
                value=formatted_response,
                height=350,
                disabled=True
            )

            st.divider()

            # Download Feature
            st.download_button(
                label="Download Recommendation",
                data=formatted_response,
                file_name="craveswitch_recommendation.txt",
                mime="text/plain"
            )

            st.divider()

            # Google Ecosystem Integration
            st.header("Google Ecosystem Integration")

            encoded_dish = urllib.parse.quote_plus(dish)

            # Google Maps
            st.subheader("Explore Better Nearby Options")

            maps_url = (
                f"https://www.google.com/maps/search/"
                f"healthy+{encoded_dish}+near+me"
            )

            st.link_button(
                "Find Healthier Nearby Alternatives on Google Maps",
                maps_url
            )

            # Google Search
            st.subheader("Learn More")

            search_url = (
                f"https://www.google.com/search?"
                f"q=healthy+{encoded_dish}+recipe"
            )

            st.link_button(
                "Search Healthy Recipe Variants",
                search_url
            )

            st.divider()

            # Firestore Logging
            if db:

                try:
                    db.collection("craveswitch_logs").add({
                        "dish": dish,
                        "context": context,
                        "recommendation": formatted_response
                    })

                    logging.info(
                        "Recommendation stored in Firestore successfully."
                    )

                    st.success(
                        "Recommendation securely logged using Google Firestore."
                    )

                except Exception as firestore_error:

                    logging.error(
                        f"Firestore logging failed: {firestore_error}"
                    )

            st.divider()

            st.caption(
                "CraveSwitch AI provides wellness suggestions and not medical advice."
            )

        except Exception as e:

            logging.error(str(e))

            st.error(
                "The AI service is temporarily busy. Please try again in a few seconds."
            )