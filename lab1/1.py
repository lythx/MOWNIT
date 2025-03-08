import numpy as np
import sys

eps = sys.float_info.epsilon

def df_numeric(f, x, h):
    return (f(x + h) - f(x)) / h

x = 1

df = 1 + np.tan(x)**2

h_values = np.array([10**-k for k in range(17)])
truncation_errors = np.array([df_numeric(np.tan, x, h) - df for h in h_values])
rounding_errors = np.array([2 * eps / h for h in h_values])
computational_errors = np.array([x + y for (x, y) in zip(truncation_errors, rounding_errors)])

