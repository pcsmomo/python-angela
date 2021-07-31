programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "Test"

print(programming_dictionary)

#Loop though a dictionary
for thing in programming_dictionary:
    print(thing)