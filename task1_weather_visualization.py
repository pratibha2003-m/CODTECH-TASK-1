import requests
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_weather_data(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def visualize_weather(data):
    labels = ['Temperature', 'Feels Like', 'Min Temp', 'Max Temp']
    values = [data['main']['temp'], data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max']]

    plt.figure(figsize=(8, 5))
    sns.barplot(x=labels, y=values, palette='coolwarm')
    plt.title(f"Weather Data for {data['name']}")
    plt.ylabel("Temperature (°C)")
    plt.show()

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(city)
    visualize_weather(weather_data)
