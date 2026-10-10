# Historical Financial Market Data Archive

Universal repository for cleaned, standardized, and validated historical market data for Indian Equities (Top 400 NSE Companies), Indices, and Global Crypto assets.

## Repository Architecture & Hierarchy

All assets are strictly organized into dedicated sub-folders by **Asset/Ticker** and **Timeframe**:

```text
Historical-Data/
├── BTCUSDT/                # Bitcoin (Binance Spot) 2017 - 2026
│   └── 1m/                 # 1-Minute Historical Kline Data
│       ├── 2017/ ... 2026/
│
├── RELIANCE/               # Reliance Industries Ltd (NSE)
│   └── 1m/                 # 1-Minute Historical Kline Data
│       └── 2026/
│           ├── 09/ ➡️ RELIANCE_1m_2026-09-30.csv
│           └── 10/ ➡️ RELIANCE_1m_2026-10-01.csv, ...
│
├── TCS/                    # Tata Consultancy Services (NSE)
│   └── 1m/                 # 1-Minute Historical Kline Data
│
└── [Top 400 NSE Companies] # Complete Coverage of Top 400 Indian Companies (Nifty 500)
```

## Standard Data Schema (1-Minute Klines)
- `timestamp`: Kline open time in Unix milliseconds (UTC)
- `datetime_utc`: Human-readable UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
- `open`: Open price
- `high`: High price
- `low`: Low price
- `close`: Close price
- `volume`: Traded volume

## Asset Coverage:
- **Crypto:** `BTCUSDT` (1m full historical archive 2017–2026, 4.8M+ candles)
- **Equities:** **Top 400 Indian Listed Companies** on National Stock Exchange (NSE) organized strictly into date-wise daily 1-minute CSV files.
