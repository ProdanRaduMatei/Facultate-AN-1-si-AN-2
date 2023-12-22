from logic.recursive import *


def factorialExample():
    print("Exercise 1.")
    print(f"\tfactorial(1) = {factorial(1)}")
    print(f"\tfactorial(3) = {factorial(3)}")
    print(f"\tfactorial(5) = {factorial(5)}")


def fibonacciExample():
    print("Exercise 2.")
    print(f"\tfibonacci(0) = {fibonacci(0)}")
    print(f"\tfibonacci(1) = {fibonacci(1)}")
    print(f"\tfibonacci(6) = {fibonacci(6)}")


def multiplicationExample():
    print("Exercise 3.")
    print(f"\tmultiplication(0) = {multiplication(0)}")
    print(f"\tmultiplication(1) = {multiplication(1)}")
    print(f"\tmultiplication(6) = {multiplication(6)}")


def sumExample():
    print("Exercise 4.")
    print(f"\tsum(0) = {sum(0)}")
    print(f"\tsum(1) = {sum(1)}")
    print(f"\tsum(6) = {sum(6)}")


def pascalExample():
    print("Exercise 5.")
    print(f"\tpascal(1) = {pascal(1)}")
    print(f"\tpascal(2) = {pascal(2)}")
    print(f"\tpascal(6) = {pascal(6)}")


def minimumExample():
    print("Exercise 6.a")
    print(f"\tminimum([]) = {minimum([])}")
    print(f"\tminimum([5]) = {minimum([5])}")
    print(f"\tminimum([3, 2, 1]) = {minimum([3, 2, 1])}")
    print(f"\tminimum([3, 6, 2, 4, 7, 1, 9, 8]) = {minimum([3, 6, 2, 4, 7, 1, 9, 8])}")


def maximumExample():
    print("Exercise 6.b")
    print(f"\tmaximum([]) = {maximum([])}")
    print(f"\tmaximum([5]) = {maximum([5])}")
    print(f"\tmaximum([3, 2, 1]) = {maximum([3, 2, 1])}")
    print(f"\tmaximum([3, 6, 2, 4, 7, 1, 9, 8]) = {maximum([3, 6, 2, 4, 7, 1, 9, 8])}")


def recursiveMinExample():
    print("Exercise 7")
    print(f"\trecursive_min([]) = {recursiveMin([])}")
    print(f"\trecursive_min([[2, 9, [1, 13], 8, 6]]) = {recursiveMin([[2, 9, [1, 13], 8, 6]])}")
    print(f"\trecursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) = {recursiveMin([2, [[13, -7], 90], [1, 100], 8, 6])}")


def countExample():
    print("Exercise 8")
    print(f"\tcount(2, []) = {count(2, [])}")
    print(f"\tcount(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) = {count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])}")
    print(f"\tcount(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) = {count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])}")


def printAll():
    factorialExample()
    fibonacciExample()
    multiplicationExample()
    sumExample()
    pascalExample()
    minimumExample()
    maximumExample()
    recursiveMinExample()
    # countExample()
    pass
