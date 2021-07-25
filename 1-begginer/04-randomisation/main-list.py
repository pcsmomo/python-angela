states_of_america = ["Dalaware", "Pennsylvania", "New Jersey"]

print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[-2])

states_of_america[1] = "Penn"
states_of_america.append("Virginia")
states_of_america.extend(["New York", "North Carolina"])

print(states_of_america)

fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
