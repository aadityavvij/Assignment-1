# 2. Write a python program to compute a person's income tax. Assume following
#    tax laws:
#     • All taxpayers are charged a flat tax rate of 20%.
#     • All taxpayers are allowed a $10,000 standard deduction.
#     • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
#     • Gross income must be entered to the nearest penny.
#    Gross Income and the number of dependents must be asked from the user.

#    Hint:
#    Taxable income = GrossIncome - Standard deduction - (Dependent deduction
#    * No. of dependents)
#    Tax = Taxable Income * Tax Rate

gi = int(input("Enter the gross income in $\n"))

nd = int(input("Enter the number of dependents\n"))

ti = gi - 10000 - (3000*nd)

if(ti>=0):
    tax = (ti*20)/100
    print("Your income tax is", tax)

else:
    print("Your income tax is 0")