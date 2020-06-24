import requests
def Weather(city):
    API_key = "87bc2fcd3bb7cee050c3b5907e0f5c61"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #loc = tracker.get_slot('location')
    #loc=input('location: ')
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    # if weather_data:
    #     temp = weather_data['main']['temp']
    #     #description = weather_data['weather'][0]['description']
    #     output="The temperature of {} is {} °C.".format(city,temp)
    # else:
    #     output="We did not find any weather information for {}. Try by a city name.".format(city)
    
    return weather_data['main']
