from drone import drone

    my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    print("Performing slalom flight maneuver...")

    # Perform a slalom flight maneuver
    for _ in range(5):  # Perform 5 slalom loops
        # Perform a left slalom loop
        my_drone.roll_speed(-100, 1)
        my_drone.pitch_speed(50, 1)
        my_drone.roll_speed(100, 1)
        # Perform a right slalom loop
        my_drone.roll_speed(100, 1)
        my_drone.pitch_speed(50, 1)
        my_drone.roll_speed(-100, 1)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

