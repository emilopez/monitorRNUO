import datetime
import pickle

from pathlib import Path

import streamlit as st
from streamlit_extras.app_logo import add_logo

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots



st.set_page_config(page_title="Datos Hidrológicos", 
                    page_icon="📈", 
                    layout="wide")
add_logo("logo.jpg")
st.markdown("# Datos Hidrológicos")
st.write("""Niveles hidrométricos, precipitación y profundidad de napa freática""")

tab1, tab2 = st.tabs(["DATOS", "DISPOSITIVOS"])

# R1 niveles CANAL 1 
cwd = Path.cwd()
#fn  = cwd / "datos" / "distancia_R1.csv"
#r1_df = pd.read_csv(fn, sep=";", parse_dates=["datetime"])
fn  = cwd / "datos" / "distancia_R1.parquet.gzip"
r1_df = pd.read_parquet(fn)

# EQ-R2 NF taller ministerio
fn  = cwd / "datos" / "nf_R2.parquet.gzip"
#r2_df = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
r2_df = pd.read_parquet(fn)

# -------> nuestros datos de lluvia: hay que ejecutar antes: load_files_R2.py
fn  = cwd / "datos" / "lluvia_R2.parquet.gzip"
#lluviaR2_15min = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
lluviaR2_15min = pd.read_parquet(fn)

# EQ-R3 NF RNUO
fn  = cwd / "datos" / "nf_R3.parquet.gzip"
#r3_df = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
r3_df = pd.read_parquet(fn)

# EQ-R4 NF La REDONDA
fn  = cwd / "datos" / "nf_R4.parquet.gzip"
#r4_df = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
r4_df = pd.read_parquet(fn)

# EQ-R5 nivel alcantarilla 1 RNUO
cwd = Path.cwd()
fn  = cwd / "datos" / "nivel_R5.parquet.gzip"
#r5_df = pd.read_csv(fn, sep=";", parse_dates=["datetime"], comment="#")
r5_df = pd.read_parquet(fn)
#r5_df['datetime'] = pd.to_datetime(r5_df['datetime'], errors='coerce')
r5_df = r5_df[((r5_df["nivel"] >= 0) & (r5_df["nivel"] < 140))]

# Leer el NumPy array desde el archivo
with open('datos/lluvia_R2_diaria.pickle', 'rb') as file:
    lluvia_anio = pickle.load(file)

y = np.arange(1,13)
x = np.arange(1,32)

fig_mapa_lluvia = px.imshow(lluvia_anio, color_continuous_scale='inferno_r', origin='lower', aspect="auto",
                labels=dict(x="Mes", y="Día del mes", color="Precipitación [mm]"),
                x=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
                #x = list(range(1,13)),
                y = list(range(1,32)))
