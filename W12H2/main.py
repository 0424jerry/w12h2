import pandas as pd
import numpy as np
import talib 
from datetime import datetime
import mplfinance as mpf

SData = pd.read_csv('2330.csv',index_col = 'Date')
SData.index = pd.DatetimeIndex(SData.index)  
SData = SData.loc['2020/01/02' : '2020/12/01']

K,D = talib.STOCH(SData['High'].values,SData['Low'].values,SData['Close'].values)

ad = [mpf.make_addplot(K,color = 'lightblue',panel = 1),
      mpf.make_addplot(D,color = 'orange',panel = 1),
     ]

mpf.plot(SData, type = 'candle', mav = [10,30], volume = True , style = 'charles',figscale = 2, figratio =(4,3),main_panel = 0,
        volume_panel = 2, addplot = ad,panel_ratios=(4,1.5,5))