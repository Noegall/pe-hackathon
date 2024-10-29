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
import pandas as pd

# %%
df=pd.read_csv('PS_2024.10.29_06.08.28.csv', skiprows =291)

# %%
df.head()

# %%
df.columns

# %%
#Création d'un tableau réduit avec les données que l'on veut analyser
tab=df[['pl_name','sy_snum','sy_pnum','sy_mnum','disc_year','discoverymethod','disc_facility','pl_orbper','pl_rade','pl_masse','pl_dens','pl_orbeccen']]
tab.columns=['nom','nb_etoile','nb_planete','nb_lune','an_decouverte','methode_decouverte','labo','orbite','rayon','masse','densite','excentricity']
tab.head()

# %%
#Analyse de l'année de découverte
print(tab['disc_year'].dtypes)
print(tab['disc_year'].describe())

# %%
#Etude des données manquantes
tab.isna().describe()


# %%

# %%
