import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 11.0168,
    "longitude": 76.9558,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Asia/Kolkata"
}

headers = {
    "Accept": "application/json",
    "User-Agent": "PythonWeatherClient/1.0"
}

try:
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()
    weather = data["current"]

    print("\n===== Coimbatore Weather =====")
    print(f"Time        : {weather['time']}")
    print(f"Temperature : {weather['temperature_2m']} °C")
    print(f"Humidity    : {weather['relative_humidity_2m']} %")
    print(f"Wind Speed  : {weather['wind_speed_10m']} km/h")

except requests.exceptions.Timeout:
    print("Error: The API request timed out.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect. Check your internet connection.")

except (requests.exceptions.RequestException, ValueError, KeyError) as error:
    print(f"Error while fetching weather data: {error}")