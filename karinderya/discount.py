def apply_discount(discount_choice, ulam_price, gulay_price, subtotal):
    senior_discount = 0.0
    student_discount = 0.0
    pwd_discount = 0.0
    discount_label = "No discount"

    if discount_choice == "A":
        senior_discount = ulam_price * 0.10
        discount_label = "Senior"
    elif discount_choice == "B":
        student_discount = gulay_price * 0.05
        discount_label = "Student"
    elif discount_choice == "C":
        pwd_discount = subtotal * 0.07
        discount_label = "PWD"
    else:
        discount_label = "No discount"

    total_discount = senior_discount + student_discount + pwd_discount
    return total_discount, discount_label
