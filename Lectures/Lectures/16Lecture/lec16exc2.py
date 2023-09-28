file = input("Enter the name of the IMDB file ==> ").strip('\r')
print(file)

nums = dict()

f = open(file, encoding = 'ISO-8859-1')

# countries names
for line in f:
    name = line.split('|')[0].strip()
    nums[name] = 0
    
f.close()

# open file again
f = open(file, encoding = 'ISO-8859-1')
for line in f:
    name = line.split('|')[0].strip()
    nums[name] += 1
f.close()

        
maxi= max(nums, key = nums.get)
print('{} appears most often: {} times'.format(maxi, nums[maxi]))

count = 0
for ind in nums:
    # if only shows up once
    if nums[ind] == 1:
        count += 1
        
print('{} people appear once'.format(count))