import hashlib

print(hashlib.sha512(b"andy rocks your face off").hexdigest())

word = 'the'
f = open('dictionary.txt', 'r')
f_lines = f.read().splitlines()
for line in f_lines:
    if str(line) == str(word):
        print(word)
f.close()




