# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])


figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x*2)
axes[0,0].set_title("Graph x*2")

axes[0,1].plot(x, x**2)
axes[0,1].set_title("Graph x**2")

axes[1,0].plot(x, x**3)
axes[1,0].set_title("Graph x**3")

axes[1,1].plot(x, x**4)
axes[1,1].set_title("Graph x*2")

plt.tight_layout()
plt.show()