import requests
for i in range(1,4):
    name = input()

    response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid=c6c12d328a75bfffb8b1305248e03ea1')
    result = response.json()

    lat = result[0]['lat']
    lon = result[0]['lon']

    weather_url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c6c12d328a75bfffb8b1305248e03ea1")
    weather_data = weather_url.json()

    city_name = weather_data['name']
    country_name = weather_data['sys']['country']
    temprature = round((weather_data['main']['temp'] - 273.15),2)
    weather_description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    if i == 1:
        with open("weather_data.txt", "w", encoding="utf-8") as f:
            f.write(f"Şəhər: {city_name}\n")
            f.write(f"Ölkə adı: {country_name}\n")
            f.write(f"Temperatur: {temprature} °C\n")
            f.write(f"Hava təsviri: {weather_description}\n")
            f.write(f"Rütubət: {humidity} %\n")
            f.write(f"Küləyin sürəti: {wind_speed} m/s\n")
            f.write("\n")
    else:
        with open("weather_data.txt", "a", encoding="utf-8") as f:
            f.write(f"Şəhər: {city_name}\n")
            f.write(f"Ölkə adı: {country_name}\n")
            f.write(f"Temperatur: {temprature} °C\n")
            f.write(f"Hava təsviri: {weather_description}\n")
            f.write(f"Rütubət: {humidity} %\n")
            f.write(f"Küləyin sürəti: {wind_speed} m/s\n")       
            f.write("\n") 
        

