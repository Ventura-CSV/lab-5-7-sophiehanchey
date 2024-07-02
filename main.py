
def splitlist(*numbers):
    # split the numbers up using * and check the output
    print(f'The numbers: {numbers}')
    
    # find the minimum and idx of minimum
    min = None
    minIdx = None
    currentIdx = 0
    for n in numbers:
        if min is None or n < min:
            min = n
            minIdx = currentIdx
        currentIdx += 1
        
    # swap with first item values
    numbers[0], numbers[minIdx] = numbers[minIdx], numbers[0]
    print(numbers)
    
    return numbers

def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
