# coding=utf-8
import pandas as pd
import tushare as ts
def ma(STOCK,ma_list=[12, 26]):
	stock_data = ts.get_h_data(STOCK,start='2015-06-12').sort()
	for ma in ma_list:
	    stock_data['ma' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)
	# adjust 为True的时候，跟国内的软件不一样，为False的时候是一样的
	for ma in ma_list:
	    stock_data['ema' + str(ma)] = pd.ewma(stock_data['close'], span=ma,adjust=False)

	return stock_data
	


