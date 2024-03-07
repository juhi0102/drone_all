from drone import drone
import time

drone = drone()
drone.connect()

# Assuming the drone library provides functions for controlling roll, pitch, and yaw separately

drone.takeoff()
time.sleep(3)  # Wait for takeoff

# Perform a barrel roll
roll_speed = 100  # Adjust as necessary
yaw_speed = 50  # Adjust as necessary
duration = 3  # Adjust as necessary

# Roll right quickly while yawing right simultaneously
drone.roll(roll_speed)
drone.yaw(yaw_speed)

time.sleep(duration)

# Stop rolling and yawing
drone.roll(0)
drone.yaw(0)

# Land the drone
drone.land()

drone.disconnect()
