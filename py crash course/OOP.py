# Python Object-Oriented Programming Notes

# print(help(int)) # lists all attributes and methods for 'int' class (each datatype is basically a class)

# lists, strings, ints, dictionaries, etc are all objects in python

class Orange:    # defines a new class named 'Orange'
    pass

class Apple:
    color = ""
    flavor = ""

granny_smith = Apple()
granny_smith.color = "green"
granny_smith.flavor = "tart"

# print(f"A Granny-Smith Apple is {granny_smith.color} and {granny_smith.flavor}")

# print(granny_smith.color.upper())   # you can use other methods on attributes too

class Flower:
    color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

pun = "Dwight killed Sprinkles, and buried him too."

print(f"Roses are {rose.color},\nViolets are {violet.color}.\n{pun}\n")

