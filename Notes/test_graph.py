# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:38:49 2020

@author: Anjali
"""
#%%
#import random
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show

values = 25 + 7*np.random.rand(10)

f = figure()
x = [x for x in values]
y = [1,2,3,4,5,6,7,8,9,10]
f.line(y,x)
output_file('graph.html')
show(f)
