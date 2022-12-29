import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Tunisia infos", page_icon=":tn:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("ERROR")
        return None
    return r.json()

# ------ HEADER SECTION ----

st.subheader("Hi :wave:, here you will find infornation about Tunisia: Population, migration ...")
st.warning("the data is from [Here >](https://databank.worldbank.org)")


# --- Tunisian flag ----
flagURL = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_6adGImzoRn.json")

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
        st_lottie(flagURL, height=300, key="TNflag")