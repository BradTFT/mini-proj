
#! i still dont understand classes
class Person:
    def __init__(self, name, lastname, age, country, city):
        self.name =name
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.name} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Bradley', 'Caiola','14', 'USA',  'Richmond')
print(p.name)
print(p)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
print(p.person_info())