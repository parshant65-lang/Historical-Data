# Historical Financial Market Data Archive

Universal repository for cleaned, standardized, and validated historical market data for Indian Equities (Nifty 100), Indices, and Global Crypto assets.

## Repository Architecture & Hierarchy

All assets are strictly organized into dedicated sub-folders by **Asset/Ticker** and **Timeframe**:

```text
Historical-Data/
├── BTCUSDT/                # Bitcoin (Binance Spot)
│   └── 1m/                 # 1-Minute Historical Kline Data (2017 - 2026)
│       ├── 2017/ ... 2026/
│
├── RELIANCE/               # Reliance Industries Ltd (NSE)
│   └── 1m/                 # 1-Minute Historical Kline Data
│       └── 2026/
│           ├── 09/ ➡️ RELIANCE_1m_2026-09.csv
│           └── 10/ ➡️ RELIANCE_1m_2026-10.csv
│
├── TCS/                    # Tata Consultancy Services (NSE)
│   └── 1m/                 # 1-Minute Historical Kline Data
│       └── 2026/
│           ├── 09/ ➡️ TCS_1m_2026-09.csv
│           └── 10/ ➡️ TCS_1m_2026-10.csv
│
└── [Top 100 NSE Companies] # Complete Nifty 100 Constituent Coverage
```

## Standard Data Schema (1-Minute Klines)
- `timestamp`: Kline open time in Unix milliseconds (UTC)
- `datetime_utc`: Human-readable UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
- `open`: Open price
- `high`: High price
- `low`: Low price
- `close`: Close price
- `volume`: Traded volume

## Top 100 Indian Companies Covered (Nifty 100 Index):
ABB, ADANIENSOL, ADANIENT, ADANIGREEN, ADANIPORTS, ADANIPOWER, AMBUJACEM, APOLLOHOSP, ASIANPAINT, DMART, AXISBANK, BSE, BAJAJ-AUTO, BAJFINANCE, BAJAJFINSV, BAJAJHLDNG, BANKBARODA, BEL, BPCL, BHARTIARTL, BOSCHLTD, BRITANNIA, CGPOWER, CANBK, CHOLAFIN, CIPLA, COALINDIA, CUMMINSIND, DLF, DIVISLAB, DRREDDY, EICHERMOT, ETERNAL, GAIL, GODREJCP, GRASIM, HCLTECH, HDFCAMC, HDFCBANK, HDFCLIFE, HINDALCO, HAL, HINDUNILVR, HINDZINC, POWERINDIA, HYUNDAI, ICICIBANK, ITC, IOC, IRFC, INFY, INDIGO, JSWSTEEL, JINDALSTEL, JIOFIN, KOTAKBANK, LTM, LT, M&M, MARUTI, MAXHEALTH, MAZDOCK, MUTHOOTFIN, NTPC, NESTLEIND, ONGC, PIDILITIND, POLYCAB, PFC, POWERGRID, PNB, RELIANCE, SBILIFE, MOTHERSON, SHRIRAMFIN, ENRIN, SIEMENS, SOLARINDS, SBIN, SUNPHARMA, TVSMOTOR, TATACAP, TCS, TATACONSUM, TMCV, TMPV, TATAPOWER, TATASTEEL, TECHM, TITAN, TORNTPHARM, TRENT, ULTRACEMCO, UNIONBANK, VBL, VAML, VEDL, IDEA, WIPRO, ZYDUSLIFE.
