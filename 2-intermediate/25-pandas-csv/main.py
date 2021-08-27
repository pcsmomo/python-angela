# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
# <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"]))
# <class 'pandas.core.series.Series'>

print(data["temp"])

# Frame to Dictionary
data_dict = data.to_dict()
print(data_dict)

# Series to list
temp_list = data["temp"].to_list()
print(temp_list)

# print average
average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

# max
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Temperature in Fahrenheit
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
