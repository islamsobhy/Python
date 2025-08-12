#If condition 

money= int(input("How much money do you have?"))
#why i have used the function "int()", because The > operator can't be used to compare a string ('str') with an integer ('int').
if money > 500:
    print("You are rich")
elif money > 100:
    print("You are comfortable")
else:
    print("Do you need money?")

#First, check if money > 500. If this is true, it prints "You are rich" and stops.
#If the first condition is false, it then checks if money > 100. If this is true, it prints "You are comfortable" and stops.
#If both of the above conditions are false, it defaults to the else block and prints "Do you need money?".