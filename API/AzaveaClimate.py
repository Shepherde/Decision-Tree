import requests
import json

from urllib.parse import urljoin
from OpenWeather import weather_fetch


def climate_fetch(zipcode):
    ''' function fetches the json data for a zipcodes' climate data
    returns the raw json data ''' 
    
    # Get lat lon data from weather_fetch Open Weather API
    weather_data = weather_fetch(zipcode)
    lat = weather_data[3]
    lon = weather_data[4]
    
    token = ''
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
    crunches all the max and mins throughout each year for as many years as are on record ''' 

    temp_total = 0
    counter = 0

    # for each year in the data, get all max 
    for item in api_data['data']:
        # print(' ----------------------------------------------------------- ')
        # print(api_data['data'][item]['tasmax'])

        for temp in api_data['data'][item]['tasmax']:
            if type(temp) == int or type(temp) == float:
                counter += 1
                temp_total += temp

        for temp in api_data['data'][item]['tasmin']:
            if type(temp) == int or type(temp) == float:
                counter += 1
                temp_total += temp
        

    climate_average =round(temp_total / counter)
    climate_f = round((climate_average - 273.15) * 1.8 + 32)


    print(climate_f, temp_total, counter)

    # print(api_data['data']['2003']['tasmax'])

    return climate_f
        

def clim_num(zipcode):
    fetch = climate_fetch(zipcode)
    process = climate_process(fetch)
            


if __name__ == "__main__":
    
    zipcode = '94103'
    clim_num(zipcode)