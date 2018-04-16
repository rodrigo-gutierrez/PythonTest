import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = np.sin(x)

plt.scatter(x, y)
plt.show()
