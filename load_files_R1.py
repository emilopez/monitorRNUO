import os
import glob

import pandas as pd

path = r'datos/R1/'              
all_files = glob.glob(os.path.join(path, "*.CSV"))
all_files = sorted(all_files, reverse=False)

dfs = (pd.read_csv(f, sep=";", parse_dates=['datetime'], names=['datetime', 'voltaje', 'distancia'], comment='#') for f in all_files)
eqR1   = pd.concat(dfs, ignore_index=True)

eqR1.to_csv("datos/distancia_R1.csv", sep=";", index=False)