import math


class SineGenerator:
    def __init__(self):
        pass

    def generate(self, xes, a, b):
        result = []
        for i in range(0, len(xes)):
            val = xes[i]
            result.append(a * math.sin(b * val))
        return result