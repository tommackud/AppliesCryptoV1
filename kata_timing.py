import time
import bcrypt
import hashlib


def test_func(n):
    start_time = time.time()
    for i in range(n):
        for j in range(n):
            x = i * j
    end_time = time.time()
    return end_time - start_time


# print(test_func(10000))
# print(test_func(10))
# print(test_func(100))


import bcrypt
import hashlib
import time

count_sec = 0
my_pwd = 'This is a new password'
time = time.time()
print(time)

def calc_time(password):
    the_hash = ''
    salt = bcrypt.gensalt()
    r = 0
    while r < 1:
        the_hash = hashlib.sha256(password.encode()).hexdigest()

    return salt, r, the_hash


print(calc_time(my_pwd))


#
# t_end = time.time() + 1
# while time.time() < t_end:
#     result = hashlib.sha256(my_srt.encode() + salt).hexdigest()
#     count_sec += 1
#
#
# print('Salt: ' + str(salt.decode()))
# print('Count: ' + str(count_sec / 1000000))
# print('Result: ' + str(my_srt))



