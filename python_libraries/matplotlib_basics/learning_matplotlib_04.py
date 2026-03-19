# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores","Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
colors = ["Blue", "Gray", "Green", "Red"]

plt.pie(values, labels=categories, 
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.1],
                startangle=45)
plt.title("Bro Code College")
plt.show()