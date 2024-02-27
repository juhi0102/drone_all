from drone import drone
import time
drone=drone()
drone.connect()
drone = drone()
drone.connect()
drone.takeoff()
time.sleep(2)  # Wait for takeoff
# Perform a series of movements
drone.roll_speed(50, 2)  # Roll right for 2 seconds
drone.pitch_speed(50, 2)  # Move forward for 2 seconds
drone.yaw_speed(100, 2)  # Yaw right for 2 seconds
drone.roll_speed(-50, 2)  # Roll left for 2 seconds
drone.pitch_speed(-50, 2)  # Move backward for 2 seconds
drone.yaw_speed(-100, 2)  # Yaw left for 2 seconds
# Land
drone.land()
drone.disconnect()
