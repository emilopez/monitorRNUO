import os
import glob

import pandas as pd

path = r'datos/R4-NF-La-Redonda/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nf', 'cmca'], comment='#') for f in all_files)
eqR4   = pd.concat(dfs, ignore_index=True)

eqR4.to_csv("datos/nf_R4.csv", sep=";", index=False)
eqR4.to_parquet("datos/nf_R4.parquet.gzip", compression='gzip')

last_week = eqR4[-10080:]
last_week.to_csv("datos/nf_R4_last_week.csv", sep=";", index=False)
