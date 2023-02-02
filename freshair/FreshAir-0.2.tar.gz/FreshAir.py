import requests

def get_weather():
    api_key = "INSERT_YOUR_KEY_HERE"

    #get users current location
    ipinfo = requests.get("http://ipinfo.io").json()
    lat = ipinfo['loc'].split(',')[0]
    lon = ipinfo['loc'].split(',')[1]
    # Get the weather information for the current location
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    response = requests.get(url)
    weather_data = response.json()
    
    temperature = weather_data['main']['temp']
    wind_speed = weather_data['wind']['speed']
    print(f"The temperature is currently {temperature} degrees F in {ipinfo['city']}, {ipinfo['region']} with wind speeds of {wind_speed} mph.")
    if temperature  > 80:
        print("It's hot out! Try not to melt!")
    elif temperature > 68:
        print("It's a beautiful day out. You could probably get away with just a T-shirt!")
    elif temperature > 50:
        print("It's a little chilly out. Light jacket reccomended.")
    elif temperature > 32:
        print("It's cold out! Make sure to wear a coat!")
    elif temperature > 0:
        print("It's freezing out! Bundle up!")
    else:
        print("No. Just no. Stay inside. You think youre Wim Hof or something?")

    
    