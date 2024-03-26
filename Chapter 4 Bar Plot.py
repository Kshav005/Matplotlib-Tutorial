# Now let's suppose, we have a poll asking "which is your favorite game?" and we gave some options. To represent it in a form of a graph, we can use a bar graph! Let us how!

import random
import matplotlib.pyplot as plt

game = ["GTA5", "FarCry", "PUBG",  "Pacman", "Mario", "GTAVC"]
votes = []

for x in range(len(game)) : 
    votes.append(random.randint(500, 2000))
    
plt.bar(game, votes)
plt.show()

# And as usual, we can change color and apply some of the parameters here.
# To set width of a bar
plt.bar(game, votes, width=0.4)
plt.show()

# You can also set edgecolor and edge width
plt.bar(game, votes, edgecolor="blue", color="black", linewidth=3)
plt.show()

# Hatch can also be used to fill the bars with a symbol. It can take values from - [/, \, |, -, +, x, o, O, ., *]
plt.bar(game, votes, edgecolor="blue", color="black", linewidth=3, hatch="*")
plt.show()


# Hence, the chapter has been completed! Let's meet in the next chapter for histogram.