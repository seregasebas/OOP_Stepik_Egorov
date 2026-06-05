#from datetime import datetime
#from time import perf_counter, sleep

print("Hello, World! I'm a povtor!")

'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
# def filter_even(func):
#
#     def wrapper(*args, **kwargs):
#         res = []
#         for arg in args:
#             if isinstance(arg, int):
#                 if arg % 2 == 0:
#                     res.append(str(arg))
#             else:
#                 if len(arg) % 2 == 0 or arg == False:
#                     res.append(str(arg))
#         return func(*res, **kwargs)
#     return wrapper
#
# def delete_short(func):
#
#     def wrapper(*args, **kwargs):
#         res = {}
#         for key, value in kwargs.items():
#             if len(key) > 4:
#                 res[key] = value
#         return func(*args, **res)
#     return wrapper

# @delete_short
# def info_kwargs(**kwargs):
#     """Выводит информацию о переданных kwargs"""
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)


# @filter_even
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))

@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))
'--------------------------------------------'
# def validate_all_kwargs_int_pos(func):
#
#     def wrapper(*args, **kwargs):
#         for key, value in kwargs.items():
#             if isinstance(value, int):
#                 continue
#             else:
#                 print('Все именованные аргументы должны быть положительными числами')
#                 return None
#         return func(*args, **kwargs)
#     return wrapper
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a="i", b='Love', c="Python"))
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a=10, b=20, c=50))
'--------------------------------------------'
# def validate_all_args_str(func):
#
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, str):
#                 continue
#             else:
#                 print('Все аргументы должны быть строками')
#                 return None
#         return func(*args, **kwargs)
#     return wrapper
#
# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Через", 9, "Месяцев"))

# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
'--------------------------------------------'
# def first_validator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f"Начинаем важную проверку")
#         if len(args) == 3:
#             func(*args, **kwargs)
#         else:
#             print(f"Важная проверка не пройдена")
#             return None
#         print(f"Заканчиваем важную проверку")
#
#     return my_wrapper
#
#
# def second_validator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f"Начинаем самую важную проверку")
#         if kwargs.get('name') == 'Boris':
#             func(*args)
#         else:
#             print(f"Самая важная проверка не пройдена")
#             return None
#         print(f"Заканчиваем самую важную проверку")
#
#     return my_wrapper
#
#
# # используйте декораторы
# @second_validator
# @first_validator
# def sum_values(*args):
#     print(f'Получили результат равный {sum(args)}')
#
# sum_values(11, 33, 33, name='Boris')
'--------------------------------------------'
# def uppercase_elements(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, list):
#             res_new = []
#             for element in res:
#                 if isinstance(element, str):
#                     res_new.append(element.upper())
#                 else:
#                     res_new.append(element)
#         elif isinstance(res, dict):
#             res_new = {}
#             for key, value in res.items():
#                 if isinstance(key, str):
#                     key = key.upper()
#                     res_new[key] = value
#                 else:
#                     res_new[key] = value
#
#         return res_new
#
#     return wrapper
#
# @uppercase_elements
# def my_func(**kwargs):
#     return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs
#
# print(my_func(**{'Five': 5, 'sIx': 6}))

