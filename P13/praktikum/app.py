def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

import numpy as np
arr_error = []
def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
            arr_error.append(sum_error)
        return weights, arr_error
    
#contoh kasus OR
dataset = [[1,1,1],
          [1,0,1],
          [0,1,1],
          [0,0,0]]

weights = [0,0,0] #bias, w1, w2
l_rate = 1
n_epoch =7
weights, arr_error = train_weights(dataset, l_rate, n_epoch)
print(weights)

#visualisasi
import matplotlib.pyplot as plt
plt.plot(arr_error)

Nweights = [-1, 1, 1]
for row in dataset:
    prediction = predict(row, weights)
    print("Expected=%d, Predicted=%d" % (row[-1], prediction))
    
Nweights = [-1, 1, 1]
datatest = [[1,0,1]]
for row in datatest:
    prediction = predict(row, weights)
    print("Expected=%d, Predicted=%d" % (row[-1], prediction))