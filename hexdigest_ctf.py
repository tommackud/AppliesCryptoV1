import hashlib
import string

# open files and store data in arrays

f = open('ctf_hashes', 'r')
h_lines = [line.strip() for line in f]
f.close()

f = open('dictionary.txt', 'r')
words = [word.strip() for word in f]
f.close()

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def check_dictionary(key):
    return [letter for letter in letters if hashlib.sha256(letter.encode('utf-8')).hexdigest() == key]


for entry in h_lines:
    result = check_dictionary(entry)
    result2 = ' '.join(result)
    print(result2, end='')
    if not result:
        print(' ', end='')