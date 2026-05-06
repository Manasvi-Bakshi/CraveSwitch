# 🍽 CraveSwitch AI

**Keep the craving. Switch the damage.**

CraveSwitch AI is a culturally-aware intelligent food swapping assistant built to help users navigate their cravings. It provides practical, non-judgmental, and healthy alternatives to favorite dishes based on the specific psychological and situational context of the craving.

## 🔴 Live Demo
🚀 **[Deployed on Google Cloud Run](#)** *(Replace with actual URL after deployment)*

## 📸 Screenshots

*(Placeholder for App Dashboard Screenshot)*

*(Placeholder for Recommendation Output Screenshot)*

*(Placeholder for Google Maps Integration Screenshot)*

## 🚀 Project Overview

CraveSwitch AI takes a user's desired dish and their current craving context (like "Stress eating" or "Late-night craving") and generates a personalized breakdown. Instead of just saying "eat a salad," it offers:
- Insights into why the food is appealing
- Healthier alternatives that preserve flavor and cultural familiarity
- Cooking modifications
- Smarter restaurant ordering strategies

## 🏗 Architecture

User Input → Streamlit UI → Gemini API → Contextual Food Analysis → Healthier Recommendations

## ✨ Features

- Context-aware craving analysis
- AI-powered healthier food swaps
- Behavioral eating insights
- Cooking modifications
- Restaurant ordering intelligence
- Cloud-native deployment

## 🌐 Google Ecosystem Integration

This application relies on a robust Google ecosystem stack to deliver value:
- **Gemini API (`gemini-1.5-flash`)**: Used for contextual food reasoning and personalized health swapping.
- **Google Cloud Run**: Serverless compute platform hosting the Streamlit application.
- **Google Cloud Build**: Automated CI/CD pipelines to build the container images.
- **Artifact Registry**: Secure storage for the Docker container images.
- **Google Maps Workflow Integration**: Dynamically generates local search queries to find healthier restaurant alternatives.
- **Google Search Integration**: Quickly links out to healthy recipe variations for user cooking.

## ♿ Accessibility Features

CraveSwitch AI is built with accessibility and usability in mind:
- **Readable Layouts**: A wide, spacious layout ensures text isn't cramped.
- **Explicit Labels**: Clear helper text and captions guide users effectively.
- **Downloadable Outputs**: Users can easily download their recommendations as `.txt` files.
- **Structured Recommendation Sections**: The UI features semantic headings, clear dividers, and a dedicated `text_area` view specifically optimized for screen readers to easily consume the AI output.

## 🧪 Testing

Code quality and reliability are ensured using **pytest**-based validation. The test suite covers:
- API configuration and secrets availability
- Input string validation
- Context option integrity
- Prompt variable injection logic
- Score range constraints

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
     --region asia-south1 \
     --allow-unauthenticated \
     --set-env-vars="GEMINI_API_KEY=your_actual_api_key_here"
   ```

## 🔮 Future Improvements

- Nutritional database integration
- Real-time calorie estimation
- Personalized health profiles
- Voice-based craving assistant
- Multi-language support
