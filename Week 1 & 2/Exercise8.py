def calculate_area(base, height, shape_type="triangle"):
    if shape_type == "triangle":
        return 0.5 * base * height
    elif shape_type == "rectangle":
        return base * height
    else:
        raise ValueError("Invalid shape type. Use 'triangle' or 'rectangle'.")

# Example usage:
triangle_area = calculate_area(4, 6)  # Triangle area
rectangle_area = calculate_area(5, 8, "rectangle")  # Rectangle area
print("Area of the triangle:", triangle_area)
print("Area of the rectangle:", rectangle_area)



def print_pattern(number):
    for i in range(1, number + 1):
        for j in range(i):
            print("*", end="")
        print()

# Example usage:
print_pattern(3)
print_pattern(4)
