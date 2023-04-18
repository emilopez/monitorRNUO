import os
import glob

import pandas as pd

path = r'datos/R3/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'bateria', 'nf', 'cmca'], comment='#') for f in all_files)
eqR3   = pd.concat(dfs, ignore_index=True)

eqR3.to_csv("datos/nf_R3.csv", sep=";", index=False)

last_week = eqR3[-10080:]
last_week.to_csv("datos/nf_R3_last_week.csv", sep=";", index=False)
