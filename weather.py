import requests

# Replace this with your actual OpenWeatherMap API key
API_KEY = API_KEY = '3165c5b210e5158861bfa21c5d77845d'
    
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# City to fetch weather for
city = 'Chennai'

# Create the full API URL
url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'

# Send the request
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    temperature = main['temp']
    weather_description = weather['description']
    city_name = data['name']

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_description.capitalize()}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
