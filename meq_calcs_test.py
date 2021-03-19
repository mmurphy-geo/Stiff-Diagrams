# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:25:56 2021

@author: Michael
"""
from meq_calcs import MeqCalc

data = '2020_Q3_stiff_data.xlsx'

test1 = MeqCalc(data)
test1.calc_meq()
print(test1.df2.head())

