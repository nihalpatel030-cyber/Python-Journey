print("Currency Converter")
print("1. Dollar to Rupees")
print("2. Euro to Rupees")
print("3. Pound to Rupees")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    rupees = amount * 83
    print("Rupees =", rupees)

elif choice == 2:
    rupees = amount * 90
    print("Rupees =", rupees)

elif choice == 3:
    rupees = amount * 105
    print("Rupees =", rupees)

else:
    print("Invalid choice")
