import talib
import numpy as np
import pandas as pd
import tushare as ts
import ma

def macd(stock='600000',fastperiod=12, slowperiod=26, signalperiod=9):
	data = ts.get_h_data(stock, start='2016-07-01').sort()

	price = np.array(data['close'].values)
	
	ewma12 = ma.ma(stock)['ema12']
	ewma26 = pd.ewma(price,span=slowperiod,adjust=False)
	dif = ewma12-ewma26
	dea = pd.ewma(dif,span=signalperiod,adjust=False)
	bar = (dif-dea)*2

	data['diff'] = dif
	data['dea'] = dea
	data['macd'] = bar

	return data

