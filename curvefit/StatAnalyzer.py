import math


class StatAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def chi_square_test(theoretical, actual):
        chisq = 0
        for i in range(0, len(actual)):
            if theoretical[i] != 0.0:
                chisq += (math.pow(actual[i] - theoretical[i], 2))/theoretical[i]
        return chisq
