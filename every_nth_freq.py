

f = open('challenge.txt', 'r')
data = f.read().replace(' ', '')
f.close()

print(data)


def get_nt_letters(text, n):
    return text[::n]


print(get_nt_letters(data, 8))

