my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    print("Performing square flight path...")

    # Fly forward for 5 seconds
    my_drone.pitch_speed(100, 5)

    # Turn right for 2 seconds
    my_drone.yaw_speed(100, 2)

    # Fly forward for 5 seconds
    my_drone.pitch_speed(100, 5)

    # Turn right for 2 seconds
    my_drone.yaw_speed(100, 2)

    # Fly forward for 5 seconds
    my_drone.pitch_speed(100, 5)

    # Turn right for 2 seconds
    my_drone.yaw_speed(100, 2)

    # Fly forward for 5 seconds
    my_drone.pitch_speed(100, 5)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")
