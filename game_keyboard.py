import time
import os
import keyboard_control 
import keyboard
from Pluto import pluto   # Importing the Pluto module for interfacing with the Pluto drone
from drone import drone   # Importing the drone module for drone control

# Initialize Pluto drone object
my_pluto = pluto()
da = drone()
da.connect()

# Function to handle smooth landing
def smooth_landing():
    print("Performing smooth landing...")
    # Implement smooth landing logic here
    my_pluto.land()
    my_pluto.disarm()

# Function to handle the game
def play_game():
    # Takeoff the drone
    my_pluto.takeoff()
    print("Drone is taking off...")
    time.sleep(5)  # Wait for stable flight

    start_time = time.time()
    while time.time() - start_time < 10:
        key = keyboard.read_event().name

        # Map key to drone controls
        if key == 'up':
            da.throttle_up()
        elif key == 'down':
            da.throttle_down()
        elif key == 'left':
            da.yaw_left()
        elif key == 'right':
            da.yaw_right()
        elif key == 'space':
            da.arm_disarm_toggle()
        elif key == 'q':
            da.takeoff()
        elif key == 'e':
            da.land()
        elif key == 'w':
            da.pitch_forward()
        elif key == 's':
            da.pitch_backward()
        elif key == 'a':
            da.roll_left()
        elif key == 'd':
            da.roll_right()
        elif key == 'n':
            print("Entering developer mode...")  # Placeholder for developer mode
        elif key == 'r':
            print("Action r performed...")  # Placeholder for additional action
        elif key == 't':
            print("Action t performed...")  # Placeholder for additional action
        elif key == 'p':
            print("Action p performed...")  # Placeholder for additional action

        # Check for game over condition (LED turns red)
        if my_pluto.check_led_color() == "red":
            print("Game over: LED turned red")
            break

        time.sleep(0.01)  # Adjust sleep time as needed

    # Perform smooth landing
    smooth_landing()

# Start the game
play_game()

# Key Controls:
# c : Connect
# spacebar : arm or disarm
# w : increase height
# s : decrease height
# a : yaw left
# d : yaw right
# q : take off
# e : land
# n : To enter developer mode
# Up arrow : go forward
# Down arrow : go backward
# Left arrow : go left
# Right arrow : go right
# e : to quit
