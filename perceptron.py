import random

class Perceptron:
    def __init__(self, num_features, learning_rate=0.01, max_epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.weights = [random.random() for _ in range(num_features + 1)]  # +1 for bias

    def activation_function(self, x):
        # Binary step / Threshold function
        # Step function: 1 if x >= 0, 0 otherwise
        return 1 if x >= 0 else 0

    def predict(self, x):
        x_with_bias = [1] + x  # Adding bias term
        net_input = sum(w * xi for w, xi in zip(self.weights, x_with_bias))
        return self.activation_function(net_input)

    def train(self, X, y):
        for epoch in range(self.max_epochs):
            total_error = 0
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                error = label - prediction
                total_error += abs(error)
                x_with_bias = [1] + inputs
                self.weights = [w + self.learning_rate * error * xi for w, xi in zip(self.weights, x_with_bias)]
            if total_error == 0:
                print(f"Converged after {epoch + 1} epochs.")
                break
        else:
            print("Max epochs reached, the model may not have converged.")

# Example usage
if __name__ == "__main__":
    # Sample dataset with two features (X1 and X2) and their corresponding labels (0 or 1)
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]

    # Create a perceptron with 2 input features
    perceptron = Perceptron(num_features=2)

    # Train the perceptron
    perceptron.train(X, y)

    # Test the perceptron with new data
    test_data = [[0, 0], [1, 0], [0, 1], [1, 1]]
    for inputs in test_data:
        prediction = perceptron.predict(inputs)
        print(f"Input: {inputs}, Prediction: {prediction}")
