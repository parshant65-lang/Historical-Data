# Global 1-Minute Historical Market Data Archive (4,000 Unique Equities & Crypto)

An institutional-grade, open-source archive of cleaned, standardized, and validated **1-minute intraday historical kline data** covering **Bitcoin (`BTCUSDT`)** and **4,000 Unique Publicly Traded Companies** (Indian NSE equities and US NYSE/NASDAQ equities).

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
├── crypto/                                 # 24/7 Digital Asset Pairs
│   └── BTCUSDT/
│       └── 1m/                             # August 2017 to Present (4.8M+ candles)
│           ├── 2017/ ... 2026/
│               └── 10/
│                   └── BTCUSDT_1m_2026-10.csv
│
├── india/                                  # Indian Equities (NSE) - 1,418 Companies
│   ├── 0-9/                                # Numerically prefixed symbols
│   │   ├── 20MICRONS/1m/...
│   │   └── 3MINDIA/1m/...
│   ├── A/                                  # Tickers starting with A
│   │   ├── A2ZINFRA/1m/...
│   │   └── ADANIENT/1m/...
│   ├── H/
│   │   ├── HCLTECH/1m/...
│   │   ├── HDFCBANK/1m/...
│   │   └── HINDUNILVR/1m/...
│   ├── R/
│   │   └── RELIANCE/
│   │       └── 1m/
│   │           ├── README.md
│   │           └── 2026/10/
│   │               ├── RELIANCE_1m_2026-10-01.csv
│   │               └── RELIANCE_1m_2026-10-09.csv
│   └── Z/
│       └── ZOMATO/1m/...
│
└── usa/                                    # US Equities (NYSE / NASDAQ) - 2,582 Companies
    ├── A/
    │   ├── A/1m/...
    │   ├── AAPL/
    │   │   └── 1m/
    │   │       ├── README.md
    │   │       └── 2026/10/
    │   │           └── AAPL_1m_2026-10-09.csv
    │   └── AMZN/1m/...
    ├── M/
    │   └── MSFT/1m/...
    ├── N/
    │   └── NVDA/1m/...
    ├── T/
    │   └── TSLA/1m/...
    └── Z/
        └── ZTS/1m/...
```

---

## 📑 Data Schema & Specifications

Every single CSV file adheres to a uniform column schema with zero missing values or headers mismatch:

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | `int64` | Candle open time in Unix milliseconds (UTC) | `1791552600000` |
| `datetime_utc` | `string` | Standard ISO human-readable UTC timestamp | `2026-10-09 13:30:00` |
| `open` | `float64` | Opening price of the 1-minute candle | `331.79` |
| `high` | `float64` | Highest price reached during the 1-minute window | `333.35` |
| `low` | `float64` | Lowest price reached during the 1-minute window | `331.28` |
| `close` | `float64` | Closing price of the 1-minute candle | `332.74` |
| `volume` | `float64` | Cumulative volume traded in the 1-minute candle | `3416928` |

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

# 3. Load Bitcoin Spot Kline (e.g., October 2026)
url_crypto = "https://raw.githubusercontent.com/parshant65-lang/Historical-Data/main/crypto/BTCUSDT/1m/2026/10/BTCUSDT_1m_2026-10.csv"
df_btc = pd.read_csv(url_crypto)
print(df_btc.head())
```

---

## 🔄 Future Ingestion & Continuous Data Preservation

### 1. Rolling Ingestion Pipeline
To keep this repository perpetually updated as time moves forward:
* Every Friday post-market (or weekend), an automated ingestion script pulls the latest 7-day rolling window for all constituents.
* New trading days are sliced by date and saved into their respective `<country>/<bucket>/<symbol>/1m/<YYYY>/<MM>/<symbol>_1m_<DATE>.csv` paths.

### 2. Zero-Duplicate Guarantee (Timestamp Deduplication)
When overlapping dates or partial sessions are ingested:
```python
# Automated deduplication logic:
combined_df = pd.concat([existing_df, new_df], ignore_index=True)
combined_df.drop_duplicates(subset=["timestamp"], keep="last", inplace=True)
combined_df.sort_values(by="timestamp", inplace=True)
```
Existing completed historical days are never overwritten or corrupted; only newly closed candles are appended.

---

## 🌐 Coverage Overview (4,000 Unique Assets)

1. **Crypto:** `BTCUSDT` — Full historical archive (Aug 2017 to Present, 4.8M+ 1-minute candles).
2. **Indian Equities (NSE):** 1,418 active companies across Large, Mid, and Small Cap segments in `india/<0-9|A-Z>/<SYMBOL>/`.
3. **Global / US Equities:** 2,582 S&P 500, NASDAQ, and NYSE companies in `usa/<A-Z>/<SYMBOL>/`.
