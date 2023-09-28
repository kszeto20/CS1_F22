co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
total = 0
for co2_level in co2_levels:
    total += co2_level
    
avg = total / len(co2_levels) 
count = 0 # count above avg

for co2_level in co2_levels:
    if co2_level > avg:
        count += 1
    
print("Average: {:.2f}".format(avg))
print("Num above average: {}".format(count))

    