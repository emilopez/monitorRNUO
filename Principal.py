# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://github.com/blackary/st_pages
from pathlib import Path

import streamlit as st

from st_pages import Page, show_pages, add_page_title, Section
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

show_pages(
    [
        Page("Principal.py", "Principal", "🏠"),
        Page("pages/dashboard.py", "Monitor general", ":computer:"),
        Page("pages/parametros_hidrologicos.py", "Parámetros Hidrológicos", "📈"),
        Page("pages/parametros_ambientales.py", "Parámetros Ambientales", "📊"),
        Page("pages/puntos_de_observacion.py", "Puntos de Observación", "🌎"),
        Page("pages/niveles_rio_salado.py", "Altura Río Salado", "♒"),
        Page("pages/clasificacion.py", "Clasificación Satelital", ":satellite:"),
        Page("pages/acercade.py", "Acerca de...", ":clipboard:"),
    ]
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Monitor Hidro-Ambiental de datos abiertos | RNUO - Santa Fe")
st.write("""En este sitio se pueden encontrar los datos registrados durante la ejecución del 
Proyecto Científico denominado **Monitoreo hidro-ambiental para la gestión del agua de la Reserva Natural
Urbana del Oeste (RNUO) de la ciudad de Santa Fe**.

El proyecto ha sido ganador del concurso Aguas Claras, financiado por la Fundación Bunge y Born y es llevado
adelante por investigadores del **Centro de Estudios Fluviales e HidroAmbientales del Litoral** (CEFHAL), 
perteneciente a la Facultad de Ingeniería y Ciencias Hídricas de la Universidad Nacional del Litoral junto al **Instituto
Nacional de Limnología** (UNL - CONICET).

Contamos con la colaboración del Municipio de la ciudad de Santa Fe a través de la Secretaría de Medio Ambiente y 
Cambio Climático y la Secretaría de Infraestructura y Asuntos Hídricos; del Gobierno Provincial de Santa Fe mediante 
del Ministerio de Infraestructura, Servicios Públicos y Hábitat; y la Asociación Civil Contraversiones.

El monitor se encuentra en permanente desarrollo por lo que se irá actualizando durante el transcurso del proyecto. En el 
menú lateral se encuentran los enlaces para la visualización interactiva de la información registrada. Para contactarte y 
obtener más información del proyecto podés ir a la sección **Acerca de**. 

### Parámetros monitoreados
- Niveles hidrométricos en los canales de ingreso y del reservorio
- Profundidad de la napa freática en tres puntos: cuenca alta, media y baja (reservorio)
- Precipitación en la cuenca de aporte y en la Reserva.
- Temperatura, conductividad eléctrica, oxígeno disuelto, pH, potencial Redox.
- Coliformes, hidrocarburos, metales
- Microplásticos, Fitoplancton, Zooplancton

""")

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: right; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<a style='display: inline; text-align: left;' href="https://github.com/emilopez" target="_blank"> developed by emilopez</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
    



