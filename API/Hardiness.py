
''' this file encodes the average climate in farenheit into a hardiness zone.
zone values are from USDA Agricultural Research https://planthardiness.ars.usda.gov/PHZMWeb/ '''

from API.AzaveaClimate import total_climate_num

def hardiness_encoder(zipcode):

    climate_num = total_climate_num(zipcode)

    if climate_num != False:

        zone = "out of range "

        if -60 <= climate_num < -55: 
            zone = '1a'
        if -55 <= climate_num < -50: 
            zone = '1b'
        if -50 <= climate_num < -45: 
            zone = '2a'
        if -45 <= climate_num < -40: 
            zone = '2b'
        if -40 <= climate_num < -35: 
            zone = '3a'
        if -35 <= climate_num < -30: 
            zone = '3b'
        if -30 <= climate_num < -25: 
            zone = '4a'
        if -25 <= climate_num < -20: 
            zone = '4b'
        if -20 <= climate_num < -15: 
            zone = '5a'
        if -15 <= climate_num < -10: 
            zone = '5b'
        if -10 <= climate_num < -5: 
            zone = '6a'
        if -5 <= climate_num < 0: 
            zone = '6b'
        if 0 <= climate_num < 5: 
            zone = '7a'
        if 5 <= climate_num < 10: 
            zone = '7b'
        if 10 <= climate_num < 15: 
            zone = '8a'
        if 15 <= climate_num < 20: 
            zone = '8b'
        if 20 <= climate_num < 25: 
            zone = '9a'
        if 25 <= climate_num < 30: 
            zone = '9b'
        if 30 <= climate_num < 35: 
            zone = '10a'
        if 35 <= climate_num < 40: 
            zone = '10b'
        if 40 <= climate_num < 45: 
            zone = '11a'
        if 45 <= climate_num < 50: 
            zone = '11b'
        if 50 <= climate_num < 55: 
            zone = '12a'
        if 55 <= climate_num < 60: 
            zone = '12b'
        if 60 <= climate_num < 65: 
            zone = '13a'
        if 65 <= climate_num < 70: 
            zone = '13b'
        
        print('hardiness: ', zone[:-1])

        # we only care about the first integer, not the character
        return zone[:-1]

    else:
        return climate_num

if __name__ == "__main__":

    zipcode = '61801'
    hardiness_encoder(zipcode)