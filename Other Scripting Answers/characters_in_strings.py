
#Function to handle matching characters in two strings
def find_chars(string1, string2):
	output = []
	for char in string2:
		if char in string1:
			output.append(char)
	return ''.join(output)

#Get strings from user
user_string1 = raw_input("Enter First String > ")
user_string2 = raw_input("Enter Second String > ")

#Append quotes to strings and call functions
string1 = '"' + user_string1 + '"'
string2 = '"' + user_string2 + '"'
print "\n---------- Results ----------"
print "Common Characters found in %r and %r are: " % (string1, string2)
print find_chars(string1, string2)
print "---------- End ----------"
