#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:42:39 2018

@author: Jackie
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pandas as pd

#%%
years = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
         '2016', '2017']
BASE_URL = 'http://www.baseball-reference.com/awards/awards_'
END_URL = '.shtml'

awards = ['all_AL_CYA_voting', 'all_NL_CYA_voting']
leagues = ['AL', 'NL']

finalists = []
for year in years:
    url = BASE_URL + year + END_URL
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    
    for ix, award in enumerate(awards):
        div = soup.find('div', id=award)
        
        # Table is within comment
        al = div.find('div', class_='placeholder').next_sibling.next_sibling
        
        new_soup = BeautifulSoup(al, 'lxml')
        body = new_soup.find('tbody')
        for tr in body.findAll('tr'):
            info = {}
            info['Season'] = year
            info['League'] = leagues[ix]
            info['Rank'] = tr.find('th', class_='right').text
            info['Name'] = tr.find('a').text
            td = tr.find('td').next_sibling.next_sibling
            info['Points_won'] = td.text
            info['Votes_first'] = td.next_sibling.text
            info['Share'] = td.next_sibling.next_sibling.text[:-1]
            
            finalists.append(info)

df = pd.DataFrame(finalists)
cols = ['Season', 'League', 'Rank', 'Name', 'Points_won', 'Votes_first', 'Share']
df = df[cols]

df.to_csv('cy_young_finalists.csv', index=False)