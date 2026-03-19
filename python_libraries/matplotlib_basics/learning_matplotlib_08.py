# Author: Rodrigo Souza Galvão
# Creation Date: March 19th 2026
# Last Modification: March 19th 2026

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("database.csv")

typeCount = df["Type1"].value_counts(ascending=True)

plt.barh(typeCount.index, typeCount.values)
plt.title("Number of pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()