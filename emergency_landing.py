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

    # Simulate an emergency situation
    print("Initiating emergency stop...")

    # Cut throttle to stop the drone immediately
    my_drone.throttle_speed(-500, 1)  # Reduce throttle by 500 (assuming current throttle is 1500)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
