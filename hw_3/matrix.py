# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LsfGEy539Se8G2k49yx8ZTzZNAy-cZqL
"""

import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices have different shapes")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices have different shapes")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        try:
            return Matrix(np.matmul(self.data, other.data))
        except ValueError as e:
            raise ValueError("Matrices have incompatible shapes for matrix multiplication") from e

    def __str__(self):
        return str(self.data)

np.random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_add = A + B
matrix_mul = A * B
matrix_matmul = A @ B

def save_to_file(matrix, filename):
    with open(filename, 'w') as f:
        f.write(str(matrix))

save_to_file(matrix_add, "matrix+.txt")
save_to_file(matrix_mul, "matrix*.txt")
save_to_file(matrix_matmul, "matrix@.txt")

class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __truediv__(self, other):
        return self.__class__(self.data / other.data)


class FileIOMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            data = np.array([list(map(float, line.split())) for line in f.readlines()])
        return cls(data)


class RepresentationMixin:
    def __str__(self):
        return str(self.data)


class AccessorMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

class AdvancedMatrix(ArithmeticMixin, FileIOMixin, RepresentationMixin, AccessorMixin):
    def __init__(self, data):
        self.data = data

np.random.seed(0)
A = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))
B = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))

matrix_add = A + B
matrix_sub = A - B
matrix_mul = A * B
matrix_div = A / B

matrix_add.save_to_file("matrix+.txt")
matrix_sub.save_to_file("matrix-.txt")
matrix_mul.save_to_file("matrix*.txt")
matrix_div.save_to_file("matrixd.txt")

class HashMixin:
    """
    Сумма всех элементов матрицы.
    """
    def __hash__(self):
        return int(np.sum(self.data))

    def __matmul__(self, other):
        if (hash(self), hash(other)) in matrix_product_cache:
            return matrix_product_cache[(hash(self), hash(other))]
        else:
            result = self.__class__(np.matmul(self.data, other.data))
            matrix_product_cache[(hash(self), hash(other))] = result
            return result

class AdvancedMatrix(ArithmeticMixin, FileIOMixin, RepresentationMixin, AccessorMixin, HashMixin):
    def __init__(self, data):
        self.data = data

matrix_product_cache = {}

class AdvancedMatrix(ArithmeticMixin, FileIOMixin, RepresentationMixin, AccessorMixin, HashMixin):
    def __init__(self, data):
        self.data = data

import itertools

def find_collision(n):
    for comb in itertools.product(range(-10, 11), repeat=4):
        A = np.array([[comb[0], comb[1]], [comb[2], comb[3]]])
        C = np.array([[comb[1], comb[0]], [comb[3], comb[2]]])
        if np.array_equal(A, C):
            continue
        if hash(AdvancedMatrix(A)) == hash(AdvancedMatrix(C)):
            return A, C
    return None, None

A, C = find_collision(2)
if A is not None and C is not None:
    B = np.array([[1, 2], [3, 4]])
    D = B.copy()

    A = AdvancedMatrix(A)
    B = AdvancedMatrix(B)
    C = AdvancedMatrix(C)
    D = AdvancedMatrix(D)

    AB = A @ B
    CD = C @ D

    A.save_to_file("A.txt")
    B.save_to_file("B.txt")
    C.save_to_file("C.txt")
    D.save_to_file("D.txt")
    AB.save_to_file("AB.txt")
    CD.save_to_file("CD.txt")

    with open("hash.txt", "w") as f:
        f.write(f"Hash(AB): {hash(AB)}\n")
        f.write(f"Hash(CD): {hash(CD)}\n")
else:
    print("No collision found")

