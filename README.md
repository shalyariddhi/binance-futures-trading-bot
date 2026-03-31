# Binance Futures Trading Bot

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file with `BINANCE_API_KEY` and `BINANCE_API_SECRET`.

## Assumptions
- Uses the **Binance Futures Testnet** (`testnet.binancefuture.com`).
- The bot assumes the user has sufficient USDT balance in their Testnet account.
- Designed for **USDT-M** (USDT-Margined) futures only.

## Running Examples
- **Market Order:** `python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001`
- **Limit Order:** `python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000`

## Implementation Notes & Assumptions
- **Notional Value:** During testing, the Binance Futures Testnet enforced a minimum notional value of 100 USDT. Orders with quantity 0.001 BTC were rejected; increasing quantity to 0.002 BTC (~140 USDT) resolved this.
- **Environment:** API credentials are managed via a `.env` file for security (not included in this repo).
- **Error Handling:** The bot handles API errors (like code -4164) and logs the full JSON response for auditability.
