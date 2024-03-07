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

    print("Performing terrain following flight...")

    # Fly while maintaining a constant altitude above terrain
    # For demonstration, simulate a sequence of forward movements and altitude adjustments
    for _ in range(5):
        my_drone.pitch_speed(100, 2)  # Forward movement
        my_drone.altitude_follow(30)  # Maintain altitude at 30 meters

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
