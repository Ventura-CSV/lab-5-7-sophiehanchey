
def splitlist(numbers):
    minidx = numbers.index(min(numbers))
    numbers[0], numbers[minidx] = numbers[minidx], numbers[0]
    first, *others = numbers
    return first, others


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    ###########################
    # Make your code
    # Complet this main function
    ###########################
    print(first)  # Expected output
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
