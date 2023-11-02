#!/usr/bin/python3
if __name__ == "__main__":
    """imports all functions from the file and handles basic operations."""
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        operator = sys.argv[2]

        if operator in operators:
            result = operators[operator](num1, num2)
            print("{} {} {} = {}".format(num1, operator, num2, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
