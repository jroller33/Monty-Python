# for Loops vs. while Loops
# for loops and while loops share several characteristics. Both loops can be used with a variety of data types, both can be nested, and both can be used with the keywords break and continue. However, there are important differences between the two types of loops: 

# while loops are used when a segment of code needs to execute repeatedly while a condition is true

# for loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence

# Syntax 
# The syntax of a for loop with the in keyword:

# for variable in sequence:
#     body of loop

def example1():
    # This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to include 6. The incremental value
# for the loop is 2 (number+2).

    for number in range(1,6+1,2):
        print(number*3) # 3, 9, 15

# Common pitfalls when using the range() function:
# Forgetting that the upper limit of a range() isn’t included in the range.

# Iterating over non-sequences. For example, strings are iterable letter by letter, but not word by word. 

def forrange():
    # This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print() 
# function will output the resulting value of "number" squared.

    for number in range(2,8):
        print(number**2) # The loop should print 4, 9, 16, 25, 36, 49



# Nested for Loops 

# for x in sequence:
    # start of the outer loop body
#   for y in sequence:
        # start of the inner loop body

        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body


# ---------------------------------------------------------------------


def nested_for_loops_example():
    # This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.


    for x in range(2):
        print("This is the outer loop iteration number " + str(x))
        for y in range(3+1):
            print("Inner loop iteration number " + str(y))
        print("Exit inner loop")


# --------------------------------------------------------------------


def for_loop_nested_if():
    # This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

    for x in range(7):
        if x % 2 == 0:
            print(x) # The loop should print 0, 2, 4, 6

