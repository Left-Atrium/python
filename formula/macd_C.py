import talib
import numpy as np
import pandas as pd
import ma

def macd(stock_data,fastperiod=12, slowperiod=26, signalperiod=9):

	price = np.array(stock_data['close'].values)
	
	ewma12 = ma.ma(stock_data,12)['ema12']
	ewma26 = ma.ma(stock_data,26)['ema26']
	dif = ewma12-ewma26
	dea = pd.ewma(dif,span=signalperiod,adjust=False)
	bar = (dif-dea)*2

	stock_data['diff'] = dif
	stock_data['dea'] = dea
	stock_data['macd'] = bar

	return stock_data

