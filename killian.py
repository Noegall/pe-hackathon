# +
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv('PS_2024.10.29_06.08.28.csv', index_col=0)

#Mass en fonction du rayon
a = df[["pl_masse","pl_rade","tran_flag"]][df["tran_flag"] == 1]
b = df[["pl_masse","pl_rade","tran_flag"]][df["tran_flag"] == 0]
ax = a.plot("pl_masse","pl_rade",style="xb",logx=True,ms=1)
b.plot("pl_masse","pl_rade",style="or",logx=True,ms=1, ax=ax)


c = df[["pl_orbper","pl_insol","tran_flag"]][df["tran_flag"] == 1]
d = df[["pl_orbper","pl_insol","tran_flag"]][df["tran_flag"] == 0]
ax = c.plot("pl_orbper","pl_insol",style="xb",loglog=True,ms=1)
d.plot("pl_orbper","pl_insol",style="or",loglog=True,ms=1, ax=ax)
# -







