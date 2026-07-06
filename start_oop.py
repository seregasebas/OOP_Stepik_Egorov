from functools import wraps
import time
from datetime import datetime

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
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
# class Celsius:
#
#     def __init__(self, temp):
#         self.temp = temp
#
#     def to_fahrenheit(self):
#         return (self.temp * 9 / 5) + 32
#
#     @property
#     def temperature(self):
#         return self.temp
#
#     @temperature.setter
#     def temperature(self, value):
#         if -273.15 < value:
#             self.temp = value
#         else:
#             raise ValueError
#
# celsius = Celsius(25)
# assert celsius.temperature == 25
# assert celsius.to_fahrenheit() == 77.0
#
# celsius.temperature = 30
# assert celsius.temperature == 30
# assert celsius.to_fahrenheit() == 86.0
#
# print('Good')
'-------------------------------------------------------'
# class Person:
#     def __init__(self, new_name, new_age):
#         self.name = new_name  # здесь name - имя свойства
#         self._age = new_age
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         if isinstance(value, str) and len(value) > 0:
#             self._name = value
#         else:
#             raise ValueError('Имя должно быть непустой строкой')
#
#     def delete_name(self):
#         del self._name
#     name = property(get_name)
#     name = name.setter(set_name)
#     name = name.deleter(delete_name)
#
# a = Person('dsfsd', 56)
#
# a.name = 'Vas'
# print(a.name)
# print(a.get_name())
'-------------------------------------------------------'
# class UserMail:
#
#     logins = []
#
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email
#
#     def get_login(self):
#         return self.__login
#
#     def set_login(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} не является строкой")
#         else:
#             if value in UserMail.logins:
#                 UserMail.logins.remove(value)
#                 raise ValueError(f"Логин {value} уже имеется в системе")
#             else:
#                 self.__login = value
#                 UserMail.logins.append(value)
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, value):
#         if isinstance(value, str) and value.count('@') == 1 and '.' in value.split('@')[1]:
#             self.__email = value
#         else:
#             raise ValueError(f'ErrorMail:{value}')
#
#     email = property(fget=get_email, fset=set_email)
#     login = property(fget=get_login, fset=set_login)

