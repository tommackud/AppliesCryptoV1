import time
import bcrypt
import hashlib


# def test_func(n):
#     start_time = time.time()
#     for i in range(n):
#         for j in range(n):
#             x = i * j
#     end_time = time.time()
#     return end_time - start_time


# print(test_func(10000))
# print(test_func(10))
# print(test_func(100))


# def test_func(n):
#     start_time = time.time()
#     for i in range(n):
#         for j in range(n):
#             x = i * j
#     end_time = time.time()
#     if .09 < end_time - start_time < .11:
#         return end_time - start_time

# Now use timing and some guessing to make a function which consumes just a password and returns a (salt, r, theHash)
# triplet that took around 1 second to create. Verify that you can recreate theHash.

import hashlib
import bcrypt

salt = bcrypt.gensalt()

def timing_func(pwd):
    while time < 1 sec

