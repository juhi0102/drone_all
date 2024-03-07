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

    print("Performing controlled descent with hover...")

    # Descend slowly for 10 seconds
    my_drone.throttle_speed(-50, 10)

    # Hover for 5 seconds
    my_drone.throttle_speed(0, 5)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
