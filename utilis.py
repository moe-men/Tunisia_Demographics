import requests
from bs4 import BeautifulSoup
import pandas as pd
from geopy.geocoders import Nominatim

def get_city_coordinates():  
    URL = "https://www.worldometers.info/world-population/tunisia-population/"

    population_per_city = pd.DataFrame(columns=["city", "lat", "lon", "pop"])

    geolocator = Nominatim(user_agent="MyApp")

    error_cities = []

    coordinates_error_cities = {
        "La Mohammedia" : [36.67446, 10.15633],
        "Oued Lill" : [36.83408, 10.04057],
        "Djemmal" : [35.62231, 10.75696],
        "Dar Chabanne" : [36.46798, 10.75167],
        "La Sebala du Mornag" : [36.67931, 10.29195],
        "Ar Rudayyif" : [34.3827, 8.15549],
        "Douar Tindja" : [37.16667, 9.75],
        "Ouardenine" : [35.70915, 10.67397],
        "Mennzel Bou Zelfa" : [36.68312, 10.58431]
    }

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")   

    Tab = soup.find("table", class_="table table-hover table-condensed table-list").find("tbody")

    tab = Tab.find_all("tr")

    for t in tab:

        city_name = [v.text for v in t.find_all("td")][1]

        city_pop = [v.text for v in t.find_all("td")][2]

        city_code = city_name + " tunisia"

        try :

            location = geolocator.geocode(city_code)

            dict = {
                "city": city_name,
                "lat": location.latitude,
                "lon": location.longitude,
                "pop":city_pop
            }

            newDF = pd.DataFrame(dict,index=[0])

            population_per_city = pd.concat([population_per_city, newDF], ignore_index=True)

        except Exception as e:

            if city_name in coordinates_error_cities:

                dict = {
                "city": city_name,
                "lat": coordinates_error_cities[city_name][0],
                "lon": coordinates_error_cities[city_name][1],
                "pop":city_pop
                }

                newdf = pd.DataFrame(dict,index=[0])

                population_per_city = pd.concat([population_per_city, newdf], ignore_index=True)

            else :

                error_cities.append(city_name)
                
            pass
        
    population_per_city.to_csv("Population_Per_City.csv")

    return population_per_city



def weather_icon(): 

    Base_URL = "https://www.accuweather.com"

    URL = Base_URL + "/en/tn/tunis/321398/weather-forecast/321398"

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}   

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")   

    Temp = soup.find(class_="temp").text

    Temp_icon_URL = Base_URL + soup.find("svg", class_="weather-icon")['data-src']

    return Temp, Temp_icon_URL