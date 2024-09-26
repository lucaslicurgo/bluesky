import requests
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASS_LOGIN')

url = "https://bsky.social/xrpc/com.atproto.server.createSession"

data = {
    "identifier": email,
    "password": password
}

response = requests.post(url, json=data)

tokens = response.json()


print("Token de acesso: ", tokens['accessJwt'])