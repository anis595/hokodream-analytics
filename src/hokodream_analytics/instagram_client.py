import os
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_instagram_media():
    token = os.getenv("INSTAGRAM_ACCESS_TOKEN")

    if not token:
        raise ValueError("Le token Instagram est manquant")

    url_media = "https://graph.instagram.com/me/media"
    params = {"fields": "id,media_type,timestamp"}
    headers = {"Authorization": f"Bearer {token}"}
    toutes_publications = []

    while url_media:
        response_media = requests.get(
            url_media, headers=headers, timeout=10, params=params
        )
        params = None
        response_media.raise_for_status()
        donnees_media = response_media.json()
        url_suivante = donnees_media.get("paging", {}).get("next")
        url_media = url_suivante
        toutes_publications.extend(donnees_media["data"])

    donnees_media["data"] = toutes_publications

    return donnees_media


if __name__ == "__main__":
    resultat = fetch_instagram_media()
    print(resultat.keys())
