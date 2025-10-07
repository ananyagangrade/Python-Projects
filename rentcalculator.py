rent = int(input("Enter your house rent: "))
food = int(input("Enter Total amount offood ordered: "))
electricity = int(input("Enter your total electricity spend: "))
charge_per_unit = int(input("Enter charge per unit: "))
persons = int(input("Enter the number of persons living: "))

total_bill = electricity * charge_per_unit
total = (rent + food + total_bill) // persons
print(f'Total amount you have to pay is: {total}')