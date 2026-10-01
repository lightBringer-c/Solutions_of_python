print("Day 2: 30 Days of python programming")

first_name = "Arthur"
last_name = "Pendragon"
ful_name = "Arthur Pendragon"
country = "Vietnam"
city = "Hanoi"
age = 30
year = 2026
is_married = False

#Declare multiple variable on one line
first_name_2, last_name_2, city_2, age_2, is_married_2 = "Arthur", "Pendragon", "Hanoi", 30, False


print(type(first_name))
print(type(age))
print(type(is_married))

print(len(first_name))

#Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

#The radius of a circle is 30 meters
radius = 30
area_of_circle = 3.14*radius*radius
circum_of_circle = 3.14*radius*2
#Take radius as user input and calculate the area
radius_2 = int(input("input radius of circle: "))
area_of_circle_2 = 3.14*radius_2*radius_2
circum_of_circle_2 = 3.14*radius_2*2
print(area_of_circle_2)
print(circum_of_circle_2)