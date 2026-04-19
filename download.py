import yfinance as yf
import pandas as pd

# 时间范围：2021 - 2025 年（完全匹配你的回测）
START = "2021-01-01"
END = "2025-12-31"

# 标普 500 板块指数（最适合口袋支点板块强度）
SECTORS = [
    "S5INFT", "S5HLTH", "S5COND", "S5CONS", "S5ENRS",
    "S5FINL", "S5INDU", "S5MATR", "S5UTIL", "S5REAL", "S5TELS"
]

# 热门概念指数（口袋支点核心回测）
CONCEPTS = [
    "SOXX", "DJUSAI", "DJUSCL", "DJUSSC", "DJUSBT",
    "SMH", "QQQ", "ARKK", "TAN", "LIT", "BOTZ", "ICLN"
]

TICKERS = SECTORS + CONCEPTS

print("开始下载美股指数/ETF 2021-2025 数据...\n")

# 下载
data = yf.download(
    TICKERS,
    start=START,
    end=END,
    interval="1d",
    auto_adjust=True,
    group_by="ticker"
)

# 导出独立 CSV（2.9口袋支点直接导入）
for ticker in TICKERS:
    try:
        df = data[ticker][["Open", "High", "Low", "Close", "Volume"]].copy()
        df.to_csv(f"{ticker}_2021_2025.csv")
        print(f"✅ {ticker} 完成")
    except:
        print(f"❌ {ticker} 失败")

print("\n🎉 全部下载完成！所有 CSV 已生成")
