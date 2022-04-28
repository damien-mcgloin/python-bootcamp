#Challenge 1 - convert sentence into dictionary containing words and word length

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()

result = {item: len(item) for item in sentence_list}

print(result)

#Challenge 2 - convert temperatures in list into fahrenheit and output in dict

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

#Challenge 3
