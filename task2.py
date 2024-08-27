import sys
import math

def determine_position(circle_file, points_file):
    # Read the circle's center and radius from the first file
    with open(circle_file, 'r') as f:
        x_center, y_center = map(float, f.readline().split())
        radius = float(f.readline().strip())
    
    # Read the points from the second file and determine their position
    with open(points_file, 'r') as f:
        points = [tuple(map(float, line.split())) for line in f.readlines()]
    
    # Calculate and output the position for each point
    for x, y in points:
        distance = math.sqrt((x - x_center)**2 + (y - y_center)**2)
        
        if math.isclose(distance, radius, abs_tol=1e-7):
            print(0)  # On the circle
        elif distance < radius:
            print(1)  # Inside the circle
        else:
            print(2)  # Outside the circle

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]
        determine_position(circle_file, points_file)
