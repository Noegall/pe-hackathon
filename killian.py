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

#On essaie d'enelever les multiples inutiles des planètes
df = df.drop_duplicates()
#Y'a des différence sur des flag dans certaines colonnes
df = df.drop("rv_flag",axis="columns")
df = df.drop("pul_flag",axis="columns")
df = df.drop("ptv_flag",axis="columns")
df = df.drop("tran_flag",axis="columns")
df = df.drop("ast_flag",axis="columns")
df = df.drop("obm_flag",axis="columns")
df = df.drop("micro_flag",axis="columns")
df = df.drop("etv_flag",axis="columns")
df = df.drop("ima_flag",axis="columns")
df = df.drop("dkin_flag",axis="columns")
df = df.drop_duplicates()

# -







