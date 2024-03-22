# In this chapter, we will study about histogram.
import pandas as pd, matplotlib.pyplot as plt, random

# Remember, the difference between bar graph and histogram is that histogram is used to look at the frequency distribution. On the x-axis, we will have the list of choices that people chose and on y-axis will be there frequencies.

votes = ["hey", "no", "life", "life", "hail", "yes", "what", "hey", "no", "no", "left", "yes"]

# To display a histogram, we use a function 'hist'
plt.hist(votes)
plt.show()

# The data tells how many times, a certain point has occured.