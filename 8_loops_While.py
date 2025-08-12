# print(1)
# print(2)
# print(3)
# print(4)

################################################################################################################
number = 1    #This line initializes a variable called number and assigns it the starting value of 1.
while number <= 5:  #This is the condition for the loop. The code inside the loop will continue to run as long as the value of number is less than or equal to 5.
    print (number) # Inside the loop, this line prints the current value of the number variable.
    number = number + 1  # This is the crucial part that prevents an infinite loop. It increments the value of number by 1 after each iteration.


######################## Here's how the code executes step-by-step:########################
###########################################################################################
# The code uses a while loop to repeatedly execute a block of code as long as a certain condition is true.

# number is initialized to 1.
# The loop checks if 1 <= 5. It's true, so it prints 1.
    # number becomes 1 + 1, which is 2.
# The loop checks if 2 <= 5. It's true, so it prints 2.
    # number becomes 2 + 1, which is 3.
# The loop checks if 3 <= 5. It's true, so it prints 3.
    # number becomes 3 + 1, which is 4.
# The loop checks if 4 <= 5. It's true, so it prints 4.
    # number becomes 4 + 1, which is 5.
# The loop checks if 5 <= 5. It's true, so it prints 5.
    # number becomes 5 + 1, which is 6.
# The loop checks if 6 <= 5. It's false, so the loop terminates.