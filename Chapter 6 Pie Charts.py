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

# 'explode' is a feature which is used to slice the part. For example, I want to show the 'female' category to be represented apart from others so I can set it's value of explode. You need to create a list and values for each pie part. Here, the female part is on index 1, so I kept the value to 0.3 in the index 1.
plt.pie(ppl, labels=gender, explode=[0, 0.05, 0])
plt.show()

# To show percentage written on it, you need to use another argument called 'autopct'.
plt.pie(ppl, labels=gender, autopct="%.2f%%")       #'%.2f%% specifies that 2 digits are to be used after decimal.'
plt.show()

# You can also choose a starting angle, for example start at 90 degrees.
plt.pie(ppl, labels=gender, startangle=90)
plt.show()

# That's all for pie chart! I hope you learnt something today and make sure that you always revise these concepts in order to work more efficiently.

