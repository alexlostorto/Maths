from math import gcd
import random


def linearSolve(start, end, between):
    difference = int(end) - int(start)
    interval = difference / (int(between) + 1)
    betweens = []
    newinterval = interval
    for i in range(int(between)):
        newinterval = newinterval + interval
        if newinterval == int(newinterval):
            betweens.append(str(int(newinterval)))
        else:
            betweens.append(str(newinterval))
    print(f'Linear Sequence Solved: {start}, {", ".join(betweens)}, {end}')


def geometricSolve(start, end, between):
    newend = end / start
    newbetween = between + 1
    betweens = []
    multiplier = root(newbetween, newend)
    interval = multiplier / start
    newinterval = start
    for i in range(between):
        newinterval = newinterval * interval
        if newinterval == int(newinterval):
            betweens.append(str(int(newinterval)))
        else:
            betweens.append(str(newinterval))
    print(f'Geometric Sequence Solved: {start}, {", ".join(betweens)}, {end}')


def ratioSimplify(ratiostr):
    ratiolist = ratiostr.split(':')
    ratiolist = [int(i) for i in ratiolist]
    divisor = gcd(*ratiolist)
    simplified = []
    for ratio in ratiolist:
        newratio = ratio / divisor
        if newratio == int(newratio):
            simplified.append(str(int(newratio)))
        else:
            simplified.append(str(newratio))
    print(f'Simplified Ratio: {":".join(simplified)}')


def addFractions(n1, d1, n2, d2):
    x = gcd(d1, d2)
    frac = (((n1 * d2) + (n2 * d1)) / x, (d1 * d2) / x)

    return frac


def root(exponent, number):
    rootAnswer = number**(1/exponent)
    # print(rootAnswer)

    return rootAnswer


def geometricCreate(start, multiplier, length):
    betweens = []
    newinterval = start
    for i in range(int(length - 1)):
        newinterval = newinterval * multiplier
        betweens.append(str(newinterval))
    print(f'Geometric Sequence Created: {start}, {", ".join(betweens)}')


def linearCreate(start, interval, length):
    betweens = []
    newinterval = start
    for i in range(int(length - 1)):
        newinterval = newinterval + interval
        if newinterval == int(newinterval):
            betweens.append(str(int(newinterval)))
        else:
            betweens.append(str(newinterval))
    print(f'Linear Sequence Created: {start}, {", ".join(betweens)}')


def timeElapsed(function, *args):
    from timeit import default_timer as timer

    startTime = timer()
    params = []
    if len(args) != 0:
        for param in args:
            params.append(param)
        try:
            function(*params)
            endTime = timer()
            elapsed = (endTime - startTime)
            elapsed = '{:f}'.format(elapsed).rstrip('0')
            print(f'[Finished in {elapsed}s]')
        except:
            raise Exception("Unable to call function with params")
    else:
        try:
            function()
            endTime = timer()
            elapsed = float(endTime - startTime)
            elapsed = '{:f}'.format(elapsed).rstrip('0')
            print(f'[Finished in {elapsed}s]')
        except:
            raise Exception("Unable to call function")


def quadraticSequenceCreate(a, b, c, length):
    numbers = []
    for i in range(length):
        i += 1
        number = (i**2)*a
        number = number + (i*b+c)
        numbers.append(str(number))
    print(f'{", ".join(numbers)}')

    return numbers


