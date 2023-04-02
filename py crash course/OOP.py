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

class Piglet:
	name = "piglet"		# default value for 'name' attribute
	def speak(self):
		print(f"oink oink I'm {self.name}")


hamlet = Piglet()
hamlet.name = "Piggy"	# new value for 'name' attribute on the 'hamlet' instance of 'Piglet'
hamlet.speak()		# calls .speak() method, using the new 'name' value