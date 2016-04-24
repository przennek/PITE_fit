import numpy as np

class NoiseSineGenerator:
    noiseVal = None
    randXGen = None

    def __init__(self, noiseVal=0.1):
        self.noiseVal = noiseVal

    def generate(self, xes, a, b):
        result = []
        for i in range(0, len(xes)):
            x = xes[i]
            val = a * np.sin(x * b) + np.random.uniform(-self.noiseVal, self.noiseVal)
            result.append(val)
        return result