def quadraticSequenceSolve(quadraticList):
    length = len(quadraticList)
    firstPair = 0
    secondPair = 1
    pairs = []
    # calculates 1st difference
    for i in range(length - 1):
        pair1 = quadraticList[firstPair + i]
        pair2 = quadraticList[secondPair + i]
        pairDifference = pair2 - pair1
        pairs.append(pairDifference)
        # print(f"1st Difference: {pairDifference}  Index: {i}")
    firstPair = 0
    secondPair = 1
    pairs2 = []
    # calculates 2nd difference
    for i in range(length-2):
        pair1 = pairs[firstPair + i]
        pair2 = pairs[secondPair + i]
        pairDifference = pair2 - pair1
        pairs2.append(pairDifference)
        # print(f"2nd Difference: {pairDifference}  Index: {i}")
    # checks if 2nd differences are the same
    for pair in pairs2:
        if pairs2[0] != pair:
            print(f"Not quadratic sequence  2nd Differences: {pairs2}")
            return
    # print(f"The sequence is a quadratic  2nd Difference: {pairs2[0]}")
    # the double slash '//' rounds it to the nearest integer
    a = pairs2[0]//2

    # calculates bn + c from the an^2 + bn + c
    quadraticSequence = quadraticSequenceCreate(a, 0, 0, length)
    quadraticDifferenceList = []
    for i in range(length):
        number = int(quadraticList[i]) - int(quadraticSequence[i])
        quadraticDifferenceList.append(str(number))
    # print(f'{", ".join(quadraticDifferenceList)}')
    firstPair = 0
    secondPair = 1
    pairs3 = []
    # calculates 1st difference
    for i in range(length - 1):
        pair1 = int(quadraticDifferenceList[firstPair + i])
        pair2 = int(quadraticDifferenceList[secondPair + i])
        pairDifference = pair2 - pair1
        pairs3.append(str(pairDifference))
        # print(f"1st Difference: {pairDifference}  Index: {i}")
    for pair in pairs3:
        if pairs3[0] != pair:
            print(
                f"Difference of quadratic sequences don't have a common difference  1st Differences: {pairs3}")
            return
    b = int(pairs3[0])
    c = int(quadraticDifferenceList[0]) - b
    newQuadratic = quadraticSequenceCreate(a, b, c, length+4)
    print(f'a: {a}  b: {b}  c: {c}  Sequence: {", ".join(newQuadratic)}')


def lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcmNumber = greater
            break
        greater += 1

    print(f"The LCM is: {lcmNumber}")

    return lcm


def compute_gcd(x, y):
    while y:
        x, y = y, x % y

    print(f"The GCD is: {x}")

    return x


def hcf(x, y):
    r = y
    while r != 0:
        y = r
        r = x % y
        x = y

    # print(f"The GCD is: {x}")

    return x


def lcm2(x, y):
    # This function computes LCM
    lcm = (x*y)//hcf(x, y)

    # print(f"The LCM is: {lcm}")

    return lcm


def simulatenousSolve(set1, sum1, set2, sum2):
    # [a1,b1,c1], [a2,b2,c2], x, y
    if len(set1) != len(set2):
        print(f"Sets not equal  Set 1: {len(set1)} Set 2: {len(set2)}")
    setIndex = random.randint(-1, len(set1)-1)
    multiplier = lcm(set1[setIndex], set2[setIndex])
    multiplier1 = multiplier//set1[setIndex]
    multiplier2 = multiplier // set2[setIndex]

    newSet1 = []
    newSet2 = []
    for i in range(len(set1)):
        newSet1.append(str(set1[i]*multiplier1))
        newSet2.append(str(set2[i]*multiplier2))
    print(f'Set 1: {", ".join(newSet1)}')
    print(f'Set 2: {", ".join(newSet2)}')


def linearSequenceSolve(linearList):
    length = len(linearList)
    firstPair = 0
    secondPair = 1
    pairs = []
    # calculates 1st difference
    for i in range(length - 1):
        pair1 = linearList[firstPair + i]
        pair2 = linearList[secondPair + i]
        pairDifference = pair2 - pair1
        pairs.append(pairDifference)
    for pair in pairs:
        if pairs[0] != pair:
            print(f"Not Linear sequence  1st Differences: {pairs}")
            return
        else:
            a = pairs[0]
    b = linearList[0] - a
    if b == 0:
        print(f"Nth Term: {a}n")
    elif b < 0:
        print(f"Nth Term: {a}n{b}")
    else:
        print(f"Nth Term: {a}n+{b}")
    newSequence = linearSequenceCreate(a, b, 10)
    print(f"Sequence: {', '.join(newSequence)}")

    return a, b


