payment_methood = ["cash" "gcash" "card"]
payment = input("Enter your payment method: ").lower()
if payment in payment_methood:
    print("Payment method is valid")
else:
    print("Payment method is not valid")