IMDBfile = input('Data file name: ').strip('\r')
print(IMDBfile)

lastName = input('Prefix: ').strip('\r')
print(lastName)

names = set()
occurs = 0

for line in open(IMDBfile, encoding="ISO-8859-1"):
    sline = line.strip()
    sline = sline.split('|')
    # name, title, number
    name = sline[0].split(',')
    lastName = name[0]
    
    names.add(lastName)
 
for name in names:
    if (name[0:len(lastName)] == lastName):
      occurs += 1
      

print('{} last names'.format(len(names)))
print('{} start with {}'.format(occurs, lastName))