# with open("weather_data.csv") as file:
#     print(file.readlines())

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#
#     temperature = []
#     for row in data:
#         # print(row)
#         # print(row[1])
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
# import statistics
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list)/len(temp_list)
# print(avg)
#
# print(data["temp"].mean())
# # print(statistics.mean(temp_list))
#
# max_num = data["temp"].max()
# print(max_num)
#
# Get data in row Monday
# print(data[data.day == "Monday"])

# Return the row that contains the maximum temperature
# print(data[data.temp == data.temp.max()])

#Return condition of Monday
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# cel_temp = monday.temp
# fah_temp = cel_temp*1.8 + 32
# print(fah_temp)


#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
#
# data_frame.to_csv("new_data.csv")



#Create squirrel count based on the db from central park
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# fur_color_list = data["Primary Fur Color"]
# count_color = fur_color_list.value_counts()
# print(count_color)
# df = pandas.DataFrame(count_dict)
# print(df)
# df.to_csv("squirrel_count.csv")


grey = data[data["Primary Fur Color"] == "Gray"]
# print(len(grey))

red = data[data["Primary Fur Color"] == "Cinnamon"]
# print(len(red))

black = data[data["Primary Fur Color"] == "Black"]
# print(len(black))

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey), len(red), len(black)]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")




# new_dataframe = pandas.DataFrame()
