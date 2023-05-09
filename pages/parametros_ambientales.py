from pathlib import Path

import streamlit as st
from streamlit_extras.app_logo import add_logo

import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px



st.set_page_config(page_title="Parámetros ambientales", 
                    page_icon="♒", 
                    layout="wide")
add_logo("logo.jpg")

st.markdown("# Parámetros ambientales")
#st.write("""Registros mediante sondas multiparamétricas""")

cwd = Path.cwd()

tab1, tab2, tab3 = st.tabs(["DATOS", "CALIBRACIÓN SONDAS", "INCENDIOS"])
with tab1:
    
    fn_calidad_agua  = cwd / "datos" / "RESULTADOS-calidad-de-agua.csv"
    datos_calidad_agua = pd.read_csv(fn_calidad_agua, sep=";", parse_dates=["FECHA"])
    
    fig_te, fig_pH, fig_CE, fig_OD = go.Figure(), go.Figure(), go.Figure(), go.Figure()
    puntos = "Canal 1", "Canal 2", "Canal 3"
    for punto in puntos:
        idx = datos_calidad_agua["PUNTO"]== punto
        val = datos_calidad_agua.loc[idx, ["FECHA", "Temperatura (ºC)", "pH", "Conductividad (uS/cm)", "Sat OD %"]]
        fig_te.add_trace(go.Scattergl(x=val["FECHA"], y=val["Temperatura (ºC)"], name=punto))
        fig_pH.add_trace(go.Scattergl(x=val["FECHA"], y=val["pH"], name=punto))
        fig_CE.add_trace(go.Scattergl(x=val["FECHA"], y=val["Conductividad (uS/cm)"], name=punto))
        val.dropna(inplace=True)
        fig_OD.add_trace(go.Scattergl(x=val["FECHA"], y=val["Sat OD %"], name=punto))
    fig_te.update_layout(title="Temperatura", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_pH.update_layout(title="pH", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_CE.update_layout(title="Conductividad Eléctrica", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_OD.update_layout(title="Oxígeno Disuelto (%)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    
    fig_col1, fig_col2, fig_col3, fig_col4  = st.columns(4)

    fig_col1.plotly_chart(fig_te, use_container_width=True)
    fig_col2.plotly_chart(fig_pH, use_container_width=True)
    fig_col3.plotly_chart(fig_CE, use_container_width=True)
    fig_col4.plotly_chart(fig_OD, use_container_width=True)
    # 2da fila de graficas
    fig_fito_dt, fig_fito_rt, fig_zoop_dt, fig_zoop_rt = go.Figure(), go.Figure(), go.Figure(), go.Figure() 
    for punto in puntos:
        idx = datos_calidad_agua["PUNTO"]== punto
        val = datos_calidad_agua.loc[idx,["FECHA", "Fitoplancton densidad total (ind/mL)", "Fitoplancton (riqueza total)", "Zooplancton densidad total (ind/L)", "Zooplancton (riqueza total)"]]
        fig_fito_dt.add_trace(go.Scattergl(x=val["FECHA"],y=val["Fitoplancton densidad total (ind/mL)"], name=punto))
        fig_fito_rt.add_trace(go.Scattergl(x=val["FECHA"],y=val["Fitoplancton (riqueza total)"], name=punto))
        fig_zoop_dt.add_trace(go.Scattergl(x=val["FECHA"],y=val["Zooplancton densidad total (ind/L)"], name=punto))
        fig_zoop_rt.add_trace(go.Scattergl(x=val["FECHA"],y=val["Zooplancton (riqueza total)"], name=punto))  
    fig_fito_dt.update_layout(title="Fitoplancton densidad total (ind/mL)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_fito_rt.update_layout(title="Fitoplancton (riqueza total)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_zoop_dt.update_layout(title="Zooplancton densidad total (ind/L)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_zoop_rt.update_layout(title="Zooplancton (riqueza total)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    
    fig_col1, fig_col2, fig_col3, fig_col4  = st.columns(4)

    fig_col1.plotly_chart(fig_fito_dt, use_container_width=True)
    fig_col2.plotly_chart(fig_fito_rt, use_container_width=True)
    fig_col3.plotly_chart(fig_zoop_dt, use_container_width=True)
    fig_col4.plotly_chart(fig_zoop_rt, use_container_width=True)

    # 3er fila de graficas
    fig_ecoli, fig_colit, fig_cloro = go.Figure(), go.Figure(), go.Figure()
    for punto in puntos:
        idx = datos_calidad_agua["PUNTO"]== punto
        val = datos_calidad_agua.loc[idx, ["FECHA", "Coliformes totales (NMP/100 mL)", "E. coli (NMP/100 mL)", "Clorofila-a (µg/L)"]]
        fig_colit.add_trace(go.Scattergl(x=val["FECHA"], name=punto, y=val["Coliformes totales (NMP/100 mL)"]))
        fig_ecoli.add_trace(go.Scattergl(x=val["FECHA"], name=punto, y=val["E. coli (NMP/100 mL)"]))
        fig_cloro.add_trace(go.Scattergl(x=val["FECHA"], name=punto, y=val["Clorofila-a (µg/L)"]))
    fig_colit.update_layout(title="Coliformes totales (NMP/100 mL)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_ecoli.update_layout(title="E. coli (NMP/100 mL)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    fig_cloro.update_layout(title="Clorofila-a (µg/L)", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
    
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    fig_col1.plotly_chart(fig_colit, use_container_width=True)
    fig_col2.plotly_chart(fig_ecoli, use_container_width=True)
    fig_col3.plotly_chart(fig_cloro, use_container_width=True)

    
   

with tab2:
    
    fn  = cwd / "datos" / "multiparametricas.csv"

    datos = pd.read_csv(fn, sep=",")
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
        with open(fn) as f:
            st.download_button('Download CSV', f)
        st.write(datos)
with tab3:
    fn  = cwd / "datos" / "incendios.csv"
    df = pd.read_csv(fn, sep=",")
    
    st.write("**Mapa de incendios en la RNUO** *(en construcción)*")
    
    

    #fig = px.density_mapbox(df, lat='LAT', lon='LON', radius=5,
    #                        center=dict(lat=0, lon=180), zoom=0,
    #                        mapbox_style="stamen-terrain")
    
    fig = go.Figure(go.Densitymapbox(lat=df.LAT, lon=df.LON, radius=10))
    fig.update_layout(
        mapbox_style="stamen-terrain",
        mapbox_center_lon = -60.6928896,
        mapbox_center_lat = -31.6243968,
        mapbox_zoom = 11,
        width = 600, 
        height = 500,
    )
    st.plotly_chart(fig, use_container_width=False)
    st.write(df)