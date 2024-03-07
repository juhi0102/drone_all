    my_drone = drone()

    # Perform actions with the drone
    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)  # Trim the drone
    my_drone.arm()  # Arm the drone
    print("Drone is armed.")
    
    # Takeoff
    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    # Perform some actions (e.g., flying)
    print("Performing actions...")

    # Example: Roll left for 2 seconds
    my_drone.roll_speed(-100, 2)

    # Example: Pitch forward for 2 seconds
    my_drone.pitch_speed(100, 2)

    # Example: Yaw left for 2 seconds
    my_drone.yaw_speed(-100, 2)

    # Example: Flip
    my_drone.flip()

    # Land the drone
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")
