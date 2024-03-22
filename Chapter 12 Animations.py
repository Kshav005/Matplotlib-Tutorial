import matplotlib.pyplot as plt, numpy as np, random
from matplotlib import style

# Let's create an interesting thing.
# We will be creating a loop, which will count number of votes (done using random)
style.use("ggplot")
game = ["Sleeping dogs", "State Of Decay", "MGS5 PP "]
votes = [0, 0, 0]           # Initially, the votes are 0 for every game

for i in range(400) : 
    # The below line of code will randomly choose index and increases it's value with random number from 1 to 10.
    votes[random.randint(0, 2)] += random.randint(1, 10)
    plt.bar(game, votes, color=["red", "blue", "green"])
    plt.pause(0.001)            # The function may say pause, but it's the start of creating animation

# You can use 'show' and you will see an animation.
plt.show()

# Hence, the chapter is complete. Congrats on completing this module. Now keep practicing.