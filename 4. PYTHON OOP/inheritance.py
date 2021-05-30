class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal): #Inherit parent class Mammal
    def bark(self):
        print('bhow bhow')


class Cat(Mammal):
    def walk(self):
        print('i am walking') # We can also overwrite method in parent class
    def bark(self):
        print('meaw meaw')


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.bark()

