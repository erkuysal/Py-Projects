# This file is created for better understanding for the activation functions for ML.

def threshold(x): #
    if x <= 0:
        return False
    else:
        return True

def sigmoid(x): # sigmoid(x) = 1 / (1 + e^(-x))
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

# ------------------- Ridge Activation Functions ----------------------------

def  linear(m, x, n): # f(x) = mx + n
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

def relu(x): # ReLU(x) = max(0, x)
    """
       Rectified Linear Unit (ReLU) function.

       Parameters:
           x (float): The input value.

       Returns:
           float: The result of the ReLU function.
       """
    return max(0, x)

def heaviside(x): # H(x) = 0, for x < 0 , H(x) = 1, for x >= 0
    """
        Heaviside step function.

        Parameters:
            x (float): The input value.

        Returns:
            float: The result of the Heaviside function.
        """
    return 1 if x >= 0 else 0


def logistic(x): # f(x) = 1 / (1 + e^(-x))
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


# ----------------- Radial Activation Functions --------------------------

def gaussian(x, mean, std_dev): # f(x) = (1 / (σ * √(2π))) * e^(-((x - μ)^2) / (2 * σ^2))
    """
    Gaussian function (normal distribution).

    Parameters:
        x (float): The input value.
        mean (float): The mean of the distribution.
        std_dev (float): The standard deviation of the distribution.

    Returns:
        float: The result of the Gaussian function.
    """
    coefficient = 1 / (std_dev * (2 * 3.14159265358979323846)**0.5)
    exponent = -((x - mean)**2) / (2 * std_dev**2)
    return coefficient * 2.718281828459045 ** exponent

def multiquadratic(x, y, c): # f(x, y) = sqrt(x^2 + y^2 + c^2)
    """
        Multiquadratic function.

        Parameters:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
            c (float): The constant.

        Returns:
            float: The result of the multiquadratic function.
        """
    return (x ** 2 + y ** 2 + c ** 2) ** 0.5

def inv_Multiquadratics(x, y, c): # f(x, y) = 1 / sqrt(x^2 + y^2 + c^2)
    """
        Inverse multiquadratic function.

        Parameters:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
            c (float): The constant.

        Returns:
            float: The result of the inverse multiquadratic function.
        """
    denominator = (x ** 2 + y ** 2 + c ** 2) ** 0.5
    if denominator != 0:
        return 1 / denominator
    else:
        raise ValueError("Denominator is zero.")

# Folding Activation Functions




