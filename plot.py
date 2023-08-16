import numpy as np
import matplotlib.pyplot as plt
import math
import random

f = open("XandY") # this file contains the x and y points 
data = f.readline()
x = [] # keep track of the x axis points
y = [] # keep track of the y axis points 

while data:
    fields = data.split("|") # the file is pipe delimited 
    xAxis = fields[1]
    yAxis = fields[2]

    if float(yAxis) < 400: # remove outliers, so anything above 400, don't count
        x.append(float(xAxis))
        y.append(float(yAxis))

    data = f.readline()

f.close()

f = plt.figure()

# make random colors for the plot
colors = [random.random() for i in range(len(x))]

# make the scatter plot 
plt.scatter(x,y, c = colors, alpha=0.5)

# these are the x and y labels 
plt.ylabel("Total Drug Days per Dementia Cases")
plt.xlabel("Average Income")

# save the plot as a pdf 
f.savefig("plot.pdf")

