#Write a program to find the distance and slope between two points in cartesian cordinate system
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def calculate_distance(p1, p2):
    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return distance

def calculate_slope(p1, p2):
    if p2.x - p1.x == 0:
        return None  # Slope is undefined for vertical lines
    slope = (p2.y - p1.y) / (p2.x - p1.x)
    return slope

P1=Point(7,5)
P2=Point(5,7)

distance = calculate_distance(P1, P2)
slope = calculate_slope(P1, P2)

print(f"Distance between the points: {distance:.2f}")
if slope is None:
    print("Slope: Undefined (vertical line)")
else:
    print(f"Slope between the points: {slope:.2f}")