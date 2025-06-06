import os
import requests
from config import load_env
load_env()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

def crear_repo_remoto(nombre_repo):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "name": nombre_repo,
        "private": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"🌐 Repo remoto creado: https://github.com/{GITHUB_USERNAME}/{nombre_repo}")
        return f"https://github.com/{GITHUB_USERNAME}/{nombre_repo}.git"
    else:
        print("❌ Error al crear el repo remoto:", response.json())
        return None
