# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([7,23,38,5])
y3 = np.array([13,15,20,30])

plt.title("Diferença entre algoritmos de ordenção", fontsize=20,
                                                    family="Arial",
                                                    fontweight="bold",
                                                    color="#2d4cfc"
                                                    )
plt.xlabel("Year", fontsize=20,
                    fontweight="bold",
                    color="#2dbefc")

plt.ylabel("Students", fontsize=20,
                    fontweight="bold",
                    color="#2dbefc")

plt.xticks(x)
plt.tick_params(axis="both")

lineStyle = dict(marker="o",
                markersize=8,
                markerfacecolor="#ff0000",
                markeredgecolor="#00ff00",
                linestyle="dashed",
                linewidth=2,
                color="#3333ff")

plt.plot(x,y1, **lineStyle)
plt.plot(x,y2, **lineStyle)
plt.plot(x,y3, **lineStyle)

plt.show()
