from drone_module import drone
import random
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

    print("Simulating dynamic obstacle avoidance...")

    # Simulate flying forward while avoiding randomly generated obstacles
    for _ in range(20):
        # Generate random obstacle position (x, y) within the drone's flight range
        obstacle_x = random.randint(-50, 50)
        obstacle_y = random.randint(-50, 50)

        print(f"Detected obstacle at ({obstacle_x}, {obstacle_y})")

        # Adjust drone's flight path to avoid the obstacle
        if obstacle_x < 0:
            my_drone.roll_speed(50, 1)  # Move right
        else:
            my_drone.roll_speed(-50, 1)  # Move left

        if obstacle_y < 0:
            my_drone.pitch_speed(50, 1)  # Move forward
        else:
            my_drone.pitch_speed(-50, 1)  # Move backward

        time.sleep(1)  # Pause for observation

    # Continue flying forward after avoiding obstacles
    my_drone.pitch_speed(100, 5)  # Fly forward

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
