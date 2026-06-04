#from datetime import datetime
#from time import perf_counter, sleep

print("Hello, World! I'm a povtor!")

'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
'--------------------------------------------'
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