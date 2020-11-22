import requests
from AzaveaClimate import climate_fetch_perc, climate_fetch_temp
from OpenWeather import weather_fetch



URI = "http://www.meteotemplate.com/template/plugins/climateClassification/calcTrewartha.php?hemisphere=N&t1=0&t2=5.4&t3=6.8&t4=12.1&t5=14.2&t6=19.4&t7=21.1&t8=22.2&t9=16.9&t10=11&t11=7.4&t12=5.4&r1=0&r2=27.1&r3=42&r4=20.4&r5=125.7&r6=200.8&r7=89.6&r8=149.6&r9=122.5&r10=115.7&r11=63&r12=undefined&unitsT=C&unitsR=mm"

def trewartha(zipcode):
    """Gets the trewartha classification from an online calculator"""
    
    # Get lat lon data from weather_fetch Open Weather API
    weather_data = weather_fetch(zipcode)
    lat = weather_data[3]
    lon = weather_data[4]

    # Check whether or not the location is in the norther or the southern hemisphere
    hemisphere = "N"
    if lat[0] == "-":
        hemisphere = "S"

    # get the monthly temperature data from the appropriate API calls respectively.
    temp_data = climate_fetch_temp(lat, lon)
    percip_data = climate_fetch_perc(lat, lon)

    # URI for the trewartha calculator
    URI = "http://www.meteotemplate.com/template/plugins/climateClassification/calcTrewartha.php"
    # params for the trewartha calculator
    params = {
        "hemisphere": hemisphere,
        "t1": str(temp_data["data"]["2005-01"]["avg"]),
        "t2": str(temp_data["data"]["2005-02"]["avg"]),
        "t3": str(temp_data["data"]["2005-03"]["avg"]),
        "t4": str(temp_data["data"]["2005-04"]["avg"]),
        "t5": str(temp_data["data"]["2005-05"]["avg"]),
        "t6": str(temp_data["data"]["2005-06"]["avg"]),
        "t7": str(temp_data["data"]["2005-07"]["avg"]),
        "t8": str(temp_data["data"]["2005-08"]["avg"]),
        "t9": str(temp_data["data"]["2005-09"]["avg"]),
        "t10": str(temp_data["data"]["2005-10"]["avg"]),
        "t11": str(temp_data["data"]["2005-11"]["avg"]),
        "t12": str(temp_data["data"]["2005-12"]["avg"]),
        "r1": str(percip_data["data"]["2005-01"]["avg"]),
        "r2": str(percip_data["data"]["2005-02"]["avg"]),
        "r3": str(percip_data["data"]["2005-03"]["avg"]),
        "r4": str(percip_data["data"]["2005-04"]["avg"]),
        "r5": str(percip_data["data"]["2005-05"]["avg"]),
        "r6": str(percip_data["data"]["2005-06"]["avg"]),
        "r7": str(percip_data["data"]["2005-07"]["avg"]),
        "r8": str(percip_data["data"]["2005-08"]["avg"]),
        "r9": str(percip_data["data"]["2005-09"]["avg"]),
        "r10": str(percip_data["data"]["2005-10"]["avg"]),
        "r11": str(percip_data["data"]["2005-11"]["avg"]),
        "r12": str(percip_data["data"]["2005-12"]["avg"]),
        "unitsT": "C",
        "unitsR": "mm",
    }

    # try the request, if it fails raise an error
    try:
        response = requests.get(URI, params=params)
        return response.text.split(" ", 1)[0]

    except requests.exceptions.RequestException as e:
        raise e

def translate_trewartha(zipcode):
    # Translates the trewartha value into category for decision tree

    classified = trewartha(zipcode)
    value = None

    if type(classified) != bool:

        classi = str(classified[0])
        # print("class: ", classi)

        if classi == 'B':
            # arid / semi-arid
            value = '1'

        elif classi == 'D':
            # temperate / continental
            value = '2'

        elif classi == 'C':
            # subtropical
            value = '3'

        elif classi == 'A':
            # tropical
            value = '4'

        print('value: ', value)
        return value
    else:
        return False 


if __name__ == '__main__':

    zipcode = '61801'
    translate_trewartha(zipcode)