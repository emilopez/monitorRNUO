from pathlib import Path

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

mapbox_access_token = st.secrets["mapbox_token"]

st.set_page_config(page_title="Puntos de observación", 
                    page_icon="🌎", 
                    layout="wide")

st.markdown("# Puntos de observación")


data = [("Alcantarilla 1", -31.607389567484503, -60.72415767069878),
        ("Alcantarilla 2", -31.606938478563542, -60.72508183841553),
        ("Canal 1", -31.607579126197045, -60.72454258578498),
        ("Reservorio", -31.608526281424744, -60.724909548109295)]


puntos_df = pd.DataFrame(data, columns=["Sitio", "lat", "lon"])

mapa = go.Scattermapbox(mode = "markers", lon = puntos_df["lon"], lat = puntos_df["lat"], marker = {'size': 10}, name = "",
                                        hovertemplate =   "<b>" + puntos_df["Sitio"] + "</b><br><br>" + "Coord: %{lon},%{lat}<br>" 
                                        )
layout = go.Layout(
    #title = "Estaciones de medición",
    title_x=0.5,
    title_y=0.95,
    width=600, height=900, 
    margin ={'l':0,'t':50,'b':0,'r':0},
    mapbox = {
        'accesstoken':mapbox_access_token,
        'center': {'lat': -31.608526281424744, 'lon': -60.724909548109295},
        'style': "satellite-streets",
        'zoom': 17})
figure = go.Figure(data=[mapa], layout=layout)

placeholder = st.empty()

with placeholder.container():
    # show mapa 
    st.plotly_chart(figure, use_container_width=False)