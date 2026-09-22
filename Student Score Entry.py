number = (input("Pls enter your score: "))
if number.isdigit():
    number = int(number)
    if 0 <= number <= 100:
        print("Valid score")
    else:
        print("Invalid range! Must be between 0 and 100.")
else:
    print("Invalid input! Please use numbers.")