import os
import glob
import pickle

import pandas as pd
import numpy as np

path = r'datos/R2-NF-Taller-Ministerio/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nf', 'cmca', 'cangilones'], comment='#') for f in all_files)
eqR2   = pd.concat(dfs, ignore_index=True)

eqR2.loc[eqR2["cangilones"].isna(),"cangilones"] = 0

eqR2.to_csv("datos/nf_R2.csv", sep=";", index=False)
eqR2.to_parquet("datos/nf_R2.parquet.gzip", compression='gzip')

last_week = eqR2[-800:]
last_week.to_csv("datos/nf_R2_last_week.csv", sep=";", index=False)

eqR2["mm"] = eqR2["cangilones"]*0.25
eqR2[["datetime", "cangilones", "mm"]].to_csv("datos/lluvia_R2.csv", sep=";", index=False)

# esto estaba en get_mm_R2.py
# ahora lo pongo acá para usar solamente este script
fn  = "datos/lluvia_R2.csv"
contenido = open(fn).readlines()
out = open("datos/lluvia_R2.csv", "w")
header = f"{contenido[0].strip()};mm15min\n"
out.write(header)
for i,linea in enumerate(contenido[2:],2):
    fh_actual, cangilon_act, mm_act = linea.split(";")
    fecha_act, hora_act = fh_actual.split()
    
    fh_ant, cangilon_ant, mm_ant = contenido[i-1].split(";")
    fecha_ant, hora_ant = fh_ant.split()
    dmm = float(mm_act)-float(mm_ant)
    dmm = 0 if (dmm)<0 else dmm
    oline = f"{linea.strip()};{dmm}\n"
    out.write(oline)
out.close()

lluviaR2_15min = pd.read_csv(fn, parse_dates=["datetime"], sep=";")
lluviaR2_15min.to_parquet("datos/lluvia_R2.parquet.gzip", compression='gzip')

# genero un DF con la lluvia por dia
lluviaR2_15min["date"] = lluviaR2_15min["datetime"].dt.date
lluvia_x_dia_R2 = lluviaR2_15min.groupby("date").sum(numeric_only = True)
lluvia_x_dia_R2["mm"] = lluvia_x_dia_R2["mm15min"]
lluvia_x_dia_R2 = lluvia_x_dia_R2["mm"]
lluvia_x_dia_R2.to_csv("datos/lluvia_R2_diaria.csv", sep=";")

data = open("datos/lluvia_R2_diaria.csv")
data.readline() # salteo el primer renglon pq esta el header

# creo matriz con NaN
anio = np.full((31,12), np.nan)

# cargo mm en fila (dia), columna (mes)
for line in data:
    line = line.strip();
    fecha,mm = line.split(";")
    a,m,d = fecha.split("-")
    m, d = int(m), int(d)
    anio[d-1,m-1] = mm

# Guardar el NumPy array en un archivo
with open('datos/lluvia_R2_diaria.pickle', 'wb') as file:
    pickle.dump(anio, file)

#contenido = open("datos/lluvia_R2.csv").readlines()
#contenido = contenido[1:]
#salida = open("datos/lluvia_R2_mm.csv", "a")
#
#fecha_hora, cangi_acum = contenido[1].split(";")
#fecha_ant, hora_ant = fecha_hora.split()
#
#for i,renglon in enumerate(contenido[1:]):
#    renglon = renglon.strip()
#    fecha_hora, cangi_acum = renglon.split(";")
#    fecha, hora = fecha_hora.split()
#    if fecha != fecha_ant:
#        fecha_ant = fecha
#        fh_prev, cangi_prev = contenido[i-1].split(";")
#        f_prev, h_prev = fh_prev.split()
#        renglon_salida = f_prev + ";" + str(float(cangi_acum.rstrip())*0.25) + "\n"
#        salida.write(renglon_salida)
#salida.close()