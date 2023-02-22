import math

print("Hello Console")
my_name = "My name is Andrew Jarjis"
print(my_name)
work_from_home = True
side = 15
radius = 10
print("I work from home:" + str(work_from_home))
txt = "The radius of the circle is " + str(radius)
print(f"The length of each side of the square is {side}")
print(txt)
square_area = side * side
square_perimeter = 4 * side
circle_area = math.pi * radius * radius
circle_perimeter = radius * math.pi * 2
print(
    f"The square area is {square_area} and the perimeter is {square_perimeter} and the perimeter is {square_perimeter}")
print(f"The circle area is {circle_area} and the perimeter is {circle_perimeter}")
travel_options = ['foot', "bike", "car", "airplane"]
print('The travel options are:')
print(f"1) {travel_options[0]}")
print(f"2) {travel_options[1]}")
print(f"3) {travel_options[2]}")
print(f"4) {travel_options[3]}")
print("How would you like to travel?")
travel_type = input()
print(f"Travel type: {travel_type}")
distance = 100
time = 0
cost = 0
if travel_type == 'foot':
    print("Walking is free! Speed is 3mph")
    cost = 0
    time = distance / 3
    cost_bar = "Cost: "
    for x in range(int(cost)):
        cost_bar += "$"
    print(cost_bar)  # "Cost: $$$"

    time_bar = "Time: "
    for x in range(math.ceil(time)):
        time_bar += "/"
    print(time_bar)  # "Cost: $$$"

elif travel_type == "bike":
    rent_bike = input("Do you need to rent the bike? (yes or no)")
    if rent_bike == "yes":
        print("Bike rental is $45! Speed is 10mph")
        cost = 45
        cost_bar = "Cost: "
        for x in range(int(cost)):
            cost_bar += "$"
        print(cost_bar)  # "Cost: $$$"

        time_bar = "Time: "
        for x in range(math.ceil(time)):
            time_bar += "/"
        print(time_bar)  # "Cost: $$$"

    else:
        print("Biking is free! Speed is 10mph")
        cost = 0

    time = distance / 10
    cost_bar = "Cost: "
    for x in range(int(cost)):
        cost_bar += "$"
    print(cost_bar)  # "Cost: $$$"

    time_bar = "Time: "
    for x in range(math.ceil(time)):
        time_bar += "/"
    print(time_bar)  # "Cost: $$$"

elif travel_type == "car":
    print("Driving is $0.25/mi.Speed is 60mph")
    cost = .25 * distance
    time = distance / 60

    cost_bar = "Cost: "
    for x in range(int(cost)):
        cost_bar += "$"
    print(cost_bar)  # "Cost: $$$"

    time_bar = "Time: "
    for x in range(math.ceil(time)):
        time_bar += "/"
    print(time_bar)  # "Cost: $$$"

elif travel_type == "airplane":
    passenger_count = input("How many passengers?")
    passenger_count = int(passenger_count)
    print("Flying is $0.10/mi. Speed is 400mph")
    cost = .1 * distance * passenger_count
    time = distance / 400
    cost_bar = "Cost: "
    for  x in range(int(cost)):
        cost_bar += "$"
    print(cost_bar)  # "Cost: $$$"

    time_bar = "Time: "
    for x in range(math.ceil(time)):
        time_bar += "/"
    print(time_bar)  # "Cost: $$$"
else:
    print(f"Sorry.  {travel_type} is an invalid option")
print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")
