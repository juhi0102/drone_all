import pygame

# Initialize pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check if any joysticks are connected
if pygame.joystick.get_count() == 0:
    print("No joysticks found.")
    pygame.quit()
    quit()

# Initialize the first joystick
controller = pygame.joystick.Joystick(0)
controller.init()

# Main loop
try:
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Print axis values
                print("Axis:", event.axis, "Value:", round(event.value, 2))
            elif event.type == pygame.JOYBUTTONDOWN:
                # Print button press
                print("Button:", event.button, "Pressed")

except KeyboardInterrupt:
    # Quit pygame on Ctrl+C
    pygame.quit()
