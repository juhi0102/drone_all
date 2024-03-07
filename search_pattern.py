from drone import drone

    my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    print("Performing search pattern...")

    # Perform a search pattern (square flight with altitude changes)
    for _ in range(4):  # Perform square flight pattern for 4 iterations
        my_drone.pitch_speed(100, 3)  # Forward movement
        my_drone.throttle_speed(50, 2)  # Ascend
        my_drone.yaw_speed(90, 1)  # Turn right
        my_drone.throttle_speed(-50, 2)  # Descend
        my_drone.yaw_speed(-90, 1)  # Turn back to original orientation

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

