import talib
import numpy as np
import pandas as pd
def macd(stock_data,fastperiod=12, slowperiod=26, signalperiod=9):
	macd, signal, hist = talib.MACD(stock_data[u'close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
	stock_data['macd_x']=(macd-signal)*2
	return stock_data