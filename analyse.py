# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:40:07 2019

@author: 92305
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime

df_polls=pd.read_csv(open('presidential_polls.csv'))
print(df_polls)
print(df_polls.keys())
df_polls.info()
print("\n\n\n\n\n\n\n")
print(df_polls.describe())
print("\n\n\n")
print(df_polls.head(10))

print(df_polls.isnull().sum())


tem_df_polls=df_polls[~df_polls['state'].isin(['U.S.'])]
tem_df_polls_trump=tem_df_polls.groupby('state')['adjpoll_trump'].sum()
tem_df_polls_clinton=tem_df_polls.groupby('state')['adjpoll_clinton'].sum()
pic_state=pd.DataFrame({"特朗普":tem_df_polls_trump,"希拉里":tem_df_polls_clinton})
pic_state.plot(kind='bar',title='地区投票人数分布')
from pylab import *
subplots_adjust(left=0.0,bottom=0.0,top=1,right=2,hspace=0.2,wspace=0.2)
plt.show()
print('trump:')
print(tem_df_polls_trump.sum())
print('clinton:')
print(tem_df_polls_clinton.sum())

tem_df_polls_trump=tem_df_polls.groupby('grade')['adjpoll_trump'].mean()
tem_df_polls_clinton=tem_df_polls.groupby('grade')['adjpoll_clinton'].mean()
pic_state=pd.DataFrame({"特朗普":tem_df_polls_trump,"希拉里":tem_df_polls_clinton})
pic_state.plot(kind='bar',title='grade投票平均')
from pylab import *
subplots_adjust(left=0.0,bottom=0.0,top=1,right=2,hspace=0.2,wspace=0.2)
plt.show()


weekly_nat_CvTvJ_raw_ts = nat_CvTvJ_raw_ts
weekly_nat_CvTvJ_raw_ts['createddate'] = weekly_nat_CvTvJ_raw_ts['createddate'].astype('datetime64[ns]')
weekly_nat_CvTvJ_raw_ts['date_minus_time'] = weekly_nat_CvTvJ_raw_ts["createddate"].apply( 
        lambda df : datetime.datetime(year=df.year, month=df.month, day=df.day)) 
weekly_nat_CvTvJ_raw_ts.set_index(
        weekly_nat_CvTvJ_raw_ts["date_minus_time"],inplace=True)


tem_df_polls_trump=tem_df_polls.groupby('createddate')['adjpoll_trump'].sum()
tem_df_polls_clinton=tem_df_polls.groupby('createddate')['adjpoll_clinton'].sum()
pic_state=pd.DataFrame({"特朗普":tem_df_polls_trump,"希拉里":tem_df_polls_clinton})
pic_state.plot(kind='bar',title='时间与投票人数分布')
from pylab import *
subplots_adjust(left=0.0,bottom=0.0,top=1,right=2,hspace=0.2,wspace=0.2)
plt.show()

df_polls['createddate']=df_polls['createddate'].astype('datetime64[ns]')
df_polls['startdate_set']=df_polls['startdate_set'].apply(lambda df:datetime.datetime(year=df.year,month=df.month,day=df.day))
df_polls.set_index(df_polls['startdate_set'],inplace=True)



tem2_df_polls=tem_df_polls.set_index('createddate')
temlist=[]
for i in range(len(tem_df_polls)):
    tem=time.strptime(tem2_df_polls.index[i],"%m/%d/%y")
    temlist.append(str(tem.tm_year)+"/"+str(tem.tm_mon))
tem_df_polls['month']=temlist

tem_df_polls_trump=tem_df_polls.groupby('month')['adjpoll_trump'].mean()
tem_df_polls_clinton=tem_df_polls.groupby('month')['adjpoll_clinton'].mean()
pic_state=pd.DataFrame({"特朗普":tem_df_polls_trump,"希拉里":tem_df_polls_clinton})
pic_state.plot(kind='bar',title='时间与投票人数分布')
from pylab import *
subplots_adjust(left=0.0,bottom=0.0,top=1,right=2,hspace=0.2,wspace=0.2)
plt.show()







