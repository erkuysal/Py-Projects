# This file is created to better understanding the maths for ML.

# Threshold function // Binary Step function
def threshold(x):
    if x <= 0:
        return False
    else:
        return True

def sigmoid(x):
    """
        Calculate the sigmoid function for a given input.

        Parameters:
            x (float): The input value.

        Returns:
            float: The result of the sigmoid function.
        """
    # Calculate e^(-x) using the Taylor series expansion
    ex_neg_x = 1.0
    term = 1.0
    for i in range(1, 100):  # 100 terms are sufficient for a good approximation
        term *= (-x) / i
        ex_neg_x += term

    # Calculate and return the sigmoid function
    return 1 / (1 + ex_neg_x)

# Ridge Activation Functions

def  linear(m, x, n):
    """
       Calculate the value of a linear function for a given input.

       Parameters:
           x (float): The input value.
           m (float): The slope of the line.
           n (float): The y-intercept of the line.

       Returns:
           float: The result of the linear function.
       """
    return m * x + n

def relu(x):
    """
       Rectified Linear Unit (ReLU) function.

       Parameters:
           x (float): The input value.

       Returns:
           float: The result of the ReLU function.
       """
    return max(0, x)

def heaviside(x):
    """
        Heaviside step function.

        Parameters:
            x (float): The input value.

        Returns:
            float: The result of the Heaviside function.
        """
    return 1 if x >= 0 else 0

def logistic(x):
    """
       Logistic function (sigmoid function).

       Parameters:
           x (float): The input value.

       Returns:
           float: The result of the logistic function.
       """
    # Calculate e^(-x) using the Taylor series expansion
    ex_neg_x = 1.0
    term = 1.0
    for i in range(1, 100):  # 100 terms are sufficient for a good approximation
        term *= (-x) / i
        ex_neg_x += term

    # Calculate and return the logistic function
    return 1 / (1 + ex_neg_x)


# Radial Activation Functions

def gaussian():

def multiquadratics():

def inv_Multiquadratics():

# Folding Activation Functions




