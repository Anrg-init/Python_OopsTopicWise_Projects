class Dog:
    species = "Canis familiaris"    # class variable

    def __init__(self, name, age):
        self.name = name            # object variable
        self.age = age              # object variable

    # INSTANCE — works with object data (self)
    def show(self):
        print(f"name: {self.name}, age: {self.age}")

    # CLASS — works with class data (cls)
    @classmethod
    def get_species(cls):
        print(f"species: {cls.species}")

    # STATIC — works with nothing, just a helper
    @staticmethod
    def is_adult(age):
        print(f"is adult: {age >= 2}")


d1 = Dog("Bruno", 3)
d2 = Dog("Max", 1)

# instance — needs an object
d1.show()               # name: Bruno, age: 3
d2.show()               # name: Max, age: 1

# classmethod — no object needed, called on class
Dog.get_species()       # species: Canis familiaris

# staticmethod — no object needed, just pass data in
Dog.is_adult(3)         # is adult: True
Dog.is_adult(1)         # is adult: False
```

That's it. Three methods, three different things they have access to:
```
show()         → self  → knows Bruno, knows 3
get_species()  → cls   → knows Dog.species
is_adult()     → nothing → just calculates whatever you pass in