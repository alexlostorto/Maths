# To measure speed
import timeit


def main():
    print(timeit.timeit('conicalFrustum(version=1, frustumHeight=10, baseRadius=20, frustumRadius=15)', number=10000, setup="from Volume_of_Shapes import conicalFrustum"))
    print(timeit.timeit('conicalFrustum(version=2, frustumHeight=10, baseRadius=20, frustumRadius=15)', number=10000, setup="from Volume_of_Shapes import conicalFrustum"))


if __name__ == '__main__':
    main()
