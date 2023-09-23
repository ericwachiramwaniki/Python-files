import math

# Input the radius from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume = (4/3) * math.pi * math.pow(radius, 3)

# Print the result
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")
