#Rotating an array

#function to rotate array
def repostion(numbers):
	n = input("Enter position")
	#numbers = input("Enter Array of numbers")
	return numbers[-n:] + numbers[:-n]

numbers = input("Enter Array of numbers")
print repostion(numbers)