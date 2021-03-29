import hashlib
import bcrypt

salt = bcrypt.gensalt()
print('Salt: ' + str(salt))
my_word = 'proceed'
print('my_word: ' + str(my_word.encode()))
my_word_hash = hashlib.sha256(my_word.encode() + salt).hexdigest()
print('Salty hash: ' + str(my_word_hash))

# Check dictionary for word
# f = open('dictionary.txt', 'r')
# words = [word.strip() for word in f]
# for word in words:
#     if hashlib.sha256(word.encode()).hexdigest() == my_word_hash:
#         print(word)
# f.close()
