import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(data, xes, label, type):
        plt.plot(xes, data, type)
        plt.ylabel(label)

    @staticmethod
    def show():
        plt.show()
