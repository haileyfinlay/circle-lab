import math

radius = float(input("Please enter a radius size: "))
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def diameter(self):
        return 2*self.radius
    def circumference(self):
        return 2*math.pi*self.radius
    def area(self):
        return math.pi*(self.radius**2)

    def grow(self):
        self.radius = 2*self.radius

    def get_radius(self):
        return(self.radius)

user_circle = Circle(radius)

print(f'Diameter: {user_circle.diameter()}\
    \nCircumference: {user_circle.circumference()}\
    \nArea: {user_circle.area()}')

user_grow = input("Do you want the circle to grow? (y/n): ")

if user_grow == "y":
    print("Stand by while your circle magically grows...")
    user_circle.grow()
    print(f'Diameter: {user_circle.diameter()}\
        \nCircumference: {user_circle.circumference()}\
        \nArea: {user_circle.area()}')
else:
    print(f"Goodbye. Your radius was {user_circle.get_radius()}")