#init module
#selection module
#calculate module
#service charge module
#selection discount module
#change module
#cash module
#use if and else in selesction of discount
#a. select your ulam: pork adobo-25 ,menudo-50, lechon-75, friedchicken-50 and sinigang na salmon-40. (1 ulam only). else no ulam selected
#b. select your gulay: mixed vegetables-125, pinakbet-150, chop suey-175. (1 gulay only) else no gulay selected
#c. amount of rice = 30 (default value, apply if a or b selected a ulam or gulay)
#d. the user can add 1 extra rice if the customer order gulay or ulam
#e. calculate and display the total amount ordered by the customer
#f. add and display the 7% service charge to the total amount of ordered by the customer.
#g. (a. 10% discount for senior for the amount of ulam). (b.5% discount for student for the amount of gulay). (c. 7% discount for PWD for the total amount ordered by the customer)
#h. calculate and display cash change)
#i. create a receipt and display all the inputted and calculation in the program.
import datetime
import random
import string
from . import change
from . import cash
from . import service_charge
from . import discount
from . import calculate
from . import selection


def main():
    print("=" * 60)
    print(f"{'KERI N\' DERYA':^60}")
    print("=" * 60)
    cashier_name = "SARTE MALAPAD"
    customer_name = input("Enter Customer Name : ")
    
    #  menu selections
    ulam_choice = selection.get_ulam_choice()
    ulam_name, ulam_price = selection.get_ulam_details(ulam_choice)

    gulay_choice = selection.get_gulay_choice()
    gulay_name, gulay_price = selection.get_gulay_details(gulay_choice)

    #  rice quantity
    if ulam_price > 0 or gulay_price > 0:
        extra_rice = selection.ask_extra_rice()
    else:
        extra_rice = False

    rice_qty = calculate.determine_rice_quantity(ulam_price, gulay_price, extra_rice)
    rice_price = 30.0
    rice_total = calculate.calculate_rice_total(rice_qty, rice_price)

    # Calculate subtotal
    subtotal = calculate.calculate_subtotal(ulam_price, gulay_price, rice_total)

    # Apply discount
    discount_choice = selection.get_discount_choice()
    total_discount, discount_label = discount.apply_discount(discount_choice, ulam_price, gulay_price, subtotal)
    amount_after_discount = subtotal - total_discount

    # Calculate service charge
    service_charge_amount = service_charge.calculate_service_charge(amount_after_discount)
    grand_total = amount_after_discount + service_charge_amount

    # Get cash and calculate change
    cash_amount = cash.get_cash_input()
    change_amount = change.calculate_change(grand_total, cash_amount)
    
    #datetime
    def get_current_datetime(format="%Y-%m-%d %H:%M"):
        now = datetime.datetime.now()
        return now.strftime(format)
    
    #ID generator
    def generate_id(length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters)for _ in range(length))

    # Display receipt
    print("\n" + "=" * 60)
    print(f"{'R E C E I P T':^60}")
    print("=" * 60)
    print(f"{'Keri N\' Derya Inc.':^60}")
    print(f"TR ID: {generate_id()}")
    print(f"Cashier : {cashier_name}")
    print(f"Customer: {customer_name}")
    print(f"Date/Time: {get_current_datetime(format='%Y-%m-%d %H:%M %p')}")
    print("-" * 60)
    print(f"{'ITEMS':<42}{'AMOUNT':>18}")
    print("-" * 60)
    print(f"{'Ulam  : ' + ulam_name:<42}{('₱ ' + format(ulam_price, '.2f')):>18}")
    print(f"{'Gulay : ' + gulay_name:<42}{('₱ ' + format(gulay_price, '.2f')):>18}")
    print(f"{'Rice  : ' + str(rice_qty) + ' x ₱' + format(rice_price, '.2f'):<42}{('₱ ' + format(rice_total, '.2f')):>18}")
    print("-" * 60)
    print(f"{'Subtotal':<42}{('₱ ' + format(subtotal, '.2f')):>18}")
    print(f"{'Discount Type':<42}{discount_label:<18}")
    print(f"{'Total Discount':<42}{('- ₱ ' + format(total_discount, '.2f')):>18}")
    print(f"{'Amount After Discount':<42}{('₱ ' + format(amount_after_discount, '.2f')):>18}")
    print(f"{'Service Charge (7%)':<42}{('+ ₱ ' + format(service_charge_amount, '.2f')):>18}")
    print("-" * 60)
    print(f"{'GRAND TOTAL':<42}{('₱ ' + format(grand_total, '.2f')):>18}")
    print(f"{'Cash Paid':<42}{('₱ ' + format(cash_amount, '.2f')):>18}")

    if change_amount is None:
        print(f"{'Status':<42}{'Insufficient cash!':>18}")
        print(f"{'Needed':<42}{('₱ ' + format(grand_total - cash_amount, '.3f')):>18}")
    else:
        print(f"{'Change':<42}{('₱ ' + format(change_amount, '.3f')):>18}")

    print("=" * 60)
    print(f"{'THANK YOU KAAYO!':^60}")


if __name__ == "__main__":
    main()




