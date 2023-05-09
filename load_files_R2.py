import os
import glob

import pandas as pd

path = r'datos/R2-NF-Taller-Ministerio/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nf', 'cmca'], comment='#') for f in all_files)
eqR2   = pd.concat(dfs, ignore_index=True)

eqR2.to_csv("datos/nf_R2.csv", sep=";", index=False)

last_week = eqR2[-800:]
last_week.to_csv("datos/nf_R2_last_week.csv", sep=";", index=False)
