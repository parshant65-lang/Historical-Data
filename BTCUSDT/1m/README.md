# Binance BTC/USDT 1-Minute Historical Kline Dataset

- **Symbol:** `BTCUSDT` (Binance Spot)
- **Timeframe:** 1 Minute (`1m`)
- **Coverage:** August 17, 2017 to Present (October 10, 2026)
- **Format:** Clean, uncompressed `.csv` files organized strictly by Year and Month folders.
- **Data Source:** Official Binance Public Data Archives + Binance REST API

## Directory Hierarchy:
```text
BTCUSDT/1m/
├── 2017/
│   ├── 08/
│   │   └── BTCUSDT_1m_2017-08.csv
│   └── ...
├── 2024/
│   ├── 01/
│   │   └── BTCUSDT_1m_2024-01.csv
│   └── ...
└── 2026/
    ├── 10/
    │   └── BTCUSDT_1m_2026-10.csv
```

## Column Specification:
1. `timestamp`: Kline open time in Unix milliseconds (e.g. `1704067200000`)
2. `datetime_utc`: Human-readable UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
3. `open`: Open price (USDT)
4. `high`: High price (USDT)
5. `low`: Low price (USDT)
6. `close`: Close price (USDT)
7. `volume`: BTC volume traded during the 1-minute candle
8. `quote_volume`: Total volume in USDT
9. `trade_count`: Total number of executed trades
10. `taker_buy_volume`: Taker aggressor buy volume (BTC)
11. `taker_buy_quote_volume`: Taker aggressor buy volume (USDT)
