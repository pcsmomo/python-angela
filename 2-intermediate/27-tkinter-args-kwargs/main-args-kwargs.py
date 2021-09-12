# Unlimited Arguments (Unlimited Positional Arguments)
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 7, 9, 10))
