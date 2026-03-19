# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

x = [n for n in range(1,6)]
y = [n*5 for n in range(1,6)]

plt.grid(axis="both",
         linewidth=2,
         color="#cccccc",
         linestyle="dashed")

plt.plot(x,y)
plt.show()
