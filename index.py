### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that
 # will print the value of all the properties/attributes of the Movie class
#
# * In your ```main``` function create *two* instances of the Product class
# * Assign a value of your choosing for each property/attribute
# * Print all properties to the console.
#
# Remember, this is the basic model of a Python file with a class
# ```
# class Movie:
# 	def __init__(self):
# 	# Class constructor code and property handling
#
# 	OTHER PROPERTIES AND METHODS HERE
#
# def main():
# 	# Create class instance(s) and perform other activities in/from this function
# }
#
# main()
# ```
# This line starts your class definition with 'class' and the class name you assigned
class Movie:
    def __init__(self, movieName, rating, yearReleased):
        # attribute/property
        self.movieName = movieName
        self.rating = rating
        self.yearReleased = yearReleased
    def printMovie(self):
        print(f"{self.movieName}, {self.rating}, {self.yearReleased}")
    # Function inside of a class. A method. 
    def __str__(self):
       my_instance_str = f'movieName = {self.movieName}\n' \
                         f'rating = {self.rating}\n' \
                         f'yearReleased = {self.yearReleased}'
       return my_instance_str
# calls the functions from the class above
def main():
    newMovie = Movie("Attack", "9/10", "2016")
    newMovie2 = Movie("Run out", "7/10", 2017)
    print(newMovie)
    # newMovie2.printMovie()

main()

# ### Problem 2:
# Create a class Product that represents a product sold online.
#
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# * In your ```main``` function create *two* instances of the Product class
# * Assign a value of your choosing for each property/attribute
# * Print all properties to the console.

# This line starts your class definition with 'class' and the class name you assigned
class Product:
# Initialize/set up a new object/instance/'class copy' with the parameters provided. Similar to a constructor. You must include self in the parameters.
    def __init__(self, price, quantity, name):
# Assign a new property to the object/instance/'class copy' from the parameter. Bringing the properties to LIFE (useability)!
        self.price = price
        self.quantity = quantity
        self.name = name
    def __str__(self):
       my_product = f'price = {self.price}\n' \
                    f'quantity = {self.quantity}\n' \
                    f'name = {self.name}'
       return my_product

def main2():
    newProduct = Product("$50", "20", "MagicWand")
    print(newProduct)

main2()
