import os
from dotenv import load_dotenv
import requests

load_dotenv()


INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")


if not INSTAGRAM_ACCESS_TOKEN:
    raise ValueError("Le token est manquant")
print("Token chargé avec succès")

url = "https://graph.instagram.com/me"
headers = {"Authorization": f"Bearer {INSTAGRAM_ACCESS_TOKEN}"}
r = requests.get(url, headers=headers)
