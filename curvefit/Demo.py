import math
import numpy as np
from numpy import arange

from curvefit.Fitter import Fitter
from curvefit.Plotter import Plotter
from curvefit.StatAnalyzer import StatAnalyzer
from curvefit.generators.NoiseSineGenerator import NoiseSineGenerator
from curvefit.generators.SineGenerator import SineGenerator


def sine(x, a, b):
    return a * np.sin(b * x)


def line(x, a, b):
    return a * x + b


if __name__ == "__main__":
    noise = 0.4
    parama = 1
    paramb = 1

    sineGenerator = SineGenerator()
    noiseSine = NoiseSineGenerator(noise)
    xses = np.asarray(arange(0, 2 * math.pi, 0.01)).ravel()

    yses = noiseSine.generate(xses, parama, paramb)
    ysesSine = sineGenerator.generate(xses, parama, paramb)

    Plotter.plot(ysesSine, xses, "Sinus", 'r')
    Plotter.plot(yses, xses, "Sinus", 'bo')

    ysesNumpy = np.asarray(yses).ravel()
    ysesFit = None
    guess = 1.0
    oldp = None
    p = float("inf")
    sign = True
    step = 0.1
    guessa = np.abs((np.amax(ysesNumpy)) + np.abs(np.amin(ysesNumpy)))/2

    while True:
        oldp = p
        popt, popz = Fitter.fit(sine, xses, ysesNumpy, [guessa, guess])
        ysesFit = sineGenerator.generate(xses, popt[0], popt[1])
        p = StatAnalyzer.chi_square_test(ysesSine, ysesFit)
        print "p_val: " + str(math.fabs(p)) + ", guess: " + str(guess) + ", " + str(guessa)
        if math.fabs(p) < 0.05:
            break
        guess += step

    Plotter.plot(ysesFit, xses, "SinusFit", 'g')
    Plotter.show()

