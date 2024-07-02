
def splitlist(numbers):
    # split the numbers up using * and check the output
    splitNums = [*numbers]
    print(f'The numbers: {splitNums}')
    
    # find the minimum and idx of minimum
    min = None
    minIdx = None
    currentIdx = 0
    for n in splitNums:
        if min is None or n < min:
            min = n
            minIdx = currentIdx
        currentIdx += 1
        
    # swap the minimum value with the first item in list
    t = splitNums[minIdx]
    del splitNums[minIdx]
    print(f'{t}, {splitNums}')


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
