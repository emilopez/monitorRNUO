# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://github.com/blackary/st_pages
from pathlib import Path

#from st_pages import Page, Section, show_pages, add_page_title
import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Monitor Reserva Natural Urbana del Oeste - Santa Fe",
    layout="wide"
)

add_logo("logo.jpg")

st.write("# Proyecto Científico de *Monitoreo hidro-ambiental*...")
col_inv, col_est = st.columns(2)
col_inv.write("#### Investigadores")
col_inv.write("""
- **Director:** Emiliano López, CEFHAL (FICH / UNL) - elopez@fich.unl.edu.ar
- Emiliano A. Veizaga, CEFHAL (FICH / UNL)
- María Florencia Gutiérrez, INALI/CONICET
- Lucas Dominguez, CEFHAL (FICH / UNL) - CONICET
- Francisco Latosinski, CEFHAL (FICH / UNL) - CONICET
- Jorge Prodolliet, CEFHAL (FICH / UNL)
- Diego Frau, INALI/CONICET
- Elisabet Walker, CEFHAL (FICH / UNL) - CONICET
- Juan Pablo de Rosas, IMASL (UNSL - CONICET)
- Guillermo Contini, CIM (FICH / UNL)

#### Instituciones
- Centro de Estudios Fluviales e HidroAmbientales del Litoral (CEFHAL) - FICH / UNL
- Instituto Nacional de Limnología (INALI), CONICET / UNL
- Secretaría de Ambiente y Cambio Climático (SACC), Municipalidad de Santa Fe
- Secretaría de Infraestructura y Gestión Hídrica (SIGH), Municipalidad de Santa Fe
- Asociación Civil Contraversiones
""")
              
col_est.write("""              
#### Estudiantes / Pasantes
- Giuliana Luna (FICH / UNL)
- Ayelén Miranda (ESS-FBCB / UNL)
- Alex Mendoza (FICH / UNL)

#### Colaboradores 
- Luciana Manelli (FICH / UNL - SACC)
- María Paula Gagliardi (SIGH)              
- Martín Morales (AC Contraversiones)
- María Claret (FICH / UNL)
- Emanuel Blanco (AC Contraversiones)
- Lucas Palman (FICH / UNL)

#### Community Manager
- Alexia Vattovaz

#### Financiamiento y Asesoramiento técnico
[Fundación Bunge y Born](https://www.fundacionbyb.org), Concurso Aguas Claras, 2022.
""")

              
col_cto, col_datos = st.columns(2)

col_cto.write("### Contacto")
col_cto.write("""
- Twitter: [@ReservaOesteSFe](https://twitter.com/ReservaOesteSFe)
- Instagram: [reservanaturaloeste.sf](https://www.instagram.com/reservanaturaloeste.sf/)
- E-mail: reservaoeste.sfe@gmail.com
""")


col_datos.write("### Uso de datos - Licencia")

with col_datos:
    st.write('''Se deslinda toda responsabilidad por el uso que se haga de los datos aquí publicados. 
    Los datos son publicados bajo la licencia CC BY-NC-SA:''')
   
    # Render the h1 block, contained in a frame of size 200x200.
    st.components.v1.html('''<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Monitor hidro-ambiental de la RNUO</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
    ''', width=500, height=300)
