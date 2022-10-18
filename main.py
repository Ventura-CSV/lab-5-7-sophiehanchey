
def findmin(numbers):
	minidx = numbers.index(min(numbers))
	numbers[0], numbers[minidx] = numbers[minidx], numbers[0]

	

numbers = [5, 4, 3, 2, 1]

others = numbers

###########################
# Make your code
# Complet this main function
###########################

print (numbers) # Expected output     1 2 3 4 5
