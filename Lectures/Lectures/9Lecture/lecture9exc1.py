n = input('Enter a positive integer: ').strip('\r')
print(n)

num = int(n)

i = 0
while i < num:
    if i % 3 == 0:
        print(i)
    i += 1
