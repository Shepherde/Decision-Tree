
''' This file fetches climate data for a zipcode from the Azavea Climate organization
and compiles the numbers for each year into a decision tree readable value ''' 


import requests
import json
import datetime

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

    querystring = '/api/climate-data/{}/{}/{}/'.format(lat, lon, scenario)

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
    based on pattern of weather for the next three months at the location ''' 

    temp_total = 0
    counter = 0

    # for each year in the data, get all max 
    for item in api_data['data'].keys():
        print(' ----------------------------------------------------------- ')
        print(item)
        # print(api_data['data'][item]['tasmin'])

        if item == '2005':
            
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

            print('ZIPPED: --------------------- ')
            # counter3 = 1
            for index, item in enumerate(zipped):
                print(index, item)

            # Find current month
            currentDT = datetime.datetime.now()

            print ("Current Year is: %d" % currentDT.year)
            print ("Current Month is: %d" % currentDT.month)
            
            # Find the range of days in the year of the next 3 months


        # for temp in api_data['data'][item]['tasmax']:
        #     if type(temp) == int or type(temp) == float:
        #         counter += 1
        #         temp_total += temp

        # for temp in api_data['data'][item]['tasmin']:
        #     if type(temp) == int or type(temp) == float:
        #         counter += 1
        #         temp_total += temp
        

    # climate_average =round(temp_total / counter)
    # climate_f = round((climate_average - 273.15) * 1.8 + 32)


    # print(climate_f, temp_total, counter)

    # print(api_data['data']['2003']['tasmax'])

    # return int(climate_f)
    return

def climate_translate(avg_climate):
    ''' Climate: 1=Arid, 2=Temperate, 3=Subtropical, 4=Tropical '''

    category = None

    if avg_climate >= 64:
        category = '4'
    elif 50 <= avg_climate < 64:
        category = '3'
    elif 26 <= avg_climate < 50:
        category = '2'
    else:
        category = '1'
    
    


def clim_num(zipcode):
    fetch = climate_fetch(zipcode)
    process = climate_process(fetch)
            


if __name__ == "__main__":
    
    zipcode = '94103'
    clim_num(zipcode)