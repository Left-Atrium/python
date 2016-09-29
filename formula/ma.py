# coding=utf-8
import pandas as pd
import tushare as ts
def ma(stock_data,period=5):
	stock_data['ma' + str(period)] = pd.rolling_mean(stock_data['close'], period)
	# adjust 为True的时候，跟国内的软件不一样，为False的时候是一样的
	stock_data['ema' + str(period)] = pd.ewma(stock_data['close'], span=period,adjust=False)
	return stock_data
	


