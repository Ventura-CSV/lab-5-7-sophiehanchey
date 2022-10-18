

def printfunction1(*str):
	print (str)
	for v in str:
		print (v, end='')
	print()

def printfunction2(str):
	for v in str:
		print (v, end='')
	print()


def main():
	str = 'Python Programming'
	printfunction1(*str)
	printfunction2(str)

	morestr = 'C++ Programming'
	printfunction1(str, morestr)
	# printfunction2(str, morestr)  # Error

main()
