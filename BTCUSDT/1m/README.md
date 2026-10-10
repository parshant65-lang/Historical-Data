# Binance BTC/USDT 1-Minute Historical Kline Dataset

- **Symbol:** BTCUSDT (Binance Spot)
- **Timeframe:** 1 Minute (1m)
- **Coverage:** August 17, 2017 to Present (October 10, 2026)
- **Total Candles:** 4,802,751
- **Data Source:** Official Binance Public Archives (data.binance.vision) + Binance REST API

## Column Specification:
1. `timestamp`: Kline open time in Unix milliseconds
2. `datetime_utc`: Human-readable UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
3. `open`: Open price (USDT)
4. `high`: High price (USDT)
5. `low`: Low price (USDT)
6. `close`: Close price (USDT)
7. `volume`: BTC volume traded in the 1-minute window
8. `quote_volume`: Total volume in USDT
9. `trade_count`: Total number of executed trades
10. `taker_buy_volume`: Taker buy volume (BTC)
11. `taker_buy_quote_volume`: Taker buy quote asset volume (USDT)

## Files:
- Year-wise clean `.csv` files (e.g., `BTCUSDT_1m_2024.csv`)
- Year-wise compressed `.csv.gz` files (e.g., `BTCUSDT_1m_2024.csv.gz`) — Perfect for GitHub without exceeding file size limits!
