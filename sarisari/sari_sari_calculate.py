def calculate_total(price_qty_list):
    total = 0.0
    for price, qty in price_qty_list:
        total += price * qty
    return total
