import requests

def get_atmospheric_pressure():
    response = requests.get('https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Mexico')
    weather_data = response.json()
    return weather_data['current']['pressure_mb']

def get_fortnite_users():
    response = requests.get('https://api.fortniteapi.com/v1/stats')
    fortnite_data = response.json()
    return fortnite_data['current_users']
