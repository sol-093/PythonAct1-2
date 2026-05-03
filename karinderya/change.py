def calculate_change(total, cash):
    if cash < total:
        return None
    else:
        return cash - total
