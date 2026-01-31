import requests
import urllib.parse

def fetch_rebel_news():
    """
    Fetches news from GDELT 2.0 Doc API.
    Fixed: Uses correct parentheses for Boolean queries.
    """
    base_url = "https://api.gdeltproject.org/api/v2/doc/doc"
    
    # CORRECT SYNTAX: Parentheses around the OR block are mandatory!
    query = '("rebel group" OR insurgents OR militia) sourcelang:eng'
    
    params = {
        "query": query,
        "mode": "artlist",
        "format": "json",
        "maxrecords": 10,
        "timespan": "1m"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Research Project Bot; contact: anh.nguyen1@campus.lmu.de)"
    }
    
    print(f"\n   [Ingestion] Connecting to GDELT with query: {query}")
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                articles = data.get('articles', [])
                print(f"   [Success] Found {len(articles)} articles.")
                return articles
            except:
                print("   [Error] Server returned 200 but content was not JSON.")
                return []
        else:
            print(f"   [Error] GDELT Status Code: {response.status_code}")
            # print(response.text) # Uncomment if you need deep debugging
            return []

    except Exception as e:
        print(f"   [Fatal Error] Connection failed: {e}")
        return []