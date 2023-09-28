values = []
while True:
    a = input('Enter a value (0 to end): ').strip('\r')
    print(a)

    num = int(a)
    if num == 0:
        break
    else:
        values.append(num)

avg = sum(values) / len(values)

print('Min:', min(values))
print('Max:', max(values))
print('Avg: {:.1f}'.format(avg))