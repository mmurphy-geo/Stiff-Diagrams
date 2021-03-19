# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:10:18 2021

@author: Michael
"""
#from meq_calcs import MeqCalc
from stiff_diagrams import StiffDiagram

data1 = '2020_Q3_stiff_data.xlsx'
test_01 = StiffDiagram(data1)
print(type(test_01.df))

test_01.plot()