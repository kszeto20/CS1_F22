co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

perc = input("Enter the fraction: ").strip('\r')
print(perc)
perc = float(perc)

for i in range(len(co2_levels)):
    co2_levels[i] = co2_levels[i] * (1 + perc)
    
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))