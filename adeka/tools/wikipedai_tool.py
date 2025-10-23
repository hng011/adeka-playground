import requests
from bs4 import BeautifulSoup

def search_wikipedia_tool(query: str) -> str:
    """Search Wikipedia and return summarized content."""
    try:
        search_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            return f"Could not find Wikipedia page for '{query}'."
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        content_nodes = soup.select("#mw-content-text p, #mw-content-text li, p")
        
        parts = [n.get_text(separator=" ", strip=True) for n in content_nodes[:10]]
        text = " ".join(p for p in parts if p)
        
        print("DEBUG: ", text)
        
        return text.strip()
    
    except Exception as e:
        return f"Error fetching data: {e}"