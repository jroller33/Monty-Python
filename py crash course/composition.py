# ALWAYS INITIALIZE MUTABLE ATTRIBUTES IN THE CONSTRUCTOR

# if two different classes are related, but there's no inheritance, this is called composition- where one class uses code from another class.

# in the example below, there's a Package class that rep's a software package.
# there's also a Repository class, which contains all the packages available
# there's no inheritance, but they're related bc Repository contains a dicitonary or list of Packages that are contained in the repo.

class Repository:
    def __init__(self):
        self.packages = {}  # initialize packages dictionary

# initialize the dictionary in the constructor so every instance of the Repository class has its own dictionary.

    def add_package(self, package):
        """
        takes Package object as a parameter, and then adds it to the dictionary, using the package name attribute as the key."""
        self.packages[package.name] = package

    def total_size(self):
        """
        computes the total size of all packages contained in our repository
        """
        result = 0

        for package in self.package.values():
            result += package.size
        return result

    # we’re making use of Package attributes within our Repository class 
    # and the values() method on our packages dictionary instance. 
    # Composition allows us to use objects as attributes, as well as access all their attributes and methods.
    

# --------------------------------------------------------

class Clothing:
    stock={ 'name': [],'material' :[], 'amount':[]}

    def __init__(self,name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)


    def Stock_by_Material(self, material):
        count=0
        n=0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count



class shirt(Clothing):
    material="Cotton"
class pants(Clothing):
    material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)