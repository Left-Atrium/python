from ma import ma
def ene(stock_data,N=11,M1=10.0,M2=9.0):
	stock_data['upper']=(1+M1/100.0) * ma(stock_data,N)['ma']
	stock_data['lower']=(1-M2/100.0) * ma(stock_data,N)['ma']
	stock_data['ene']=(stock_data['upper']+stock_data['lower'])/2
	return stock_data