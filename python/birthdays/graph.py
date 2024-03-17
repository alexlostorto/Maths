import matplotlib.pyplot as plt


class Graph:
    def __init__(self, ):
        self.x = []
        self.y = []

    def update(self, x, y):
        self.x.append(x)
        self.y.append(y)

        plt.plot(self.x, self.y)
        plt.show(block=False)
