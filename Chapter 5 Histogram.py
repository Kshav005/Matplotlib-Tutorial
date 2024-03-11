# In this chapter, we will study about histogram.
import pandas as pd, matplotlib.pyplot as plt, random


df = pd.read_csv("file.csv")

# To display a histogram, we use a function 'hist'
plt.hist(df["x-axis"])
plt.show()

# The data tells how many times, a certain data has occured.