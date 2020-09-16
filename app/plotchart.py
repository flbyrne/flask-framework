from datetime import datetime,date,timedelta
from bokeh.plotting import figure, output_file, show
import pandas as pd
import requests

def get_EOD_data(symbol,sdate,edate):
    
    base_url='https://api.tiingo.com/tiingo/daily/'+symbol+'/prices?'
    api_key='9fa4df1e30e2fb224f1a625b7c43867b1880d05f'
    parameters={
        'token':api_key,
        'startDate':sdate,
        'endDate': edate,
    }
    response = requests.get(base_url, params=parameters)
    return response

def plotChart(ticker):
    from datetime import datetime,date,timedelta
    #set up data
    weeks=26
    startDate=str(date.today()-timedelta(weeks=weeks))
    endDate=str(date.today())
    ticker=ticker.upper()
    df_EOD=pd.DataFrame(get_EOD_data(ticker,startDate,endDate).json())
    df_EOD['date']=df_EOD['date'].apply(lambda x:x[:10]).apply(lambda x:datetime.strptime(x,'%Y-%m-%d'))
    date = df_EOD['date']
    close = df_EOD['adjClose']
    open_=df_EOD['adjOpen']
    high=df_EOD['adjHigh']
    low=df_EOD['adjLow']
    direction=df_EOD['adjClose']-df_EOD['adjOpen']
    colorchoice=["green" if x>=0 else "red" for x in direction ]
    openBarStart=[x-timedelta(hours=15) for x in date]
    closeBarEnd=[x+timedelta(hours=15) for x in date]
    #set output
    #output_file("plotchart.html")
    #Create plot
    figTitle='{} Weeks Open-High-Low-Close Bar Chart for {}'.format(weeks,ticker)
    p = figure(
        title=figTitle, x_axis_label='Date',plot_width=800
        , y_axis_label='Closing Price',x_axis_type='datetime')
    p.quad(top=high,bottom=low,left=date,right=date, color=colorchoice)
    p.quad(top=open_,bottom=open_,left=openBarStart,right=date, color=colorchoice)
    p.quad(top=close,bottom=close,left=date,right=closeBarEnd, color=colorchoice)
    return p

    
