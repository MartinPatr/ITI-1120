import math

class Vector:

    def __init__(self,vector):
        self.vector = vector

    def dimension(self):
        dim = len(self.vector)
        return dim

    def add_dimension(self):
        self.vector.append(self.vector[-1])
        return self.vector

    def remove_dimension(self):
        self.vector.pop(-1)
        return self.vector
    
    def insert_dimension(self, index, value):
        self.vector.insert(index, value)
        return self.vector
    def erase_dimension(self, index):
        del self.vector[index]
        return self.vector
    def set_dimension(self, index, value):
        self.vector[index] = value
        return value
    def get_dimension(self, index):
        return self.vector[index]

    def magnitude(self):
        magnitude = []
        magni = 0
        for i in range(len(self.vector)):
            magnitude.append((self.vector[i]) ** 2)
        for i in range(len(self.vector)):
            magni += magnitude[i]
        magni = math.sqrt(magni)

        return magni

    def multiply(self, scalar):
        for i in range(0,len(self.vector)):
            self.vector[i] = self.vector[i] * scalar

    def equal(self, other):
        return self.vector == other.vector

    def not_equal(self, other):
        return self.vector != other.vector

    def __add__(self,other):
        if len(self.vector)>len(other.vector) or len(self.vector)==len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                self.vector.append(0)
            for i in range(0,len(self.vector)):
                self.vector[i] = self.vector[i] + other.vector[i]
            return self.vector

        elif len(self.vector)<len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                self.vector.append(0)
            for i in range(0,len(self.vector)):
                other.vector[i] = other.vector[i] + self.vector[i]
            return other.vector

    def __sub__(self,other):
        if len(self.vector)>len(other.vector) or len(self.vector)==len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                other.vector.append(0)
            for i in range(0,len(self.vector)):
                self.vector[i] = self.vector[i] - other.vector[i]
            return self.vector

        elif len(self.vector)<len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                self.vector.append(0)
            for i in range(0,len(self.vector)):
                other.vector[i] = other.vector[i] - self.vector[i]
            return other.vector

    def __mul__(self,other):
        if len(self.vector)>len(other.vector) or len(self.vector)==len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                self.vector.append(0)
            for i in range(0,len(self.vector)):
                self.vector[i] = self.vector[i] * other.vector[i]
            return self.vector

        elif len(self.vector)<len(other.vector):
            for i in range(0,(len(self.vector) - len(other.vector))):
                self.vector.append(0)
            for i in range(0,len(self.vector)):
                other.vector[i] = other.vector[i] * self.vector[i]
            return other.vector

    def printer(self): 
        return print(self.vector)

v1 = Vector([1,2,3])
print(v1.dimension())
print(v1.multiply(2))