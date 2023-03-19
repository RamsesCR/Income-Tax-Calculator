grossIncome = float(input("Enter the gross income: "))

dependentsNumber = int(input("Enter the number of dependents: "))

depdeducTax = grossIncome - 10000 - (3000 * dependentsNumber)

incomeTax = depdeducTax * 0.2

print("The income tax is $" + str(incomeTax))