# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80,scale=10,size=100)
scores = np.clip(scores,0,100)

plt.title('Exam Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.hist(scores)
plt.show()