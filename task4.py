odd_even = int(input('Enter a number: '))
a = odd_even % 2
b = odd_even % 4

if a != 0:
    print('The number is odd')
if a == 0 and b != 0:
    print('The number is even')
elif a == 0 and b == 0:
    print('The number is a multiple of 4 and it is also even')