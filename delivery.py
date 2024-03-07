from drone_module import drone
import time

def main():
    my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    print("Performing delivery mission...")

    # Fly to delivery destination and drop the package
    delivery_destination = (50, 50, 20)  # (x, y, altitude)
    print(f"Delivering package to destination: {delivery_destination}")
    my_drone.fly_to_waypoint(delivery_destination[0], delivery_destination[1], delivery_destination[2])
    # Simulate dropping the package
    print("Dropping package...")
    time.sleep(1)  # Simulate package drop time

    # Return to home
    print("Returning to home...")
    my_drone.return_to_home()

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
