#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:34:33 2018

Join all of the pitching data into one csv

@author: Jackie
"""

import pandas as pd

# Load all baseball data files
xlsx = pd.ExcelFile('data/starters_2008-2017.xlsx')
fangraphs = pd.read_excel(xlsx, 'fangraphs')
statcast = pd.read_excel(xlsx, 'statcast')
cya_finalists = pd.read_csv('data/cy_young_finalists.csv')
pitch_fx = pd.read_csv('data/baseball_prospectus_pitchfx.csv')

# Join fangraphs and statcast data
res = pd.merge(fangraphs, statcast, on = ['Name', 'Season'], how = 'left')

# Join result of join above with cya_finalists
res2 = pd.merge(res, cya_finalists, on = ['Name', 'Season'], how = 'left')

# Join result of join above with pitch_fx
df = pd.merge(res2, pitch_fx, on = ['Name', 'Season'], how = 'left')

#%%
# Write out df as csv
df.to_csv('data/joined_pitching_data_2008-2017.csv', index = False)