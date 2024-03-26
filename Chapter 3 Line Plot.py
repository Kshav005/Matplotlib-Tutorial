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

# You can specify a drawstyle, which has values - [default, steps, steps-pre, steps-mid, steps-post] and marker style which has values - ['.' for point, ',' for pixel, 'o' for circle, 'v' for triangle down, 'h' for hexagon, 'd' for diamond, '4' for caretleft, 'p' for plus, etc.]
plt.plot(year, ylabel, ds="steps-post", marker="d")
plt.show()

# To enhance your markers, there are 1 more argument for that. However, there are only some of the markers which support it. Print 'filled_markers' in order to get which markers have the argument supported.
# The argument is 'fill_style' which let's you either fully fill, partially fill or no fill the marker.
plt.plot(year, ylabel, ds="steps-post", marker="o", fillstyle="none")
plt.show()

# That's all for this chapter! We will meet in the next chapter and study more about this amazing module. Keep on coding!