# @uppercase_elements
# def my_func(name, surname):
#     return ['temple', 'store', name, surname, *[1, 2, 3]]
#
# print(my_func('Gerard', 'Pique'))
'--------------------------------------------'
# def decorator(func):
#
#     def inner(*args, **kwargs):
#         print(f'---Start calculation---')
#         res = func(*args, **kwargs)
#         print(f'---Finish calculation. Result is {res}---')
#     return inner
#
# @decorator
# def add_with_factor(*values, factor=1):
#     return sum(values) * factor
#
# add_with_factor(1, 4, 5, 6, factor=2)
'--------------------------------------------'
# def uppercase(func):
#     def inner(n, i, rate):
#         res = func(n, i, rate)
#         return res.upper()
#
#     return inner
#
#
# # Задекорируйте функцию calculate_tax
# @uppercase
# def calculate_tax(name, income, tax_rate):
#     tax = income - income * (1 - tax_rate / 100)
#     return f'{name} должен заплатить налог {tax}$'
#
#
# print(calculate_tax("Ivan", 5000, 25))
# print(calculate_tax("vaSilIy", 15000, 30))
# print(calculate_tax("depardieu", 215000, 40))
'--------------------------------------------'
# def swapcase(func):
#     def wrapper(*args, **kwargs):
#         func_res = func(*args, **kwargs)
#         print(f'Функция func вернула значение "{func_res}"')
#         return func_res.swapcase()
#     return wrapper
#
#
# @swapcase
# def say_hello_to(name, surname):
#     return f'Hello {name} {surname}'
#
#
# res = say_hello_to('Vasya', 'Ivanov')
# print(f'{res=}')
#
# print(say_hello_to('gennadi', 'LOSKOV'))
'--------------------------------------------'
# def create_dict():
#     count = 0
#     res = {}
#     def inner(args):
#         nonlocal count
#         count += 1
#         res[count] = args
#         return res
#     return inner
#
# f_1 = create_dict()
# print(f_1('privet'))
# print(f_1('poka'))
# print(f_1([5, 2, 3]))
#
# f2 = create_dict()
# print(f2(5))
# print(f2(15))
'--------------------------------------------'
# def create_counter():
#     count = 0
#     def inner():
#         pass
#
#     def increment(value: int = 1):
#         nonlocal count
#         count += value
#         return count
#
#     def decrement(value: int = 1):
#         nonlocal count
#         count -= value
#         return count
#
#     inner.inc = increment
#     inner.dec = decrement
#     return inner
#
# ex1 = create_counter()
# print(ex1.inc(3))
# print(ex1.inc(5))
# print(ex1.dec(90))
#
# ex2 = create_counter()
# print(ex2.inc(1))
# print(ex2.inc(2))
# print(ex2.inc(23))
#
# # def create_counter():
# #     count = 0
# #
# #     def increment(value: int = 1):
# #         nonlocal count
# #         count += value
# #         return count
# #
# #     def decrement(value: int = 1):
# #         nonlocal count
# #         count -= value
# #         return count
# #
# #     return increment, decrement
# #
# #
# # inc_1, dec_1 = create_counter()
# # print(inc_1())  # увеличиваем на 1
# # print(inc_1(2))  # увеличиваем на 2
# # print(inc_1(3))  # увеличиваем на 3
# # print(dec_1())  # уменьшаем на 1
# # print(dec_1())  # уменьшаем на 1
# #
# # print('-' * 15)
# # print('Создаем новый объект замыкания с другим счетчиком')
# #
# # inc_2, dec_2 = create_counter()
# # print(inc_2(10))  # увеличиваем на 10
# # print(dec_2(5))  # уменьшаем на 5
# # print(inc_2(100))  # увеличиваем на 100
# # print(inc_2(50))  # увеличиваем на 50
# # print(dec_2())  # уменьшаем на 1
'--------------------------------------------'
# def timer():
#     start = perf_counter()
#
#     def inner():
#         return perf_counter() - start
#
#     return inner
#
#
# q = timer()
# sleep(1)  # делаем паузу в 1 секунду
# print(q())
# sleep(2)  # делаем паузу в 2 секунды
# print(q())
# sleep(3)  # делаем паузу в 3 секунды
# print(q())
'--------------------------------------------'
# def timer():
#     start = datetime.now()
#     def inner():
#         print(f'{start=}')
#         return datetime.now() - start
#     return inner
#
# r1 = timer()
# print(r1())
#
# for i in range(200000):
#   2**10000
#
# print(r1())
'--------------------------------------------'
# def add(a, b):
#     return a + b
#
# def counter(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'функция {func.__name__} вызывалась {count} раз')
#         return func(*args,**kwargs)
#
#     return inner
# q = counter(add)
#
# q(10, 20)
# q(2,5)
'--------------------------------------------'
# def count_calls():
#     def inner():
#         inner.total_calls += 1
#         return inner.total_calls
#     inner.total_calls = 0
#     return inner
#
# counter = count_calls()
# counter()
# counter()
# print(counter.total_calls)
# counter()
# print(counter.total_calls)
'--------------------------------------------'
# def countdown(n: int):
#     count = n+1
#     def inner():
#         nonlocal count
#         if count > 1:
#             count -= 1
#             print(count)
#         else:
#             print(f'Превышен лимит, вы вызвали более {n} раз')
#     return inner
#
# count = countdown(3)
# count()
# count()
# count()
# count()
# count()
'--------------------------------------------'
# def create_accumulator(x: int = 0):
#     count = x
#     def inner(n: int) -> int:
#         nonlocal count
#         count += n
#         return count
#     return inner
#
# summator_1 = create_accumulator(100)
# print(summator_1(5))
# print(summator_1(7))
# print(summator_1(2))
#
# summator_2 = create_accumulator()
# print(summator_2(3))
# print(summator_2(6))
'--------------------------------------------'
# def make_repeater(n: int):
#     def inner(text: str) -> str:
#         return text * n
#     return inner
#
# repeat_5 = make_repeater(5)
# print(repeat_5('Hello'))
# print(repeat_5('World'))
#
# '--------------------------------------------'
# def multiply(num):
#     def inner(x):
#         return num * x
#     return inner
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30