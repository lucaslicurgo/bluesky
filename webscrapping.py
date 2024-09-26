import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

url = "https://public.api.bsky.app/xrpc/app.bsky.actor.getPreferences"

payload = {}
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Erro {response.status_code}: {response.text}")