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

    print("Performing zigzag flight pattern...")

    # Fly forward and sideways in a zigzag pattern
    for _ in range(5):  # Perform 5 cycles
        my_drone.pitch_speed(100, 2)
        my_drone.roll_speed(100, 1)
        my_drone.roll_speed(-100, 1)
        my_drone.pitch_speed(100, 2)
        my_drone.roll_speed(-100, 1)
        my_drone.roll_speed(100, 1)

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
