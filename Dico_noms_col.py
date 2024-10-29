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
file = open('PS_2024.10.29_06.08.28.csv','r')
file.readline()
file.readline()
file.readline()
dico = {}
for i in range(287):
    content = file.readline()
    content = content.split('# COLUMN ')
    content = content[1].split(': ')
    dico[content[0]] = content[1].lstrip().rstrip()

# %%
dico['pl_name']

# %%
