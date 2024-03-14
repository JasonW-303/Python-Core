# Basic - Print all integers from 0 to 150.
num = 150
for i in range(1, num + 1):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 0 to 1,000.
num = 1000
for i in range(5, num + 1):
    if i % 5 == 0:
        print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
num = 100
for i in range(1, 100 + 1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
num = 500000
for i in range(0, num + 1):
    if i % 2 == 1:
        sum += i
print(sum)
#  Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
num = 2018
for i in range(num, 0, -4):
    print(i)
# Flexible Counter - Set three variables (lo, high, mult). Start at low, go through high, print only ints that are a multiple of mult.
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)