fig_mapa_lluvia.update_layout(title="Mapa de lluvias", coloraxis_showscale=False, height=135, modebar={'remove': True}, margin=dict(l=20, r=20, t=40, b=20),)
#fig_mapa_lluvia.update_xaxes(side="top")
with tab1:
    placeholder = st.empty()
    with placeholder.container(): 
        
        c1, c2 = st.columns([1.7,2.3])
        #c2.caption("Mapa de lluvias")
        c2.plotly_chart(fig_mapa_lluvia, use_container_width=True)
        ultimo_dato = datetime.date(2023, 11, 21)  ## <<----- FECHA ULTIMO DATO UPDATE!!!
        quincena = datetime.timedelta(days=20)
        ultima_semana = ultimo_dato - quincena
        fecha_desde = c1.date_input("Seleccione fecha", ultima_semana)
        fecha_hasta = fecha_desde + quincena
        #c2.write(f"Fecha hasta: {fecha_hasta}")
        
        idx = ((r1_df.datetime.dt.date >= fecha_desde) & (r1_df.datetime.dt.date <= fecha_hasta))
        r1_df = r1_df[idx]
        idx = ((r2_df.datetime.dt.date >= fecha_desde) & (r2_df.datetime.dt.date <= fecha_hasta))
        r2_df = r2_df[idx]
        idx = ((lluviaR2_15min.datetime.dt.date >= fecha_desde) & (lluviaR2_15min.datetime.dt.date <= fecha_hasta))
        lluviaR2_15min = lluviaR2_15min[idx]
        idx = ((r3_df.datetime.dt.date >= fecha_desde) & (r3_df.datetime.dt.date <= fecha_hasta))
        r3_df = r3_df[idx]
        idx = ((r4_df.datetime.dt.date >= fecha_desde) & (r4_df.datetime.dt.date <= fecha_hasta))
        r4_df = r4_df[idx]
        idx = ((r5_df.datetime.dt.date >= fecha_desde) & (r5_df.datetime.dt.date <= fecha_hasta))
        r5_df = r5_df[idx]

        option = c1.selectbox('Precipitación',('Diaria', 'Intensidad'))
        if option == "Intensidad":
            # intensisdad lluvia para R2
            xdata_R2_lluvia = lluviaR2_15min["datetime"]
            ydata_R2_lluvia = lluviaR2_15min["mm15min"]
        elif option == "Diaria":
            #lluvia diaria R2: mejorar: estoy apurado
            lluviaR2_15min["date"] = lluviaR2_15min["datetime"].dt.date
            lluvia_x_dia_R2 = lluviaR2_15min.groupby("date").sum(numeric_only = True)
            xdata_R2_lluvia = lluvia_x_dia_R2.index
            ydata_R2_lluvia = lluvia_x_dia_R2["mm15min"]

        fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=("<b>Altura hidrométrica</b>", "<b>Precipitación Cuenca Urbana</b>", "<b>Napa freática</b>"))
        # Niveles R1 (canal 1) y R5 (alcantarilla Lavaisse)
        fig.add_trace(go.Scattergl(x = r1_df.datetime, y = 300-r1_df.distancia, mode="lines", name="Altura Canal 1 (R1)"), row=1, col=1)
        fig.add_trace(go.Scattergl(x = r5_df.datetime, y = r5_df.nivel, name="Altura Alcantarilla 1 (R5)", mode="lines"), row=1, col=1)
        
        # Precipitacion R2 (taller ministerio)
        fig.add_trace(go.Bar(x = xdata_R2_lluvia, y = ydata_R2_lluvia, name="Precipitación Ministerio (R2)", marker_color='rgb(26, 118, 255,0)'), row=2, col=1)
        
        # Niveles Freaticos R2, R3, R4
        fig.add_trace(go.Scattergl(x = r2_df.datetime, y = r2_df.nf, name="NF MISPyH (R2)", mode="lines"), row=3, col=1)
        fig.add_trace(go.Scattergl(x = r3_df.datetime, y = r3_df.nf, name="NF Reserva (R3)", mode="lines"), row=3, col=1)
        fig.add_trace(go.Scattergl(x = r4_df.datetime, y = r4_df.nf, name="NF La Redonda (R4)", mode="lines"), row=3, col=1)

        fig.update_yaxes(title_text="Nivel [cm]", range=[0, 150], row=1, col=1)
        fig.update_yaxes(title_text="Precipitación [mm]",  row=2, col=1)
        fig.update_yaxes(title_text="Profundidad [cm]", autorange="reversed", row=3, col=1)
        fig.update_xaxes(title_text="Fecha", row=3, col=1)

        fig.update_layout(height=700, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)

        #with open(fn) as f:
        #    st.download_button('Download CSV', f)
with tab2:
    placeholder2 = st.empty()
    with placeholder2.container():
        fig = go.Figure()
        fig.add_trace(go.Scattergl(x = r1_df.datetime, y = r1_df.voltaje*92.59-296.28, mode="lines", name="R1 Nivel (Canal 1 Reserva)"))
        fig.add_trace(go.Scattergl(x = r2_df.datetime, y = r2_df.bateria, mode="lines", name="R2 NF/Pluvio (MISPyH)"))
        fig.add_trace(go.Scattergl(x = r3_df.datetime, y = r3_df.bateria, mode="lines", name="R3 NF (Reserva)"))
        fig.add_trace(go.Scattergl(x = r4_df.datetime, y = r4_df.bateria, mode="lines", name="R4 NF (La Redonda)"))
        fig.add_trace(go.Scattergl(x = r5_df.datetime, y = r5_df.bateria, mode="lines", name="R5 Alcantarilla 1 (Reserva)"))

        fig.update_layout(title="Voltaje equipos",legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))
        st.plotly_chart(fig, use_container_width=True)