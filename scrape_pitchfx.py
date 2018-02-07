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
long_names = ['fourseam', 'sinker', 'cutter', 'curve', 'slider', 'change',
              'splitter', 'screwball', 'knuckleball']

stats = []
for year in years:
    for pitch in pitch_types:
        # scrape urls for each year and pitch type
        url_pieces = ['https://legacy.baseballprospectus.com/pitchfx/',
                      'leaderboards/index.php?hand=&reportType=pfx&prp=P',
                      '&month=&year=', year, '&pitch=', pitch, 
                      '&ds=velo&lim=200']
        url = ''.join(url_pieces)
        
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('tbody')
        
        for tr in table.findAll('tr'):
            
            tds = tr.findAll('td')
        
            info = {}
            info['year'] = year
            info['pitch_type'] = pitch
            info['name'] = tds[1].text
            info['throws'] = tds[3].text
            info['num_pitches'] = tds[4].text
            info['velocity'] = tds[5].text
            info['H_movement'] = tds[6].text
            info['V_movement'] = tds[7].text
            info['swing_rate'] = tds[8].text[:-1]
            info['whiff/swing'] = tds[9].text[:-1]
            info['foul/swing'] = tds[10].text[:-1]
            info['GB/FB'] = tds[11].text
            info['GB/BIP'] = tds[12].text[:-1]
            info['LD/BIP'] = tds[13].text[:-1]
            info['FB/BIP'] = tds[14].text[:-1]
            info['PU/BIP'] = tds[15].text[:-1]
            
            stats.append(info)

#%%
df = pd.DataFrame(stats)
df.to_csv('baseball_prospectus_pitchfx.csv', index=False)