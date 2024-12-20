# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://github.com/blackary/st_pages
from pathlib import Path

#from st_pages import Page, Section, show_pages, add_page_title
import streamlit as st
from streamlit_extras.app_logo import add_logo

import datetime
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots 

st.set_page_config(
    page_title="Monitor Reserva Natural Urbana del Oeste - Santa Fe",
    layout="wide"
)
add_logo("logo.jpg")
st.write("# Monitor RNUO | Santa Fe")
st.write("Proyecto Científico de Monitoreo Hidro-Ambiental de la Reserva Natural Urbana del Oeste.")


fechas_muestreo = [datetime.datetime(2022,12,3), datetime.datetime(2023,2,24), datetime.datetime(2023,3,23),
                   datetime.datetime(2023,3,30), datetime.datetime(2023,4,27), datetime.datetime(2023,5,30)]
pH = {"Canal 1": [7.82, 7.84, 8.7, 7.49, 7.5, 8.0], 
      "Canal 2": [7.88, 7.66, 8.9, 7.97, 7.6, 7.8], 
      "Reservorio":     [8.44, 7.45, 8.1, 7.38, 6.8, 7.4]}

data_pH = pd.DataFrame(pH, columns=['Canal 1', 'Canal 2', 'Reservorio', 'fecha'])

def SetColor(y):
        if(y <= 1):
            return "red"
        elif(2 <= y < 4):
            return "yellow"
        elif(4 <= y < 9):
            return "green"
        else:
            return "blue"

placeholder = st.empty()
with placeholder.container():
    #hoy = datetime.datetime.now()
    #st.write(f"#### Últimos datos recibidos: {hoy.day}/{hoy.month}/{hoy.year} {hoy.hour}:{hoy.minute}:{hoy.second}")
    c1, c2, c3, c4 = st.columns(4)
    # fill in those three columns with respective metrics or KPIs

    fig_col1, fig_col2, fig_col3, fig_col4 = st.columns(4)
    with fig_col1:
        # https://stackoverflow.com/questions/61892036/plotly-how-to-colorcode-plotly-graph-objects-bar-chart-using-python
        y = data_pH.iloc[-1:].to_numpy().flatten()
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Canal 1","Canal 2", "Reservorio"], y = y, marker = dict(color = list(map(SetColor,y)))))
        fig.update_layout(title="pH  |  " + fechas_muestreo[-1].strftime("%d/%m/%Y"), yaxis_title = "pH ",  yaxis_range=[0,14],
                          legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))
        
        st.plotly_chart(fig, use_container_width=True)
    with fig_col2:
        fig = go.Figure()
        x = ["Canal 1","Canal 2", "Reservorio"]
        fig.add_trace(go.Scattergl(x = x, y = [0.63, 0.63, 0.63], mode="markers+lines", name="HTP"))
        fig.add_trace(go.Scattergl(x = x, y = [0.25, 0.25, 0.25], mode="markers+lines", name="GRO"))
        fig.add_trace(go.Scattergl(x = x, y = [0.63, 0.63, 0.63], mode="markers+lines", name="DRO"))
        fig.add_trace(go.Scattergl(x = x, y = [0.63, 0.63, 0.63], mode="markers+lines", name="HO"))

        fig.update_layout(title="Hidrocarburos  | " + fechas_muestreo[-1].strftime("%d/%m/%Y"), yaxis_title="mg/L", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))
        #fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),)

        st.plotly_chart(fig, use_container_width=True)

    with fig_col3:
        xdata = ["Canal 1","Canal 2", "Reservorio"]
        ydata = [25.3, 24.6, 22.5]
        fig = go.Figure()
        fig.add_trace(go.Bar(x = xdata, y = ydata, name="temperatura", marker=dict(color = ydata, colorscale='Bluered')))
        fig.update_layout(title="Temperatura  |  " + fechas_muestreo[-1].strftime("%d/%m/%Y"), yaxis_title="ºC", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)

    with fig_col4:
        # https://plotly.com/python/builtin-colorscales/ 
        xdata = ["Canal 1","Canal 2", "Reservorio"]
        ydata = [367, 396, 1788]
        fig = go.Figure()
        fig.add_trace(go.Bar(x = xdata, y = ydata,marker=dict(color = ydata, colorscale='Tealgrn')))
        fig.update_layout(title="Conductividad", yaxis_title="μS/cm", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)        
    
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        cwd = Path.cwd()
        fn  = cwd / "datos" / "distancia_R1_last_week.csv"
        data_R1_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
        xdata = data_R1_last_week["datetime"]
        ydata = 300 - data_R1_last_week["distancia"]

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata, y = ydata, name="Canal 1", fill='tozeroy', mode="none"))
        fig.update_layout(title="Niveles hidrométricos (Canal 1)", yaxis_title = "Nivel [cm]", xaxis_title = "Fecha", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)
    
    with fig_col2:
        
        cwd = Path.cwd()
        fn  = cwd / "datos" / "lluvia_cim" / "estacion_cim_nueva_solo_lluvia.csv"
        data_cim = pd.read_csv(fn, parse_dates=["Fecha"], dayfirst=True, sep=";")
        data_cim = data_cim[["Fecha", "Lluvia Caida (mm)"]] 
            
        data_cim["date"] = data_cim["Fecha"].dt.date
        lluvia_x_dia = data_cim.groupby("date").sum(numeric_only=True)
        
        xdata = lluvia_x_dia.index
        ydata = lluvia_x_dia["Lluvia Caida (mm)"]

        fig = go.Figure()
        fig.add_trace(go.Bar(x = xdata, y = ydata, name="Precipitación", marker_color='rgb(26, 118, 255,0)'))
        fig.update_yaxes(title_text="Precipitación [mm]")
        fig.update_layout(title="Precipitación Diaria")
        st.plotly_chart(fig, use_container_width=True)

    with fig_col3:
        cwd = Path.cwd()
        fn  = cwd / "datos" / "nf_R2_last_week.csv"
        data_R2_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
        xdata_R2 = data_R2_last_week["datetime"]
        ydata_R2 = data_R2_last_week["nf"]

        fn  = cwd / "datos" / "nf_R3_last_week.csv"
        data_R3_last_week = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
        xdata_R3 = data_R3_last_week["datetime"]
        ydata_R3 = data_R3_last_week["nf"]

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata_R2, y = ydata_R2, name="MISPyH (R2)", mode="lines"))
        fig.add_trace(go.Scattergl(x = xdata_R3, y = ydata_R3, name="Reserva (R3)", mode="lines"))
        fig.update_layout(title="Napa freática", yaxis_title = "Profundidad [cm]", xaxis_title = "Fecha", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)