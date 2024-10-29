# +
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv('PS_2024.10.29_06.08.28.csv', index_col=0)
df

#Mass en fonction du rayon
a = df[["pl_masse","pl_rade","tran_flag"]][df["tran_flag"] == 1]
ax = a.plot("pl_masse","pl_rade",style="x",logx=True,ms=1)
df.plot("pl_masse","pl_rade",style="o",logx=True,ms=1, ax=ax)



# +
# pd.DataFrame.plot?
# -




