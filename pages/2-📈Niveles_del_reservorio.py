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

cwd = Path.cwd()
fn  = cwd / "datos" / "distancia_R1.csv"
r1_df = pd.read_csv(fn, sep=";")

fechaR1 = r1_df["datetime"]
distaR1 = 300 - r1_df["distancia"]
voltaR1 = r1_df["voltaje"]

with tab1:
    placeholder = st.empty()

    with placeholder.container():

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        #lluvia_df = pd.DataFrame({"Fecha": ["2023-01-01 13:50"], "Precipitación":[9.25]})
  
        # niveles
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1,    mode="markers+lines", opacity=0.8, name="Canal 1"),secondary_y=False)
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1+50, mode="markers+lines", opacity=0.2, name="Alcantarilla 1 (falso)"),secondary_y=False)
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1+60, mode="markers+lines", opacity=0.2, name="Alcantarilla 2 (falso)"),secondary_y=False)
        fig.add_trace(go.Scattergl(x = fechaR1, y = distaR1+70, mode="markers+lines", opacity=0.2, name="Reservorio (falso)"),secondary_y=False)

        # precipitacion
        #fig.add_trace(go.Bar(x = lluvia_df["Fecha"], y = lluvia_df["Precipitación"], name="Lluvia"), secondary_y=True)

        fig.update_yaxes(title_text="Nivel hidrométrico [cm]", secondary_y=False)#, range=[50,150])
        #fig.update_yaxes(title_text="Precipitación [mm]", secondary_y=True, range=[10,0])
        fig.update_layout(title="Niveles del reservorio (Distancia!)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)

with tab2:
    placeholder2 = st.empty()
    with placeholder2.container():

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = fechaR1, y = voltaR1, mode="markers+lines", name="Equipo R1"))
        

        fig.update_layout(title="Voltaje equipos", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)