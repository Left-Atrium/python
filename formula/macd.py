import talib
import numpy as np
import pandas as pd
import tushare as ts
import ma

def macd(stock,fastperiod=12, slowperiod=26, signalperiod=9):
	price = np.array(stock['close'].values)
	
	ewma12 = ma.ma(stock)['ema12']
	ewma26 = pd.ewma(price,span=slowperiod,adjust=False)
	dif = ewma12-ewma26
	dea = pd.ewma(dif,span=signalperiod,adjust=False)
	bar = (dif-dea)*2

	stock['diff'] = dif
	stock['dea'] = dea
	stock['macd'] = bar

	return stock

