'''
Checkpoint 4: Framed Greeting
In this last checkpoint, you will write a new program that outputs a framed greeting for a
person who enters a first and a last name. An example of running this is

Please enter your first name: John
Please enter your last name: Cleese
*************
** Hello,  **
** John    **
** Cleese! **
*************
'''

fName = input("Please enter your first name: ").strip('\r')
print(fName)
lName = input("Please enter your last name: ").strip('\r')
print(lName)

hString = "Hello,"
lName += "!"
print(lName)

fLen = len(fName)
print(fLen)
lLen = len(lName)
hLen = len(hString)

pLen = max(fLen, lLen, hLen) + 6

print('*' * (pLen))
print('** ' + hString + (" " * (pLen - (hLen + 6))) + ' **')
print('** ' + fName + (" " * (pLen - (fLen + 6))) + ' **')
print('** ' + lName + (" " * (pLen - (lLen + 6))) + ' **')
print('*' * (pLen))