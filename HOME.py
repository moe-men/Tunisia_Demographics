import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup
from utilis import get_city_coordinates, weather_icon
import plotly.graph_objs as go
import folium
import streamlit.components.v1 as components
############# ADD flag counter https://s01.flagcounter.com/more/sKzp/


# --- SET PAGE CONFIG ---
st.set_page_config(page_title="Discover Tunisia", page_icon="🇹🇳", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("ERROR")
        return None
    return r.json()
flagURL = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6adGImzoRn.json")



# ------ HEADER SECTION ----
col1, col2, col3 = st.columns([1,2,1])
with col1 :
    temperature, link_weather_icon = weather_icon()
    if temperature.split("°")[-1] == "F" :
        temperature = str(int((int(temperature.split("°")[0]) - 32 ) / 1.8 )) + "°C"
    st.markdown(f"![Alt Text]({link_weather_icon})")
    col1.metric(label="Temperature" , value=temperature)



# --- TUNUISIA: IMAGE ---
with col2 :
    st.image("img/img_tn.jpg", use_column_width="always")



# --- TUNUISIAN FLAG ----
with col3 :
    st_lottie(flagURL, height=300, key="TNflag")



# --- POPULATION COORDINATES ---
with st.container():
    st.write("---")
    df = pd.read_csv("data/Population_Per_City.csv")
    #df = get_city_coordinates()
    st.map(df[['lat', 'lon']])


# ------- Introdution Tunisia -----------
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("Tunisia is :")
        st.write("##")
        st.write(
            """
            - Officially the Republic of Tunisia
            - Situated on the Mediterranean
            - A great environmental diversity due to its north–south extent
            """
            )
    with right_col:
        st.image("img/tn_boarder.png")




df = pd.read_csv("data/Population_Per_City.csv")
df.drop("Unnamed: 0", axis = 1, inplace=True)
df.columns = ["city", "lat", "lon", "popu"]
cities = []
for index, rows in df.iterrows():
    my_list =[rows.city, int(rows.popu.replace(',', '')), [rows.lat,rows.lon]]
    cities.append(my_list)
# Create a map object
m = folium.Map(location=[33.8439408, 9.400138], zoom_start=8)

# Add points to the map
for city, population, coord in cities:
    folium.CircleMarker(coord, radius=population/50000, fill_color="#3db7e4", fill_opacity=0.9).add_to(m)

# SAVE the map
m.save('img/map.html')

# Display the map
with open('img/map.html', 'r') as f:
    html = f.read()
components.html(html, width=1200, height=1800)





