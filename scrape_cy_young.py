#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:42:39 2018

@author: Jackie
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#%%
url = 'http://www.baseball-reference.com/awards/awards_2008.shtml'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

finalists = []
div = soup.find('div', id='all_AL_CYA_voting')

# Table is within comment
al = div.find('div', class_='placeholder').next_sibling.next_sibling

new_soup = BeautifulSoup(al, 'lxml')
body = new_soup.find('tbody')
for tr in body.findAll('tr'):
    info = {}
    info['rank'] = tr.find('th', class_='right').text
    info['name'] = tr.find('a').text
    td = tr.find('td').next_sibling.next_sibling
    info['points_won'] = td.text
    info['votes_first'] = td.next_sibling.text
    info['share'] = td.next_sibling.next_sibling.text[:-1]
    
    finalists.append(info)