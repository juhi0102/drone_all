from drone_module import drone

def main():
    my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    print("Performing stabilized hover with manual control...")

    # Adjust roll, pitch, and yaw manually while hovering
    for _ in range(10):  # Adjust control for 10 seconds
        my_drone.roll_speed(50, 1)  # Adjust roll
        my_drone.pitch_speed(-50, 1)  # Adjust pitch
        my_drone.yaw_speed(50, 1)  # Adjust yaw

    # Hold stable hover
    print("Stabilizing hover...")
    my_drone.roll_speed(0, 5)
    my_drone.pitch_speed(0, 5)
    my_drone.yaw_speed(0, 5)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
