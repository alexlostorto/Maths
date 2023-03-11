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


def prismSurfaceArea(face='rectangle', length=1, width=1, height=1, log=True):
    if face == 'triangle':
        surfaceArea = length * height + width * length + width * height + width * (length ** 2 + height ** 2) ** (1 / 2)
    else:
        surfaceArea = 2 * length * width + 2 * width * height + 2 * length * height

    if log == True:
        print(f"Surface Area: {surfaceArea}")

    return surfaceArea


def pyramidSurfaceArea(base='square', length=1, baseHeight=1, slantHeight=1, log=True):
    if base == 'triangle':
        surfaceArea = 0.5 * baseHeight * length + 1.5 * length * slantHeight
    else:
        surfaceArea = length * baseHeight + length * slantHeight + baseHeight * slantHeight

    if log == True:
        print(f"Surface Area: {surfaceArea}")

    return surfaceArea


__all__ = [
    circleArea,
    circleData,
    calculateDensity,
    calculateMass,
    calculateVolume,
    cylinderSurfaceArea,
    prismSurfaceArea,
    pyramidSurfaceArea
]
