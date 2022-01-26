# Title: Tuition Calculator Program
# Program created by William Schaeffer
# CPS 313
# P. 215, Exercise 10, Tuition Calculator Program
# 01.25.22

# This program will use count-controlled loop to calculate tuition changes over 5 years

START_TUITION = 8000.00         #constant start variable

tuition = START_TUITION         #initialize tuition variable to increment 

print('Tuition increases:')
print()
print('Year\tTuition')
print('***************')

for year in range(1, 6):
    tuition *= 1.03
    print(f'{year}\t${tuition:,.0f}')

print()
print()

print('Or we can format it precisely how Ahilan asked:')

tuition = START_TUITION

print()
print()

print('Tuition increases:')
for year in range(1, 6):
    tuition *= 1.03
    print(f'Year {year} - ${tuition:,.0f}')