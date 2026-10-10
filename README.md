# Global 1-Minute Historical Market Data Archive (4,000 Assets & Crypto)

An institutional-grade, open-source archive of cleaned, standardized, and validated **1-minute intraday historical kline data** covering **Bitcoin (`BTCUSDT`)** and **4,000 Unique Global & Indian Listed Companies** (NSE Large/Mid/Small-Caps and US S&P 500 / NASDAQ leaders).

---

## 🌟 The Core Problem & Purpose of this Repository

### The 7-Day Intraday Limitation
In global financial markets, public APIs (such as Yahoo Finance, Google Finance, and exchange feeds) impose a strict **rolling 7-day cutoff** on 1-minute (`1m`) historical data. Once 7 calendar days pass, granular 1-minute candles are **permanently removed** from free tiers and locked behind expensive institutional paywalls.

### The Archival Solution
This repository serves as a permanent, decentralized, version-controlled warehouse. By downloading, cleaning, and appending high-frequency intraday market data on a continuous schedule, **no minute of historical auction data is ever lost**.

---

## 🏛️ Directory Architecture & Hierarchy

To ensure clean navigation and compatibility across operating systems, every asset follows a strict, standardized Year/Month/Date partitioned tree:

```text
Historical-Data/
├── BTCUSDT/                        # Bitcoin Spot (Binance)
│   └── 1m/                         # 1-Minute Klines (August 2017 to Present)
│       ├── 2017/ ... 2026/
│           └── 10/
│               └── BTCUSDT_1m_2026-10.csv
│
├── RELIANCE/                       # Reliance Industries Ltd (NSE)
│   └── 1m/
│       ├── README.md
│       └── 2026/
│           ├── 09/
│           │   └── RELIANCE_1m_2026-09-30.csv
│           └── 10/
│               ├── RELIANCE_1m_2026-10-01.csv
│               ├── RELIANCE_1m_2026-10-05.csv
│               └── RELIANCE_1m_2026-10-09.csv
│
├── AAPL/                           # Apple Inc. (NASDAQ / US)
│   └── 1m/
│       ├── README.md
│       └── 2026/
│           └── 10/
│               ├── AAPL_1m_2026-10-02.csv
│               └── ...
│
├── NVDA/                           # NVIDIA Corp. (NASDAQ / US)
└── [4,000 Unique Companies]        # Complete Global Coverage
```

---

## 📑 Data Schema & Specifications

Every single CSV file adheres to a uniform column schema with zero missing values or headers mismatch:

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | `int64` | Candle open time in Unix milliseconds (UTC) | `1728551700000` |
| `datetime_utc` | `string` | Standard ISO human-readable UTC timestamp | `2026-10-09 09:15:00` |
| `open` | `float64` | Opening price of the 1-minute candle | `2745.50` |
| `high` | `float64` | Highest price reached during the 1-minute window | `2751.20` |
| `low` | `float64` | Lowest price reached during the 1-minute window | `2744.10` |
| `close` | `float64` | Closing price of the 1-minute candle | `2749.80` |
| `volume` | `float64` | Cumulative volume traded in the 1-minute candle | `14520` |

---

## 🔄 Future Ingestion & Continuous Data Preservation

### 1. Rolling Weekly Ingestion Pipeline
To keep this repository perpetually updated as time moves forward:
* Every Friday post-market (or weekend), an automated sync script pulls the latest 7-day rolling window for all constituents.
* New trading days are sliced by date and saved into their respective `YYYY/MM/<SYMBOL>_1m_<DATE>.csv` paths.

### 2. Zero-Duplicate Guarantee (Timestamp Deduplication)
When overlapping dates or partial sessions are ingested:
```python
# Automated deduplication logic:
combined_df = pd.concat([existing_df, new_df], ignore_index=True)
combined_df.drop_duplicates(subset=["timestamp"], keep="last", inplace=True)
combined_df.sort_values(by="timestamp", inplace=True)
```
Existing completed historical days are never overwritten or corrupted; only newly closed candles are committed.

---

## ⚡ How to Consume This Data in Python (1-Line Load)

You do **not** need to clone the entire repository to analyze a stock. You can stream any file directly from GitHub's raw CDN into Pandas:

```python
import pandas as pd

# Example: Read Reliance 1-Minute data for October 09, 2026
url = "https://raw.githubusercontent.com/parshant65-lang/Historical-Data/main/RELIANCE/1m/2026/10/RELIANCE_1m_2026-10-09.csv"
df = pd.read_csv(url)

print(df.head())
```

---

## 🌐 Coverage Overview (4,000 Unique Assets)

1. **Crypto:** `BTCUSDT` — Full historical archive (Aug 2017 to Present, 4.8M+ 1-minute candles).
2. **Indian Equities (NSE):** All active listed companies (~2,400 companies across Large, Mid, and Small Cap segments).
3. **Global / US Equities:** S&P 500 & NASDAQ technology and growth leaders (Apple, Microsoft, Nvidia, Alphabet, Amazon, Meta, Tesla, etc.).
