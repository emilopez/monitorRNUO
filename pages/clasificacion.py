import streamlit as st
import streamlit.components.v1 as components

from streamlit_extras.app_logo import add_logo

import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Clasificación Satelital - RNUO", 
                    page_icon="🌎", 
                    layout="wide")
add_logo("logo.jpg")

st.markdown("# Clasificación satelital")
st.write("""Superficies identificadas en diferentes estaciones del año""")

c1, c2, c3, c4 = st.columns(4)
with c1:
    c1.write("Verano (Fecha: 08/03/2022)")
    components.iframe("""https://umap.openstreetmap.fr/en/map/clasificacion-rnuo-08032022_933751?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true""", height=600, width=350)
with c2:
    c2.write("Otoño (Fecha: 18/05/2022)")
    components.iframe("""https://umap.openstreetmap.fr/en/map/clasificacion-rnuo-18052022_933741?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true""", height=600, width=350)
with c3:
    c3.write("Invierno (Fecha: 09/07/2023)")
    components.iframe("""https://umap.openstreetmap.fr/en/map/clasificacion-09072022_933760?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true""", height=600, width=350)
with c4:
    c4.write("Primavera (Fecha: 02/09/2022)")
    components.iframe("""https://umap.openstreetmap.fr/en/map/rnuo_933335?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true""", height=600, width=350)

# superficie en m2 (pasado a hectareas* 1e-4) por clase para las fechas
sup_por_clase = {"fecha":["2022-03-08", "2022-05-18", "2022-07-09", "2022-09-02"], 
                   "clase1":np.array([129474.07, 67170.75, 242447.48, 295142.29])*1e-4, 
                   "clase2":np.array([348116.49, 339776.33, 341782.65, 323195.11])*1e-4,
                   "clase3":np.array([102303.29, 284876.66, 248934.38, 217742.02])*1e-4,
                   "clase4":np.array([222141.59, 134152.36, 143284.19, 130139.77])*1e-4,
                   "clase5":np.array([264085.09, 240144.45, 89671.96, 99901.35])*1e-4}
sup_por_clase = pd.DataFrame(sup_por_clase)
fig = go.Figure()
fig.add_trace(go.Scattergl(x=sup_por_clase.fecha, y=sup_por_clase.clase1, name="Clase 1"))
fig.add_trace(go.Scattergl(x=sup_por_clase.fecha, y=sup_por_clase.clase2, name="Clase 2 (Agua)"))
fig.add_trace(go.Scattergl(x=sup_por_clase.fecha, y=sup_por_clase.clase3, name="Clase 3"))
fig.add_trace(go.Scattergl(x=sup_por_clase.fecha, y=sup_por_clase.clase4, name="Clase 4"))
fig.add_trace(go.Scattergl(x=sup_por_clase.fecha, y=sup_por_clase.clase5, name="Clase 5"))
fig.update_layout(title="Hectáreas de superficie por clase", legend=dict(orientation="h", yanchor="bottom", y=1.02,xanchor="right", x=0.9))

c1, c2 = st.columns(2)
c1.plotly_chart(fig, use_container_width=True)
c2.subheader("Datos de superficie por cada clase (hectáreas)")
c2.write(sup_por_clase)