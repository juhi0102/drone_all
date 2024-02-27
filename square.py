from drone import drone
import time
drone=drone()
drone.connect()
drone.calibrate_acceleration()
drone.disarm()
drone.takeoff()
time.sleep(2)  # Wait for takeoff
# Fly in a square pattern
for _ in range(4):
    drone.roll_speed(50, 5)  # Roll to the right for 5 seconds
    drone.yaw_speed(90, 1)  # Rotate 90 degrees clockwise in 1 second
# Land after completing the square flight
drone.land()
drone.disconnect()
