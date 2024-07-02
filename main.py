
def splitlist(numbers):
    # print(f'The numbers: {numbers}')
    # find the minimum and idx of minimum
    min = None
    minIdx = None
    currentIdx = 0
    for n in numbers:
        if min is None or n < min:
            min = n
            minIdx = currentIdx
        currentIdx += 1
        
    # move first item to where minIdx is located
    numbers.insert(minIdx, numbers[0])
    del numbers[0]
    
    # remove the minimum value
    numbers.remove(min)
    
    return min, numbers

def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(*others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
