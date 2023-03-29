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


class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):

#We're going to have Martin and Johanna exchange ALL their apples with one another.

    you, me = me, you
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.

    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



