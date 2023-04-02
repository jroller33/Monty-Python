# create an Elevator class, with bottom floor, top floor and current floor attributes
# create methods for this class that give it the functionality of a real elevator.

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        
    def __str__(self):
        """Outputs the current floor with a message."""
        return f"Current floor: {self.current}"
    
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top: 
            self.current = self.current+1
            return self.current
        
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current = self.current-1
            return self.current
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        return self.current

elevator = Elevator(-1, 10, 0)	# creates an instance of Elevator, with bottom, top, and current floor values

elevator.up() 
elevator.current #should output 1

elevator.down() 
elevator.current #should output 0

elevator.go_to(10) 
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1


elevator.go_to(5)
print(elevator)		# using __str__ method, prints current floor the elevator is on.


# ----------------------------------------------------------------------------------

class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

class Snake(Animal):
    category = "reptile"


class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) # how many zoo animal types in the reptile category, should output '2'