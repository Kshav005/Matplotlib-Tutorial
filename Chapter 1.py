# Hello and welcome to another tutorial which is going to teach you about matplolib, another famous library which is used in the field of data science in order to create amazing visualizations.
# First of all, let's create a random csv file in order to test our matplotlib features! You just need to run the program, python will automatically create a csv file in your folder! Type `pip install pandas` in the terminal first.

import pandas as pd 
import random

lis = [10, 20 , 30, 40, 50, 60, 70, 80, 90, 100]
xy = {"x-axis" : [], "y-axis" : []}


for i in range(1, 21) :
    xy["x-axis"].append(random.choice(lis))
    xy["y-axis"].append(random.choice(lis))

df = pd.DataFrame(data=xy)
df.to_csv("file.csv", index=False)


# You need to run this code and let's move to the next chapter!