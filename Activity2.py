#JAYDIEL RAIN S. SALVATIERRA
#8 ADELFA

print("Yo i AM your CLANKER bot :)")
print("I will CALCULATE addition AND subtraction ")
print("I will CALCULATE for YOU just GIVE me 2 NUMBERS")

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

sum = 0
diff = 0
def total_sum():
    global subtotal,n1,n2
    subtotal = n1 + n2
    print(f"Your sum is {subtotal}")

def total_difference():
    global difference,n1,n2
    difference = n1 - n2
    print(f"Your difference is {difference}")

total_sum()
total_difference()
