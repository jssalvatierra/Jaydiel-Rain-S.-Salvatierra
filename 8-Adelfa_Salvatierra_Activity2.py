#JAYDIEL RAIN S. SALVATIERRA
#8 ADELFA

print("Yo i AM your CLANKER bot :)")
print("I will CALCULATE addition AND subtraction ")
print("I will CALCULATE for YOU just GIVE me 2 NUMBERS")

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

subtotal = 0
difference = 0
product = 0
quotient = 0

def total_sum(n1,n2):
    global subtotal
    subtotal = n1 + n2
    print(f"Your sum is {subtotal}")

def total_difference(n1,n2):
    global difference
    difference = n1 - n2
    print(f"Your difference is {difference}")

def total_product(n1,n2):
    global product
    product = n1 * n2
    print(f"Your product is {product}")

def total_quotient(n1,n2):
    global quotient
    quotient = n1 / n2
    print(f"Your quotient is {quotient}")

total_sum(n1,n2)
total_difference(n1,n2)
total_product(n1,n2)
total_quotient(n1,n2)
