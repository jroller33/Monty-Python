# A while loop executes the body of the loop while a specified condition remains True. They are commonly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

# while specified condition is True:
    # body of loop



# This while loop prints the multiples of 5 between 1 and 50. 
def example1():
    multiplier = 1
    result = multiplier*5
    while result <= 50:
        print(result)
        multiplier += 1
        result = multiplier*5
print("Done")


# -------------------------------------------------------

# *** Common Errors in while Loops: ***

# If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:

# Failure to initialize variables. Make sure all the variables used in the loop’s condition are initialized before the loop.

# Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by adding end criteria to the condition part of the while loop.


# ----------------------------------------------------------------


# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):
 
  # To include the "given_number" variable as a "factor", initialize
  # the "factor" variable with the value 1 (if the "factor" variable
  # were to start at 2, the "given_number" itself would be excluded). 
    factor = 1
    count = 1
 
    if given_number == 0:
    # If True, the return value will be 0 factors. 
        return 0
 
  # The while loop will run while the "factor" is still less than
  # the "given_number" variable.
    while factor < given_number:
    # This "if" block checks if the "given_number" can be divided by the "factor" variable without leaving a remainder. The modulo operator % is used to test for a remainder.
        if given_number % factor == 0:
      # If True, then the "factor" variable is added to the count of
      # the "given_number"’s integer factors.
            count += 1
    # When exiting the if block, increment the "factor" variable by 1
    # to divide the "given_number" variable by a new "factor" value
    # inside the while loop.
        factor += 1
 
  # When the interpreter exits either the while loop or the top if
  # block, it will return the value of the "count" variable.
    return count
 
# print(count_factors(0)) # Count value will be 0
# print(count_factors(3)) # Should count 2 factors (1x3)
# print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
# print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6). 


# --------------------------------------------------------------------


# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20. 
 
# The function accepts a "given_number" variable through its 
# parameters.
def addition_table(given_number):
 
    # The "iterated_number" and "my_sum" variables are initialized with
    # the value of 1. Although the "my_sum" variable does not need any
    # specific initial value, it still must be assigned a data type
    # before being used in the while loop. By initializing "my_sum"
    # with any integer, the data type will be set to int.
    iterated_number = 1
    my_sum = 1
 
    # The while loop will run while it is True that the   
    # "iterated_number" is less than or equal to 5.
    while iterated_number <= 5:
 
        # The "my_sum" variable is assigned the value of the
        # "given_number" plus the "iterated_number" variables.
        my_sum = given_number + iterated_number
 
        # Test to see if the "my_sum" variable is greater than 20.
        if my_sum > 20:
            # If True, then use the break keyword to exit the loop. 
            break
        # If False, the Python interpreter will move to the next line 
        # in the while loop after the if-statement has ended.  
 
        # The print function will output the "given_number" plus
        # the "iterated_number" equals "my_sum".
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
 
        # Increment the "iterated_number" before the while loop starts
        # over again to print a new "my_sum" value.
        iterated_number += 1
 
 
# addition_table(5)
# addition_table(17)
# addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None


# ----------------------------------------------------------------------