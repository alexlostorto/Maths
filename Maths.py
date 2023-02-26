from math import gcd
import random
import re


def floatToString(inputValue, symbol=True):
    if inputValue >= 0 and symbol == True:
        return '+' + ('%.15f' % inputValue).rstrip('0').rstrip('.')
    else:
        return ('%.15f' % inputValue).rstrip('0').rstrip('.')


def linearSolve(start, end, between, log=True):
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

    if log == True:
        print(f'Linear sequence: {start}, {", ".join(betweens)}, {end}')

    return [start, ", ".join(betweens), end]


def geometricSolve(start, end, between, log=True):
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

    if log == True:
        print(f'Geometric sequence: {start}, {", ".join(betweens)}, {end}')

    return [start, ", ".join(betweens), end]


def ratioSimplify(ratiostr, log=True):
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

    if log == True:
        print(f'Simplified ratio: {":".join(simplified)}')

    return ":".join(simplified)


def addFractions(n1, d1, n2, d2, log=True):
    x = gcd(d1, d2)
    frac = (((n1 * d2) + (n2 * d1)) / x, (d1 * d2) / x)

    if log == True:
        print(f'Fraction: {frac}')

    return frac


def root(exponent, number, log=True):
    rootAnswer = number**(1/exponent)

    if log == True:
        print(f'Root: {rootAnswer}')

    return rootAnswer


def geometricCreate(start, multiplier, length, log=True):
    betweens = []
    newinterval = start
    for i in range(int(length - 1)):
        newinterval = newinterval * multiplier
        betweens.append(str(newinterval))

    if log == True:
        print(f'Geometric sequence: {start}, {", ".join(betweens)}')

    return [start, ", ".join(betweens)]


def linearCreate(start, interval, length, log=True):
    betweens = []
    newinterval = start
    for i in range(int(length - 1)):
        newinterval = newinterval + interval
        if newinterval == int(newinterval):
            betweens.append(str(int(newinterval)))
        else:
            betweens.append(str(newinterval))

    if log == True:
        print(f'Linear sequence: {start}, {", ".join(betweens)}')

    return [start, ", ".join(betweens)]


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


def quadraticSequenceCreate(a, b, c, length, log=True):
    numbers = []
    for i in range(length):
        i += 1
        number = (i**2)*a
        number = number + (i*b+c)
        numbers.append(str(number))

    if log == True:
        print(f'{", ".join(numbers)}')

    return ", ".join(numbers)


def quadraticSequenceSolve(quadraticList, log=True):
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

    if log == True:
        print(f'a: {a}  b: {b}  c: {c}  Sequence: {", ".join(newQuadratic)}')

    return [a, b, c, ", ".join(newQuadratic)]


def lcm(x, y, log=True):
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

    if log == True:
        print(f"The LCM is: {lcmNumber}")

    return lcmNumber


def gcd(x, y, log=True):
    while y:
        x, y = y, x % y

    if log == True:
        print(f"The GCD is: {x}")

    return x


def hcf(x, y, log=True):
    r = y
    while r != 0:
        y = r
        r = x % y
        x = y

    if log == True:
        print(f"The HCF is: {x}")

    return x


def lcm2(x, y, log=True):
    # This function computes LCM
    lcm = (x*y)//hcf(x, y)

    if log == True:
        print(f"The LCM is: {lcm}")

    return x


def simulatenousSolve(set1, sum1, set2, sum2, log=True):
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

    if log == True:
        print(f'Set 1: {", ".join(newSet1)}')
        print(f'Set 2: {", ".join(newSet2)}')

    return [", ".join(newSet1), ", ".join(newSet2)]


def linearSequenceSolve(linearList, log=True):
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
    newSequence = linearSequenceCreate(a, b, 10)
    print(f"Sequence: {', '.join(newSequence)}")

    if log == True:
        if b == 0:
            print(f"Nth Term: {a}n")
        elif b < 0:
            print(f"Nth Term: {a}n{b}")
        else:
            print(f"Nth Term: {a}n+{b}")

    return a, b


def linearSequenceCreate(a, b, length, log=True):
    linearList = []
    for i in range(length):
        number = a*(i+1)+b
        linearList.append(str(number))

    if log == True:
        print(f"Linear Sequence: {', '.join(linearList)}")

    return linearList


def printReturn(args):
    printStatus = False
    for ar in args:
        ar = str(ar)
        if ar == 'y' or ar == 'yes' or ar == 'True':
            printStatus = True

    return printStatus


def quadraticCreate(a, b, c, length, log=True):
    quadraticList = []
    for i in range(length):
        i += 1
        number = a * (i ** 2) + b * i + c
        quadraticList.append(str(number))

    if log == True:
        print(f"Quadratic Sequence: {', '.join(quadraticList)}")

    return quadraticList


