################### Scope ####################

enemies = 1
game_level = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  if game_level < 5:
      new_enemy = enemies[0]
  print(new_enemy)

increase_enemies()
print(f"enemies outside function: {enemies}")

#Out of scope
# print(new_enemy)