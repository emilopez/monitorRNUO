import datetime

from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config(page_title="Niveles del Reservorio", 
                    page_icon="📈", 
                    layout="wide")

st.markdown("# Niveles del Reservorio")
st.write("""Altura hidrométrica en diferentes puntos del reservorio""")

tab1, tab2 = st.tabs(["DATOS", "DISPOSITIVOS"])

# niveles
cwd = Path.cwd()
fn  = cwd / "datos" / "distancia_R1.csv"
r1_df = pd.read_csv(fn, sep=";")

fechaR1 = r1_df["datetime"]
distaR1 = 300 - r1_df["distancia"]
voltaR1 = r1_df["voltaje"]

# estacion pegasus nueva CIM
fn  = cwd / "datos" / "lluvia_cim" / "estacion_cim_nueva.csv"
data_cim = pd.read_csv(fn, parse_dates=["Fecha"], dayfirst=True, sep=";")
data_cim = data_cim[["Fecha", "Lluvia Caida (mm)"]]

with tab1:
    placeholder = st.empty()

    with placeholder.container(): 
        
        option = st.selectbox('Precipitación',('Diaria', 'Intensidad'))
        if option == "Intensidad":
            xdata = data_cim["Fecha"]
            ydata = data_cim["Lluvia Caida (mm)"]
        elif option == "Diaria":
            data_cim["date"] = data_cim["Fecha"].dt.date
            lluvia_x_dia = data_cim.groupby("date").sum()
            
            xdata = lluvia_x_dia.index
            ydata = lluvia_x_dia["Lluvia Caida (mm)"]


        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=("Niveles", "Precipitación"))

        fig.add_trace(go.Bar(x = xdata, y = ydata, name="Precipitación", marker_color='rgb(26, 118, 255,0)'), row=2, col=1)
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1, mode="lines", name="Canal 1"), row=1, col=1)

        fig.update_yaxes(title_text="Precipitación [mm]",  row=2, col=1)
        fig.update_yaxes(title_text="Nivel [cm]", range=[0, 150], row=1, col=1)

        fig.update_layout(height=700)

        st.plotly_chart(fig, use_container_width=True)

        with open(fn) as f:
            st.download_button('Download CSV', f)
with tab2:
    placeholder2 = st.empty()
    with placeholder2.container():

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = fechaR1, y = voltaR1, mode="markers+lines", name="Equipo R1"))
        

        fig.update_layout(title="Voltaje equipos", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)
