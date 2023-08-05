import os
import glob

import pandas as pd

path = r'datos/R1-Nivel-RNUO-Canal1/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'voltaje', 'distancia'], comment='#') for f in all_files)
eqR1   = pd.concat(dfs, ignore_index=True)

eqR1.to_csv("datos/distancia_R1.csv", sep=";", index=False)
eqR1.to_parquet("datos/distancia_R1.parquet.gzip", compression='gzip')
last_week = eqR1[-10080:]
last_week.to_csv("datos/distancia_R1_last_week.csv", sep=";", index=False)
