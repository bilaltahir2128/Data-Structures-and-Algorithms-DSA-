months=['jan','feb','mar','apr','may']
expenses=[2200,2350,2600,2130,2190]

print("Money spent extra in feb as compared to jan : ",expenses[1]-expenses[0])

print("Total expenses in the first quater of the year : ",expenses[0]+expenses[1]+expenses[2])

spent=False
for i in range(len(expenses)):
    if expenses[i]==2000:
        print(f"You spent {expenses[i]} in the month {months[i]}")
        spent=True

if spent == False:
    print("You don't spent 2000 in any month.")
    

expenses.append(1980)
months.append("jun")

print("Expense list just updated which are as below: ")
for i in range(len(months)):
    print(f"{months[i] } : { expenses[i]}")


expenses[3]=expenses[3]-200
print("Expense list after updating arirl is as below: ")
for i in range(len(months)):
    print(f"{months[i] } : { expenses[i]}")
