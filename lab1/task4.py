def calculate_area(length, width):
    # Calculate the area of a rectangle.
    area = length * width
    return area


def calculate_volume(length, width, height):
    # Calculate the volume of a rectangle.
    volume = length * width * height
    return volume


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = calculate_area(length, width)
volume = calculate_volume(length, width, height)

print("Area of the rectangle:", area)
print("Volume of the rectangle:", volume)

print("Cleaning Starts...")
