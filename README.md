# 🍽 CraveSwitch AI

**Keep the craving. Switch the damage.**

CraveSwitch AI is a culturally-aware intelligent food swapping assistant built to help users navigate their cravings. It provides practical, non-judgmental, and healthy alternatives to favorite dishes based on the specific psychological and situational context of the craving.

## 🚀 Project Overview

CraveSwitch AI takes a user's desired dish and their current craving context (like "Stress eating" or "Late-night craving") and generates a personalized breakdown. Instead of just saying "eat a salad," it offers:
- Insights into why the food is appealing
- Healthier alternatives that preserve flavor and cultural familiarity
- Cooking modifications
- Smarter restaurant ordering strategies

## 🏗 Architecture

The project is built using a modern, lightweight, and scalable stack:
- **Frontend/UI:** [Streamlit](https://streamlit.io/) for a clean, interactive, and modern web interface.
- **Backend/Logic:** Python.
- **AI Engine:** Google's Gemini API (`gemini-1.5-flash`), accessed via `google-generativeai`.
- **Environment Management:** `python-dotenv` for secure API key loading.
- **Containerization:** Docker for easy deployment to cloud platforms.

## 🔄 Workflow

1. **User Input:** The user enters a dish they are craving and selects the context from a dropdown menu.
2. **Prompt Generation:** The app dynamically inserts the user's input into a carefully engineered prompt.
3. **AI Inference:** The prompt is sent securely to the Gemini API (`gemini-1.5-flash`).
4. **Structured Output:** The AI returns a highly structured response formatted with emojis and specific sections.
5. **Display:** Streamlit renders the generated markdown elegantly on the screen for the user.

## 🧠 How Gemini is Used

CraveSwitch AI leverages the Google `gemini-1.5-flash` model. The integration happens via the `google-generativeai` SDK. 
The system prompt enforces a very specific persona ("culturally-aware intelligent food swapping assistant") and mandates a strict output format (Original Dish, Craving Insight, Nutrition Risks, Smart Switches, Cook Smarter, Order Smarter, Why This Works). The prompt enforces non-judgmental and culturally respectful outputs to ensure maximum user retention and satisfaction.

## ☁️ Google Cloud Deployment Instructions

This application is containerized and ready to be deployed to Google Cloud Run.

1. **Prerequisites:** 
   - Ensure you have the [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install) installed and authenticated.
   - Set your active project: `gcloud config set project YOUR_PROJECT_ID`

2. **Build and Push the Image:**
   You can use Google Cloud Build to build and push the container to Google Artifact Registry:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/craveswitch-ai
   ```

3. **Deploy to Cloud Run:**
   Deploy the image, ensuring you pass your Gemini API key as an environment variable:
   ```bash
   gcloud run deploy craveswitch-ai \
     --image gcr.io/YOUR_PROJECT_ID/craveswitch-ai \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars="GEMINI_API_KEY=your_actual_api_key_here"
   ```

## 🔮 Future Improvements

- **Image Recognition:** Allow users to upload a picture of a meal or menu to get instant swapping advice.
- **Dietary Profiles:** Add user accounts to save allergies, specific diets (keto, vegan), and past swaps.
- **Recipe Generation:** Integrate functionality to generate full step-by-step recipes for the suggested "Smart Switches."
- **Restaurant Integration:** Use location services to recommend specific healthy dishes from nearby restaurants.
