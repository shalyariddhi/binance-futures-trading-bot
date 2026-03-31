import logging

logger = logging.getLogger("trading_bot")

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }
        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        logger.info(f"Sending Request: {params}")
        response = client.futures_create_order(**params)
        logger.info(f"Received Response: {response}")
        return response, True
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return str(e), False
