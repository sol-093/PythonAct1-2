def get_ulam_choice():
    print("\n" + "=" * 60)
    print(f"{'ULAM MENU (SELECT 1)':^60}")
    print("-" * 60)
    print(f"{'A. Pork Adobo':<42}{('₱ ' + format(25, '.2f')):>18}")
    print(f"{'B. Menudo':<42}{('₱ ' + format(50, '.2f')):>18}")
    print(f"{'C. Lechon':<42}{('₱ ' + format(75, '.2f')):>18}")
    print(f"{'D. Fried Chicken':<42}{('₱ ' + format(50, '.2f')):>18}")
    print(f"{'E. Sinigang na Salmon':<42}{('₱ ' + format(40, '.2f')):>18}")
    print("=" * 60)
    return input("Enter choice (A-E): ").upper()

def get_gulay_choice():
    print("\n" + "=" * 60)
    print(f"{'GULAY MENU (SELECT 1)':^60}")
    print("-" * 60)
    print(f"{'A. Mixed Vegetables':<42}{('₱ ' + format(125, '.2f')):>18}")
    print(f"{'B. Pinakbet':<42}{('₱ ' + format(150, '.2f')):>18}")
    print(f"{'C. Chop Suey':<42}{('₱ ' + format(175, '.2f')):>18}")
    print("=" * 60)
    return input("Enter choice (A-C): ").upper()

def get_discount_choice():
    print("\n" + "=" * 60)
    print(f"{'DISCOUNT MENU':^60}")
    print("-" * 60)
    print("A. Senior  (10% discount on ulam amount)")
    print("B. Student (5% discount on gulay amount)")
    print("C. PWD     (7% discount on total amount)")
    print("D. No discount")
    print("=" * 60)
    return input("Enter choice (A-D): ").upper()

def ask_extra_rice():
    print("\n" + "-" * 60)
    return input("Add 1 extra rice? (Y/N): ").upper() == "Y"


def get_ulam_details(choice):
    if choice == "A":
        return "Pork Adobo", 25.0
    elif choice == "B":
        return "Menudo", 50.0
    elif choice == "C":
        return "Lechon", 75.0
    elif choice == "D":
        return "Fried Chicken", 50.0
    elif choice == "E":
        return "Sinigang na Salmon", 40.0
    else:
        return "No ulam selected", 0.0

def get_gulay_details(choice):
    if choice == "A":
        return "Mixed Vegetables", 125.0
    elif choice == "B":
        return "Pinakbet", 150.0
    elif choice == "C":
        return "Chop Suey", 175.0
    else:
        return "No gulay selected", 0.0
