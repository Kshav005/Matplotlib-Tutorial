# Now let's install matplotlib by using `pip install matplotlib` and install numpy by `pip install numpy`
# After it is done, we can now use it in our tutorial. Also, I recommend you to have some knowledge about numpy and pandas beforehand. They are the general tools which are required for data science and can be used in matplotlib further.

# importing the library 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Getting the values from the csv file
df = pd.read_csv("file.csv")

xlabel = df["x-axis"]
ylabel = df["y-axis"]

# Scatter plot : just plotting points without joining them. They are actually dots on the graph.
plt.scatter(x=xlabel, y=ylabel)

# You need to show result after every plot
plt.show()

# To change color of the graph points
plt.scatter(xlabel, ylabel, c="green")          # hex codes and rgb can be used too!
plt.show()          # will be opened after closing 1st window

# To change the mark (point) of the graph (only particular symbols can be used)
plt.scatter(xlabel, ylabel, c="blue", marker="^")
plt.show()

# To change the size of the points then we can use another parameter
plt.scatter(xlabel, ylabel, s=150, marker="*")
plt.show()



# Now if you look out graph, then you can see many points scattered everywhere, basically they represent x,y pairs.