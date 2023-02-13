# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
from pathlib import Path

import datetime
import streamlit as st
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots



st.set_page_config(
    page_title="Monitor Reserva Natural Urbana del Oeste - Santa Fe",
    page_icon="🍻",
    layout="wide"
)

st.write("# Monitor RNUO 🍻")

placeholder = st.empty()
with placeholder.container():
    hoy = datetime.datetime.now()
    st.write(f"#### Últimos datos recibidos: {hoy.day}/{hoy.month}/{hoy.year} {hoy.hour}:{hoy.minute}:{hoy.second}")
    c1, c2, c3, c4 = st.columns(4)
    # fill in those three columns with respective metrics or KPIs

    c1.metric(
        label="Canal 1",
        value=11,
        delta=12,
    )
    
    c2.metric(
        label="Reservorio",
        value=21,
        delta=20,
    )
    
    c3.metric(
        label="Alcantarilla 1",
        value=31,
        delta=32,
    )

    c4.metric(
        label="Alcantarilla 2",
        value=31,
        delta=32,
    )
    fig_col1, fig_col2, fig_col3, fig_col4 = st.columns(4)
    with fig_col1:
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [50, 55, 43, 39], name="Últimos"))
        fig.add_trace(go.Scattergl(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [55, 65, 53, 49],mode="markers", name="Máximos"))
        fig.add_trace(go.Scattergl(x = ["Canal 1", "Reservorio", "Alcantarilla 1","Alcantarilla 2"], y = [20, 35, 23, 29],mode="markers", name="Mínimos"))
        fig.update_layout(title="Niveles hidrométricos", yaxis_title = "Nivel [mts]", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)
    
    with fig_col2:
        fig = go.Figure()
        fig.add_trace(go.Bar(x = ["Reservorio", "Cuenca de aporte"], y = [50, 55], name="Actuales"))
        fig.add_trace(go.Scattergl(x = ["Reservorio", "Cuenca de aporte"], y = [65, 75,],mode="markers", name="Máximos"))
        fig.add_trace(go.Scattergl(x = ["Reservorio", "Cuenca de aporte"], y = [10, 17],mode="markers", name="Mínimos"))
        fig.update_layout(title="Precipitación", yaxis_title="Lluvia [mm]", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))
        #fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),)

        st.plotly_chart(fig, use_container_width=True)

    with fig_col3:
        xdata = np.arange(0,2,0.01)
        ydata = np.exp(xdata)*np.sin(2*np.pi*2*xdata)
        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata, y = ydata, name="temperatura", mode="lines+markers"))
        fig.update_layout(title="Temperatura", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)

    with fig_col4:
        xdata = np.arange(0,10,0.01)
        ydata = 1/(0.005 + np.exp(-0.9*xdata))
        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata, y = ydata, name="temperatura", mode="lines+markers"))
        fig.update_layout(title="Nivel freático", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)        
    
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = xdata, y = 0.7*np.sin(2*np.pi*xdata+np.pi/4),mode="lines", name="Canal 1"))
        fig.add_trace(go.Scattergl(x = xdata, y = np.exp(-xdata)*np.sin(2*np.pi*xdata),mode="lines+markers", name="Alcantarilla 1"))
        fig.add_trace(go.Scattergl(x = xdata, y = 0.2 + np.sin(2*np.pi*xdata),mode="lines", name="Alcantarilla 2"))
        fig.add_trace(go.Scattergl(x = xdata, y = 0.3*np.sin(2*np.pi*xdata+np.pi),mode="lines", name="Reservorio"))
        fig.update_layout(title="Niveles hidrométricos", yaxis_title = "Nivel [mts]", xaxis_title = "Fecha", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))

        st.plotly_chart(fig, use_container_width=True)
    
    with fig_col2:
        cwd = Path.cwd()
        fn  = cwd / "datos" / "lluvia_cim" / "precipitacion.csv"
        
        data_cim = pd.read_csv(fn, sep="\t", parse_dates=["Fecha"], dayfirst=True)
        st.write(data_cim)
        xdata = data_cim["Fecha"]
        ydata = data_cim["Lectura"]

        fig = go.Figure()
        fig.add_trace(go.Bar(x = xdata, y = ydata, name="Precipitación", marker_color='rgb(26, 118, 255,0)'))

        #fig.add_trace(go.Scattergl(x = xdata, y = -2 + -0.5*np.sin(2*np.pi*xdata+np.pi/2), name="N. Freática"), secondary_y=False)


        #fig.update_layout(title="Hidro-Meteorología", yaxis_title="Lluvia [mm]", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))
        fig.update_yaxes(title_text="Precipitación [mm]")
        #fig.update_yaxes(title_text="Profundiad NF [cmca]", secondary_y=False, range=[-5,0])
        fig.update_layout(title="Precipitación acumulada cada 10 minutos", xaxis_range=[datetime.datetime(2023, 1, 1), datetime.datetime(2023, 2, 8)])
        st.plotly_chart(fig, use_container_width=True)