def quadraticSolve(a, length, log=True):
    b = 0
    c = 0
    interval = 0
    quadraticList = quadraticCreate(a, b, c, 2*length, True)
    while interval <= length:
        b += 2*a
        c = 0
        while c <= int(quadraticList[length*2-1]):
            c += 1
            newQuadratic = quadraticCreate(a, b, c, length, log)
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


def checkPrime(number, log=True):
    number = int(number)
    primeState = True
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            if log == True:
                print(f"Number is divisible by {i}")
            primeState = False
    if primeState:
        if log == True:
            print(f"{number} is a prime")
    else:
        if log == True:
            print(f"{number} is NOT a prime")

    return primeState


def listPrimes(start, length, log=True):
    primesList = []
    for i in range(start, length):
        primeStatus = checkPrime(i, log)
        if primeStatus:
            prime = i
            primesList.append(str(prime))

    if log == True:
        print(f"Primes: {', '.join(primesList)}")

    return ', '.join(primesList)


def stampToDate(timeStamp, log=True):
    from datetime import datetime

    date = datetime.fromtimestamp(timeStamp)

    if log == True:
        print(date)

    return date


def quadraticSolver(a, b, c, log=True):
    discriminant = (b**2-4*a*c)**(1/2)
    solutions = [((-b+discriminant)/2*a), ((-b-discriminant)/2*a)]
    for i in range(len(solutions)):
        solutions[i] = f"x = {solutions[i]}"

    if log == True:
        print(' '.join(str(solution) for solution in solutions))

    return ' '.join(str(solution) for solution in solutions)


def interiorAngle(sides, log=True):
    if log == True:
        print(f"Interior angle: {180-(360/int(sides))}")

    return 180-(360/int(sides))


def exteriorAngle(sides, log=True):
    if log == True:
        print(f"Exterior angle: {360/int(sides)}")

    return 360/int(sides)


def completeTheSquare(a, b, c, log=True):
    b = b / a / 2
    c = c - a * b ** 2

    if log == True:
        print(f"Equation: {a}(𝑥²{floatToString(b)}){floatToString(c)}")

    return a, b, c


def expandDoubleBrackets(a1, b1, a2, b2, log=True):
    superscipt = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

    def mutltiplyExpressions(x, y):
        values = x + y
        coefficient = 1
        variables = []
        for value in values:
            if value.isdigit():
                coefficient *= float(value)
            elif '-' in value:
                coefficient *= -1
                variables.append(value[1:])
            else:
                variables.append(value)

        variablesDict = {}
        for variable in variables:
            if variable in variablesDict:
                variablesDict[variable] += 1
            else:
                variablesDict[variable] = 1

        return [coefficient, variablesDict]

    def simplifyExpressions(expressions):
        coefficients = []
        variables = []
        for expression in expressions:
            if expression[1] in variables:
                index = variables.index(expression[1])
                coefficients[index] += expression[0]
            else:
                coefficients.append(expression[0])
                variables.append(expression[1])

        equation = []
        for i in range(len(coefficients)):
            expression = ''
            if coefficients[i] == 0:
                continue
            elif coefficients[i] > 1:
                expression += floatToString(coefficients[i], False)
            elif coefficients[i] == -1:
                expression += '- '
            elif coefficients[i] <= -2:
                expression += '- ' + floatToString(coefficients[i]*-1, False)
            for variable, power in variables[i].items():
                if power == 1:
                    expression += variable
                else:
                    expression += variable + superscipt[power]
            equation.append(expression)

        return equation

    expressions = []
    for expression in [a1, b1, a2, b2]:
        expressions.append(
            list(filter(None, re.split('(\d+)', str(expression)))))

    multiplied = []
    for expression1 in expressions[0:2]:
        for expression2 in expressions[2:4]:
            multiplied.append(mutltiplyExpressions(expression1, expression2))

    equation = simplifyExpressions(multiplied)
    equation = ' + '.join(equation)
    equation = equation.replace('+ -', '-')

    if log == True:
        print(f"Equation: {equation}")

    return equation


__all__ = [
    linearSolve,
    geometricSolve,
    ratioSimplify,
    addFractions,
    root,
    geometricCreate,
    linearCreate,
    timeElapsed,
    quadraticSequenceCreate,
    quadraticSequenceSolve,
    lcm,
    gcd,
    hcf,
    lcm2,
    simulatenousSolve,
    linearSequenceSolve,
    linearSequenceCreate,
    printReturn,
    quadraticCreate,
    quadraticSolve,
    checkPrime,
    listPrimes,
    stampToDate,
    quadraticSolver,
    interiorAngle,
    exteriorAngle,
    completeTheSquare,
    expandDoubleBrackets
]
