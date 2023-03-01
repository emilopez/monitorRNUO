from pathlib import Path

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

mapbox_access_token = st.secrets["mapbox_token"]

st.set_page_config(page_title="Niveles del Río Salado", 
                    page_icon="🌎", 
                    layout="wide")

st.markdown("# Niveles del Río Salado")
st.write("""Altura hidrométrica en Recreo Ruta Provincial 70 y en Santo Tomé.""")

# Datos Rio Salado
cwd = Path.cwd()
fn  = cwd / "datos" / "Alturas-RecreoR70-SantoTome.csv"
data_salado = pd.read_csv(fn, parse_dates=["Fecha"], dayfirst=True, sep=";")

fig = go.Figure()
fig.add_trace(go.Scattergl(x=data_salado["Fecha"], y=data_salado["Recreo R70"], name="Recreo RP 70"))
fig.add_trace(go.Scattergl(x=data_salado["Fecha"], y=data_salado["Santo Tome"], name="Santo Tomé"))

st.plotly_chart(fig, use_container_width=True)
st.write("""*Datos proporcionados por la Secretaría de Recursos Hídricos, Ministerios de
Infraestructura, Servicios Públicos y Hábitat de la Provincia de Santa Fe*.""")
