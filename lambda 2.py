def function(n):
 return lambda x : x * n
number = int(input("Your number: "))
result = function(2)
print("Double your number :", result(number))
result = function(3)
print("Triple your number :", result(number))
result = function(4)
print("Quadruple your number :", result(number))
result = function(5)
print("Quintuple your number :", result(number))

