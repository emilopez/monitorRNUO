from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config(page_title="Niveles del Reservorio", 
                    page_icon="📈", 
                    layout="wide")

st.markdown("# Altura hidrométrica")
st.write("""Altura canal pasarela 1""")

tab1, tab2 = st.tabs(["DATOS", "DISPOSITIVOS"])

with tab1:
    placeholder = st.empty()

    with placeholder.container():

        xdata = np.arange(0,1,0.01)
        ydata = np.sin(2*np.pi*xdata)

        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata, y = ydata + 1.5, mode="markers+lines", name="Canal 1"))
        fig.add_trace(go.Scattergl(x = xdata, y = 1.5*ydata + 1.5, mode="markers+lines", name="Canal 2"))
        fig.add_trace(go.Scattergl(x = xdata, y = ydata-0.2 + 1.5, mode="markers+lines", name="Reservorio"))

        fig.update_layout(title="Niveles del reservorio", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)