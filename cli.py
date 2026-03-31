import argparse
import logging
from bot.client import BinanceClient
from bot.orders import place_order

logging.basicConfig(filename='trading_bot.log', level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    args = parser.parse_args()

    client = BinanceClient().client
    res, success = place_order(client, args.symbol, args.side, args.type, args.quantity, args.price)
    
    if success:
        print(f"✅ SUCCESS: OrderID {res['orderId']} | Status: {res['status']}")
    else:
        print(f"❌ FAILED: {res}")

if __name__ == "__main__":
    main()
