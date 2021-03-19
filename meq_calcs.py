# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:50:06 2021

@author: Michael J. Murphy
"""
# Calculate meq/L for Stiff diagrams

import pandas as pd

class MeqCalc:
    
    def __init__(self, data):
        self.data = data
        self.df1 = pd.read_excel(self.data, engine='openpyxl') # All data
        self.df2 = self.df1[["LocCode", "Field_ID", "Sampled_Date-Time", "ChemName", "Conc_num"]] # Required columns
        
    def calc_meq(self):
        
        # Expected analytes and sorting: ['Alkalinity (Bicarbonate)','Calcium','Chloride','Magnesium','Potassium','Sodium','Sulfate']
        chems = sorted(self.df2.ChemName.unique().tolist())
        ions = ["HCO3-", "Ca++", "Cl-", "Mg++", "Na+ + K+", "Na+ + K+", "SO4--"]
        charges = [-1, 2, -1, 2, 1, 1, -2]
        molar_masses = [61.0168, 40.078, 35.453, 24.305, 39.0983, 22.99, 96.06]
        chem_zip = zip(chems, charges, molar_masses, ions)
        
        # Write mass charge to dataframe for conversion to meq/L
        self.df2["mass_charge"] = 0
        self.df2["meq/L"] = 0
        self.df2["ion"] = ''
        for chem, charge, mass, ion in chem_zip:
            self.df2.loc[self.df2.ChemName==chem, 'mass_charge'] = mass / charge
            self.df2.loc[self.df2.ChemName==chem, "meq/L"] = self.df2.Conc_num / self.df2.mass_charge
            self.df2.loc[self.df2.ChemName==chem, "ion"] = ion
        return self.df2

    