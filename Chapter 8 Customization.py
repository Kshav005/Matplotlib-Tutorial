# Did you know that you can customize the graph? Not just the colors but you can also use legends, labels, titles, etc. in your graph! In this chapter, we are going to look at such things and let's code!

import pandas as pd, numpy as np, matplotlib.pyplot as plt

car = ["BMW", "Bentley", "Ferrari", "Pagani", "Audi"]
votes = [600, 350, 900, 670, 450]

# Let's create a box plot!
plt.bar(height=votes, x=car)

# As you can see, we created our graph but now let's put a title and a label!
# For labelling the x-axis
plt.xlabel("Car Companies of the World")

# For labelling the y-axis
plt.ylabel("Total No. of Votes")

# For putting up a title and changing it's font (font is applicable for labels too!)
plt.title("Number of Votes recorded by Car Companies in 20xx", fontsize=12, fontname="Army")
plt.show()


# You can also have legends! Let's see how. First, I am going to create a sample data set for line graph.
leg = ["Male", "Female", "Others"]
male = [224, 450, 580, 435, 990, 965, 1000]
female = [833, 121, 444, 342, 432, 999, 1030]
others = [500, 400, 432, 433, 454, 456, 457]
year = [2000+x for x in range(0, 70, 10)]

plt.plot(year, male, label="Male")
plt.plot(year, female, label="Female")
plt.plot(year, others, label="Other")



# To toggle legends
plt.legend()

# You can see a box showing the meaning of each colored line!
# You can change the location of the legend by using the argument 'loc'
plt.legend(loc="center")
plt.legend(loc="upper right")
plt.legend(loc="lower left")
plt.legend(loc="upper center")
plt.show()

# Legends work for every type of graph so you needn't worry about anything!
# Enough for this chapter, next chapter is going to be interesting as we are going to study about themes in matplotlib.