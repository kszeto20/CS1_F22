values = [ 14, 10, 8, 19, 7, 13 ]

x = input("Enter a value: ")
print(x)
a = int(x)
values.append(a)

y= input("Enter another value: ")
print(y)
b = int(y)
values.insert(2, b)

print(values[3], values[-1])

print("Difference: {}".format(max(values)-min(values)))
print("Average: {:.1f}".format(sum(values) / len(values)))

values.sort()

median_added = (values[3] + values[4])

print("Median: {:.1f}".format(median_added/2 ))