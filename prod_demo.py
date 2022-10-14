# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:38:30 2022

@author: elodi
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Pyc énergétique', layout='wide')

st.title("Pyc énergétique")

df=pd.read_csv("conso.csv", sep=",")
df.Date=pd.to_datetime(df.Date)
df.Heure=pd.to_datetime(df.Heure.apply(lambda x: x[-8:]))
df=df.set_index("Date")

st.write("On propose de représenter la production électrique en France par type d'énergie. Les données s'étendent des années 2013 à 2021.")
st.write("En déplaçant le cursus Temporalité, on pourra représenter les données sur une année, un mois ou une journée.")

def graph():
    
    energie = st.multiselect(label="Type d'énergie", options=["Eolien", "Hydraulique", "Nucléaire", "Pompage", "Solaire", "Thermique", "Bioénergies"])    
    temp = st.select_slider("Choix de la temporalité",options=['Année', 'Mois', 'Jour'])
    annee=st.selectbox(label = "Choix de lannée", options=["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"])
    if temp=="Année":
        chart_data=df[energie][annee].resample("M").mean()
        st.line_chart(chart_data)
    elif temp=="Mois":    
        mois=st.selectbox(label = "Choix du mois", options=["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"])
        dico={"Janvier":1, "Février":2, "Mars":3, "Avril":4, "Mai":5, "Juin":6, "Juillet":7, "Août":8, "Septembre":9, "Octobre":10, "Novembre":11, "Décembre":12}                  
        chart_data=df[energie][annee+"-"+str(dico[mois])].resample("D").mean()
        st.line_chart(chart_data)
    elif temp=="Jour":
        mois=st.selectbox(label = "Choix du mois", options=["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"])
        dico={"Janvier":1, "Février":2, "Mars":3, "Avril":4, "Mai":5, "Juin":6, "Juillet":7, "Août":8, "Septembre":9, "Octobre":10, "Novembre":11, "Décembre":12}                  
        jour=st.selectbox(label = "Choix du jour", options=[str(i) for i in range(1,32)])
        chart_data=df.loc[annee+"-"+str(dico[mois])+"-"+jour]
        st.line_chart(chart_data, x="Heure", y=energie)
    
    
graph()
