from scipy.optimize import curve_fit


class Fitter:
    def __init__(self):
        pass

    @staticmethod
    def fit(method, xs, ys, initguess):
        return curve_fit(method, xs, ys, p0=initguess)
