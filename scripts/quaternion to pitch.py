import math

pitch = 0
roll = 0
yaw = 0

w = 0.7
x = -0.002
y = 0.704
z = 0.002

pitch = math.atan2(2*(w*z+x*y), 1-2*(y*y + z*z))
yaw = math.atan2(2*(w*x+y*z), 1-2*(x*x + y*y))
roll = math.atan2(2*(w*y+z*x), 1-2*(x*x + z*z))

print (math.degrees(pitch))
print (math.degrees(roll))
print (math.degrees(yaw))
