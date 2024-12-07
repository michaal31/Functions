import converters

print('### Test converters')

print(f'Three meters is {converters.m_to_cm(3)} cm')

print(f'532 cm = {converters.cm_to_m(532)} meters')

centimeters = 100
inches = converters.cm_to_inch(centimeters)
print(f'{centimeters} cm = {inches:.2f} inches')

feet = 5
inches = 10
total_cm = converters.ft_inch_to_cm(feet, inches)
print(f'{feet} feet {inches} inches = {total_cm:.2f} cm')
