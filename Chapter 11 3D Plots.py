# Hello everyone, this chapter is going to be awesome as we are going to look at how 3d graphs are made in matplotlib!

import matplotlib.pyplot as plt, numpy as np

# To start using 3d plots, include the code below
plt.axes(projection="3d")

# Let's use scatter plot for experimentation!
x = np.random.random(20)
y = np.random.random(20)
z = np.random.random(20)

plt.scatter(x, y, s=105)
plt.title("3D PLOT")
plt.xlabel("Nothing")
plt.show()


# 3D plotting is used in rare cases and it can be used to beautify your insights a little more. That's why we are going to stop it here. The last chapter will be about animations in matplotlib!