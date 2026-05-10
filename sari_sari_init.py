# sari_sari_init.py
# Sari-sari store main module

import datetime
import random
import string
import sari_sari_selection as selection
import sari_sari_calculate as calculate
import sari_sari_discount as discount
import sari_sari_cash as cash
import sari_sari_change as change

def main():
    print("=" * 60)
    print(f"{'SARI-SARI STORE':^60}")
    print("=" * 60)
    cashier_name = "SARTE MALAPAD"
    print("\n{:^60}".format("CUSTOMER DETAILS"))
    print("-" * 60)
    customer_name = input("{:>25} ".format("Customer Name:"))

    # Get details for 3 products
    print("\n{:^60}".format("PRODUCT ENTRY"))
    print("-" * 60)
    products = []
    for i in range(1, 4):
        print(f"| {'Product ' + str(i):<56}|")
        print("|" + " " * 58 + "|")
        code = int(input("|   {:<20}: ".format("Product Code")))
        name = input("|   {:<20}: ".format("Product Name"))
        price = float(input("|   {:<20}: ₱ ".format(f"Price for {name}")))
        qty = int(input("|   {:<20}: ".format(f"Quantity for {name}")))
        print("|" + " " * 58 + "|")
        print("-" * 60)
        products.append((code, name, price, qty))

    # Calculate subtotal
    subtotal = sum(price * qty for _, _, price, qty in products)
    print(f"\nSubtotal: ₱{subtotal:.2f}")

    # Discount selection
    print("\n{:^60}".format("DISCOUNT SELECTION"))
    print("-" * 60)
    print(f"|""A. Senior (10% discount on total)")
    print(f"|""B. Student (5% discount on total)")
    print(f"|""C. PWD (7% discount on total)")
    print(f"|""D. (No discount)")
    discount_choice = input("Enter choice: ").upper()
    total_discount, discount_label = discount.apply_discount(discount_choice, subtotal)
    print(f"Discount ({discount_label}): -₱{total_discount:.2f}")

    # Grand total
    grand_total = subtotal - total_discount
    print(f"Total: ₱{grand_total:.2f}")

    # Payment
    cash_given = cash.get_cash(grand_total)
    change_amt = change.get_change(cash_given, grand_total)
    print(f"Change: ₱{change_amt:.2f}")

    # formatted receipt (karinderya style)
    def generate_id():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def get_current_datetime(format='%Y-%m-%d %H:%M %p'):
        return datetime.datetime.now().strftime(format)

    print("\n" + "=" * 60)
    print(f"{'R E C E I P T':^60}")
    print("=" * 60)
    print(f"{'Sari-Sari Store Inc.':^60}")
    print(f"TR ID: {generate_id()}")
    print(f"Cashier : {cashier_name}")
    print(f"Customer: {customer_name}")
    print(f"Date/Time: {get_current_datetime()}")
    print("-" * 60)
    print(f"{'ITEMS':<42}{'AMOUNT':>18}")
    print("-" * 60)
    for _, name, price, qty in products:
        item_line = f"{name} x{qty}"
        print(f"{item_line:<42}{('₱ ' + format(price * qty, '.2f')):>18}")
    print("-" * 60)
    print(f"{'Subtotal':<42}{('₱ ' + format(subtotal, '.2f')):>18}")
    print(f"{'Discount Type':<42}{discount_label:<18}")
    print(f"{'Total Discount':<42}{('- ₱ ' + format(total_discount, '.2f')):>18}")
    print(f"{'Amount After Discount':<42}{('₱ ' + format(grand_total, '.2f')):>18}")
    print("-" * 60)
    print(f"{'GRAND TOTAL':<42}{('₱ ' + format(grand_total, '.2f')):>18}")
    print(f"{'Cash Paid':<42}{('₱ ' + format(cash_given, '.2f')):>18}")
    if change_amt < 0:
        print(f"{'Status':<42}{'Insufficient cash!':>18}")
        print(f"{'Needed':<42}{('₱ ' + format(grand_total - cash_given, '.2f')):>18}")
    else:
        print(f"{'Change':<42}{('₱ ' + format(change_amt, '.2f')):>18}")
    print("=" * 60)
    print(f"{'THANK YOU KAAYO!':^60}")

if __name__ == "__main__":
    main()
