import os
import glob

import pandas as pd

path = r'datos/R5-RNUO-Alcantarilla1/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nivel', 'dist'], comment='#') for f in all_files)
eqR5   = pd.concat(dfs, ignore_index=True)

eqR5.to_csv("datos/nivel_R5.csv", sep=";", index=False)

last_week = eqR5[-10080:]
last_week.to_csv("datos/nivel_R5_last_week.csv", sep=";", index=False)
