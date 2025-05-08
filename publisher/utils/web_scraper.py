import requests
from bs4 import BeautifulSoup

def find_artists() -> list:
    url = "https://it.wikipedia.org/wiki/Eurovision_Song_Contest_2025"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", {"class": "wikitable"})

    artisti = []

    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        if "Artista" in headers:
            idx_artista = headers.index("Artista")
            for row in table.find_all("tr")[1:]:
                cells = row.find_all(["td", "th"])
                if len(cells) > idx_artista:
                    artista = cells[idx_artista].get_text(strip=True)
                    artisti.append(artista)
            break
    
    return artisti