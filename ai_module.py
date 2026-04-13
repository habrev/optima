import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv, find_dotenv

# Automatically finds .env in the root while code is in src/
load_dotenv(find_dotenv())

# Initialize the new 2026 SDK Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_burnout(text):
    """
    TRL4 Extraction Layer: Converts unstructured text into 
    validated JSON schema for the Heuristic Engine.
    """
    
    # Define a strict schema to prevent engine crashes
    config = types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema={
            'type': 'object',
            'properties': {
                'primary_emotion': {'type': 'string'},
                'stress_level_int': {'type': 'integer'},
                'burnout_risk_score': {'type': 'number'},
                'context_summary': {'type': 'string'}
            },
            'required': ['primary_emotion', 'stress_level_int', 'burnout_risk_score', 'context_summary']
        }
    )

    prompt = f"""
    Act as a clinical data extractor for a Gen Z professional burnout app.
    Analyze the following telemetry and return data matching the schema.
    
    User Telemetry: {text}
    """

    try:
        # Using Gemini 3 Flash Preview as seen in your configuration
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt,
            config=config
        )
        
        # The new SDK provides the text attribute containing the JSON string
        return json.loads(response.text)
        
    except Exception as e:
        print(f"GenAI SDK Diagnostic Error: {e}")
        return None