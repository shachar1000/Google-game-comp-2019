from random import randrange
import numpy as np
from math import exp

def printMatrix(matrix, msgY, msgX):
    print("".join([(6-(i*4))*" "+"{}:".format(msgX) for i, val in enumerate(matrix[0])]))
    print('\n'.join(["{}: ".format(msgY)+(' '*7).join(['{}'.format(x) for x in y]) for y in matrix]))

class matrix():
    def __init__(self, y, x):
        self.y = y; #y
        self.x = x; #x
        self.data = [[None]*self.x]*self.y

    def map(self, functionToPass): # apply function for each matrix value
        array = []
        for y in range(self.y):
            for x in range(self.x):
                array.append(functionToPass(self.data[y][x], y, x))
        self.data=matrix.matrixFromArray(array).data
        return self

    def randomize(self):
        #return self.map(lambda val, y, x: randrange(0, 10))
        self.data = (np.random.randint(1, 10, (self.y,self.x))).tolist()

    @staticmethod
    def multiply(a, b):
        def funcToApply(val, y, x):
            sum = 0
            for k in range(len(b.data)): #for the amount of inputs could be a.x or b.y
                sum = sum + (a.data[y][k] * b.data[k][x]) # y is each hidden, x could be 0
            return sum
        if (a.x == b.y): # for example in NN a.x is amount of inputs and b.y is that too although a is weights (so y is each hidden) and b is inputs
            return matrix(a.y, b.x).map(funcToApply)
        else:
            print("input not good please fix it or I won't work like wtf is wrong with you cunt")

    @staticmethod
    def matrixFromArray(array):
        matrixFrom = matrix(len(array), 1)
        matrixFrom.data = [[array[y]] for y in range(len(array))]
        return matrixFrom

    def add(self, whatToAdd):
        if not isinstance(whatToAdd, matrix):
            for y in range(len(self.data)):
                for x in range(len(self.data[y])):
                    self.data[y][x] = self.data[y][x] + whatToAdd
        else:
            if ((self.y is not whatToAdd.y) or (self.x is not whatToAdd.x)):
                return
            else:
                for y in range(len(self.data)):
                    for x in range(len(self.data[y])):
                        self.data[y][x] = self.data[y][x] + whatToAdd.data[y][0]
    def activate(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                self.data[y][x] = 1 / (1 + exp(-(self.data[y][x])))

class neuralNetwork:
    def __init__(self, in_nodes, hid_nodes, out_nodes):
        self.input_nodes = in_nodes
        self.hidden_nodes = hid_nodes
        self.output_nodes = out_nodes

        self.weights_ih = matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ih.randomize()
        self.weights_ho = matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ho.randomize()

        self.bias_h = matrix(self.hidden_nodes, 1)
        self.bias_o = matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    @staticmethod
    def activation(val, y, x):
        return 1 / (1 + exp(-val))

    def predict(self, inputList):
        inputs = matrix.matrixFromArray(inputList)
        print(inputs.data)
        printMatrix(self.weights_ih.data, 'hidden', 'input')
        hidden = matrix.multiply(self.weights_ih, inputs)
        print(hidden.data)
        hidden.add(self.bias_h)
        print(self.bias_h.data)
        print(hidden.data)
        hidden.activate()
        print(hidden.data)
        output = matrix.multiply(self.weights_ho, hidden);
        printMatrix(self.weights_ho.data, 'output', 'hidden')
        print(self.bias_o.data)
        output.add(self.bias_o);
        print(output.data)
        output.activate()
        return output

NN = neuralNetwork(2, 2, 1)
print(NN.predict([1, 2]).data)