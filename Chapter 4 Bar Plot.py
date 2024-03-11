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

# Hence, the chapter has been completed! Let's meet in the next chapter for histogram.