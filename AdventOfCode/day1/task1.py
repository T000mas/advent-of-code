def part_1():
    finalNumbersList = []
    
    with open('day1/dataset1.txt') as f:
        for line in f:
            firstNumber = None
            lastNumber = None
            for letter in line:
                if letter.isnumeric():
                    if firstNumber is None:
                        firstNumber = letter
                    else:
                        lastNumber = letter
            if lastNumber is not None:
                finalNumbersList.append(firstNumber + lastNumber)
            else:
                finalNumbersList.append(firstNumber + firstNumber)
            
    sumOfNumbers = 0
    for number in finalNumbersList:
        sumOfNumbers += int(number)

    print(sumOfNumbers)


def part_2():
    finalNumbersList = []
    
    with open('day1/dataset1.txt') as f:
        for line in f:
            firstNumber = None
            lastNumber = None
            for letter in line:
                if letter.isnumeric():
                    if firstNumber is None:
                        firstNumber = letter
                    else:
                        lastNumber = letter
            if lastNumber is not None:
                finalNumbersList.append(firstNumber + lastNumber)
            else:
                finalNumbersList.append(firstNumber + firstNumber)
            
    sumOfNumbers = 0
    for number in finalNumbersList:
        sumOfNumbers += int(number)

    print(sumOfNumbers)