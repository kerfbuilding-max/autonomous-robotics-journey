robot_name = "Rover-01"
battery = 15
distance_to_obstacle = 5

print("Robot:", robot_name)
print("Battery:", battery, "%")
print("Obstacle distance:", distance_to_obstacle, "metres")

if distance_to_obstacle < 1:
    print("STOP!")
elif distance_to_obstacle < 3:
    print("Obstacle nearby - slow down")
else:
    print("Path clear - continue")

if battery < 20:
    print("Battery low - return to charging station")