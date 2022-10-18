
import main


def test_main():
    str = 'Python Programming'
	printfunction1(*str)
	printfunction2(str)

	morestr = 'C++ Programming'
	printfunction1(str, morestr)
    
    printfunction1('a', 'b', 'c', 'd', 'e')
    # assert v1 == -10, "Min value does not match"
    # assert v2 == 5, "Max value does not match"
    
