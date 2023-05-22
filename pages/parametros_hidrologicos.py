import datetime

from pathlib import Path

import streamlit as st
from streamlit_extras.app_logo import add_logo

import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config(page_title="Parámetros Hidrológicos", 
                    page_icon="📈", 
                    layout="wide")
add_logo("logo.jpg")
st.markdown("# Parámetros Hidrológicos")
st.write("""Niveles hidrométricos, precipitación y profundidad de napa freática""")

tab1, tab2 = st.tabs(["DATOS", "DISPOSITIVOS"])

# R1 niveles CANAL 1 
cwd = Path.cwd()
fn  = cwd / "datos" / "distancia_R1.csv"
r1_df = pd.read_csv(fn, sep=";")

## ultimos 14 dias (para un T=1min) = 14*24*60 = 7200
cant_dias = 60
nobs = cant_dias * 24 * 60
r1_df = r1_df[-nobs:]

fechaR1 = r1_df["datetime"]
distaR1 = 300 - r1_df["distancia"]
voltaR1 = r1_df["voltaje"]

# estacion pegasus nueva CIM
fn  = cwd / "datos" / "lluvia_cim" / "estacion_cim_nueva_solo_lluvia.csv"
data_cim = pd.read_csv(fn, parse_dates=["Fecha"], dayfirst=True, sep=";")
data_cim = data_cim[["Fecha", "Lluvia Caida (mm)"]]

# ultimos 5 dias (para un T=15min) = 14*24*4 = 480
nobs = cant_dias * 24 * 4
data_cim = data_cim[-nobs:]

# R5 nivel alcantarilla 1 RNUO
cwd = Path.cwd()
fn  = cwd / "datos" / "nivel_R5.csv"
r5_df = pd.read_csv(fn, sep=";",parse_dates=["datetime"])

# EQ-R2 NF taller ministerio
fn  = cwd / "datos" / "nf_R2_last_week.csv"
data_R2_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
xdata_R2 = data_R2_last_week["datetime"]
ydata_R2 = data_R2_last_week["nf"]
batep_R2 = data_R2_last_week["bateria"]
lluvia_R2= data_R2_last_week["cangilones"]*0.25

# EQ-R3 NF RNUO
fn  = cwd / "datos" / "nf_R3_last_week.csv"
data_R3_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
xdata_R3 = data_R3_last_week["datetime"]
ydata_R3 = data_R3_last_week["nf"]
batep_R3 = data_R3_last_week["bateria"]

# EQ-R4 NF La REDONDA
fn  = cwd / "datos" / "nf_R4_last_week.csv"
data_R4_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
xdata_R4 = data_R4_last_week["datetime"]
ydata_R4 = data_R4_last_week["nf"]
batep_R4 = data_R4_last_week["bateria"]

with tab1:
    placeholder = st.empty()

    with placeholder.container(): 
        
        option = st.selectbox('Precipitación',('Diaria', 'Intensidad'))
        if option == "Intensidad":
            xdata = data_cim["Fecha"]
            ydata = data_cim["Lluvia Caida (mm)"] 
        elif option == "Diaria":
            data_cim["date"] = data_cim["Fecha"].dt.date
            lluvia_x_dia = data_cim.groupby("date").sum(numeric_only = True)
            xdata = lluvia_x_dia.index
            ydata = lluvia_x_dia["Lluvia Caida (mm)"]

        fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=("<b>Altura hidrométrica</b>", "<b>Precipitación FICH</b>", "<b>Precipitación Cuenca Urbana</b>", "<b>Napa freática</b>"))
        # Niveles R1 (canal 1) y R5 (alcantarilla Lavaisse)
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1, mode="lines", name="Canal 1"), row=1, col=1)
        fig.add_trace(go.Scattergl(x = r5_df["datetime"], y = r5_df["nivel"], name="Alcantarilla 1 (R5)", mode="lines"), row=1, col=1)
        
        # Precipitacion FICH y R2 (taller ministerio)
        fig.add_trace(go.Bar(x = xdata, y = ydata, name="Precipitación", marker_color='rgb(26, 118, 255,0)'), row=2, col=1)
        fig.add_trace(go.Bar(x = xdata_R2, y = lluvia_R2, name="Precipitación", marker_color='rgb(26, 118, 255,0)'), row=3, col=1)
        
        # Niveles Freaticos R2, R3, R4
        fig.add_trace(go.Scattergl(x = xdata_R2, y = ydata_R2, name="MISPyH (R2)", mode="markers+lines"), row=3, col=1)
        fig.add_trace(go.Scattergl(x = xdata_R3, y = ydata_R3, name="Reserva (R3)", mode="markers+lines"), row=3, col=1)
        fig.add_trace(go.Scattergl(x = xdata_R4, y = ydata_R4, name="La Redonda (R4)", mode="markers+lines"), row=3, col=1)

        fig.update_yaxes(title_text="Nivel [cm]", range=[0, 150], row=1, col=1)
        fig.update_yaxes(title_text="Precipitación [mm]",  row=2, col=1)
        fig.update_yaxes(title_text="Precipitación [mm]",  row=3, col=1)
        fig.update_yaxes(title_text="Profundidad [cm]", autorange="reversed", row=3, col=1)
        fig.update_xaxes(title_text="Fecha", row=3, col=1)

        fig.update_layout(height=700)

        st.plotly_chart(fig, use_container_width=True)

        with open(fn) as f:
            st.download_button('Download CSV', f)
with tab2:
    placeholder2 = st.empty()
    with placeholder2.container():
        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = fechaR1[fechaR1>="2023-04-01"], y = voltaR1[fechaR1>="2023-04-01"]*92.59-296.28, mode="markers+lines", name="R1 Nivel (Canal 1 Reserva)"))
        fig.add_trace(go.Scattergl(x = xdata_R2[-1400:], y = batep_R2[-1400:], mode="markers+lines", name="R2 NF (MISPyH)"))
        fig.add_trace(go.Scattergl(x = xdata_R3[-1400:], y = batep_R3[-1400:], mode="markers+lines", name="R3 NF (Reserva)"))
        fig.add_trace(go.Scattergl(x = xdata_R4[-1400:], y = batep_R4[-1400:], mode="markers+lines", name="R4 NF (La Redonda)"))
        fig.add_trace(go.Scattergl(x = r5_df["datetime"], y = r5_df["bateria"], name="R5 Alcantarilla 1 (Reserva)", mode="markers"))

        fig.update_layout(title="Voltaje equipos",legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
        st.plotly_chart(fig, use_container_width=True)