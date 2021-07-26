def turn_left():
    print("turn left")
def move():
    print("move")
def at_goal():
    print("at_goal")
def front_is_clear():
    print("front_is_clear")
def right_is_clear():
    print("right_is_clear")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()