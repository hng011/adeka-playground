import requests
from bs4 import BeautifulSoup

def get_latest_arxiv_papers(domain: str, limit: int = 3):
    """
    Fetches the latest papers from arXiv for the given domain.
    """
    url = f"https://arxiv.org/search/?query={domain}&searchtype=all&abstracts=show&order=-announced_date_first&size=50"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    papers = soup.find_all("li", class_="arxiv-result")[:limit]

    for paper in papers:
        title = paper.find("p", class_="title").text.strip()
        authors = paper.find("p", class_="authors").text.strip().replace("Authors:", "").strip()
        abstract = paper.find("span", class_="abstract-full").text.strip().replace("\n", " ")
        link = paper.find("p", class_="list-title").find("a")["href"]

        results.append({
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "link": link
        })
    
    return results


def search_latest_arxiv(domain: str, n_paper: int = 3) -> list:
    """
    Search for arXiv publications in a given domain.
    
    Args:
        domain: The research domain to search for (e.g., 'machine learning').
        n_paper: The number of papers to fetch. Defaults to 3.
    """
    
    print(f"[DEBUG]: Fetching {n_paper} papers for domain: {domain}")
    papers = get_latest_arxiv_papers(domain, limit=n_paper)
    return papers