"""
Anthony Quinn X00138635
Continuous Assessment 2
"""
print("*******************************\n*       MealsOnline         *\n*******************************"
      "\n1) Calculate Employee Pay\n2) Generate User Password\n3) Exit")
options = int(input("Please select menu option: "))

hoursThreshold = 48
tax_threshold = 500
tax_allowance = 300
tax = .20
bonusRate = 5

if options == 1:
    print("*******************************************\n"
          "*       Calculate Employee Pay         *\n"
          "*******************************************")
    employeeName = input("Employees Name: ")
    hoursWorked = int(input("Hours worked: "))
    hourlyRate = float(input("Hourly rate: "))
    pay = hourlyRate * hoursWorked
    if hoursWorked > hoursThreshold:
        bonus = (pay / 100) * bonusRate
        print(employeeName, "will receive a bonus for hours worked of €" + str(round(bonus,2)))
        if pay > tax_threshold:
            tax = (pay - tax_allowance) * tax
            print("Total taxed amount: €" + str(round(tax, 2)))
            total_pay = pay + bonus - tax
            print("Your net pay is €" + str(round(total_pay,2)))
        else:
            print("Your net pay is €" + str(round(pay,2)))
    elif pay > tax_threshold:
        tax = (pay - tax_allowance) * tax
        print("Total taxed amount: €" + str(round(tax, 2)))
        total_pay = pay - tax
        print("Your net pay is €" + str(round(total_pay,2)))

    else:
        print("No bonus added or tax!")
        print("Your net pay is €" + str(round(pay,2)))

elif options == 2:
    print("*******************************************\n"
          "*       Generate User Password         *\n"
          "*******************************************")
    password = input("Enter your social security number: ")

    newPassword = password[-3:]
    if len(password) % 2 == 0:
        newPassword2 = "116"
    else:
        newPassword2 = "226"
    finalPassword = str(newPassword) + newPassword2
    print("Your new password is: ", finalPassword.lower())

elif options == 3:
    print("The program has finished running!")
else:
    print("Error... invalid option chosen!")

