import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_names = len(names)
random_choice = random.randint(0, number_of_names-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
# random.choice() is a simpler method 