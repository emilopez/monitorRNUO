import os
import glob

import pandas as pd

path = r'datos/R2-NF-Taller-Ministerio/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nf', 'cmca', 'cangilones'], comment='#') for f in all_files)
eqR2   = pd.concat(dfs, ignore_index=True)

eqR2.loc[eqR2["cangilones"].isna(),"cangilones"] = 0

eqR2.to_csv("datos/nf_R2.csv", sep=";", index=False)

last_week = eqR2[-800:]
last_week.to_csv("datos/nf_R2_last_week.csv", sep=";", index=False)

eqR2["mm"] = eqR2["cangilones"]*0.25
eqR2[["datetime", "cangilones", "mm"]].to_csv("datos/lluvia_R2.csv", sep=";", index=False)


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