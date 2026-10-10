# Historical Financial Market Data Archive

Universal repository for cleaned, standardized, and validated historical market data for Indian Equities, Indices, and Global Crypto assets.

## Repository Architecture & Hierarchy

All assets are strictly organized into dedicated sub-folders by **Asset/Ticker** and **Timeframe**:

```text
Historical-Data/
├── BTCUSDT/                # Bitcoin (Binance Spot)
│   └── 1m/                 # 1-Minute Historical Kline Data (2017 - Present)
│       ├── BTCUSDT_1m_2017.csv.gz
│       ├── BTCUSDT_1m_2018.csv.gz
│       └── ...
├── NIFTY50/                # Nifty 50 Index
│   └── 1d/                 # Daily Historical Bars
└── TCS/                    # Tata Consultancy Services
    └── 1d/                 # Daily Historical Bars
```

## Standard Data Schema (1-Minute Klines)
- `timestamp`: Kline open time in Unix milliseconds
- `datetime_utc`: UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
- `open`: Open price
- `high`: High price
- `low`: Low price
- `close`: Close price
- `volume`: Base asset volume
- `quote_volume`: Total quote volume
- `trade_count`: Total executed trades
- `taker_buy_volume`: Taker aggressor buy volume
- `taker_buy_quote_volume`: Taker aggressor buy volume in quote asset
