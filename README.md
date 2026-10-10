# Global 1-Minute Historical Market Data Archive (4,000 Equities & 11 Major Cryptos)

An institutional-grade, open-source archive of cleaned, standardized, and validated **1-minute intraday historical kline data** covering **11 Major Cryptocurrencies (`BTC`, `ETH`, `BNB`, `SOL`, `XRP`, `ADA`, `DOGE`, `AVAX`, `DOT`, `LINK`, `NEAR`)** and **4,000 Unique Publicly Traded Companies** (Indian NSE equities and US NYSE/NASDAQ equities).

---

## 🌟 The Core Problem & Purpose of this Repository

### The 7-Day Intraday Limitation
In global financial markets, free public APIs (such as Yahoo Finance, Google Finance, and exchange feeds) impose a strict **rolling 7-day cutoff** on 1-minute (`1m`) historical data. Once 7 calendar days pass, granular 1-minute candles are **permanently lost** from free tiers and locked behind expensive institutional paywalls.

### The Archival Solution
This repository serves as a permanent, decentralized, version-controlled warehouse. By downloading, cleaning, and appending high-frequency intraday market data on a continuous schedule, **no minute of historical auction data is ever lost**.

---

## 🏛️ Directory Architecture & Sharding Hierarchy

To prevent GitHub Web UI directory truncation (which limits views to 1,000 items) and optimize file system navigation, assets are organized by **Asset Class / Country** and **Alphabetical Shards (`0-9`, `A-Z`)**:

```text
Historical-Data/
├── crypto/                                 # 24/7 Digital Asset Pairs (11 Major Cryptos, 44M+ candles)
│   ├── BTCUSDT/1m/...                      # August 2017 to Present (111 months)
│   ├── ETHUSDT/1m/...                      # August 2017 to Present (111 months)
│   ├── BNBUSDT/1m/...                      # November 2017 to Present (108 months)
│   ├── SOLUSDT/1m/...                      # August 2020 to Present (75 months)
│   ├── XRPUSDT/1m/...                      # May 2018 to Present (102 months)
│   ├── ADAUSDT/1m/...                      # April 2018 to Present (103 months)
│   ├── DOGEUSDT/1m/...                     # July 2019 to Present (88 months)
│   ├── AVAXUSDT/1m/...                     # September 2020 to Present (74 months)
│   ├── DOTUSDT/1m/...                      # August 2020 to Present (75 months)
│   ├── LINKUSDT/1m/...                     # January 2019 to Present (94 months)
│   └── NEARUSDT/1m/...                     # October 2020 to Present (73 months)
│
├── india/                                  # Indian Equities (NSE) - 1,418 Companies
│   ├── 0-9/                                # Numerically prefixed symbols (20MICRONS, 3MINDIA, etc.)
│   ├── A/                                  # Tickers starting with A (A2ZINFRA, ADANIENT, etc.)
│   ├── H/                                  # (HCLTECH, HDFCBANK, HINDUNILVR, etc.)
│   ├── R/                                  # (RELIANCE, etc.)
│   └── Z/                                  # (ZOMATO, etc.)
│
└── usa/                                    # US Equities (NYSE / NASDAQ) - 2,582 Companies
    ├── A/                                  # (AAPL, AMZN, etc.)
    ├── M/                                  # (MSFT, etc.)
    ├── N/                                  # (NVDA, etc.)
    ├── T/                                    # (TSLA, etc.)
    └── Z/                                  # (ZTS, etc.)
```

---

## 📑 Data Schema & Specifications

### 1. Equities Schema (India & USA):
| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | `int64` | Candle open time in Unix milliseconds (UTC) | `1791552600000` |
| `datetime_utc` | `string` | Standard ISO human-readable UTC timestamp | `2026-10-09 13:30:00` |
| `open` | `float64` | Opening price of the 1-minute candle | `331.79` |
| `high` | `float64` | Highest price reached during the 1-minute window | `333.35` |
| `low` | `float64` | Lowest price reached during the 1-minute window | `331.28` |
| `close` | `float64` | Closing price of the 1-minute candle | `332.74` |
| `volume` | `float64` | Cumulative volume traded in the 1-minute candle | `3416928` |

### 2. Crypto Schema (Binance Spot Klines):
`timestamp, datetime_utc, open, high, low, close, volume, quote_volume, trade_count, taker_buy_volume, taker_buy_quote_volume`

---

## ⚡ How to Stream Any Asset in Python (1-Line Load)

You do **not** need to clone the entire repository to run backtests. You can stream any file directly from GitHub's raw CDN into Pandas:

```python
import pandas as pd

# 1. Load an Indian Stock (e.g., Reliance on October 09, 2026)
url_india = "https://raw.githubusercontent.com/parshant65-lang/Historical-Data/main/india/R/RELIANCE/1m/2026/10/RELIANCE_1m_2026-10-09.csv"
df_reliance = pd.read_csv(url_india)
print(df_reliance.head())

# 2. Load a US Stock (e.g., Apple on October 09, 2026)
url_usa = "https://raw.githubusercontent.com/parshant65-lang/Historical-Data/main/usa/A/AAPL/1m/2026/10/AAPL_1m_2026-10-09.csv"
df_aapl = pd.read_csv(url_usa)
print(df_aapl.head())

# 3. Load Crypto Spot Kline (e.g., Ethereum for September 2026)
url_crypto = "https://raw.githubusercontent.com/parshant65-lang/Historical-Data/main/crypto/ETHUSDT/1m/2026/09/ETHUSDT_1m_2026-09.csv"
df_eth = pd.read_csv(url_crypto)
print(df_eth.head())
```

---

## 🔄 Future Ingestion & Continuous Data Preservation

### 1. Rolling Ingestion Pipeline
To keep this repository perpetually updated as time moves forward:
* Every Friday post-market (or weekend), an automated ingestion script pulls the latest 7-day rolling window for equities and weekly klines for crypto.
* New trading sessions are saved directly into their respective `<country>/<bucket>/<symbol>/1m/<YYYY>/<MM>/` paths.

### 2. Zero-Duplicate Guarantee (Timestamp Deduplication)
When overlapping dates or partial sessions are ingested:
```python
# Automated deduplication logic:
combined_df = pd.concat([existing_df, new_df], ignore_index=True)
combined_df.drop_duplicates(subset=["timestamp"], keep="last", inplace=True)
combined_df.sort_values(by="timestamp", inplace=True)
```

---

## 🌐 Coverage Overview

1. **Crypto (11 Assets, 44M+ candles):** `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `ADAUSDT`, `DOGEUSDT`, `AVAXUSDT`, `DOTUSDT`, `LINKUSDT`, `NEARUSDT`.
2. **Indian Equities (NSE - 1,418 Assets):** Complete listed universe across Large, Mid, and Small Cap segments.
3. **US Equities (NYSE / NASDAQ - 2,582 Assets):** S&P 500, NASDAQ-100, and growth leaders.
