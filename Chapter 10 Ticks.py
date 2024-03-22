# In this chapter, we are going to study about ticks in matplotlib which is quite important for plotting multiple graphs. 
# By using 'plot' again and again, you can plot multiple graphs in a single window.
# In this chapter, we will plot multiple bar graphs.
# However, bars might overlap and thus, it's import to give some space like telling python next bar when one bar ends. Let's see how ticks and width can be helpful to do so.
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

# Creating a sample dataset for our work.
year = [2000+x for x in range(4)]
us = [340, 500, 600, 780]
ind = [300, 432, 654, 485]
rus = [113, 200, 566, 567]
pak = [360, 600, 234, 490]

# As you already know, width is used to set the bar width. I put it as 0.2 for example, you can use any value but make sure you apply the same concept.
width = 0.2

# We create a list in which number of elements are equal to the list which we are going to use in x-axis.
tick = np.arange(len(year))         # [1, 2, 3, 4]

# Now we plot our first bar, which takes the list 'tick' (contains numbers till length of x-axis list). Right now, you might think why there are numbers on x-axis when you need the year to be put up there. We will understand it later.
# As you know, a graph is plotted according to x and y axis. So, we want our graph to be plotted using the numbers on x-axis and then we can change those numbers to the 'year'.
# The 1st bar set.
plt.bar(tick, ind, width=width, label="India")       # Ticks for this bar set = [1, 2, 3, 4]

# We plot our 2nd graph when 1st bar ends. So, if you remember the width was set to '0.2'. Hence, we will plot graph after taking a space of '0.2' where the first graph ends in order to avoid overlapping.
plt.bar(tick+width, us, width=width, label="USA")   # Ticks for this bar set = [1.2, 2.2, 3.2, 4.2]

# 3rd bar set is plotted after both 1st and 2nd, thus we add width 2 times.
plt.bar(tick+width+width, pak, width=width, label="Pakistan")       # Ticks for this bar set = [1.4, 2.4, 3.4, 4.4]

# Now here's our main task. We use 'xticks' to manipulate x-axis.
# If you run the code without the below function then you will see, that the x-axis is quite misplaced when want it to be in between of the whole bars. Like we plot 3 graphs on 1 x tick, so we will need to be in between of all the 3.
# We know the total width will be 0.4 for each x-tick as the width set for each bar is 0.2, then we want place the name each x-tick to the half of the whole bar which will be 0.4/2 = 0.2. As our width is set to 0.2, that's why we use it and add to ticks..
plt.xticks(tick+width, labels=year)         # Ticks will be set on locations = [1.2, 2.2, 3.2, 4.2]

# 'labels' is an argument which takes a list and thus, we replace the numbers on x-axis to the 'year' list.

# And that's how we use ticks! For more explanation, suppose I want to set the width as 0.4 for each bar. Then the values will be as followed :-
# Tick for bar 1 = [1, 2, 3, 4]
# Tick for bar 2 = [1.4, 2.4, 3.4, 4.4]
# Tick for bar 3 = [1.8, 2.8, 3.8, 4.8]
# Then total width of the bar per tick = 1.8-1 = 2.8-2 = 3.8-3 = 4.8-4 = 0.8
# To set the x-tick name in between = 0.8/2 = 0.4
# Therefore, we add 0.4 to the tick list. Either you can simply write it as 'tick+0.4' or 'tick+width', both are applicable.

plt.legend(loc="upper left")
plt.show()

# This chapter might be long for you but it's extremely helpful if you are going to plot multiple bars on a single graph. That's this concept had it's own chapter.