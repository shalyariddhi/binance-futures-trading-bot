import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key or not api_secret:
            raise ValueError("Missing API Key/Secret in .env")
        
        # Connect to Testnet
        self.client = Client(api_key, api_secret, testnet=True)
        # Force the Futures Testnet URL
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'
