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
#Construction d'une sous data-frame avec moins de données prises en compte
#df_systeme : données liées aux planètes, étoiles, lunes des exoplanètes
df_systeme = df[['sy_snum', 'sy_pnum', 'sy_mnum']]
df_systeme.head(3)

# %%
#df_decouverte : données liées à la découverte des exoplanètes
df_decouverte = df[['pl_name', 'discoverymethod', 'disc_year', 'disc_telescope', 'disc_refname', 'disc_pubdate', 'disc_locale', 'disc_facility', 'disc_telescope', 'disc_instrument']]
df_decouverte.head(2)

# %%
#df_donnees : données générales liées à l'exoplanète
df_donnees=df[['pl_name', 'hd_name', 'pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_masse', 'pl_dens', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'pl_orbincl', 'pl_tranmid']]
df_donnees.head(10)

# %%
#Affichage du nombre de valeurs manquantes
df.isna().sum()

# %%
df.sort_values(by='pl_masse')

# %%
#On remarque que beaucoup de valeurs de masses et de rayons sont manquantes
df['pl_masse'].isna().sum()
df['pl_rade'].isna().sum()

# %%
summary_masses = df['pl_masse'].describe()
summary_masses

# %%
summary_rade = df['pl_rade'].describe()
summary_rade

# %% [markdown]
# #On veut analyser les données pour les exoplanètes dont on connaît les masse et rayon
# #On créer donc un nouveau dataframe contenant seulement les exoplanètes pour
# #lesquelles les données de masse et rayon sont connues
# #ensuite on regardera la technologie utilisée pour la découverte de l'exoplanète

# %%
df_new = df_donnees.merge(df_decouverte)
df_new.head(2)

# %%
df_new['pl_masse'].drop(axis=0, inplace=True)
df_new['pl_rade'].drop(axis=0, inplace=True)
df.dropna(axis=0, how='all', inplace=True)
df_new.head(10)

# %%
# pd.DataFrame.drop?

# %%
df.pivot_table(
    values=['pl_masse', 'pl_rade', 'disc_telescope', 'disc_instrument'],
    index='pl_name'
)

# %%
