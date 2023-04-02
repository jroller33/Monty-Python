class Fruit:
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor

class Apple(Fruit): # Apple class inherits everything from Fruit
    pass

class Grape(Fruit): # Grape class inherits everything from Fruit
    pass

some_fruit = Apple("granny_smith", "green", "tart")

other_fruit = Grape("white", "green", "sweet")

# ---------------------------------------------------------------------------------

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.sound} I'm {self.name}! {self.sound}")

class Piglet(Animal):
    sound = "Oink"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "mooo"

cow1 = Cow("Big Bertha")
cow1.speak()


# ----------------------------------------------------------------------------

class Clothing:
    material = ""

    def __init__(self,name):
        self.name = name

    def checkmaterial(self):
        print(f"This {self.name} is made of {self.material}")
			
class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()



