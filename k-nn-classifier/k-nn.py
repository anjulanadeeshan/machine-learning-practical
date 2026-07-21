import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

irisData = load_iris()
#features
X = irisData.data
#labels
y = irisData.target

# for i in range(len(X)):
#     print(f"{X[i]} {y[i]}")

# plt.scatter(X[:,0],X[:,2],c=y)
# plt.show()

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size = 0.2,
    random_state = 42
)

k = 3
prediction = []

def euclidiean_distance(point1,point2): #each point has four values
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i]-point2[i])**2
    return math.sqrt(distance)

def predict(X_train,y_train,test_point,k) :
    distances = []
    for i in range(len(X_train)):
        dist = euclidiean_distance(test_point,X_train[i])
        distances.append((dist,y_train[i]))
    
    distances.sort(key=lambda x: x[0])
    neighbours = distances[:k]

    votes = {}
    for _ , label in neighbours:
        if label in votes:
            votes[label] += 1
        else :
            votes[label] = 1
    
    prediction = max(votes, key=votes.get)
    return prediction

for test_point in X_test:
    prediction.append(predict(X_train,y_train,test_point,k))

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, prediction)
print("cm :",cm)