# jim = UserMail("aka47", 'hello@com.org')
# print(isinstance(type(jim).login, property)) # Проверка на наличие свойства login
# print(f'Jim login is {jim.login}')
# try:
#     bim = UserMail("aka47", 'world@com.org') # Попытка создать экземпляр с занятым логином
# except ValueError as e:
#     print(e)
# jim.login = 'aka48'
# print(f'Jim login is {jim.login}')
# bim = UserMail("aka47", 'world@com.org')
# print(f'Bim login is {bim.login}')
#
# for value in [True, [1, 2, 3], 5, {'a': 'b'}]:
#     try:
#         UserMail(value, 'world@com.org')
#     except TypeError as e:
#         print(e)
'-------------------------------------------------------'
# class UserMail:
#
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, value):
#         if isinstance(value, str) and value.count('@') == 1 and '.' in value.split('@')[1]:
#             self.__email = value
#         else:
#             print(f'ErrorMail:{value}')
#
#     email = property(fget=get_email, fset=set_email)
#
# # jim = UserMail("aka47", 'hello@com.org')
# # print(jim.login)
# # print(jim._UserMail__email)
# # print(isinstance(type(jim).email, property))
# # print(jim.email)
# # try:
# #     jim.email = [1, 2, 3]
# # except ValueError as e:
# #     print(e)
# # try:
# #     jim.email = 'hello@@re.ee'
# # except ValueError as e:
# #     print(e)
# # jim.email = 'hello@re.w3'
# # print(jim.email)
#
# # try:
# #     UserMail('belosnezhka', {1, 2, 3})
# # except ValueError as e:
# #     print(e)
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)
# print(k.login)
# for value in [True, 'prince@still@.wait', 'prince@stillwait']:
#     try:
#         k.email = value
#     except ValueError as e:
#         print(e)
#
# k.email = 'prince@still.wait'
# print(k.get_email())
# try:
#     k.email = 'pri.nce@stillwait'
# except ValueError as e:
#     print(e)
# print(k.email)
'-------------------------------------------------------'
# class Employee:
#
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     def __get_name(self):
#         return self.__name
#
#     def __get_salary(self):
#         return self.__salary
#
#     def __set_salary(self, value):
#         if isinstance(value, (int, float)) and value >= 0:
#             self.__salary = value
#         else:
#             print(f"ErrorValue:{value}")
#
#     title = property(fget=__get_name)
#     reward = property(fget=__get_salary, fset=__set_salary)
#
# employee = Employee("John Doe", 50000)
# assert employee.title == "John Doe"
# assert employee._Employee__name == "John Doe"
# assert isinstance(employee, Employee)
# assert isinstance(type(employee).title, property), 'Вы не создали property title'
# assert isinstance(type(employee).reward, property), 'Вы не создали property reward'
#
# assert employee.reward == 50000
# employee.reward = -100  # ErrorValue:-100
#
# employee.reward = 1.5
# assert employee.reward == 1.5
#
# employee.reward = 70000
# assert employee.reward == 70000
# employee.reward = 'hello'  # Печатает ErrorValue:hello
# employee.reward = '777'  # Печатает ErrorValue:777
# employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
# assert employee.reward == 70000
# employee._Employee__set_salary(55000)
# assert employee._Employee__get_salary() == 55000
'-------------------------------------------------------'
# class BankAccount:
#
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self):
#         return self._account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def set_balance(self, new_balance):
#         self._balance = new_balance
#
# account = BankAccount("1234567890", 1000)
# assert account._balance == 1000
# assert account._account_number == "1234567890"
# assert account.get_account_number() == "1234567890"
# assert account.get_balance() == 1000
# account.set_balance(1500)
# assert account.get_balance() == 1500
#
# print('Good')
'-------------------------------------------------------'
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         print(f"К атрибуту _name обращались в {datetime.now()}")
#         return self._name
#
#     def set_name(self, new_name):
#         print(f"Атрибут _name изменился в {datetime.now()}")
#         self._name = new_name
#
#
# bob = Person('bob')
# print(bob.get_name())
# time.sleep(3)
# bob.set_name('Bill')
# print(bob.get_name())
'-------------------------------------------------------'
# class Person:
#     def __init__(self, name, age):
#         self.set_name(name)
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         if isinstance(value, str) and len(value) > 0:
#             self._name = value
#         else:
#             raise ValueError('Имя должно быть непустой строкой')
# p = Person('Artem', 33)
# try:
#     p.set_name(100)
# except ValueError as ex:
#     print(ex)
'-------------------------------------------------------'
# class Employee:
#
#     def __init__(self, name, position, hours_worked, hourly_rate):
#         self.name = name
#         self.__position = position
#         self.__hours_worked = hours_worked
#         self.__hourly_rate = hourly_rate
#
#     def __calculate_salary(self):
#         return (self.__hours_worked * self.__hourly_rate)
#
#     def _set_position(self, position: str):
#         self.__position = position
#
#     def get_position(self):
#         return self.__position
#
#     def get_salary(self):
#         return self.__calculate_salary()
#
#     def get_employee_details(self):
#         return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"
#
# employee = Employee("Джеки Чан", 'manager', 20, 40)
# assert employee.name == 'Джеки Чан'
# assert employee._Employee__hours_worked == 20
# assert employee._Employee__hourly_rate == 40
# assert employee._Employee__position == 'manager'
# assert employee.get_position() == 'manager'
# assert employee.get_salary() == 800
# assert employee._Employee__calculate_salary() == 800
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
# employee._set_position('Director')
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
#
# employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
# assert employee_2._Employee__calculate_salary() == 1050
# assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'
#
# print('Good')
'-------------------------------------------------------'
# class Library:
#
#     def __init__(self, books: list):
#         self.__books = books
#
#     def __check_availability(self, book: str):
#         return book in self.__books
#
#     def search_book(self, book: str):
#         return self.__check_availability(book)
#
#     def return_book(self, book: str):
#         self.__books.append(book)
#
#     def _checkout_book(self, book: str):
#         if book in self.__books:
#             self.__books.remove(book)
#             return True
#         else:
#             return False
#
# library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
#
# assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
# assert library.search_book("Moby-Dick") == True
# assert library.search_book("Jane Air") == False
#
# assert library._Library__check_availability("War and Peace") == True
# assert library._checkout_book("Moby-Dick") == True
# assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
#
# assert library.search_book("Moby-Dick") == False
# assert library.return_book("Moby-Dick") is None
# assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
# assert library.search_book("Moby-Dick") == True
# print('Good')
'-------------------------------------------------------'
# class BankDeposit:
#
#     def __init__(self, name, balance, rate):
#         self.name = name
#         self.balance = balance
#         self.rate = rate
#
#     def __calculate_profit(self):
#         return self.balance * (self.rate/100)
#
#     def get_balance_with_profit(self):
#         return self.balance + self.__calculate_profit()
#
# account = BankDeposit("John Connor", 1000, 5)
# print(account._BankDeposit__calculate_profit())
# print(account.get_balance_with_profit())
'-------------------------------------------------------'
# class Student:
#
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}\n'
#               f'Возраст: {self.__age}\n'
#               f'Направление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
#
# # adam = Student("Adam Smith", 25, "Information Technology")
# # adam.access_private_method()
#
# piter = Student("Piter Parker", 34, "Information Security")
# piter.access_private_method()
# print(piter._Student__branch)
# print(piter._Student__name)
# print(piter._Student__age)
# piter._Student__display_details()
'------------------------------------------------------'
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self._course = 1
#         self.__marks = []
#
# student = Student(name="Kevin")
# print(student.__dict__)
'-------------------------------------------------------'
# class WeatherStation:
#     __shared_attr = {"temperature": 0, "humidity": 0, "pressure": 0}
#
#     def __init__(self):
#         self.__dict__ = WeatherStation.__shared_attr
#
#     def update_data(self, temperature, humidity, pressure):
#         self.__shared_attr["temperature"] = temperature
#         self.__shared_attr["humidity"] = humidity
#         self.__shared_attr["pressure"] = pressure
#
#     def get_current_data(self):
#         return tuple(WeatherStation.__shared_attr.values())
#
# sensor1 = WeatherStation()
# assert sensor1.temperature == 0
# assert sensor1.humidity == 0
# assert sensor1.pressure == 0
# sensor2 = WeatherStation()
# assert sensor2.get_current_data() == (0, 0, 0)
# sensor1.update_data(25, 60, 103)
# assert sensor1.get_current_data() == (25, 60, 103)
# assert sensor2.get_current_data() == (25, 60, 103)
# sensor3 = WeatherStation()
# assert sensor3.get_current_data() == (25, 60, 103)
# sensor3.update_data(50, 20, 10)
# assert sensor1.get_current_data() == (50, 20, 10)
# assert sensor2.get_current_data() == (50, 20, 10)
# print('Good')
'-------------------------------------------------------'
# class Point:
#
#     points = []
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.points.append(self)
#
#     def get_distance_to_origin(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def get_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             print('Передана не точка')
#             return None
#         return ((self.x - another_point.x) ** 2
#                 + (self.y - another_point.y) ** 2) ** 0.5
#
#     def display(self):
#         print(f"Point({self.x}, {self.y})")
#
#     def get_point_with_max_distance(self):
#         self.max_point = max(Point.points, key = lambda x: (x.get_distance_to_origin(), x.y))
#         self.max_point.display()
#
# p1 = Point(4, 5)
# p2 = Point(2, 4)
# p3 = Point(5, 1)
# p2.get_point_with_max_distance()
'-------------------------------------------------------'
# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_exists(self):
#         return self.a < self.b + self.c and self.b < self.c + self.a and self.c < self.a + self.b
#
#     def is_equilateral(self):
#         return self.a == self.b == self.c
#
#     def is_isosceles(self):
#         return self.is_exists() and (self.a == self.b or self.a == self.c or self.b == self.c)
#
# triangle = Triangle(5, 16, 5)
# print(f"Is Triangle exist: {triangle.is_exists()}")
# print(f"Is Equilateral: {triangle.is_equilateral()}")
# print(f"Is Isosceles: {triangle.is_isosceles()}")
'-------------------------------------------------------'
# class Task:
#     def __init__(self, name , description, status = False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         if self.status:
#             print(f'{self.name} (Сделана)')
#         else:
#             print(f'{self.name} (Не сделана)')
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
# class TaskManager:
#     def __init__(self, task_list: TaskList):
#         self.task_list = task_list
#
#     def mark_done(self, task: Task):
#         self.task = task
#         self.task.status = True
#
#     def mark_undone(self, task: Task):
#         self.task = task
#         self.task.status = False
#
#     def show_tasks(self):
#         for task in self.task_list.tasks:
#             task.display()
#
# # Ниже код для проверки классов Task, TaskList и TaskManager
#
# # Создаем список задач
# todo = TaskList()
# assert todo.tasks == []
#
# # Создаем несколько задач и добавляем их в список
# task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
# assert task1.name == 'Стирка'
# assert task1.description == 'Постирать трусы, носки, слюнявчики'
# assert task1.status is False
# task1.display()
#
# todo.add_task(task1)
# assert len(todo.tasks) == 1
#
# task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
# assert task2.name == 'Продукты'
# assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
# assert task2.status is False
#
# todo.add_task(task2)
# assert len(todo.tasks) == 2
#
# # Создаем менеджер задач и показываем список задач
# manager = TaskManager(todo)
# assert isinstance(manager.task_list, TaskList)
# print('-----Список дел-----')
# manager.show_tasks()
#
#
# # Отмечаем первую задачу выполненной и показываем список задач
# manager.mark_done(task1)
#
# # Проверяем изменился ли статус 2мя способами
# assert task1.status is True
# assert manager.task_list.tasks[0].status is True
#
# print('-----Список дел-----')
# manager.show_tasks()
#
# # Удаляем вторую задачу и показываем список задач
# todo.remove_task(task2)
#
# assert len(todo.tasks) == 1
# assert len(manager.task_list.tasks) == 1
#
# print('-----Список дел----3')
# manager.show_tasks()
'-------------------------------------------------------'
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
# class Company:
#
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
# class Employee:
#
#     def __init__(self, name, age, company_name, location):
#         self.name = name
#         self.age = age
#         self.company_name = company_name
#         self.location = location
#         self.personal_data = Person(name=name, age=age)
#         self.work = Company(company_name=company_name, location=location)

