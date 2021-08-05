################### Scope ####################

enemies = 1
game_level = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  if game_level < 5:
      new_enemy = 'new enemy'
  print(new_enemy)

increase_enemies()
print(f"enemies outside function: {enemies}")

#Out of scope
# print(new_enemy)


################### Scope ####################

enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")