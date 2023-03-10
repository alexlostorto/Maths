<h1 align="center">Maths Functions</h1>

This program contains many maths functions which you will probably find useful!

```python
# List of functions
def linearSolve(start, end, between):
def geometricSolve(start, end, between):
def ratioSimplify(ratiostr):
def addFractions(n1, d1, n2, d2):
def root(exponent, number):
def geometricCreate(start, multiplier, length):
def linearCreate(start, interval, length):
def timeElapsed(function, *args):
def quadraticSequenceCreate(a, b, c, length):
def quadraticSequenceSolve(quadraticList):
def lcm(x, y):
def gcd(x, y):
def hcf(x, y):
def lcm2(x, y):
def simulatenousSolve(set1, sum1, set2, sum2):
def linearSequenceSolve(linearList):
def linearSequenceCreate(a, b, length):
def printReturn(args):
def quadraticCreate(a, b, c, length, *args):
def quadraticSolve(a, length, *args):
def checkPrime(number, *args):
def listPrimes(start, length, *args):
def stampToDate(timeStamp, *args):
def quadraticSolver(a, b, c):
def interiorAngle(sides):
def exteriorAngle(sides):
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