# ivan = Person('Ivan', 32)
# assert ivan.name == 'Ivan'
# assert ivan.age == 32
# ivan.display_person_info()
#
# zara = Company('Zara', 'Prague')
# assert zara.company_name == 'Zara'
# assert zara.location == 'Prague'
# zara.display_company_info()
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# assert isinstance(emp.personal_data, Person)
# assert isinstance(emp.work, Company)
#
# assert emp.personal_data.name == 'Jessica'
# assert emp.personal_data.age == 28
# emp.personal_data.display_person_info()
#
# assert emp.work.company_name == 'Google'
# assert emp.work.location == 'Atlanta'
# emp.work.display_company_info()
#
# emp2 = Employee('Kolya', 11, 'Facebook', 'Seattle')
# assert isinstance(emp2.personal_data, Person)
# assert isinstance(emp2.work, Company)
#
# assert emp2.personal_data.name == 'Kolya'
# assert emp2.personal_data.age == 11
# emp2.personal_data.display_person_info()
#
# assert emp2.work.company_name == 'Facebook'
# assert emp2.work.location == 'Seattle'
# emp2.work.display_company_info()
'-------------------------------------------------------'
# class CustomLabel:
#
#     def __init__(self, text, **kwargs):
#         self.text = text
#         self.config(**kwargs)
#
#     def config(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
# # Ниже код для проверки методов класса CustomLabel
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}
'-------------------------------------------------------'
# class Worker:
#
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# worker_objects = [Worker(name, salary, gender, passport) for name, salary, gender, passport in persons]
#
# # for person in persons:
# #     worker_objects.append(Worker(person[0], person[1], person[2], person[3]))
#
# for worker_object in worker_objects:
#     worker_object.get_info()
'-------------------------------------------------------'
# class Stack:
#
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if len(self.values) == 0:
#             print('Empty Stack')
#             return None
#         else:
#             element = self.values.pop()
#             return element
#
#     def peek(self):
#         if len(self.values) == 0:
#             print('Empty Stack')
#             return None
#         else:
#             return self.values[-1]
#
#     def is_empty(self):
#         return False if len(self.values) > 0 else True
#
#     def size(self):
#         return len(self.values)
#
#
# s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)
#
# s.peek()  # распечатает 'Empty Stack'
# assert s.is_empty() is True
# s.push('cat')
# assert s.size() == 1
# assert s.peek() == 'cat'
#
# s.push('dog')
# assert s.size() == 2
# assert s.peek() == 'dog'
#
# s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False
#
# s.push(777)
# assert s.size() == 4
#
# assert s.pop() == 777
# assert s.size() == 3
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
#
# d = Stack()
# assert d.peek() is None  # Печатает "Empty Stack"
# assert d.pop() is None  # Печатает "Empty Stack"
# d.push('hello')
# assert d.size() == 1
# d.push('world')
# assert d.size() == 2
# assert d.peek() == 'world'
# assert d.pop() == 'world'
# assert d.peek() == 'hello'
'-------------------------------------------------------'
# class Numbers:
#
#     def __init__(self, *args):
#         self.numbers = list(args)
#     def add_number(self, number: int):
#         self.numbers.append(number)
#     def get_positive(self):
#         return [num for num in self.numbers if num > 0]
#     def get_negative(self):
#         return [num for num in self.numbers if num < 0]
#     def get_zeroes(self):
#         return [num for num in self.numbers if num == 0]
#
# nums = Numbers(1, 2, -4, -5, 3)
#
# print(nums.get_positive())
# print(nums.get_negative())
# print(nums.get_zeroes())
#
# nums = Numbers(10, 20, 30, 0, 0, 5)
#
# print(nums.get_positive())
# print(nums.get_zeroes())
# nums.add_number(100)
# nums.add_number(0)
# nums.add_number(7)
# print(nums.get_positive())
# print(nums.get_zeroes())
'-------------------------------------------------------'
# class Dog():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound: str):
#         return f'{self.name} says {sound}'
#
# # Ниже код для проверки класса Dog
# curt = Dog("Curt", 4)
# assert isinstance(curt, Dog)
# assert curt.name == 'Curt'
# assert curt.age == 4
# assert curt.description() == 'Curt is 4 years old'
# assert curt.speak("Wo") == 'Curt says Wo'
# assert curt.speak("Bow") == 'Curt says Bow'
#
# jack = Dog("Jack", 12)
# assert isinstance(curt, Dog)
# assert jack.name == 'Jack'
# assert jack.age == 12
# assert jack.description() == 'Jack is 12 years old'
# assert jack.speak("Woof Woof") == 'Jack says Woof Woof'
# assert jack.speak("Bow Wow") == 'Jack says Bow Wow'
#
# assert Dog('Karl', 6).description() == 'Karl is 6 years old'
# print('Good')
'-------------------------------------------------------'
# class Person():
#
#     def __init__(self, first_name , last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     def is_adult(self):
#         return True if self.age >= 18 else False
#
# p1 = Person('Ash', 'Ketchum', 20)
# assert isinstance(p1, Person)
# assert p1.full_name() == 'Ketchum Ash'
# assert p1.age == 20
# assert p1.first_name == 'Ash'
# assert p1.last_name == 'Ketchum'
# assert p1.is_adult() is True
#
# p2 = Person('Hermione', 'Granger', 16)
# assert isinstance(p2, Person)
# assert p2.age == 16
# assert p2.first_name == 'Hermione'
# assert p2.last_name == 'Granger'
# assert p2.full_name() == 'Granger Hermione'
# assert p2.is_adult() is False
# print('Good')
#
# print(p2.__dict__)
'-------------------------------------------------------'
# class Zebra():
#
#     def __init__(self):
#         self.count = 0
#
#     def which_stripe(self):
#         if self.count % 2 == 0:
#             print('Полоска белая')
#             self.count += 1
#         else:
#             print('Полоска черная')
#             self.count += 1
#
#     def run_away(self):
#         print('Oh, Sugar Honey Ice Tea')
#
# # zebra = Zebra()
# # zebra.run_away()
# # zebra.which_stripe()
# # zebra.which_stripe()
# # zebra.which_stripe()
# # zebra.which_stripe()
# # zebra.which_stripe()
# # zebra.run_away()
#
# zebra_1 = Zebra()
# zebra_2 = Zebra()
# zebra_1.which_stripe()
# zebra_2.which_stripe()
# zebra_1.which_stripe()
# zebra_1.which_stripe()
# zebra_1.which_stripe()
# zebra_2.which_stripe()
# zebra_2.which_stripe()
'-------------------------------------------------------'
# class SoccerPlayer():
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals = 1):
#         self.goals += goals
#
#     def make_assist(self, assists = 1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
#
# # Ниже код для проверки методов класса SoccerPlayer
# leo = SoccerPlayer('Leo', 'Messi')
# assert isinstance(leo, SoccerPlayer)
# assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
# leo.score(700)
# assert leo.goals == 700
# leo.make_assist(500)
# assert leo.assists == 500
#
# leo.statistics()
#
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# assert isinstance(kokorin, SoccerPlayer)
# assert kokorin.name == 'Alex'
# assert kokorin.surname == 'Kokorin'
# assert kokorin.assists == 0
# assert kokorin.goals == 0
# kokorin.score()
# assert kokorin.goals == 1
# kokorin.score(5)
# assert kokorin.goals == 6
# kokorin.make_assist()
# assert kokorin.assists == 1
# kokorin.make_assist(10)
# assert kokorin.assists == 11
#
# kokorin.statistics()
#
#
# obi = SoccerPlayer('Оби-Ван', 'Кеноби')
# obi.make_assist()
# assert obi.name == 'Оби-Ван'
# assert obi.surname == 'Кеноби'
# assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
# obi.statistics()
#
# mila = SoccerPlayer('Mila', 'Kunis')
# mila.make_assist()
# mila.statistics()
'-------------------------------------------------------'
# class Laptop():
#
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'
#
# laptop1, laptop2 = Laptop('hp', '15-bw0xx', 57000), Laptop('hp', '15-bw0xx', 57000)
#
# assert isinstance(laptop1, Laptop)
# assert isinstance(laptop2, Laptop)
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# assert hp.laptop_name == 'hp 15-bw0xx'
# assert hp.price == 57000
# assert isinstance(hp, Laptop)
#
# lenovo = Laptop('lenovo', 'z-570-dx', 61000)
# assert lenovo.brand == 'lenovo'
# assert lenovo.model == 'z-570-dx'
# assert lenovo.price == 61000
# assert lenovo.laptop_name == 'lenovo z-570-dx'
# assert isinstance(lenovo, Laptop)
# print('Good')
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

