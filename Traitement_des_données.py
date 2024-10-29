# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
df = pd.read_csv('PS_2024.10.29_06.08.28.csv', skiprows=291, index_col='rowid')

# %%
df.tail(10)

# %%
df.shape

# %%
df.columns

# %%
df.dtypes

# %%
df_2 = df[['pl_name', 'hd_name', 'sy_snum', 'sy_pnum', 'sy_mnum']]
df_2.head(3)

# %%
df_decouverte=df[['pl_name','discoverymethod','disc_year','disc_telescope']]
df_decouverte.head(2)

# %%
df['rv_flag'].dtypes
df['pl_tsystemref'].dtypes

# %%
df['pl_name']

# %%
df_tri = df[['pl_name', 'pl_masse']].sort_values(by=['pl_masse'], na_position='first')
df_tri.head(30)

# %%
df.isna().describe()

# %%

# %%
