
# This file fetches and processes weather data from Open Weather Map API
# into decision tree friendly information

import requests


def weather_fetch(zipcode):
    ''' Fetches weather data from Open Weather API based on zip code 
    returns json of the 7 day forecast or prints  error code
    ''' 

    # Request made to Open Weather, retireve location from zipcode. 
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

        # Second request made to Open Weather. Using lat long -> receive temperature forecast for the next 7 days
        # if we want to do the past 5 days: https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}
        #  We exclude data we don't need, like minute by minute data
        r2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude=hourly,minutely&appid=f56ee6c2422b8ff51dadde24ec803e5f')
        if r.status_code != 200:  # Handle erroneous requests
            print("Error: " + str(r.status_code))
        else:
            json_object_2 = r2.json()
            # for k,v in json_object.items():
            #     print(k,v)

        return [json_object_2, city, country, lat, lon]



def weather_process(api_data):
    ''' Takes raw api data and returns an integer of the average weather '''  
    
    # Get the 'daily' section of the data
    daily = api_data[0]['daily']
    print('City:', api_data[1], 'Country:', api_data[2])

    temp_total = 0
    counter = 0

    # Retrieve the temperatures, convert to farenheit, and add to the total
    days = 0
    for item_a in daily:
        days += 1
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
    Weather: 1= hot Avg high > 80; 2 = warm Avg high 65 to 80; 3 = cool Avg high 33 to 65, low: 45-33; 4 = cold Avg high < 32, low ≤ 32 
    Weather range: 1-2 or 3
    ''' 
    
    # Categorize the average temperature into one of the above categories
    category = None

    if avg_temp >= 80:
        category = 1 
    elif 65 <= avg_temp < 80: 
        category = 2
    elif 33 <= avg_temp < 65: 
        category = 3
    elif avg_temp <= 32:
        category = 4
    else:
        print('error: category')
        return  
   
    return int(category)


def wthr_num(zip_code):

    wthr_data = weather_fetch(zip_code)
    wthr_average = weather_process(wthr_data)
    wthr_value = translate_avg_weather(wthr_average)

    print(wthr_value)
    return wthr_value


if __name__ == "__main__":

    zip_code = '60565'
    wthr_num(zip_code)
    