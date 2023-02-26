PI = 3.14159265359
ROUND = 2


def circleArea(radius):
    area = round((radius**2*PI), ROUND)
    print(f"Area: {area}")


def circleData(radius):
    diameter = radius * 2
    circumference = round(diameter * PI, ROUND)
    area = round((radius ** 2 * PI), ROUND)
    print(f"Diameter: {diameter}")
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")


def calculateDensity(volume, mass):
    density = round(mass / volume, ROUND)
    print(f"Density: {density}")


def calculateMass(volume, density):
    mass = round(density * volume, ROUND)
    print(f"Mass: {mass}")


def calculateVolume(mass, density):
    volume = round(mass / density, ROUND)
    print(f"Volume: {volume}")


def cylinderSurfaceArea(radius, height):
    surfaceArea = ((radius**2*2) + (2*radius*height))
    print(f"Surface Area: {round(surfaceArea * PI, ROUND)}")
    print(f"Surface Area: {round(surfaceArea, ROUND)}π")


__all__ = [
    circleArea,
    circleData,
    calculateDensity,
    calculateMass,
    calculateVolume,
    cylinderSurfaceArea
]