def linearSequenceCreate(a, b, length):
    linearList = []
    for i in range(length):
        number = a*(i+1)+b
        linearList.append(str(number))
    # print(f"Linear Sequence: {', '.join(linearList)}")

    return linearList


def printReturn(args):
    printStatus = False
    for ar in args:
        ar = str(ar)
        if ar == 'y' or ar == 'yes' or ar == 'True':
            printStatus = True

    return printStatus


def quadraticCreate(a, b, c, length, *args):
    quadraticList = []
    for i in range(length):
        i += 1
        number = a * (i ** 2) + b * i + c
        quadraticList.append(str(number))
    if printReturn(args):
        print(f"Quadratic Sequence: {', '.join(quadraticList)}")

    return quadraticList


def quadraticSolve(a, length, *args):
    b = 0
    c = 0
    interval = 0
    quadraticList = quadraticCreate(a, b, c, 2*length, True)
    while interval <= length:
        b += 2*a
        c = 0
        while c <= int(quadraticList[length*2-1]):
            c += 1
            newQuadratic = quadraticCreate(a, b, c, length, *args)
            print(newQuadratic)
            # print(quadraticList)
            for f in range(len(newQuadratic)):
                if newQuadratic[0] == quadraticList[f]:
                    interval = f
                else:
                    quadraticSame = False
                    break
                if newQuadratic[f] == quadraticList[f+interval]:
                    quadraticSame = True
                else:
                    quadraticSame = False
            if quadraticSame:
                print(f"a: {a}  b: {b}  c: {c}")
                print(f"Sequence: {', '.join(newQuadratic)}")
                print(f"Check:    {', '.join(quadraticCreate(a, b, c, 10))}")


def checkPrime(number, *args):
    number = int(number)
    primeState = True
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            if printReturn(args):
                print(f"Number is divisible by {i}")
            primeState = False
    if primeState:
        if printReturn(args):
            print(f"{number} is a prime")
    else:
        if printReturn(args):
            print(f"{number} is NOT a prime")

    return primeState


def listPrimes(start, length, *args):
    primesList = []
    for i in range(start, length):
        primeStatus = checkPrime(i, *args)
        if primeStatus:
            prime = i
            primesList.append(str(prime))
    print(f"Primes: {', '.join(primesList)}")


def stampToDate(timeStamp, *args):
    from datetime import datetime

    date = datetime.fromtimestamp(timeStamp)
    if printReturn(args):
        print(date)


def quadraticSolver(a, b, c):
    discriminant = (b**2-4*a*c)**(1/2)
    solutions = [((-b+discriminant)/2*a), ((-b-discriminant)/2*a)]
    for i in range(len(solutions)):
        solutions[i] = f"x = {solutions[i]}"
    print(' '.join(str(solution) for solution in solutions))


def interiorAngle(sides):
    return 180-(360/int(sides))


def exteriorAngle(sides):
    return 360/int(sides)


if __name__ == '__main__':
    timeElapsed(stampToDate, 1654962147, True)
    # timeElapsed(interiorAngle(5))
    # timeElapsed(exteriorAngle(5))
    # timeElapsed(quadraticSolve(1, 10, False))
    # timeElapsed(checkPrime, 4, True)
    # timeElapsed(listPrimes, 1, 100, False)
    # timeElapsed(quadraticSolve, 1, 4, 2, 10, True)
    # timeElapsed(linearSequenceCreate, 3, 5, 10)
    # timeElapsed(linearSequenceSolve, [3, 7])
    # timeElapsed(simulatenousSolve, [3, 4], 24, [4, 3], 22)
    # timeElapsed(hcf, 22, 68)
    # timeElapsed(lcm, 22, 72)
    # timeElapsed(quadraticSequenceSolve, [6, 10, 20])
    # timeElapsed(quadraticSequenceCreate, 2, -4, -3, 11)
    # quadraticSolver(1, 5, 6)
    # linearSolve(9, 1, 1)
    # geometricSolve(1, 16, 3)
    # geometricCreate(1, 2, 8)
    # linearCreate(1, 5, 8)
    # ratioSimplify('3:9:57')
    pass
