import numpy as np

#sigmoid function
def sigmoid(valuesIN):
    return 1/(1+np.exp(-valuesIN))

# Single Instance Input
X = np.array(([0.5726, 0.5833]), dtype=float)
# Single Instance Output/target
y = 75


#forward steps (remember slide 54)
def ANN(inputsX):
    #Weights (we are using two layers here), weights are random
    W1 = np.random.randn(2, 3)
    W2 = np.random.randn(3, 1)

    # feedforward propagation
    Zi = np.dot(inputsX, W1)            # Step 1
    Ai = sigmoid(Zi)                    # Step 2
    Z4 = np.dot(Ai, W2)                 # Step 3
    y_Hat = sigmoid(Z4)                 # Step 4
    prediction = round(y_Hat[0] * 100,2)
    error = abs(prediction - y)
    return prediction, error, W1, W2



# Run 1 to get initial values, this could be the best weihghts
prediction, errorBest, W1_Final, W2_Final= ANN(X)
print("Predicted Score:",prediction,"%")

# try 1000 random weights
for item in range(2, 1001):
    # Update the weights to new random weights
    pred, error, W1, W2 = ANN(X)
    print("Run:", item)

    print("Predicted Value:",pred,"%")
    # If its the largest accuracy, save the weights and performance
    if error < errorBest:
        bestPrediction = pred
        errorBest = error
        W1_Final = W1
        W2_Final = W2

print("\n\n\n-----------------------------------")
print(" Best Model ")
print("-----------------------------------")
print("W1:\n", W1_Final)
print("\n\nW2\n:", W2_Final)
print("\n\nClosest Prediction", round(bestPrediction,4),"%")
print("Lowest Error", round(errorBest,4),"%")