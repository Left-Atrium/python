# coding=utf-8
import talib
import pandas as pd
import tushare as ts
import numpy as np

talib.OBV?
'''
ma_list=[12, 26]
stock_data = ts.get_h_data('300525',start='2015-06-12').sort()
stock_data.to_excel('F:/2/1.xlsx',sheet_name='Sheet1')
for ma in ma_list:
	stock_data['ema' + str(ma)] = talib.EMA(stock_data['close'].values, timeperiod=ma)
stock_data.to_excel('F:/2/2.xlsx',sheet_name='Sheet1')

for ma in ma_list:
	stock_data['ema' + str(ma)] = pd.ewma(stock_data['close'], span=ma,adjust=False)
stock_data.to_excel('F:/2/3.xlsx',sheet_name='Sheet1')

stock_data = ts.get_h_data('300525',start='2015-06-12').sort()

stock_data['macd']=talib.MACDFIX(stock_data['close'].values, signalperiod=9)[0]
stock_data['macdsignal']=talib.MACDFIX(stock_data['close'].values, signalperiod=9)[1]
stock_data['macdhist']=talib.MACDFIX(stock_data['close'].values, signalperiod=9)[2]
stock_data.to_excel('F:/2/1.xlsx',sheet_name='Sheet1')
'''