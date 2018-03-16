#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:35:58 2018

@author: Jackie

"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pandas as pd

#%%
years = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
         '2016', '2017']

pitch_types = ['FA', 'SI', 'FC', 'CU', 'SL', 'CH', 'FS', 'SB', 'KN']

stats = []
for year in years:
    for pitch in pitch_types:
        # scrape urls for each year and pitch type
        url_pieces = ['https://legacy.baseballprospectus.com/pitchfx/',
                      'leaderboards/index.php?hand=&reportType=pfx&prp=P',
                      '&month=&year=', year, '&pitch=', pitch, 
                      '&ds=velo&lim=0']
        url = ''.join(url_pieces)
        
        print(year, pitch)
        
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('tbody')
        
        for tr in table.findAll('tr'):
            
            tds = tr.findAll('td')
        
            info = {}
            info['Season'] = year
            info['Name'] = tds[1].text
            
            # Create keys that have the fields concatenated with the pitch type
            fields = ['Num_pitches_', 'Velocity_', 'H_movement_',
                      'V_movement_', 'Swing_rate_', 'Whiff/swing_',
                      'Foul/swing_', 'GB/FB_', 'GB/BIP_', 'LD/BIP_',
                      'FB/BIP_', 'PU/BIP_']
            td_pos = list(range(4, 16))
            field_pos = zip(fields, td_pos)
            
            # Leave out percent character in string
            less_one_pos = [8, 9, 10, 12, 13, 14, 15]
            
            for field, pos in zip(fields, td_pos):
                key = field + pitch
                if pos in less_one_pos:
                    info[key] = tds[pos].text[:-1]
                else:
                    info[key] = tds[pos].text
            stats.append(info)
            
#%%          
unagg = pd.DataFrame(stats)

# Replace nulls with '' to preserve, but ignore them
aggregated = unagg.fillna('').groupby(['Name', 'Season']).sum()

# Reformat the data into a flat file
df = aggregated.unstack(level=0).reset_index()
df = pd.DataFrame(aggregated.to_records())

#%%
# Names that are inconsistent that need to be fixed
names_to_fix = {'Nate Karns': 'Nathan Karns',
                'Jorge De La Rosa': 'Jorge de la Rosa',
                'J.C. Ramirez': 'JC Ramirez',
                'Vincent Velasquez': 'Vince Velasquez',
                'Hyun-jin Ryu': 'Hyun-Jin Ryu',
                'Rubby De La Rosa': 'Rubby de la Rosa',
                'Jake Junis': 'Jakob Junis',
                'Samuel Gaviglio': 'Sam Gaviglio',
                'Robbie Ross': 'Robbie Ross Jr.',
                'Lucas Sims': 'Luke Sims',
                'Zachary Neal': 'Zach Neal',
                'Robert Whalen': 'Rob Whalen',
                'Ramon A. Ramirez': 'Ramon Ramirez',
                'Jacob Faria': 'Jake Faria',
                'Andy Oliver': 'Andrew Oliver'}
fixed_names = df.replace({'Name': names_to_fix})

fixed_names.to_csv('data/baseball_prospectus_pitchfx.csv', index=False)