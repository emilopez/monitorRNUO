from pathlib import Path

import streamlit as st
from streamlit_extras.app_logo import add_logo

import plotly.graph_objects as go
import numpy as np
import pandas as pd

mapbox_access_token = st.secrets["mapbox_token"]

st.set_page_config(page_title="Puntos de observación", 
                    page_icon="🌎", 
                    layout="wide")
add_logo("logo.jpg")

st.markdown("# Puntos de observación")

data = [("Alcantarilla 1"    ,""  ,"", "Nivel hidrométrico", -31.607389567484503, -60.72415767069878),
        ("Alcantarilla 2"    ,""  ,"", "Nivel hidrométrico", -31.606938478563542, -60.72508183841553),
        ("Canal 1"           ,"R1","26/12/2022","Nivel hidrométrico y calidad de agua", -31.607579126197045, -60.72454258578498),
        ("Canal 2"           ,""  ,"","Calidad de agua", -31.60769708,-60.72475576),
        ("Canal 3/Reservorio",""  ,"","Calidad de agua", -31.608526281424744, -60.724909548109295),
        ("Recreo RP 70"      ,""  ,"","Nivel hidrométrico",-31.49099, -60.78164), 
        ("Santo Tomé"        ,""  ,"","Nivel hidrométrico", -31.667723, -60.752450),
        ("MISPyH"            ,"R2","15/03/2023","Napa freática",-31.6026762,-60.7131065),
        ("Reserva"           ,"R3","12/04/2023","Napa freática",-31.606833,-60.7245466),
		("La Redonda"        ,"R4","","Napa freática",-31.6199931,-60.6930897)]


puntos_df = pd.DataFrame(data, columns=["Sitio","Id", "Instalado", "Parámetros", "lat", "lon"])

mapa = go.Scattermapbox(mode = "markers", lon = puntos_df["lon"], lat = puntos_df["lat"], marker = {'size': 10}, name = "",
                                        hovertemplate =   "<b>" + puntos_df["Sitio"] + " " + puntos_df["Id"] + "</b><br><br>" + "Instalado: " + puntos_df["Instalado"] + "<br>" + "Coord: %{lon},%{lat}<br>", 
                                        )
layout = go.Layout(
    title = "Estaciones de medición",
    title_x=0,
    title_y=0.99,
    width=600, height=900, 
    margin ={'l':0,'t':50,'b':0,'r':0},
    mapbox = {
        'accesstoken':mapbox_access_token,
        'center': {'lat': -31.608526281424744, 'lon': -60.724909548109295},
        'style': "satellite-streets",
        'zoom': 11})
figure = go.Figure(data=[mapa], layout=layout)

placeholder = st.empty()

with placeholder.container():
    # show mapa 
    c1, c2 = st.columns(2)
    c1.plotly_chart(figure, use_container_width=False)
    c2.write(puntos_df)
