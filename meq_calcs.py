# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:50:06 2021

@author: Michael J. Murphy
"""
# Calculate meq/L for Stiff diagrams

import pandas as pd

data = '2020_Q3_stiff_data.xlsx'
df1 = pd.read_excel(data, engine='openpyxl')

df2 = df1[["LocCode", "Field_ID", "Sampled_Date-Time", "ChemName", "Conc_num"]]

chems = sorted(df2.ChemName.unique().tolist())
charges = [-1, 2, -1, 2, 1, 1, -2]
molar_masses = [61.0168, 40.078, 35.453, 24.305, 39.0983, 22.99, 96.06]

chem_zip = zip(chems, charges, molar_masses)
# Write mass charge to dataframe for conversion to meq/L
df2["mass_charge"] = 0
df2["meq/L"] = 0
for chem, charge, mass in chem_zip:
    df2.loc[df2.ChemName==chem, 'mass_charge'] = mass / charge
    df2.loc[df2.ChemName==chem, "meq/L"] = df2.Conc_num / df2.mass_charge

#def calc_meq():
    