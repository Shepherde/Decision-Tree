import requests
import json

from urllib.parse import urljoin
from OpenWeather import weather_fetch


def climate_fetch(zipcode):

    # Get lat lon data from weather_fetch Open Weather API
    weather_data = weather_fetch(zipcode)
    lat = weather_data[3]
    lon = weather_data[4]
    print(lat, lon)
    
    token = ''
    baseurl = 'https://app.climate.azavea.com/api/'
    header = {'Authorization': 'Token {}'.format(token),
                       'Origin': 'https://www.serch.us'}
    
    scenario = 'historical'
    params = '2010'

    querystring = '/api/climate-data/{}/{}/{}/'.format(lat, lon, scenario)

    # List all scenarios
    querystring2 = '/api/scenario'
    print(querystring)

    url = urljoin(baseurl,querystring)

    try:
        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        result = json.loads(response.content.decode())    
        return result

    except requests.exceptions.RequestException as e:
        raise e

def climate_process(api_data):

    for item in api_data['data']:
        for 
        

            


if __name__ == "__main__":
    
    fetch = climate_fetch('94103')
    process = climate_process(fetch)