def turn_left():
    print("turn left")
def move():
    print("move")
def at_goal():
    print("at_goal")
def wall_in_front():
    print("wall_in_front")
def front_is_clear():
    print("front_is_clear")
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()