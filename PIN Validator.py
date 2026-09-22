pin = input("Enter the PIN: ")

if len(pin) ==6 and pin.isdigit():
    print("PIN Valid")
else:
    print("PIN Invalid: enter exactly 6 digits")