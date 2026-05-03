def get_product_choice():
    code = int(input("Enter product code: "))
    name = input("Enter product name: ")
    price = float(input(f"Enter price for {name}: "))
    qty = int(input(f"Enter quantity for {name}: "))
    return code, name, price, qty
