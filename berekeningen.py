def addition(number1:int, number2:int) -> int:
    return str(number1) + " + " + str(number2) + " = " +  str(number1 + number2)

def subtraction(number1:int, number2:int) -> int:
    return str(number1) + " - " + str(number2) + " = " +  str(number1 - number2)

def multiplication(number1:int, number2:int) -> int:
    return str(number1) + " * " + str(number2) + " = " +  str(number1 * number2)

def division(number1:int, number2:int) -> int:
    return str(number1) + " / " + str(number2) + " = " +  str(number1/number2)

def increment(number1:int) -> int:
    return str(number1) + " + 1 = " +  str(number1 + 1)

def decrement(number1:int) -> int:
    return str(number1) + " - 1 = " +  str(number1 - 1)

print(addition(10, 12))
print(subtraction(58,34))
print(multiplication(6,7))
print(division(144,12))
print(increment(12))
print(decrement(34))

