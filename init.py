from karinderya import init
from sarisari import sari_sari_init 


while True:
    print("=" * 40)
    print("MAIN SYSTEM")
    print("=" * 40)
    print("1. Karinderya System")
    print("2. Sari-Sari Store System")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        init.main()
    elif choice == "2":
        sari_sari_init.main()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
