# #Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle

# base = float(input("input base: "))
# height = float(input("input height: "))
# area_of_triangle = 0.5*base*height
# print(area_of_triangle)
#
# #Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle

# side_a = float(input("input side a: "))
# side_b = float(input("input side b: "))
# side_c = float(input("input side c: "))
# perimeter_of_triangle = side_a + side_b + side_c
# print(perimeter_of_triangle)
#
# #Get length and width of a rectangle using prompt. Calculate its area and perimeter

# length_rec = float(input("input length of rectangle: "))
# width_rec = float(input("input width of rectangle: "))
# area_of_rectangle = length_rec*width_rec
# perimeter_of_rectangle = 2*(length_rec + width_rec)
# print(perimeter_of_rectangle)
# print(area_of_rectangle)
#
# #Get radius of a circle using prompt. Calculate the area and circumference where pi = 3.14.

# radius_c = float(input("input radius: "))
# pi = 3.14
# area_of_circle = pi*radius_c**2
# circum_of_circle = pi*radius_c*2
# print(area_of_circle)
# print(circum_of_circle)
#
# #Calculate the slope, x-intercept and y-intercept of y = 2x -2

# # Phương trình dạng y = mx + c: m = 2, c = -2
# slope = 2
# y_intercept = -2
#
# # Giao điểm với trục hoành (x-intercept) khi y = 0: 0 = 2x - 2 => x = 2 / 2 = 1
# x_intercept = 2 / slope
#
# print(f"Hệ số góc (Slope): {slope}")
# print(f"Giao diem với trục tung (Y-intercept): (0, {y_intercept})")
# print(f"Giao diem với trục hoanh (X-intercept): ({x_intercept}, 0)")
#
# #Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# x1, y1 = 2, 2
# x2, y2 = 6, 10
#
# slope = (y2-y1)/(x2-x1)
# d = ((x2-x1)*2+(y2-y1)*2)*0.5
# print(slope)
# print("Euclidean distance: ", d)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# def calculate_y(x):
#     return x*2 +6*x +9
#
# for x in range(0, 5):
#     print(calculate_y(x))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
a = "python"
b = "dragon"
target = "on"
print(target in a and target in b)