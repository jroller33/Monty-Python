print("This application calculates how many gallons of gas you'll need to drive a certain distance.\n")
number_miles = float(input("How many miles are you going to drive? \n"))
mpg = float(input("What's your average miles per gallon? \n"))
gallons = round(number_miles / mpg, 2)
gallon_cost = float(input("How much does a gallon of gas cost? \n"))
dollars = round(gallon_cost * gallons, 2)
print(f"On this trip you will use {gallons} gallons of gas.\n"
      f"It will cost ${dollars} ")

