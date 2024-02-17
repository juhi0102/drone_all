
# Pluto Python Wrapper

This is a special python wrapper for pluto drone equipped with the Lewei camera.

Go ahead and pull up the terminal and type:
```bash
git clone https://github.com/csaail/Python-Wrapper.git
```

In the script, drone is the object created of class drone which will be used to control the drone. Assuming that the name of the object created is drone, follow the lines below for using the wrapper.

```python
1. Connect The drone:
from drone import drone
drone = drone()
drone.connect()

2. Trim the drone:
drone.trim(Roll, Pitch, Throttle, Yaw) +ve, ve values depending on the trim
Example: drone.trim(0, 0, 0, 0)

3. Arm the drone:
This is typically done automatically upon connection and takeoff.
drone.arm()

4. Disarm the drone:
drone.disarm()

5. Set throttle speed:
drone.throttle_speed(value, Duration)
Example: drone.throttle_speed(5, 1) # Increase throttle speed by 5 for 1 second

6. Takeoff:
drone.takeoff()

7. Land the drone:
drone.land()

8. Roll, Pitch, Yaw:
Functions like roll_speed, pitch_speed, and yaw_speed are available for controlling the drone's
movements.
• drone.roll_speed(50,2) # Increase roll speed by 50 for 2 sec
• drone.pitch_speed(50,2) # Increase pitch speed by 50 for 2 sec
• drone.yaw_speed(50,2) # Increase yaw speed by 50 for 2 sec

9. Get Roll, Pitch & Yaw values:
Functions like get_roll, get_pitch, get_yaw are available for retrieving the drone's roll and pitch angles.

10. Get Sensor values (Magnetometer, Gyroscope, Accelerometer):
Magnetometer: get_mag_x(), get_mag_y(), get_mag_z()
Gyroscope: get_gyro_x(), get_gyro_y(), get_gyro_z()
Accelerometer: get_acc_x(), get_acc_y(), get_acc_z()
```
