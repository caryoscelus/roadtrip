"""renpy
init python:
"""

class Person:
    def __init__(self, name, display, luggage, money):
        self.name = name
        self.display = display
        self.luggage = luggage
        self.money = money

class Self(Person):
    def __init__(self):
        super().__init__('You', 'anonymous.png', [MyLuggage(self)], 0)

class Luggage:
    def __init__(self, display, owner):
        self.display = display
        self.owner = owner

class MyLuggage(Luggage):
    def __init__(self, owner):
        super().__init__('luggage.png', owner)
