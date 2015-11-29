#LEAST COMMON MULTIPLE

#imports
from fractions import gcd
from functools import reduce

#function for lcm and result output
def lcm(numbers):
	return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)
'''print ""
print "---------- LCM of Numbers ----------"
print lcm((2, 3, 10))
print "---------- END ----------"
'''
user_array = input('Enter numbers to find LCM: ')
 
print lcm((user_array))

