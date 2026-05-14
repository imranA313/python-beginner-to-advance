class Person:
    company = "Deen"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Company Name: {self.company}"


p1 = Person("Imran", 29, "Male")
p2 = Person("Rehan", 24, "Male")
p3 = Person("Sahil", 22, "Male")

print(p1)
print(p2)
print(p3)
