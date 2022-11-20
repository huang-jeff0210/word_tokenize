import pandas as pd
import requests
import bs4
import warnings
warnings.filterwarnings("ignore")

def get_stock_info(stock_type,market):
    url = f'https://isin.twse.com.tw/isin/C_public.jsp?strMode={stock_type}'
    df = pd.read_html(url,encoding='big5hkscs')
    df[0].columns = df[0].iloc[0]
    ESM_df = df[0].iloc[2:]
    ESM_df['股票代碼'], ESM_df['股票名稱'] = ESM_df['有價證券代號及名稱'].str.split('　', 1).str
    # ESM_df = ESM_df.drop(['有價證券代號及名稱','備註'],axis=1)
    ESM_df = ESM_df[['股票代碼','股票名稱','市場別','產業別','上市日','國際證券辨識號碼(ISIN Code)','CFICode']]
    ESM_df['爬取類型'] = f'{market}'
    return ESM_df

stock_info = pd.DataFrame()
stock_info = stock_info.append(get_stock_info(2,'上市'))
stock_info = stock_info.append(get_stock_info(4,'上櫃'))
stock_info = stock_info.append(get_stock_info(5,'興櫃'))
stock_info = stock_info.reset_index(drop=True)
stock_info.to_csv('a.csv',encoding='utf-8-sig')



