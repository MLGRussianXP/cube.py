from math import sin, cos
from sys import stdout

A, B, C = 0, 0, 0

cubeWidth = 40
width, height = 160, 44
zBuffer, buffer = [], []
backgroundASCIICode = ' '
distanceFromCam = 100
K1 = 40

incrementSpeed = 0.6


def calculateX(i, j, k):
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + \
           j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C)


def calculateY(i, j, k):
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - \
           j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) - \
           i * cos(B) * sin(C)


def calculateZ(i, j, k):
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)


def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch


print("\x1b[2J")
while True:
    buffer = [backgroundASCIICode] * width * height
    zBuffer = [0] * width * height

    cubeWidth = 20
    horizontalOffset = -2 * cubeWidth
    # first cube
    cubeX = -cubeWidth
    while cubeX < cubeWidth:
        cubeY = -cubeWidth
        while cubeY < cubeWidth:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')
            cubeY += incrementSpeed
        cubeX += incrementSpeed

    cubeWidth = 10
    horizontalOffset = 1 * cubeWidth
    # second cube
    cubeX = -cubeWidth
    while cubeX < cubeWidth:
        cubeY = -cubeWidth
        while cubeY < cubeWidth:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')
            cubeY += incrementSpeed
        cubeX += incrementSpeed

    cubeWidth = 5
    horizontalOffset = 8 * cubeWidth
    # third cube
    cubeX = -cubeWidth
    while cubeX < cubeWidth:
        cubeY = -cubeWidth
        while cubeY < cubeWidth:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')
            cubeY += incrementSpeed
        cubeX += incrementSpeed

    print("\x1b[H")
    for k in range(width * height):
        stdout.write(str(buffer[k]))

    A += 0.05
    B += 0.05
    C += 0.01
