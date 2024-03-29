# Python Object-Oriented Programming Notes

# print(help(int)) # lists all attributes and methods for 'int' class (each datatype is basically a class)

# lists, strings, ints, dictionaries, etc are all objects in python

class Orange:    # defines a new class named 'Orange'
    pass

class Apples:
    color = ""
    flavor = ""

granny_smith = Apples()
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

# print(f"Roses are {rose.color},\nViolets are {violet.color}.\n{pun}\n")


# -------------------------------------------------------------------------------------------

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
# We're going to have Martin and Johanna exchange ALL their apples with #one another.
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.

    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))




# -------------------------------------------------------------------------------------------


class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation

	highest_city = city1.elevation
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.elevation >= highest_city:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation >= highest_city:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation >= highest_city:
		return_city = city3

	#Format the return string
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""


# -------------------------------------------------------------------------------------

class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return f"This piece of furniture is made of {piece.color} {piece.material}"

# print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

# -----------------------------------------------------------------------------



# INSTANCE METHODS


class Piglet:
	name = "piglet"		# default value for 'name' instance variable

	years = 0

	def pig_years(self):	# 'self' represents the instance the method is being executed on
		print(self.years * 18)

	def speak(self):
		print(f"oink oink I'm {self.name}")


hamlet = Piglet()
hamlet.name = "Piggy"	# new value for 'name' attribute on the 'hamlet' instance of 'Piglet'
# hamlet.speak()		# calls .speak() method, using the new 'name' value

petunia = Piglet()
petunia.name = "Petunia"	# 'petunia' instance of Piglet has "Petunia" as the value of 'name'
# petunia.speak()

piggy = Piglet()
piggy.years = 2
# piggy.pig_years()	# prints "36"

# -----------------------------------------------------------------------------

# CONSTRUCTORS AND OTHER SPECIAL METHODS

# ALWAYS INITIALIZE MUTABLE ATTRIBUTES IN THE CONSTRUCTOR


# any method with two underscores is a special method, like '__init__'

class Apple:
	"""Represents an apple and its description"""
	def __init__(self, name, color, flavor):		# constructor
		self.name = name
		self.color = color		
		self.flavor = flavor	# sets the values as the values of the current instance

# __str__ is a special method that tells Python what to say if print() is called on the instance of the class, rather than the default value which is the object's position in computer's memory
	
	def __str__(self):	
		"""Outputs description of the apple when print() is used on the instance of the object"""
		return f"A {self.name} apple is {self.color} and {self.flavor}."

red_delicious = Apple("red delicious","red", "sweet")

print(red_delicious) 
# this will print whatever is in __str__ method. Normally this would print the object's position in memory

# ------------------------------------------------------------------------------------

# DOCSTRINGS

# docstring controls what will be shown if 'help()' is used
def to_seconds(hours, minutes, seconds):
	"""Returns the amount of seconds in the given hours, minutes and seconds."""
	return hours*3600+minutes*60+seconds

help(to_seconds)


