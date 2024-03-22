import pandas as pd, numpy as np, matplotlib.pyplot as plt

car = ["BMW", "Bentley", "Ferrari", "Pagani", "Audi"]
votes = [600, 350, 900, 670, 450]

# Let's create a box plot!
plt.boxplot(votes)
plt.show()

# How do you read a box plot?
# The yellow line in box plot represents the median.
# The upper line represents the maximum value while the bottom line shows the minimum value.
# Below the median line is the first quartile, median line is the second and above median is third quartile which is used to divide the data into 4 equal parts.
# It is mostly used to check out the distribution of a dataset.
# The quartile box (3rd to median or 1st to median) shows the range of most of the dataset about where it lies.

# The chapter was small yet important and such box plots are pretty useful when you want to find insights about the variation of your dataset.