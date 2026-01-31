import json
import os
import time
from pathlib import Path  # New import for robust paths
from ingestion import fetch_rebel_news
from extractor import analyze_article

# 1. Define the path to the .env file (one level up from /src)
env_path = Path(__file__).resolve().parent.parent / '.env'

# 2. Load the .env file using the specific path

def main():
    print("\n Starting Pipeline: Rebel Arms Tracker")
    
    # Step 1: Ingestion 
    print("\n[Step 1] Ingesting Data from GDELT...")
    articles = fetch_rebel_news()
    
    if not articles:
        print("No articles found. Please check your internet connection.")
        return

    print(f" Successfully ingested {len(articles)} articles.")
    results = []

    #Step 2: Processing & NLP 
    print("\n[Step 2] Running NLP Extraction & Verification...")
    
    for i, article in enumerate(articles):
        # Build context for the LLM
        context_text = f"{article.get('title', '')}. Date: {article.get('seendate', '')}"
        
        print(f"   Processing Article {i+1}/{len(articles)}: {article.get('title')[:40]}...")
        
        # Call the extraction logic
        extraction_result = analyze_article(context_text)
        
        # Store result
        record = {
            "source_url": article.get('url'),
            "gdelt_id": article.get('url'),
            "timestamp": article.get('seendate'),
            "nlp_analysis": extraction_result
        }
        results.append(record)
        
        # Short pause to respect API limits
        time.sleep(1.0)

    # Step 3: Storage 
    print("\n[Step 3] Saving Structured Data...")
    
    output_dir = "../data/processed"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "verified_events.json")
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f" Pipeline finished successfully!")
    print(f" Output saved to: {output_file}")

if __name__ == "__main__":
    main()