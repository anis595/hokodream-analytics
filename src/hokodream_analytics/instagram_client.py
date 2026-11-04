import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")

if not INSTAGRAM_ACCESS_TOKEN:
    raise ValueError("Le token Instagram est manquant")


def fetch_instagram_media():
    url_media = "https://graph.instagram.com/me/media"
    params = {"fields": "id,media_type,timestamp"}
    headers = {"Authorization": f"Bearer {INSTAGRAM_ACCESS_TOKEN}"}

    response_media = requests.get(url_media, headers=headers, timeout=10, params=params)

    response_media.raise_for_status()
    donnees_media = response_media.json()

    return donnees_media


if __name__ == "__main__":
    resultat = fetch_instagram_media()
    print(resultat.keys())
