""" import csv

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures) """

import pandas

data = pandas.read_csv("weather_data.csv")
""" print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
print(data["temp"].max()) """


""" print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) """

#Dataframe from scratch?
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 54, 34]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")