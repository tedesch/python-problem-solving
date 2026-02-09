# # strip off dashes
# def strip_string(b_function):
#     def wrapper():
#         func = b_function()
#         stripped = func.strip('-')
#         return stripped
#     return wrapper

# # create upper case version of clli code
# def uppercase_decorator(some_function):
#     def a_wrapper():
#         func = some_function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return a_wrapper

# @strip_string
# @uppercase_decorator
# def clli_code():
#     print('The Florida router clli code is', end=' ')
#     return '---tpaflxacg19----'

# print(clli_code())

# # map.grades.py
# # produce list of tuples
# grades = [95, 88, 85, 75]
# letter_grade = ['A', 'B+', 'B', 'C']

# print('The original list ', letter_grade)
# print('The zipped tuples ', list(zip(letter_grade, grades)))

# print('Next is a map-lambda version')

# # map returns a map object in Python 3
# m = map(lambda *a: a, letter_grade, grades)   # *a = arbitrary qty of args
# print(m)

# # convert map object to list so you can see the tuples
# print(list(m))

# # filter_clli.py
# # returns only clli codes located in Florida or California
# clli_names = ['flxa99443oc', 'gaxb32443oc', 'caxo99323oc', 'flxa11443ds']
# print(list(filter(lambda x: x[0].upper() in 'FC', clli_names)))

# # list_comp1.py
# print([(x, y) for x in ['a', 'b', 'c'] for y in ['first', 'b', 3] if x != y])

# a_list = [7, 5, -4, 6]

# def check_negative(z):
#     result = []
#     for item in z:
#         if item < 0:
#             result.append(item * -1)
#     return result

# check_negative = lambda z: [item * -1 for item in z if item < 0]
# print(check_negative([7, 5, -4, 6]))

# listcomp_vs_genexp.py
# list comprehension vs generator expression
import sys

a = [x for x in range(1000000)]   # list comp
b = (x for x in range(1000000))   # generator expr

print('list comp byte size is ', sys.getsizeof(a))
print('generator expression byte size is ', sys.getsizeof(b))