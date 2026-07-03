
incomes = []
while True:

    exit = input("want to exit press 'Y' press 'N' if not ")
    if exit == "Y":
    
        break
    elif exit == "N":
        print("next income asking.... ")
    else:
        break
    temp = int(input("Enter the income of your family  member: "))

    incomes.append(temp)


total_income = 0
total_expense = 0

for num in incomes:
    total_income += num

while True:
    expense = int(input("Enter your expense amount press -1 if want to exit the expense loop: "))

    if expense == -1:
        break

    total_expense += expense

    
total_gross_money = total_income - total_expense

print(f"your total income is {total_income}")
print(f"your total expense is {total_expense}")
print(f"your gross income is {total_gross_money}")
