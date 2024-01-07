# import sys
# sys.path.append("C:\Code")
# import functions as f
# area = f.calculate_square_area(10)
# area = f.calculate_triangle_area(5,10)
# print(area)


import sys
sys.path.append(r"C:\Code")  # Use raw string to handle backslashes
import functions as f

area_square = f.calculate_square_area(10)
area_triangle = f.calculate_triangle_area(5, 10)

print("Square Area:", area_square)
print("Triangle Area:", area_triangle)
