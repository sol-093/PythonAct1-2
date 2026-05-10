# Discount for sari-sari store (user chooses discount for total)
def apply_discount(discount_choice, total):
    discount = 0.0
    discount_label = "No discount"
    if discount_choice == "A":
        discount = total * 0.10
        discount_label = "Senior"
    elif discount_choice == "B":
        discount = total * 0.05
        discount_label = "Student"
    elif discount_choice == "C":
        discount = total * 0.07
        discount_label = "PWD"
    else:
        discount_label = "No discount"
    return discount, discount_label
