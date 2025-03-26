import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

f = lambda x: x**3 +2**2 - 1

root = bisect(f, -3, 3,full_output=True)
print(root)


x = np.linspace(-3,3, 100)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = x^3 - 6x^2 + 4x + 12', color='blue')
plt.axhline(0, color='black', linewidth=1.3, linestyle='--')  # X-axis
plt.axvline(root[0], color='red', linestyle='--', label=f'Root at x={root[0]:.4f}')  # Root
plt.scatter(root[0], 0, color='red', zorder=3)


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method Root Finding')
plt.legend()
plt.grid()
plt.show()