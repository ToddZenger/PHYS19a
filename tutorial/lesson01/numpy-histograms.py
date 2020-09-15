"""
Author: Todd Zenger, Brandeis University
This program gives a first look at Numpy and 
we plot our first plot.
"""

# First, we need to tell Python to bring in numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# np and plt are the standard shortcut names we give it

x = np.array([0,2,4,5])

# Some basic modifications
print(x)
print(x+5)
print(x**2)

# Now let's do some slicing to get specific elements
print("Without the first element")
print(x[1:])

print("Without the last two elements")
print(x[:4])
print(x[:-2]) # Negative index values means that we start going backwards

# There are also useful mathematical operations available to us
sinx = np.sin(x) # numpy uses radians
print("sin(x) is:")
print(sinx)

np.random.seed(900835)

# Now, let's turn our attention to plotting a histogram

# First, let's generate some random data
# See documentation online for this, but loc is the mean,
# scale is the standard deviation, and size is number of values
data = np.random.normal(loc=5.0, scale=1.0, size=20) 

# Let's get some statistical information from this
mean_data = np.mean(data)
std_data = np.std(data, ddof=1) #ddof is set to 1 for the sample standard deviation

# Now let's get to plotting

# First we tell python to open up a figure
plt.figure()


# Make the histogram
# Insert the data to be plotted, describe number of bins we want,
# then I personally use edge color (ec) as black for clarity
n, bins, patches = plt.hist(data, bins=5, ec="black")

# We need to sort the data for statistics
sorted_data = np.sort(data)
data_pdf = data.size*norm.pdf(sorted_data, mean_data, std_data)
plt.plot(sorted_data, data_pdf, 'r--')
# Now add labels for a presentable chart

plt.xlabel("Data Points")
plt.ylabel("Frequency")
plt.title(r"Histogram of Random Data, $\mu={:0.2f}$, $\sigma={:0.2f}$".format(mean_data, std_data))

# Now tell python to show this plot
plt.show()

print(mean_data)
print(std_data)

# Now, we can save it offline

#plt.savefig("firsthisto.png")

"""
Below is optional. Instead, it uses a normalized distribution to represent
the samples
"""

# First we tell python to open up a figure
plt.figure()


# Make the histogram
n, bins, patches = plt.hist(data, bins=5, density=True, ec="black")

# We need to sort the data for statistics
sorted_data = np.sort(data)

# Add a fit to the histogram
data_pdf = norm.pdf(sorted_data, mean_data, std_data)
plt.plot(sorted_data, data_pdf, 'r--')

# Now add labels for a presentable chart

plt.xlabel("Data Points")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")

# Now tell python to show this plot
plt.show()