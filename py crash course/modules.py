# modules are used to organize functions, classes etc together in a structured way

# Python Standard Library is a group of modules included with Python

# random module is good for making random numbers or random choices

# https://pypi.org/

import random

print(random.randint(1, 10))

import datetime
now = datetime.datetime.now()
# datetime module provides datetime class, which provides 'now()' method

print(now)
print(now.year)

print(now + datetime.timedelta(days=28))