# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

categories = ["Grains","Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
values = [4,3,2,5,3,1]

plt.bar(categories, values, color="#3333ff")
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()