import os
from dotenv import load_dotenv
import requests
from requests import HTTPError
from requests import ConnectionError
from requests import Timeout

load_dotenv()


INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")


if not INSTAGRAM_ACCESS_TOKEN:
    raise ValueError("Le token est manquant")
print("Token chargé avec succès")

url = "https://graph.instagram.com/me"
headers = {"Authorization": f"Bearer {INSTAGRAM_ACCESS_TOKEN}"}
params = {"fields": "id,username"}

try:
    response = requests.get(url, headers=headers, timeout=10, params=params)

    response.raise_for_status()
except Timeout:
    print("Le serveur ne répond pas")
except HTTPError:
    print("Instagram a refusé notre requête")
except ConnectionError:
    print("Impossible de contacter Instagram")
else:
    donnees = response.json()
    print(f"Compte instagram connecté : {donnees.get("username")}")
