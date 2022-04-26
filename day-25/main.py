import csv
import pandas

with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))

    #print(temperatures)

#     next(data_file)
#     data = data_file.readlines()
# for data in data:
#     print(data)

data = pandas.read_csv("weather_data.csv")

#data_dict = data.to_dict()
temp_list = data["temp"].to_list()

#print(temp_list)
#print(data_dict)

# total = 0
# for temp in temp_list:
#     total += temp
#     average = total/len(temp_list)
average = sum(temp_list) / len(temp_list)
max = max(temp_list)
# print(average)
# print(max)
#
# print(data.condition)
monday = data[data.day == "Monday"]
#print(data[data.temp == data.temp.max()])

#convert celsius to fahrenheit
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
#print(monday_temp_f)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

dataframe_data = pandas.DataFrame(data_dict)
#print(dataframe_data)

dataframe_data.to_csv("new_data.csv")

data2 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data2[data2.Primary_Fur_Color == "Gray"])
red = len(data2[data2.Primary_Fur_Color == "Cinnamon"])
black = len(data2[data2.Primary_Fur_Color == "Black"])
squirrel_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

squirrel_data_dict = pandas.DataFrame(squirrel_data)

squirrel_data_dict.to_csv("squirrel_count.csv")
#print(squirrel_data_dict)



