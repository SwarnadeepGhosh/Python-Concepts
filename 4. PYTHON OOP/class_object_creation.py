# When calling the eat method, you only need to pass it
# one argument, even though there are two parameters:
# >>> spot = animals.Dog()
# >>> spot.eat("biscuit")
# Yummy!
# >>> spot.eat("chair")
# That's not food!

class Dog:
    def speak(self):
        print("Woof!")
    def eat(self,food):
        if food == 'biscuit':
            print('Yummy')
        else:
            print("That's not food!")
        


