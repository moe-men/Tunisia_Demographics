import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup
from utilis import get_city_coordinates, weather_icon



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
    st.markdown(f"![Alt Text]({link_weather_icon})")
    col1.metric(label="Temperature" , value=temperature)

with col2 :
    st.image("img_tn.jpg", use_column_width="always")



# --- Tunisian flag ----
with col3 :
    st_lottie(flagURL, height=300, key="TNflag")


with st.container():
    st.write("---")
    df = pd.read_csv("Population_Per_City.csv")
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
    #with right_col:
        #st_lottie(flagURL, height=300, key="TNflag")

# ------ Ploting the Data Frame in use ----

st.header("DataFrame Used")

df = pd.read_csv("data/data.csv")
df.drop("Unnamed: 0", axis = 1, inplace=True)
st.write(df)
st.write("##")


st.subheader("List of indicators :")
indicators = df.columns[1:]
indicators
st.write("##")


st.subheader("Intentional homicides (per 100,000 people):")
st.area_chart(data = df, x= "year", y= "Intentional homicides (per 100,000 people)")
st.write("##")


st.subheader("Food exports (% of merchandise exports):")
st.area_chart(data = df, x= "year", y= "Food exports (% of merchandise exports)")
st.write("##")


st.subheader("Fuel imports (% of merchandise imports):")
st.area_chart(data = df, x= "year", y= "Fuel imports (% of merchandise imports)")
st.write("##")


st.subheader("Import volume index (2000 = 100):")
st.area_chart(data = df, x= "year", y= "Import volume index (2000 = 100)")
st.write("##")


st.subheader("International tourism, receipts (% of total exports):")
st.area_chart(data = df, x= "year", y= "International tourism, receipts (% of total exports)")
st.write("##")


st.subheader("Rural population (% of total population):")
st.area_chart(data = df, x= "year", y= "Rural population (% of total population)")
st.write("##")


st.subheader("Completeness of birth registration (%):")
st.area_chart(data = df, x= "year", y= "Completeness of birth registration (%)")
st.write("##")


st.subheader("Population, female:")
st.area_chart(data = df, x= "year", y= "Population, female")
st.write("##")


st.subheader("Population growth (annual %):")
st.area_chart(data = df, x= "year", y= "Population growth (annual %)")
st.write("##")


st.subheader("Women Business and the Law Index Score (scale 1-100):")
st.area_chart(data = df, x= "year", y= "Women Business and the Law Index Score (scale 1-100)")
st.write("##")


st.subheader("Children out of school, female (% of female primary school age):")
st.area_chart(data = df, x= "year", y= "Children out of school, female (% of female primary school age)")
st.write("##")


st.subheader("Literacy rate, adult total (% of people ages 15 and above):")
st.area_chart(data = df, x= "year", y= "Literacy rate, adult total (% of people ages 15 and above)")
st.write("##")


st.subheader("Literacy rate, youth male (% of males ages 15-24):")
st.area_chart(data = df, x= "year", y= "Literacy rate, youth male (% of males ages 15-24)")
st.write("##")


st.subheader("Energy use (kg of oil equivalent per capita):")
st.area_chart(data = df, x= "year", y= "Energy use (kg of oil equivalent per capita)")
st.write("##")

