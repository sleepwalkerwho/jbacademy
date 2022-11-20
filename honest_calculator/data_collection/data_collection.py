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
        break
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")

