from functools import wraps

print('Hello World!')
'--------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
'-------------------------------------------------------'
# def html_tag(name_tag='h1'):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return f'<{name_tag}>{result}</{name_tag}>'
#
#         return inner
#
#     return decorator
#
#
# @html_tag(name_tag='table')
# def say_hello_to(name, surname):
#     return f'Hello {name} {surname}'
#
#
# print(say_hello_to('Vasiliy', 'Ytkin'))
'-------------------------------------------------------'
# def decorator_factory(a, b):
#     print('Запуск функции создания декоратора')
#
#     def decorator(fn):
#         print("Запуск декоратора")
#         def wrapper(*args, **kwargs):
#             print("Запуск функции wrapper")
#             print('Переданные переменные: ', a, b)
#             return fn(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# print('Начало работы')
#
# @decorator_factory(10, 20)
# def original_func():
#     print('Запуск оригинальной функции')
#
# original_func()
'-------------------------------------------------------'
# def counting_calls(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         return func(*args, **kwargs)
#     wrapper.call_count = 0
#     return wrapper
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# print(add(10, b=20))
# print(add.call_count)
# print(add(30, 5))
# print(add.call_count)
'-------------------------------------------------------'
# def monkey_patching(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         args = ('Monkey' for arg in args)
#         kwargs = {k:'patching' for k, v in kwargs.items()}
#         return func(*args, **kwargs)
#     return wrapper
#
# @monkey_patching
# def info_kwargs(**kwargs):
#     """Выводит информацию о переданных kwargs"""
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# info_kwargs(c=43, b= 32, a=32)
# print(info_kwargs.__name__)
# print(info_kwargs.__doc__.strip())
#
# @monkey_patching
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# print(concatenate('my', 'name is', 'Artem'))
# print(concatenate.__name__)
# print(concatenate.__doc__.strip())
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

