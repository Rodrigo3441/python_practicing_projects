import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("API_URL")
token = os.getenv("API_KEY")

response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

print(response.status_code)

api_response = response.json()

print(api_response)