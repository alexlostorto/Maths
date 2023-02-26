PI = 3.14159265359
ROUND = 2


def circleArea(radius, log=True):
    area = round((radius**2*PI), ROUND)

    if log == True:
        print(f"Area: {area}")

    return area


def circleData(radius, log=True):
    diameter = radius * 2
    circumference = round(diameter * PI, ROUND)
    area = round((radius ** 2 * PI), ROUND)

    if log == True:
        print(f"Diameter: {diameter}")
        print(f"Circumference: {circumference}")
        print(f"Area: {area}")

    return diameter, circumference, area


def calculateDensity(volume, mass, log=True):
    density = round(mass / volume, ROUND)

    if log == True:
        print(f"Density: {density}")

    return density


def calculateMass(volume, density, log=True):
    mass = round(density * volume, ROUND)

    if log == True:
        print(f"Mass: {mass}")

    return mass


def calculateVolume(mass, density, log=True):
    volume = round(mass / density, ROUND)

    if log == True:
        print(f"Volume: {volume}")

    return volume


def cylinderSurfaceArea(radius, height, log=True):
    surfaceArea = ((radius**2*2) + (2*radius*height))

    if log == True:
        print(f"Surface Area: {round(surfaceArea * PI, ROUND)}")
        print(f"Surface Area: {round(surfaceArea, ROUND)}π")

    return round(surfaceArea * PI, ROUND), round(surfaceArea, ROUND) + "π"


__all__ = [
    circleArea,
    circleData,
    calculateDensity,
    calculateMass,
    calculateVolume,
    cylinderSurfaceArea
]
