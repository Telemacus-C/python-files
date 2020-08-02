bankBalance = 40.5
withdrawAmount = float(input("you have 40.5$ in your account, how much do you want to withdraw? "))
#print(withdrawAmount)

if(withdrawAmount <= (0.5 * bankBalance)):
    print("You can withdraw this amount of money")
elif(withdrawAmount <= bankBalance)
    print("you need verification before withdrawing this much")
else:
    print("You cannot withdraw this amount")
