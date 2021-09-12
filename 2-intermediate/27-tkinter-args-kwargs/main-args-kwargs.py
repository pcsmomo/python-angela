# Unlimited Arguments (Unlimited Positional Arguments)
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 7, 9, 10))


# kwargs : Keyword Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Hyundai", model="i30")
print(my_car.make)
print(my_car.model)

# Error occur
# my_car_error = Car(make="Hyundai")
# print(my_car_error.make)


class Car2:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


# No error
my_car2 = Car2(make="Hyundai", model="i30")
print(my_car2.make)
print(my_car2.model)
print(my_car2.colour)
