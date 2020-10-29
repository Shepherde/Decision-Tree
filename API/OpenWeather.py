
import requests


def open_weather_fetch(zipcode):
    ''' Fetches weather data from Open Weather API based on zip code 
    returns json of the 7 day forecast or prints  error code
    ''' 
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=f56ee6c2422b8ff51dadde24ec803e5f')
    if r.status_code != 200:  # Handle erroneous requests
        print("Error: " + str(r.status_code))
    else:
        json_object = r.json()
    # print(json_object)

    city = json_object['name']
    country = json_object['sys']['country']

    lat = str(json_object['coord']['lat'])
    lon = str(json_object['coord']['lon'])

    r2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude=hourly,minutely&appid=f56ee6c2422b8ff51dadde24ec803e5f')
    if r.status_code != 200:  # Handle erroneous requests
        print("Error: " + str(r.status_code))
    else:
        json_object_2 = r2.json()

    return json_object_2



def open_weather_process(api_data):
    ''' Takes raw api data and returns an integer of the average weather '''  
    
    daily = api_data['daily']
    # print(daily)

    # for item in daily:
    #     print(item['temp']['day'], item['temp'])

    temp_total = 0
    counter = 0

    # Retrieve the temperatures, convert to farenheit, and add to the total
    days = 0
    for item_a in daily:
        # print(item_a['temp'])
        days += 1
        # print('Day:',counter)

        for key, value in item_a['temp'].items():
            temp_f = round((value - 273.15) * 1.8 + 32)
            # print(temp_f)
            temp_total += temp_f 
            counter += 1
    
    # Calculate the average for the 8 days
    eight_day_average_temp = round(temp_total / counter)
    # print(temp_total, counter, eight_day_average_temp)

    return int(eight_day_average_temp)

def translate_avg_weather(avg_temp):
    ''' Translates API fetched data into Decision Tree readable information
    Climate: 1=Arid, 2=Temperate, 3=Subtropical, 4=Tropical 
    Weather: 1= hot Avg high > 80; 2 = warm Avg high 65 to 80; 3 = cool Avg high 33 to 65, low: 45-33; 4 = cold Avg high < 32, low ≤ 32 ''' 
    
    category = None

    if avg_temp >= 80:
        category = 1 
    elif 65 <= avg_temp < 80: 
        category = 2
    elif 33 <= avg_temp < 65: 
        category = 3
    elif avg_temp <= 32:
        category = 4
    
    # print(category)
    return int(category)


def wthr_num(zip_code):

    wthr_data = open_weather_fetch(zip_code)
    wthr_average = open_weather_process(wthr_data)
    wthr_value = translate_avg_weather(wthr_average)

    # print(wthr_value)
    return wthr_value


if __name__ == "__main__":

    zip_code = '94108'
    wthr_num(zip_code)
    