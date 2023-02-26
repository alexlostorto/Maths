# Lengths (compared to 1 meter)
METER = 1
KILOMETER = 1000
DECIMETER = 0.1
CENTIMETER = 0.01
MILLIMETER = 0.001
MICROMETER = 0.000001
NANOMETER = 0.000000001
MILE = 1609.344
YARD = 0.9144
FOOT = 0.3048
INCH = 0.0254
LIGHT_YEAR = 9460730472580044
EXAMETER = 1000000000000000000
PETAMETER = 1000000000000000
TERAMETER = 1000000000000
GIGAMETER = 1000000000
MEGAMETER = 1000000
HECTOMETER = 100
DEKAMETER = 10
MICRON = 0.000001
PICOMETER = 0.000000000001
FEMTOMETER = 0.000000000000001

# Times (compared to 1 second)
SECOND = 1
MILLISECOND = 0.001
MINUTE = 60
HOUR = 3600
DAY = 86400
WEEK = 604800
MONTH = 2628000
YEAR = 31557600
DECADE = 315576000
CENTURY = 3155760000
MILLENIUM = 31557600000
MICROSECOND = 0.000001
NANOSECOND = 0.000000001
PICOSECOND = 0.000000000001
FEMTOSECOND = 0.000000000000001
ATTOSECOND = 0.000000000000000001

# Custom
MILE = 1600


def convert(number, initial, final, roundTo=3):
    try:
        initial
    except NameError:
        print("Initial unit was not defined")
    try:
        final
    except NameError:
        print("Final unit was not defined")

    return round(number * initial / final, roundTo)


def convertSpeed(number, initialLength, initialTime, finalLength, finalTime, roundTo=3):
    try:
        initialLength
    except NameError:
        print("Initial length unit was not defined")
    try:
        initialTime
    except NameError:
        print("Initial time unit was not defined")
    try:
        finalLength
    except NameError:
        print("Final length unit was not defined")
    try:
        finalTime
    except NameError:
        print("Final time unit was not defined")

    return round(number * initialLength / initialTime / finalLength * finalTime, roundTo)


__all__ = [
    convert,
    convertSpeed
]
