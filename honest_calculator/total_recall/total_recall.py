def calculation(x, y, oper):
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


def store_result(result, memory):
    print("Do you want to store the result? (y / n):")
    answer = input()
    if answer == "y":
        memory = result
    if answer == "no":
        pass
    return memory


def inputs():
    memory_sign = "M"
    calc = input()
    x, oper, y = calc.split()
    if x == memory_sign:
        x = memory
    else: 
        x = float(x)
    if y == memory_sign:
        y = memory
    else:
        y = float(y)
    return x, y, oper


def do_we_continue():
    print("Do you want to continue calculations? (y / n):")
    answer = input()
    if answer == 'y':
        return 1
    if answer == 'n':
        return 0


opers = ['+', '-', '*', '/']
memory = 0.0
while True:
    try:
        print("Enter an equation")
        x, y, oper = inputs()
        if oper not in opers:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue
        if oper in opers:
            result = calculation(x, y, oper)
        print(result)
        memory = store_result(result, memory)
        more = do_we_continue()
        if more == 1:
            continue
        if more == 0:
            break
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")

