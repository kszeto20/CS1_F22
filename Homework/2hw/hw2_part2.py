# Part II: Find the Hidden Message

# program fuctions

# encrypt function
def encrypt(word):
    word = word.replace(' a', '%4%')
    word = word.replace('he', '7!')
    word = word.replace('e', '9(*9(')
    word = word.replace('y', '*%$')
    word = word.replace('u', '@@@')
    word = word.replace('an', '-?')
    word = word.replace('th', '!@+3')
    word = word.replace('o', '7654')
    word = word.replace('9', '2')
    word = word.replace('ck', '%4')
    return word

# decrypt function - reverse order of statements in reverse operation
def decrypt(word):
    word = word.replace('%4', 'ck')
    word = word.replace('2', '9')
    word = word.replace('7654', 'o')
    word = word.replace('!@+3', 'th')
    word = word.replace('-?', 'an')
    word = word.replace('@@@', 'u')
    word = word.replace('*%$', 'y')
    word = word.replace('9(*9(', 'e')
    word = word.replace('7!', 'he')
    word = word.replace('%4%', ' a')
    return word
    
# get input from user
inStr = input('Enter a string to encode ==> ').strip('\r')
print(inStr)
print('')
orig = inStr

# encrpyt and decrypt
encryptedStr = encrypt(inStr)
decStr = decrypt(encryptedStr)

# print statements
print('Encrypted as ==> ' + encryptedStr)
print('Difference in length ==> ' + str(abs(len(encryptedStr) - len(inStr))))
print('Deciphered as ==> ' + decStr)

if (orig == decStr):
    print('Operation is reversible on the string.')
else:
    print('Operation is not reversible on the string.')
    