from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urlopen("https://vip.udel.edu/crypto/encrypted_mobydick.txt", context=ctx)
mobytext = response.read()

onlyletters = filter(lambda x: x.isalpha(), mobytext)
loweronly = str(onlyletters).lower()

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

print("Should be near .065 if plain: " + str(sum_freqs_squared))
