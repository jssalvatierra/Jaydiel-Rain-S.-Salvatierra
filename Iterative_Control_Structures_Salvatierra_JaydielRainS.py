#Jaydiel Rain S. Salvatierra
#8-Adelfa

nambar = int(input("Enter how many item yu buying: "))

meeting_target = 0
below_target = 0
total_sales = 0
for i in range(int(nambar)):
    monei = int(input(f"Enter item sales for item{i+1}: "))
    total_sales += monei
    if monei >= 500:
        meeting_target += 1
    else:
        below_target += 1

def calculate_avg(total_sales,monei):
    avg = total_sales/monei
    return avg

def sales_report(meeting_target,below_target,avg):
    print("==============CANTEEN SALES REPORT ==============")
    print(f"Average Sales: PHP{avg:.2f} | Meeting target: {meeting_target} | Below target: {below_target}")

avg = calculate_avg(total_sales, nambar)
sales_report(meeting_target,below_target,avg)
