# Pie Charts
# Author: Stefanie Steffens

import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(["Apfel", "Banaan", "Blueberry", "Erdbeere", "Knoblauch", "Radieschen"])
numbers = np.array([23, 77, 201, 55, 79, 80])
colours = ["green", "yellow", "blue", "red", "#BA55D3", "#FF69B4"]

plt.title("Fruchtfreunde")
plt.pie(numbers, labels = fruit, startangle = 90, colors = colours)
# plt.legend()
plt.show()
