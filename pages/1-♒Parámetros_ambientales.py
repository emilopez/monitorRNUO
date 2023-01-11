from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config(page_title="Parámetros ambientales", 
                    page_icon="♒", 
                    layout="wide")

st.markdown("# Parámetros ambientales")
st.write("""Registros mediante sondas multiparamétricas""")


cwd = Path.cwd()
fn  = cwd / "datos" / "multiparametricas.csv"


datos = pd.read_csv(fn, sep=",")

tab1, tab2 = st.tabs(["CALIBRACIÓN","DATOS"])

with tab2:
    st.write("datos")

with tab1:
    # creating a single-element container
    placeholder = st.empty()

    with placeholder.container():
            
            # create three columns
            c1, c2, c3 = st.columns(3)
            # fill in those three columns with respective metrics or KPIs

            c1.metric(
                label="pH ⏳",
                value=11,
                delta=12,
            )
            
            c2.metric(
                label="Conductividad Eléctrica (CE) 💍",
                value=21,
                delta=20,
            )
            
            c3.metric(
                label="Oxígeno Disuelto (OD)",
                value=31,
                delta=32,
            )
            st.write("### Test sondas")

            # create three columns for charts
            fig_col1, fig_col2, fig_col3 = st.columns(3)

            datos_canal1 = datos[datos["Muestra"] == "canal 1"]
            datos_canal2 = datos[datos["Muestra"] == "canal 2"]
            datos_reservorio = datos[datos["Muestra"] == "reservorio (bancos descanso)"]
            
            with fig_col1:
                sitios = ["Canal 1", "Canal 2", "Reservorio"]            
                fig = go.Figure(data=[
                        go.Bar(name='Sonda 1', x=sitios, y=[7.53, 7.15, np.nan]),
                        go.Bar(name='Sonda 2', x=sitios, y=[7.82, 7.88, 8.44]),
                        go.Bar(name='Sonda 3', x=sitios, y=[7.64, 7.75, 8.36])
                    ])
                fig.update_layout(title="pH", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

                st.plotly_chart(fig, use_container_width=True)

            with fig_col2:
                sitios = ["Canal 1", "Canal 2", "Reservorio"]
                
                fig2 = go.Figure(data=[
                        go.Bar(name='Sonda 1', x=sitios, y=[208.3, 429.8, 3161]),
                        go.Bar(name='Sonda 3', x=sitios, y=[217.4, 752, 3175]),
                    ])
                fig2.update_layout(title="Conductividad Eléctrica", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
                st.plotly_chart(fig2, use_container_width=True)

            with fig_col3:
                
                sitios = ["Canal 1", "Canal 2", "Reservorio"]
                
                fig3 = go.Figure(data=[
                        go.Bar(name='Sonda 1', x=sitios, y=[np.nan,5.3, 4.23]),
                        go.Bar(name='Sonda 2', x=sitios, y=[6.64, 5.29, 5.17]),
                        go.Bar(name='Sonda 3', x=sitios, y=[6.4, 4.0, 3.5])
                    ])
                fig3.update_layout(title="Oxígeno Disuelto", barmode='group',legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

                st.plotly_chart(fig3, use_container_width=True)

    with st.expander("Ver tabla de registros de sondas multiparamétricas"):
        st.write(datos)