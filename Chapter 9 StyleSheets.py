# Time to study about stylesheets in matplotlib!
# Stylesheets are already made themes and can be imported using the matplotlib library.
import pandas as pd, numpy as np, matplotlib.pyplot as plt

# Include this line below
from matplotlib import style

# You can have a overview about each theme by this link - https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

# There are many types of themes available in matplotlib. We will be seeing quite a few here.
# Themes are really awesome when you need to customize your graphs fully. Along with correct plotting, it is important to improve the graph colors too.
car = ["A", "B", "C", "D"]
votes = [300, 500, 334, 491]

style.use("ggplot")     # ggplot is the name of the theme

# To get all the theme names
print(style.available)


# Also, if you want to open multiple windows which show multiple graphs, we use the function 'figure'. Let's plot a bar graph in figure 1, histogram in another.
plt.figure(1)
plt.bar(car, votes, width=0.4)

# Creating a random data for our figure 2
v = ["Y", "N", "N", "Y", "Y", "N", "Y", "N", "N", "Y", "N", "N", "Y", "N"]
plt.figure(2)
plt.hist(v)

# Thus, we used the function 'show' only 1 time and we got our multiple figures.
plt.show()

# Now let's suppose, you want to plot 4 graphs in a single window.
# For that you need to create a subplot.
fig, axs = plt.subplots(2, 2)      # Subplot of 2x2 (2 row x 2 column) 

# Thus, we will have 4 point to access. (0,0), (0,1), (1,0), (1,1). Remember, the 
axs[0, 0].hist(v)
axs[0, 1].bar(car, votes, width=0.4)

# To set individual titles of subplots
axs[1, 0].set_title("Hey there")
axs[1, 1].set_title("Where are you now")

# For a title
plt.suptitle("4 plots")

# You can disable overlapping of elements in graph by using a tight layout.
plt.tight_layout()

# You can also save the figure instead of showing it!
plt.savefig("img/a1.png")

# You can export it into a high resolution image using dpi argument
plt.savefig("img/a2.png", dpi=300)

# Set transparency while saving
plt.savefig("img/a3.png", transparent=True)


# Hope this chapter was interesting for you guys. There are a lot to do using this matplotlib library and it includes really awesome arguments which you can use while saving, plotting, labelling, etc. From the next few chapters, we are going to focus on advanced matplotlib functions in order to learn what more can be done using this library. Till then, keep coding!