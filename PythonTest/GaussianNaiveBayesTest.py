import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
print(X.shape)

import matplotlib.pyplot as plt
x, y = X[:,0], X[:,1]
plt.scatter(x, y)
plt.show()

import sklearn.naive_bayes as sk
clf = sk.GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-1, -1]]))
print(clf.predict([[5, 4]]))
