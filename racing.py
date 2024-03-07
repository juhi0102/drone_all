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

    print("Simulating drone racing...")

    # Define the sequence of actions for each lap
    actions = [(50, 0, 50), (50, 180, 50)]

    # Perform two laps
    for lap in range(2):
        print(f"Starting lap {lap + 1}...")
        for action in actions:
            pitch, yaw, next_pitch = action
            print(f"Performing action: Pitch={pitch}, Yaw={yaw}")
            # Perform the specified actions
            my_drone.pitch_speed(pitch, 1)
            my_drone.yaw_speed(yaw, 1)
            my_drone.pitch_speed(next_pitch, 1)
            # Pause briefly between actions
            time.sleep(1)

    # Finish racing
    print("Finished racing!")

    # Land
    print("Landing...")
    my_drone.land()
    print("Drone has landed.")

if __name__ == "__main__":
    main()
