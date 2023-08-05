import pandas as pd

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