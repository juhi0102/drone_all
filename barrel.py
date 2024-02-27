from drone import drone
import time
drone=drone()
drone.connect()
drone.calibrate_acceleration()


drone.takeoff()
time.sleep(3)  # Wait for takeoff
# Perform a barrel roll
drone.roll_speed(100, 3)  # Roll right quickly for 3 seconds
drone.yaw_speed(100, 2)  # Yaw right quickly for 2 seconds
# Reset and land
drone.reset_speed()
time.sleep(1)
drone.land()
drone.disconnect()
