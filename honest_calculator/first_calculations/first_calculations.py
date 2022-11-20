def calculate(x, y, oper):
    result = 0
    if oper == '+':
        result = x + y
    if oper == '-':
        result = x - y
    if oper == '*':
        result = x * y
    if oper == '/':
        result = x / y
    return result


opers = ['+', '-', '*', '/']
while True:
    try:
        print("Enter an equation")
        calc = input()
        x, oper, y = calc.split()
        x = float(x)
        y = float(y)
        if oper not in opers:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue
        result = calculate(x, y, oper)
        print(result)
        break
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
