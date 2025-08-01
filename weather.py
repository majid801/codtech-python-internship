import requests
import matplotlib.pyplot as plt

API_KEY = '3165c5b210e5158861bfa21c5d77845d'
 # Replace with your actual key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
city = 'Chennai'

url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    main = data['main']
    temperature = main['temp']
    feels_like = main['feels_like']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    weather_description = data['weather'][0]['description']
    city_name = data['name']

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_description.capitalize()}")

    # Create chart
    labels = ['Actual', 'Feels Like', 'Min', 'Max']
    values = [temperature, feels_like, temp_min, temp_max]

    plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
    plt.title(f"Temperature in {city_name}")
    plt.ylabel("Temperature (°C)")
    plt.savefig("weather_chart.png")  # Saves the chart
    plt.show()

else:
    print(f"Failed to retrieve data: {response.status_code}")
