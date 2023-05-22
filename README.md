<h1 align="center">Maths Functions</h1>

This program contains many maths functions which you will probably find useful!

```python
# List of functions
def linearSolve(start, end, between, log=True):
def geometricSolve(start, end, between, log=True):
def ratioSimplify(ratiostr, log=True):
def addFractions(n1, d1, n2, d2, log=True):
def root(exponent, number, log=True):
def geometricCreate(start, multiplier, length, log=True):
def linearCreate(start, interval, length, log=True):
def timeElapsed(function, *args):
def quadraticSequenceCreate(a, b, c, length, log=True):
def quadraticSequenceSolve(quadraticList, log=True):
def lcm(x, y, version=1, log=True):
def gcd(x, y, log=True):
def hcf(x, y, log=True):
def simulatenousSolve(set1, sum1, set2, sum2, log=True):
def linearSequenceSolve(linearList, log=True):
def linearSequenceCreate(a, b, length, log=True):
def printReturn(args):
def quadraticCreate(a, b, c, length, log=True):
def quadraticSolve(a, length, log=True):
def checkPrime(number, log=True):
def listPrimes(start, length, log=True):
def stampToDate(timeStamp, log=True):
def quadraticSolver(a, b, c, log=True):
def interiorAngle(sides, log=True):
def exteriorAngle(sides, log=True):
def completeTheSquare(a, b, c, log=True):
def expandDoubleBrackets(a1, b1, a2, b2, log=True):
```

## How it Works

#### Interior Angle

1. Find the exterior angle by doing 360 divided by the number of sides. Then use angles on a straight line to work out the interior angle.

```python
return 180-(360/int(sides))
```

#### Exterior Angle

1. Find the exterior angle by doing 360 divided by the number of sides.

```python
return 360/int(sides)
```

#### Quadratic Solve

1. Solves quadratic equations using the quadratic formula and prints both possible values.

```python
discriminant = (b**2-4*a*c)**(1/2)
solutions = [((-b+discriminant)/2*a), ((-b-discriminant)/2*a)]
for i in range(len(solutions)):
    solutions[i] = f"x = {solutions[i]}"
print(' '.join(str(solution) for solution in solutions))
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
