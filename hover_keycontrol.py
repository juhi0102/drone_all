from drone_module import drone
import keyboard  # Import the keyboard module

def main():
    my_drone = drone()

    print("Initializing...")
    my_drone.trim(0, 0, 0, 0)
    my_drone.arm()
    print("Drone is armed.")

    print("Taking off...")
    my_drone.takeoff()
    print("Drone is airborne.")

    # Function to hold the position of the drone when a specific key is pressed
    def hold_position():
        print("Holding position...")
        my_drone.roll_speed(0, 2)  # Stop rolling
        my_drone.pitch_speed(0, 2)  # Stop pitching
        my_drone.throttle_speed(0, 2)  # Stop ascending/descending

    print("Press 'H' to hold the position.")

    # Listen for the 'H' key to hold the position
    keyboard.on_press_key('h', lambda _: hold_position())

    print("Use arrow keys to control the drone.")
    print("Press 'Space' to ascend and 'Ctrl' to descend.")
    print("Press 'Q' to land the drone.")

    # Function to control the drone based on keyboard input
    def control_drone(key):
        if key.name == 'up':
            my_drone.pitch_speed(50, 1)  # Move forward
        elif key.name == 'down':
            my_drone.pitch_speed(-50, 1)  # Move backward
        elif key.name == 'left':
            my_drone.roll_speed(-50, 1)  # Move left
        elif key.name == 'right':
            my_drone.roll_speed(50, 1)  # Move right
        elif key.name == 'space':
            my_drone.throttle_speed(50, 1)  # Ascend
        elif key.name == 'ctrl':
            my_drone.throttle_speed(-50, 1)  # Descend
        elif key.name == 'q':
            my_drone.land()  # Land the drone

    # Listen for keyboard events and call the control_drone function
    keyboard.on_press(control_drone)

    # Wait for the 'Q' key to be pressed to exit the program
    keyboard.wait('q')

    print("Exiting program...")

if __name__ == "__main__":
    main()
