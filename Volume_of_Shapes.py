PI = 3.14159265359
ROUND = 2


def frustumVolume(baseShape='rectangle', frustumHeight=1, baseLength=1, baseWidth=1, frustumLength=1, frustumWidth=1, log=True):
    if baseShape.lower() == 'triangle':
        baseArea = 1 / 2 * baseLength * baseWidth
        frustumArea = 1 / 2 * frustumLength * frustumWidth
        volume = round(frustumHeight / 3 * (baseArea + frustumArea + (baseArea * frustumArea) ** (1 / 2)), ROUND)
    elif baseShape.lower() == 'circle':
        volume = round(1 / 3 * PI * frustumHeight * ((frustumLength / 2) ** 2 + (baseLength / 2) ** 2 + ((frustumLength / 2) * (baseLength / 2))), ROUND)
    else:
        baseArea = baseLength * baseWidth
        frustumArea = frustumLength * frustumWidth
        volume = round(frustumHeight / 3 * (baseArea + frustumArea + (baseArea * frustumArea) ** (1 / 2)), ROUND)

    if log == True:
        print(f"Volume: {volume}")

    return volume


def conicalFrustum(version=1, frustumHeight=1, baseRadius=1, frustumRadius=1):
    if version == 1:
        return round(1 / 3 * PI * frustumHeight * (frustumRadius ** 2 + baseRadius ** 2 + (frustumRadius * baseRadius)), ROUND)
    else:
        return round((frustumHeight * PI * (baseRadius ** 3 - frustumRadius ** 3)) / (3 * (baseRadius - frustumRadius)), ROUND)


__all__ = [
    frustumVolume
]
