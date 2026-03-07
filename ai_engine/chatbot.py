import json
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load health data
with open("data/health_data.json") as f:
    health_data = json.load(f)


# Translation function
def translate_text(text, target_language):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"Translate this text to {target_language}: {text}"

    response = model.generate_content(prompt)

    return response.text


# Chatbot response function
def get_response(user_message):

    msg = user_message.lower()

    for disease in health_data:

        if disease in msg:

            symptoms = ", ".join(health_data[disease]["symptoms"])
            prevention = ", ".join(health_data[disease]["prevention"])

            response = f"""
Disease: {disease}

Symptoms:
{symptoms}

Prevention:
{prevention}
"""

            # Translate response
            translated = translate_text(response, "Telugu")

            return translated

    return "Sorry, I don't have information about that disease."