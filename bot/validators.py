def validate_inputs(symbol, side, order_type, quantity, price=None):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must be a USDT pair (e.g., BTCUSDT).")
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if order_type == "LIMIT" and not price:
        raise ValueError("Price is required for LIMIT orders.")
