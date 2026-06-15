from functools import wraps

print('Hello World!')
'--------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name}, and I am {self.age} years old"
#
#
# # Ниже расположен код для проверок, его не нужно удалять
# bro = Person('Nikolay', 34)
# assert bro.age == 34
# assert bro.name == 'Nikolay'
# assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'
#
# sister = Person('Elena', 21)
# assert sister.age == 21
# assert sister.name == 'Elena'
# assert sister.greet() == 'Hello, my name is Elena, and I am 21 years old'
# print('Good')
'-------------------------------------------------------'
# class Vehicle():
#
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# bmw = Vehicle(240, 18)
# audi = Vehicle(123, 43)
# print(bmw.__dict__)
# print(audi.__dict__)
'-------------------------------------------------------'
# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance_to_origin(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             return (self.x ** 2 + self.y ** 2) ** 0.5
#         return None
#
#     def get_distance(self, obj):
#         if isinstance(obj, Point):
#             if hasattr(self, 'x') and hasattr(self, 'y') and hasattr(obj, 'x') and hasattr(obj, 'y'):
#                 return ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5
#             else:
#                 print('Координаты не заданы')
#                 return None
#         else:
#             print('Передана не точка')
#             return None
#
#
#     def display(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             print(f"Point({self.x}, {self.y})")
#         else:
#             print('Координаты не заданы')
#
# p1 = Point()
# p1.set_coordinates(1, 2)
# print(p1.get_distance(100))
# print(p1.get_distance([1, 2, 3]))
# print(p1.get_distance(Point()))

# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# p1.display()
# p2.display()
# print(p1.get_distance(p2))
# print(p2.get_distance(p1))
#
# p1 = Point()
# p2 = Point()
# print(p1.get_distance(p2))
# p1.set_coordinates(1, 2)
# print(p1.get_distance(p2))
# p2.set_coordinates(4, 6)
# print(p1.get_distance(p2))
'-------------------------------------------------------'
# class Point():
#
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance_to_origin(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             return (self.x**2 + self.y**2)**0.5
#         else:
#             return None
#
#     def display(self):
#         if not hasattr(self, 'x') or not hasattr(self, 'y'):
#             print('Координаты не заданы')
#         else:
#             print(f'Point({self.x}, {self.y})')
#
# p3 = Point()
# p3.display()
# print(p3.get_distance_to_origin())
# p3.x = 4
# p3.display()
# print(p3.get_distance_to_origin())
# p3.y = 3
# p3.display()
# print(p3.get_distance_to_origin())
#
# p1 = Point()
# p1.set_coordinates(6, 8)
# p1.display()
# print(p1.get_distance_to_origin())
#
# p2 = Point()
# p2.display()
# p2.set_coordinates(3, 4)
# p2.display()
# print(p2.get_distance_to_origin())
'-------------------------------------------------------'
# class Counter():
#
#     def start_from(self, start = 0):
#         self.start = start
#
#     def increment(self):
#         self.start += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.start}')
#
#     def reset(self):
#         self.start = 0
#
# num_1 = Counter()
# num_1.start_from(89)
# num_1.increment()
# num_1.increment()
# num_1.increment()
# num_1.display()
# num_1.reset()
# num_1.display()
'-------------------------------------------------------'
# class Lion():
#
#     def roar(self):
#         print('Rrrrrrr!!!')
#
# simba = Lion()
# simba.roar()
'-------------------------------------------------------'
# class Config:
#     pass
#
# def create_instance(n: int) -> Config:
#     ek = Config()
#     for i in range(1, n+1):
#         setattr(ek, f'attribute{i}', f'value{i}')
#     return ek
#
# config_4 = create_instance(4)
# config_3 = create_instance(3)
# config_2 = create_instance(2)
# print(config_4.__dict__)
# print(config_3.__dict__)
# print(config_2.__dict__)
'-------------------------------------------------------'
# class SuperHero:
#     pass
#
# batman, superman = SuperHero(), SuperHero()
#
# batman.can_fly = True
# setattr(batman, 'damage', 175)
#
# superman.can_fly = True
# setattr(superman, 'damage', 275)
# setattr(superman, 'alter_ego', 'Кларк Кент')
#
# print(f'{superman.__dict__=}, {batman.__dict__=}')
'-------------------------------------------------------'
# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
#
# words = list(map(str, input().split()))
#
# for word in words:
#     if hasattr(Person, word.lower()):
#         print(f'{word}-YES')
#     else:
#         print(f'{word}-NO')
'-------------------------------------------------------'
# def is_obj_has_attr(obj: object, attr: str) -> bool:
#     return hasattr(obj, attr)
'-------------------------------------------------------'
# class Robot:
#     material = 'steel'
#
# print(getattr(Robot, 'steel'))
#
# class Robot:
#     material = 'steel'
#
# print(getattr(Robot, 'steel', 'iron'))

