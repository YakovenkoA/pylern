"""class Cat:
    name = None
    age = None
    isHappy = None
   
    def set_data(self, name, age, isHappy):
       self.name = name
       self.age
       self.isHappy
    
cat1 = Cat()
cat1.name = "Barsik"
cat1.age = 3
cat1.isHappy = True

cat2 = Cat()
cat2.name = "Murzik"
cat2.age = 2
cat2.isHappy = False

print(cat1.name)
print(cat2.name)
"""

class Cat:
    name = None
    age = None
    isHappy = None
   
    def set_data(self, name, age, isHappy):
       self.name = name
       self.age
       self.isHappy
    
cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Murzik", 2, False)

print(cat1.name)
print(cat2.name)







"""

class Cat:
    def __init__(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age  # Fixed the missing assignment
        self.isHappy = isHappy

# Using the set_data method
cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Murzik", 2, False)

# Alternatively, using the __init__ method
cat3 = Cat("Whiskers", 1, True)

print(cat1.name)
print(cat2.name)
print(cat3.name) """