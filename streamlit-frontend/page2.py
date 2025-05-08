import streamlit as st
import pandas as pd

st.title("Participants")

# Example static data
data1 = [
    {"Artist": "Shkodra Elektronike", "Country": "Albania🇦🇱"},
    {"Artist": "Parg", "Country": "Armenia🇦🇲"},
    {"Artist": "Go-jo", "Country": "Australia🇦🇺"},
    {"Artist": "JJ", "Country": "Austria🇦🇹"},
    {"Artist": "Mamagama", "Country": "Azerbaigian🇦🇿"},
    {"Artist": "Red Sebastian", "Country": "Belgio🇧🇪"},
    {"Artist": "Theo Evan", "Country": "Cipro🇨🇾"},
    {"Artist": "Marko Bošnjak", "Country": "Croazia🇭🇷"},
    {"Artist": "Sissal", "Country": "Danimarca🇩🇰"},
    {"Artist": "Tommy Cash", "Country": "Estonia🇪🇪"},
    {"Artist": "Erika Vikman", "Country": "Finlandia🇫🇮"},
    {"Artist": "Louane", "Country": "Francia🇫🇷"},
    {"Artist": "Mariam Shengelia", "Country": "Georgia🇬🇪"},
    {"Artist": "Abor and Tynna", "Country": "Germania🇩🇪"},
    {"Artist": "Clavdia", "Country": "Grecia🇬🇷"},
    {"Artist": "Emmy", "Country": "Irlanda🇮🇪"},
    {"Artist": "Vaeb", "Country": "Islanda🇮🇸"},
    {"Artist": "Yuval Raphael", "Country": "Israele🇮🇱"},
    {"Artist": "Lucio Corsi", "Country": "Italy🇮🇹"},
    {"Artist": "Tautumeitas", "Country": "Lettonia🇱🇻"},
    {"Artist": "Katarsis", "Country": "Lituania🇱🇹"},
    {"Artist": "Laura Thorn", "Country": "Lussemburgo🇱🇺"},
    {"Artist": "Miriana Conte", "Country": "Malta🇲🇹"},
    {"Artist": "Nina Žižić", "Country": "Montenegro🇲🇪"},
    {"Artist": "Kyle Alessandro", "Country": "Norvegia🇳🇴"},
    {"Artist": "Claude", "Country": "Paesi Bassi"},
    {"Artist": "Justyna Steczkowska", "Country": "Polonia🇵🇱"},
    {"Artist": "Napa", "Country": "Portogallo🇵🇹"},
    {"Artist": "Adonxs", "Country": "Repubblica Ceca"},
    {"Artist": "Remember Monday", "Country": "Regno Unito🇬🇧"},
    {"Artist": "Gabry Ponte", "Country": "San Marino🇸🇲"},
    {"Artist": "Princ", "Country": "Serbia🇷🇸"},
    {"Artist": "Klemen", "Country": "Slovenia🇸🇮"},
    {"Artist": "Melody", "Country": "Spagna🇪🇸"},
    {"Artist": "KAJ", "Country": "Svezia🇸🇪"},
    {"Artist": "Zoe Me", "Country": "Svizzera🇨🇭"},
    {"Artist": "Ziferblat", "Country": "Ucraina🇺🇦"}
]

df = pd.DataFrame(data1)
st.table(df)  # or st.dataframe(df) for interactivity
