import yfinance as yf
import pandas as pd
from datetime import datetime

print("开始下载美股板块和概念ETF数据...")

start = "2021-01-01"
end = "2026-04-20"   # 可自行修改

# 板块 ETF
sectors = ['XLC','XLY','XLP','XLE','XLF','XLV','XLI','XLB','XLRE','XLK','XLU']
# 概念 ETF（可继续添加）
concepts = ['SMH','QQQ','ARKK','ICLN','TAN','LIT','NLR','BOTZ','GRID','SHLD']

tickers = sectors + concepts

# 批量下载
data = yf.download(tickers, start=start, end=end, interval='1d', auto_adjust=True, group_by='ticker')

# 分别保存每个ticker的独立CSV（最方便2.9口袋支点导入）
for ticker in tickers:
    try:
        df = data[ticker].copy() if len(tickers) > 1 else data
        df.to_csv(f'{ticker}_2021_2025.csv')
        print(f'✅ {ticker} 下载完成！共 {len(df)} 条记录')
    except:
        print(f'❌ {ticker} 下载失败')

print("\n全部下载完成！可以在左侧 Files 里看到所有CSV文件")
