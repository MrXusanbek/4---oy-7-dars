# 4  -oy 7 - dars
from email.generator import Generator
#
# users = ["Tohir", "Sobir","Bakir", "Jalil"]
#
# iter_user = iter (users)
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# #------------------------------------------
#
# from typing import Iterable
#
#  users = ["Tohir","Sobir","Bakir", " Jalil"]
#  print(users)




# class CustomIterator:
#     def __init__(self, users: Iterable):
#          self.__users = users
#          self.__index = -1
#
#     def __iter__(self):
#         self.__index +=1
#         if self.__index>=len(self.__users):
#             raise StopIteration(" Element qolmadi!!!")
#         return self.__users[self.__index]


#=------------------------------------------------
# # Generator
# def custome_generator():
#     yield "salom"
#
# # 1 -usul
# for user in custome_generator():
#     print(user)
#
#
# def generate_number():
#     for i in range(1000000):
#         yield i
#
#
# print(generate_number().__sizeof__())
#----------------------------------
# homeworks
# 1 misol
# Simple Iterator
# class SimpleIterator:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 10:
#             result = self.num
#             self.num += 1
#             return result
#         else:
#             raise StopIteration

# 2 misol
# List Iteration
# class ListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.lst):
#             result = self.lst[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration

# 3 misol
# Reverse Iterable
# class ReverseIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = len(lst)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index > 0:
#             self.index -= 1
#             return self.lst[self.index]
#         else:
#             raise StopIteration

# 4 misol
# String Iterable
# class StringIterator:
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.string):
#             result = self.string[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration

# 5 misol
# Filter Iterable
# class EvenFilterIterator:
#     def __init__(self, lst):
#         self.lst = iter(lst)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             num = next(self.lst)
#             if num % 2 == 0:
#                 return num

# 6 misol
# Iterator with Mathematical Operations
# class SumIterator:
#     def __init__(self, lst):
#         self.lst = iter(lst)
#
#     def total(self):
#         return sum(self.lst)

# 7 misol
# Search in Iterator
# class SearchIterator:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def search(self, target):
#         return target in self.lst

# generatorlarga oid masalalar
# 1 misol
# Oddiy generator yaratish
# def simple_generator(start, end):
#     for i in range(start, end):
#         yield i

# 2 misol
#  Har bir so'zning uzunligini hisoblash
# def word_length_generator(text):
#     for word in text.split():
#         yield len(word)

# 3 misol
#  Toq sonlar generatori
# def odd_generator(limit):
#     for i in range(limit):
#         if i % 2 != 0:
#             yield i

# 4 misol
# Juft sonlar generatori
# def even_generator(limit):
#     for i in range(limit):
#         if i % 2 == 0:
#             yield i

# 5 misol
# Cheksiz generator
# def infinite_generator():
#     num = 1
#     while True:
#         yield num
#         num += 1

# 6 misol
#Kvadrat sonlar generatori
# def square_generator(limit):
#     for i in range(limit):
#         yield i ** 2

# 7 misol
# Sum Generator
# def sum_generator(lst):
#     yield sum(lst)

# 8 misol
# def positive_generator(lst):
#     for num in lst:
#         if num > 0:
#             yield num

# 9 misol
# import random
#
# def random_generator(count):
#     for _ in range(count):
#         yield random.randint(1, 100)

# 10 misol
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def prime_generator(n):
#     count, num = 0, 2
#     while count < n:
#         if is_prime(num):
#             yield num
#             count += 1
#         num += 1

# 11 misol
# def reverse_string_generator(string):
#     for char in reversed(string):
#         yield char

# 12 misol
# def product_generator(n):
#     product = 1
#     for i in range(1, n + 1):
#         product *= i
#         yield product




