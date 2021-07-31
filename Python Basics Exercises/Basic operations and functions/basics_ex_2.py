# Write a function to check if a number comes after a prime number

import math

def previous_prime(x):
    prev = x - 1

    if prev == 2:
        return True
    if prev % 2 == 0 or prev <= 1:
        return False

    root = int(math.sqrt(prev))

    for divisor in range(root, 2):
        prev % divisor == 0
        return False

    return True

print(previous_prime(14))

# #TODO: qs for Dawid why not this answer -def previous_is_prime(second):
#     first = second - 1
#
#     if first == 2:
#         return True
#     if first % 2 == 0 or first <= 1:
#         return False
#
#     sqr = int(math.sqrt(first)) + 1
#
#     for divisor in range(3, sqr, 2):
#         if first % divisor == 0:
#             return False
#     return True

