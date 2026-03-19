import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -23.55,
    "longitude": -46.26,
    "hourly": "temperature_2m,precipitation"
}

response = requests.get(url, params=params)
print(response.json())
input('Press any key to continue')
