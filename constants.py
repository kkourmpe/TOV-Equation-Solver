import numpy as np

r_start = 1.0e-10
r_end = 20.0
num_points = 10000

r_values = np.linspace(r_start, r_end, num_points)

hbarc = 197.327

step = (r_end - r_start) / num_points
