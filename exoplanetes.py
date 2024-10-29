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
df.shape



# %%
df.columns

# %%
#Création d'un tableau réduit avec les données que l'on veut analyser
tab=df[['pl_name','sy_snum','sy_pnum','sy_mnum','disc_year','discoverymethod','disc_facility','pl_orbper','pl_rade','pl_masse','pl_dens','pl_orbeccen']]
tab.columns=['nom','nb_etoile','nb_planete','nb_lune','an_decouverte','methode_decouverte','labo','orbite','rayon','masse','densite','excentricity']
tab.head()

# %%
#Analyse de l'année de découverte
print(tab['an_decouverte'].dtypes)
print(tab['an_decouverte'].describe())

# %%
#Etude des données manquantes
tab.isna().describe()


# %%
#Données sur le nombre de planète, d'étoiles et de lune
tab[['nb_etoile','nb_planete','nb_lune']].describe()

# %%
#On veut étudier le nombre d'étoiles des planètes
tab['nb_etoile'].unique()
by_nb_etoile=tab.groupby(by=['nb_etoile'])

# %%
by_nb_etoile.size()

# %%
tab['labo'].unique()

# %%
tab['methode_decouverte'].unique()

# %%
by_methode=tab.groupby(by='methode_decouverte')


# %%
by_methode.size()

# %%
#On étudie les planètes découvertes par le laboratoire de haute provence
mask1=tab['labo']=='Haute-Provence Observatory'
tab[mask1]

# %%
#On cherche le nombre de planètes, d'étoiles et de lunes découvertes par le labo étudié chaque année
tab[mask1].pivot_table(values=['nb_etoile','nb_lune','nb_planete'],index='an_decouverte', columns='labo',aggfunc='sum')

# %%
#Quelles sont les méthodes utilisées par ce labo?
tab[mask1]['methode_decouverte'].unique()

# %%
