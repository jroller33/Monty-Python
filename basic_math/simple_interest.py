#! /usr/bin/env python3

print("\tThis Find Simple Interest application will ask user to specify\n"
      "the amount of a loan and an interest rate, and then calculate and\n"
      "display the simple interest for the given loan at the specified\n"
      "interest for a specified number of years.")
print()

choice = 'y'

while choice == 'y':

      principal = int(input(" Please enter the amount of your loan:\t"))

      rate = float(input(" Please enter your interest rate:\t"))

      time = int(input(" Please enter the number of years:\t"))

      interest = principal * (rate / 100) * time

      if interest > 30 and interest < 50:
            choice = input("Do you want to do another calculation? (y for yes)")
            if choice == 'y':
                  continue
            else:
                  break

      elif interest > 50:
            print("Interest is more than $50.")
            break

      else:
            print("Interest is not more than $30.")

print()
print(" The interest on a loan of $" + str(principal) + " at " + str(rate) + "% interest rate\n"
      " for " + str(time) + " year is $" + str(interest) + ".", sep='')
