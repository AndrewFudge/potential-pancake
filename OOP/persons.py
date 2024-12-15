class Person:
    description = 'general'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'I am {self.name} and {self.age} years old')

    def eat(self, food):
        print(f'{self.name} eats {food}')
    
    def action(self):
        print(f'{self.name} jumps')
    
class Baby(Person):
    description = 'baby' # overwrites the main

    def speak(self):
        print('bla ba boo boo')
    
    def nap(self):
        print(f'{self.name} sleeps')


person = Person('Jogn', 20)
person.speak
person.eat('cheese')
person.action