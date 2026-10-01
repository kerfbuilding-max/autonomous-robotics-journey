robot_name = "Rover-01"
battery = 51
distance_to_obstacle = 10
speed = 50

print("Robot:", robot_name)
print("Battery:", battery, "%")
print("Obstacle distance:", distance_to_obstacle, "metres")
print ("speed set to:", speed)

if distance_to_obstacle < 1:
    print("STOP!") 
    speed = 0
elif distance_to_obstacle <= 3:
    print("Obstacle nearby - slow down")
    speed = 25
else:
    speed = 50
    print("Path clear - continue")
if battery < 20:
    print("Battery low - return to charging station")

elif battery >= 20 and battery <= 50:
    print("Battery getting low")

else:
    print("Battery ok")
print("Final speed:", speed)

