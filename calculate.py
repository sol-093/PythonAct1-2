def calculate_rice_total(rice_qty, rice_price=30.0):
    return rice_qty * rice_price

def calculate_subtotal(ulam_price, gulay_price, rice_total):
    return ulam_price + gulay_price + rice_total

def determine_rice_quantity(ulam_price, gulay_price, extra_rice=False):
    if ulam_price > 0 or gulay_price > 0:
        rice_qty = 2 if extra_rice else 1
    else:
        rice_qty = 0
    return rice_qty
