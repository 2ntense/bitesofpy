def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    if type(calculation) is not str:
        raise ValueError

    s = calculation.split(" ")
    if len(s) != 3:
        raise ValueError

    try:
        num1 = int(s[0])
        num2 = int(s[2])
    except():
        raise ValueError

    operand = s[1]

    if len(operand) != 1:
        raise ValueError

    if operand == "+":
        return num1 + num2
    elif operand == "-":
        return num1 - num2
    elif operand == "*":
        return num1 * num2
    elif operand == "/":
        if num2 == 0:
            raise ValueError
        return num1 / num2
    else:
        raise ValueError
