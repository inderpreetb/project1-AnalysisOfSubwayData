# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:56:41 2015

@author: baweja
"""

import pandas
import ggplot 
import datetime

filename = r'turnstile_data_master_with_weather.csv'
df = pandas.read_csv(filename)


def is_week_day(x):
     d = datetime.datetime.strptime(x, '%Y-%m-%d')
     return d.weekday()
    
df['WEEKDAYn'] =  df['DATEn'].apply(is_week_day)

weekday_group =  df.groupby('WEEKDAYn', axis=0).sum()

#print weekday_group['WEEKDAYn','ENTRIESn_hourly']
ggplot.ggplot(aes('WEEKDAYn','ENTRIESn_hourly'), data=weekday_group) + geom_histogram()