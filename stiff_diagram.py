# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:11:57 2021

@author: Michael J. Murphy
"""
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalAxis, FactorRange
import pandas as pd


# Test categorical area plot
left_axis_labels = ['Mg++', "Ca++", "Na+ + K+"]
right_axis_labels = ["HCO3- + CO3--", "SO4-", "Cl-"]

left_data = [-3, -1.75, -4.5]
right_data = [3, 1.0, 4.75] 

p1 = figure(y_range=left_axis_labels)

p1.harea(x1=[0, 0, 0], x2=left_data, y=left_axis_labels)

p1.extra_y_ranges = {"right_range": FactorRange(factors=right_axis_labels)}
p1.add_layout(CategoricalAxis(y_range_name="right_range"), 'right')

p1.harea(x1=[0, 0, 0], x2=right_data, y=left_axis_labels) # For this to work, right y-axis must be same as left y-axis; should be converted to single dummty axis to avoid confusion

show(p1) 