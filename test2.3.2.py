import evdev

def get_joystick_values(device_path):
    try:
        # Open the joystick device
        device = evdev.InputDevice(device_path)
        print("Successfully opened joystick device:", device)

        for event in device.capabilities().get(evdev.ecodes.EV_KEY, []):
            print("Event:", event)

        # Read events from the device
        for event in device.read_loop():
            print("Event type:", event.type)
            print("Event code:", event.code)
            print("Event value:", event.value)

    except FileNotFoundError:
        print("Failed to open joystick device:", device_path)

if __name__ == "__main__":
    device_path = "/dev/input/event23"  # Replace X with the appropriate event number
    get_joystick_values(device_path)
