#monitor RNUO

Hydro-environmental monitor of the west urban natural reserve (Salado River, Santa Fe, Argentina).

## WEb

https://monitorreservasfe.streamlit.app/

## Instalación de entorno de desarrollo:

Ojo, streamlit lo installo con `pip` en vez de `conda`, sino no funca. El resto de las dependencias se instalan solitas. 

```
conda create -n webRNUO python=3.10
pip install streamlit
conda install plotly
```

Probar si streamlit funca: `strealit hello`

## Documentación

- `load_files_R1.py`: lee de de `datos/R1/` todos los CSV del equipo R1 y crea un único archivo `datos/distancia_R1.csv` que es leído por el monitor
- `datos/multiparametricas.csv`: tiene los datos de calibración de las multiparamétricas

## Streamlit cloud

Para evitar errores por versiones no disponibles de python en streamlit cloud lo quité la especificación
