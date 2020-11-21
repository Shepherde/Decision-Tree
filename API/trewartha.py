import requests
from AzaveaClimate import climate_fetch

URI = "http://www.meteotemplate.com/template/plugins/climateClassification/calcTrewartha.php?hemisphere=N&t1=0&t2=5.4&t3=6.8&t4=12.1&t5=14.2&t6=19.4&t7=21.1&t8=22.2&t9=16.9&t10=11&t11=7.4&t12=5.4&r1=0&r2=27.1&r3=42&r4=20.4&r5=125.7&r6=200.8&r7=89.6&r8=149.6&r9=122.5&r10=115.7&r11=63&r12=undefined&unitsT=C&unitsR=mm"

def trewartha(zipcode):
    data = climate_fetch(zipcode)
    print(data["data"])

trewartha("91311")