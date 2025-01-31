import math


def linear(x):
    '''Linear activation function: https://en.wikipedia.org/wiki/Identity_function
    '''
    return x


def tanh(x):
    '''Hyperbolic tangent activation function: https://en.wikipedia.org/wiki/Hyperbolic_functions#Hyperbolic_tangent
    This returns values between -1 and 1
    '''
    return math.tanh(x)


def sigmoid(x):
    '''Classical sigmoid activation function: https://en.wikipedia.org/wiki/Sigmoid_function
    This 
    '''
    return 1.0 / (1 + math.exp(-x))


def relu(x):
    '''Rectified linear unit: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
    '''
    return max(0, x)


def leaky_relu(x):
    '''Leaky rectified linear unit: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Leaky_ReLU
    Can be used to avoid the problem of dying neurons
    '''
    return p_relu(x, 0.01)


def p_relu(x, p):
    '''Parametric rectified linear unit: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Parametric_ReLU
    '''
    if x >= 0:
        return x
    else:
        return p * x


def softplus(x):
    '''Softplus activation function: https://en.wikipedia.org/wiki/Activation_function
    '''
    return math.log(1 + math.exp(x))

