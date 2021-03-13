# This program plots a list of counties into a bar chart.
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

countiesSelection = ["Mayo", "Galway", "Kerry", "Donegal", "Sloggi"]
counties = np.random.choice(
    countiesSelection, 
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size =(100)
)

unique, counts = np.unique(counties, return_counts=True)

plt.title("Counties")
plt.bar(unique, counts)
# plt.legend()
plt.show()