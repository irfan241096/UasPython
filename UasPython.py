import numpy as np
from matplotlib import pyplot as plt

npoints = 50
X, Y = [], []
# class 0
X.append(np.random.uniform(low=-2.5, high=2.3, size=(npoints,)) )
Y.append(np.random.uniform(low=-1.7, high=2.8, size=(npoints,)))

# class 1
X.append(np.random.uniform(low=-7.2, high=-4.4, size=(npoints,)) )
Y.append(np.random.uniform(low=3, high=6.5, size=(npoints,)))

learnset = []
learnlabels = []
for i in range(2):
    # adding points of class i to learnset
    points = zip(X[i], Y[i])
    for p in points:
        learnset.append(p)
        learnlabels.append(i)

npoints_test = 3 * npoints
TestX = np.random.uniform(low=-7.2, high=5, size=(npoints_test,)) 
TestY = np.random.uniform(low=-4, high=9, size=(npoints_test,))
testset = []
points = zip(TestX, TestY)
for p in points:
    testset.append(p)


colours = ["b", "r"]
for i in range(2):
    plt.scatter(X[i], Y[i], c=colours[i])
plt.scatter(TestX, TestY, c="g")
plt.show()
