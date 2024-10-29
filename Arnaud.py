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
import numpy as np

# %%
df = pd.read_csv('PS_2024.10.29_06.08.28.csv', index_col=0, skiprows=291)
df

# %%
df.plot('pl_eqt','pl_rade', logy=True, style='o', ms=0.5, title='Planetary radius vs equilibrium temperature', xlabel='Equilibrium temperature [K]', ylabel='Planetary radius [Earth radius]');

# %%
