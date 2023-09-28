'''
Checkpoint 2: Framing Four-Letter Input
Copy your program from Checkpoint 1 into a new program, check2.py, and open it in
Spyder. Add code to use the input function discussed at the end of Lecture 3 to read a
four letter word into a string. Modify your code to output this word instead of spam. The
output when you run your program should look like
Enter a four letter word: eggs
**********
** eggs **
**********
'''

inP = input("Enter a four letter word: ").strip('\r')
print(inP)

print('*' * 10)
print('**', inP, '**')
print('*' * 10)
