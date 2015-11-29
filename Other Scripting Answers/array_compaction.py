#Array Compactment Program

#Function to remove duplicate
def remove_duplicate(array):
	return list(set(array))

array = input("Enter arrays in the format 1, 2, 3, 4 > ")
print "Array has been compacted to"
print remove_duplicate(array)