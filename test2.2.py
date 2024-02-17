import pygame
import math
from plutoMultiwii import *
from threading import Thread
import time

TRIM_MAX = 1000
TRIM_MIN = -1000
MSP_STATUS = 101

class Pluto():
    def __init__(self):
        self.rcRoll = 1500
        self.rcPitch = 1500
        self.rcThrottle = 1500
        self.rcYaw = 1500
        self.rcAUX1 = 1500
        self.rcAUX2 = 1000
        self.rcAUX3 = 1500
        self.rcAUX4 = 1000
        self.commandType = 0
        self.droneRC = [1500, 1500, 1500, 1500, 1500, 1000, 1500, 1000]
        self.NONE_COMMAND = 0
        self.TAKE_OFF = 1
        self.LAND = 2
        self.thread = Thread(target=self.writeFunction)
        self.thread.start()

    def arm(self):
        print("Arming")
        self.rcRoll = 1500
        self.rcYaw = 1500
        self.rcPitch = 1500
        self.rcThrottle = 1000
        self.rcAUX4 = 1500

    def box_arm(self):
        print("Boxarm")
        self.rcRoll = 1500
        self.rcYaw = 1500
        self.rcPitch = 1500
        self.rcThrottle = 1800
        self.rcAUX4 = 1500

    def disarm(self):
        print("Disarm")
        self.rcThrottle = 1300
        self.rcAUX4 = 1200

    def forward(self):
        print("Forward")
        self.rcPitch = 1600

    def backward(self):
        print("Backward")
        self.rcPitch = 1300

    def left(self):
        print("Left Roll")
        self.rcRoll = 1200

    def right(self):
        print("Right Roll")
        self.rcRoll = 1600

    def left_yaw(self):
        print("Left Yaw")
        self.rcYaw = 1300

    def right_yaw(self):
        print("Right Yaw")
        self.rcYaw = 1600

    def reset(self):
        self.rcRoll = 1500
        self.rcThrottle = 1500
        self.rcPitch = 1500
        self.rcYaw = 1500
        self.commandType = 0

    def increase_height(self):
        print("Increasing height")
        self.rcThrottle = 1800

    def decrease_height(self):
        print("Decreasing height")
        self.rcThrottle = 1300

    def take_off(self):
        self.disarm()
        self.box_arm()
        print("Take off")
        self.commandType = 1

    def land(self):
        self.commandType = 2

    def rcValues(self):
        return [self.rcRoll, self.rcPitch, self.rcThrottle, self.rcYaw,
                self.rcAUX1, self.rcAUX2, self.rcAUX3, self.rcAUX4]

    def trim_left_roll(self):
        print("Trimming Left Roll")
        self.rcRoll = max(TRIM_MIN, self.rcRoll + 100)

    def writeFunction(self):
        requests = list()
        requests.append(MSP_RC)
        requests.append(MSP_ATTITUDE)
        requests.append(MSP_RAW_IMU)
        requests.append(MSP_ALTITUDE)
        requests.append(MSP_ANALOG)
        sendRequestMSP_ACC_TRIM()

        while True:
            self.droneRC[:] = self.rcValues()

            sendRequestMSP_SET_RAW_RC(self.droneRC)
            sendRequestMSP_GET_DEBUG(requests)

            if self.commandType != self.NONE_COMMAND:
                sendRequestMSP_SET_COMMAND(self.commandType)
                self.commandType = self.NONE_COMMAND

            time.sleep(0.022)

    def joystick_control(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print("No joysticks found.")
            return

        controller = pygame.joystick.Joystick(0)
        controller.init()

        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 1:
                            self.rcPitch = int(1500 + event.value * 500)
                        elif event.axis == 0:
                            self.rcRoll = int(1500 + event.value * 500)
                        elif event.axis == 3:
                            self.rcYaw = int(1500 + event.value * 500)
                        elif event.axis == 4:
                            self.rcThrottle = int(1500 - event.value * 500)
                    elif event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            self.take_off()
                        elif event.button == 1:
                            self.land()
                        elif event.button == 2:
                            self.increase_height()
                        elif event.button == 3:
                            self.decrease_height()
                        elif event.button == 4:
                            self.left()
                        elif event.button == 5:
                            self.right()
                        elif event.button == 6:
                            self.forward()
                        elif event.button == 7:
                            self
