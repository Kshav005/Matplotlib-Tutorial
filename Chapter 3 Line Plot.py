# We can use Line plots too. They are mostly used for time series analysis so it is harder to use csv file here. However, if we keep our x-axis constantly increasing, we can use y-axis of the file!

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("file.csv")
year = [2000 + x for x in range(20)]            # creates a list till 2019

ylabel = df["y-axis"]

plt.locator_params(integer=True)        # Used to take values in a form of integer and not in float. If you remove this line and run the command, you will see that the 'year' becomes a float in the graph
plt.plot(year, ylabel)
plt.show()

# Here too, colors can be changed and other parameters can be added.
# But if you want a thicker line
plt.plot(year, ylabel, c="r", lw=4)
plt.show()

# To change the line style 
plt.plot(year, ylabel, c="b", linestyle="--")
plt.show()

# You can even specify color and linestyle in just one parameter, type of shorthand 
plt.plot(year, ylabel, "g--")         # Generates a dashed line of 'g' (green) color.

plt.show()