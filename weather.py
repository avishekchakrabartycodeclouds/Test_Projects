import requests

city = input("Please Enter city: ")

# Replace YOUR_API_KEY with your actual WeatherAPI key
api_key = "75ef2d29e43b46d8b4d193629252306"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    r = requests.get(url)
    r.raise_for_status()  # Raises HTTPError if status != 200
    data = r.json()   
    
    print(f"\nWeather in {data['location']['name']}, {data['location']['country']}:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)
