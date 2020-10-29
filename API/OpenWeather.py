
import requests

def OpenWeatherFetch(zipcode):
    ''' fetches weather data from Open Weather API based on zip code 
    returns the average highs and lows of a 7 day forecast
    ''' 
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=f56ee6c2422b8ff51dadde24ec803e5f')
    json_object = r.json()
    # print(json_object)

    city = json_object['name']
    country = json_object['sys']['country']

    lat = str(json_object['coord']['lat'])
    lon = str(json_object['coord']['lon'])

    r2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude=hourly,minutely&appid=f56ee6c2422b8ff51dadde24ec803e5f')
    json_object_2 = r2.json()
    daily = json_object_2['daily']
    # print(daily)

    for item in daily:
        print(item['temp']['day'], item['temp'])
        

    # temp_k = float(json_object['main']['temp'])
    # temp_f = (temp_k - 273.15) * 1.8 + 32

    return

def OpenWeatherProcess(city, weather):
    ''' Translates API Fetched data into Decision Tree readable codes 
    Climate: 1=Arid, 2=Temperate, 3=Subtropical, 4=Tropical 
    Weather: 1= hot Avg high > 80; 2 = warm Avg high 65 to 80; 3 = cool Avg high 33 to 65, low: 45-33; 4 = cold Avg high < 32, low ≤ 32 ''' 
    pass


if __name__ == "__main__":
    OpenWeatherFetch('94108')