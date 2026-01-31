import os
import json
import sys
from pathlib import Path
from huggingface_hub import InferenceClient

def get_hf_token():
    """Manually reads the .env file to bypass python-dotenv parse errors."""
    try:
        # Resolve path to project root (one level up from /src)
        base_dir = Path(__file__).resolve().parent.parent
        env_path = base_dir / ".env"
        
        if not env_path.exists():
            return None
            
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                # Look for the token line, ignore 'export' if present
                clean_line = line.strip().replace("export ", "")
                if clean_line.startswith("HF_TOKEN="):
                    # Get the part after '=' and strip quotes
                    return clean_line.split("=", 1)[1].strip().strip('"').strip("'")
    except Exception as e:
        print(f"   [System Error] Manual .env read failed: {e}")
    return None

def analyze_article(text):
    """Analyzes text using Hugging Face Chat Completion (Llama 3)."""
    
    api_token = get_hf_token()
    if not api_token:
        print(" [NLP Error] HF_TOKEN not found in .env file.")
        sys.exit(1)

    # Initialize Client - using Llama 3 (excellent for extraction)
    client = InferenceClient(token=api_token)
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

    # Chat Completion is the required 'Conversational' task for this model
    messages = [
        {
            "role": "system",
            "content": (
                "You are a military hardware analyst. Extract data into JSON. "
                "If no specific weapon is named, infer the category (e.g., 'Small Arms' for clashes, "
                "'Explosives' for blasts). Always provide a 'verification_status': "
                "'VERIFIED' if a specific weapon is named, 'INFERRED' if category is used."
            )
        },
        {
            "role": "user",
            "content": f"Analyze this report and extract JSON with keys 'rebel_group', 'weapon', 'verification_status', 'evidence_quote': {text[:1500]}"
        }
    ]


    try:
        response = client.chat_completion(
            model=model_id,
            messages=messages,
            max_tokens=300,
            temperature=0.1
        )
        
        raw_content = response.choices[0].message.content.strip()
        
        # Isolate JSON from any extra text
        start = raw_content.find('{')
        end = raw_content.rfind('}') + 1
        if start != -1 and end != -1:
            return json.loads(raw_content[start:end])
        
        return {"error": "JSON not found", "raw": raw_content}

    except Exception as e:
        print(f"   [NLP Error] HF API failure: {e}")
        return {"rebel_group": "Unknown", "verification_status": "API_ERROR"}