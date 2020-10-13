from functools import reduce
 
fibonacci = lambda i: reduce(lambda a, _: a+[a[-1]+a[-2]],
  range(i-2), [0, 1])
 
print("Fibonacci up to 3:")
print(fibonacci(3))
print("\nFibonacci up to 7:")
print(fibonacci(7))
print("\nFibonacci up to 9:")
print(fibonacci(9))
print("\nFibonacci up to 11:")
print(fibonacci(11))