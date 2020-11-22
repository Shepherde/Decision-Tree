
''' This file fetches climate data for a zipcode from the Azavea Climate organization
and compiles the numbers for each year into a decision tree readable value 

We use the climate data to predict the WEATHER OF THE NEXT THREE MONTHS BASED ON ITS HISTORY
''' 


import requests
import json
import datetime

from month_counter import *

from urllib.parse import urljoin
from OpenWeather import weather_fetch


def climate_fetch(zipcode):
    ''' function fetches the json data for a zipcode's climate data
    returns the raw json data ''' 
    
    # Get lat lon data from weather_fetch Open Weather API
    weather_data = weather_fetch(zipcode)
    lat = weather_data[3]
    lon = weather_data[4]
    
    token = '6a096669f08500167edb361455210681ad1d8cbd'
    baseurl = 'https://app.climate.azavea.com/api/'
    header = {'Authorization': 'Token {}'.format(token),
                       'Origin': 'https://www.serch.us'}
    
    scenario = 'historical'
    params = '2010'

    querystring = '/api/climate-data/{}/{}/{}'.format(lat, lon, scenario)

    # List all scenarios
    scenario_querystring = '/api/scenario'

    url = urljoin(baseurl,querystring)

    try:
        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        result = json.loads(response.content.decode())    
        return result

    except requests.exceptions.RequestException as e:
        raise e

def climate_process(api_data):
    ''' takes in the api data and returns the average climate in a zipcode 
    based on pattern of weather for the next three months at the location 
    Averages the Max and Min temperature of each day of the next three months in each year for n years on record.
    ''' 

    temp_total = 0
    counter = 0

    # print(api_data)
    
    # print("length: ", len(api_data['data']))

    # Check if data exists
    if len(api_data['data']) == 0:
        print('NO DATA AVAILABLE')
        return  False

    else:
        # for each year in the data, get all max 
        for item in api_data['data'].keys():
                
            tmax = []
            tmin = []
            
            # all the data for every day of the year

            # grabs the min for each day, appends to tmin variable
            counter = 1
            for thing in api_data['data'][item]['tasmin']:
                if type(thing) == float:
                    tmin.append(thing)
                    counter += 1
            
            # grabs the max for each day, appends to max variable
            counter2 = 1
            for thing in api_data['data'][item]['tasmax']:
                if type(thing) == float:
                    tmax.append(thing)
                    counter2 += 1
            
            zipped = zip(tmax, tmin)

            # print('ZIPPED: --------------------- ')            

            # Find current month
            currentDT = datetime.datetime.now()

            # print ("Current Year is: %d" % currentDT.year)
            # print ("Current Month is: %d" % currentDT.month)
            
            # Find the range of days in the year of the next 3 months

            # get the index of next three months
            next_three = get_months(currentDT.month)
            # print(next_three)

            # get the days in that year which correspond to our next three months *** 
            days = get_days(int(item), next_three)
            # print(days)

            # loop through zipped and match the days up to grab the values at that location in zipped
            temps_list = []
            counter = 0
            month_range = 0

            for index, temps in enumerate(zipped):
                # print(index, temps)
                # print("month range: ", month_range, "counter", counter)
                for key, value in days.items():
                    # print('key, value', key, value)
                    if value[0] == index:
                        # grab that index's temp for the number of days in that month
                        # print('MATCHINGGGGGGGGG --------------------------------------------------- ')
                        month_range = value[1]
                        # print(value[0], index)
                        temps_list.append([counter, temps])
                        counter += 1
                        # print("month range: ", month_range, "counter", counter)

                if counter < month_range:
                    temps_list.append([counter, temps])
                    counter += 1
                
                else:
                    counter = 0
                    month_range = 0
            
            print('')
            print('TEMPS LIST ', item, ' --------------------------------------------------------')
            for temps in temps_list:
                print(temps)

        return temps_list

def average(averages_list):

    counter = 0
    total = 0

    if averages_list == False:
        return False
    else:
        for item in averages_list:
            for subitem in item[1]:
                counter += 1
                total += subitem

        avg_temp = total // counter
        
        # print('Average Temp (K): ', avg_temp)
        return avg_temp

def translate(average_k):
    ''' Weather '''

    ''' Translates API fetched data into Decision Tree readable information
    Weather: 1= hot Avg high > 80; 2 = warm Avg high 65 to 80; 3 = cool Avg high 33 to 65, low: 45-33; 4 = cold Avg high < 32, low ≤ 32 
    Weather range: 1-2 or 3
    ''' 

    if average_k == False:
        return False
    else:
    
        avg_temp = round((average_k - 273.15) * 1.8 + 32)

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
            print('error: weather category')
            return  
        
        print('Temp Average (K):', avg_temp, ' Category:', category)
        return category

def weather_num(zipcode):

    try:

        fetch = climate_fetch(zipcode)
        process = climate_process(fetch)
        three_mnth = average(process)
        category = translate(three_mnth)

    except requests.exceptions.RequestException as e:
        raise e

    return category

def climate_fetch_perc(lat, lon):
    ''' function fetches the json data for a zipcode's climate percipitation data
    returns the raw json data. ''' 
    
    token = '6a096669f08500167edb361455210681ad1d8cbd'
    baseurl = 'https://app.climate.azavea.com/api/'
    header = {'Authorization': 'Token {}'.format(token),
                       'Origin': 'https://www.serch.us'}
    
    scenario = 'historical'
    params = '2010'

    querystring = '/api/climate-data/{}/{}/{}/indicator/total_precipitation?units=mm&time_aggregation=monthly&years=2005'.format(lat, lon, scenario)

    # List all scenarios
    scenario_querystring = '/api/scenario'

    url = urljoin(baseurl,querystring)

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        result = json.loads(response.content.decode())    
        return result

    except requests.exceptions.RequestException as e:
        raise e

def climate_fetch_temp(lat, lon):
    ''' function fetches the json data for a zipcode's climate temperatire data
    returns the raw json data ''' 
    
    token = '6a096669f08500167edb361455210681ad1d8cbd'
    baseurl = 'https://app.climate.azavea.com/api/'
    header = {'Authorization': 'Token {}'.format(token),
                       'Origin': 'https://www.serch.us'}
    
    scenario = 'historical'
    params = '2010'

    querystring = '/api/climate-data/{}/{}/{}/indicator/average_high_temperature?time_aggregation=monthly&years=2005&units=C'.format(lat, lon, scenario)

    # List all scenarios
    scenario_querystring = '/api/scenario'

    url = urljoin(baseurl,querystring)

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        result = json.loads(response.content.decode())    
        return result

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    
    zipcode = '94108'
    weather_num(zipcode)