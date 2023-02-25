PI = 3.14159265359
ROUND = 2


def frustumVolume(baseShape='rectangle', frustumHeight=1, baseLength=1, baseWidth=1, frustumLength=1, frustumWidth=1):
    if baseShape.lower() == 'triangle':
        baseArea = 1 / 2 * baseLength * baseWidth
        frustumArea = 1 / 2 * frustumLength * frustumWidth
    elif baseShape.lower() == 'circle':
        return 1 / 3 * PI * frustumHeight * ((frustumLength / 2) ** 2 + (baseLength / 2) ** 2 + ((frustumLength / 2) * (baseLength / 2)))
    else:
        baseArea = baseLength * baseWidth
        frustumArea = frustumLength * frustumWidth

    return frustumHeight / 3 * (baseArea + frustumArea + (baseArea * frustumArea) ** (1 / 2))


if __name__ == '__main__':
    print(frustumVolume(baseShape='circle',
          frustumHeight=20, baseLength=54, frustumLength=18))
