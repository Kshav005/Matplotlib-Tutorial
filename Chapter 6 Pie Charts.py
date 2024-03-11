# Pie charts are really handy in data visualization and can be used to show a data beautifully. Let's try using it!
import pandas as pd, matplotlib.pyplot as plt, random

# Let's create a sample data
car = ["BMW", "Bentley", "Ferrari", "Pagani", "Audi"]
votes = [600, 150, 900, 670, 400]

plt.pie(votes, labels=car)      # Here is the visual representation of the cars that people like the most. 
plt.show()

# Let's play with pie chart a little more by creating another sample.
gender = ["Male", "Female", "Others"]
ppl = []

for x in range(len(gender)) :
    ppl.append(random.randint(10000, 20000))

plt.pie(ppl, labels=gender)
plt.show()
