import streamlit as st
import streamlit.components.v1 as components

from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Niveles del Río Salado", 
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