'''
Checkpoint 3: Framing Any Word

Modify your code to ask for a single word of any length
and then frame it properly. The result of running your program should look like
Enter a word: inquisition
*****************
** inquisition **
*****************
'''

inP = input("Enter a word: ").strip('\r')
print(inP)

sLen = len(inP)

print('*' * (sLen + 6))
print('**', inP, '**')
print('*' * (sLen + 6))