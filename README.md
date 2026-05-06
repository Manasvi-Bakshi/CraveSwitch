# 🍽 CraveSwitch AI

**Keep the craving. Switch the damage.**

CraveSwitch AI is a culturally-aware intelligent food swapping assistant built to help users navigate their cravings. It provides practical, non-judgmental, and healthy alternatives to favorite dishes based on the specific psychological and situational context of the craving.

## 🚀 Project Overview

CraveSwitch AI takes a user's desired dish and their current craving context (like "Stress eating" or "Late-night craving") and generates a personalized breakdown. Instead of just saying "eat a salad," it offers:
- Insights into why the food is appealing
- Healthier alternatives that preserve flavor and cultural familiarity
- Cooking modifications
- Smarter restaurant ordering strategies

## Architecture

User Input → Streamlit UI → Gemini API → Contextual Food Analysis → Healthier Recommendations

## Features

- Context-aware craving analysis
- AI-powered healthier food swaps
- Behavioral eating insights
- Cooking modifications
- Restaurant ordering intelligence
- Cloud-native deployment

## Testing

Basic validation tests were implemented using pytest to verify:
- API configuration
- Input handling
- Context option integrity

## Google Cloud Services Used

- Google Cloud Run for serverless deployment
- Gemini API for contextual food reasoning
- Google Cloud Build for automated container builds
- Artifact Registry for container storage
- Vertex AI ecosystem compatibility through Gemini models

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

## Future Improvements

- Nutritional database integration
- Real-time calorie estimation
- Personalized health profiles
- Voice-based craving assistant
- Multi-language support
