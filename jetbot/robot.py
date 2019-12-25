import time
from Adafruit_MotorHAT import Adafruit_MotorHAT
from .motor import Motor


class Robot(object):
    def __init__(self,
                 i2c_bus=1,
                 left_motor_channel=1,
                 right_motor_channel=2,
                 left_motor_alpha=1.0,
                 right_motor_alpha=1.0,
                 *args,
                 **kwargs):
        self.motor_driver = Adafruit_MotorHAT(i2c_bus=i2c_bus)
        self.left_motor = Motor(self.motor_driver,
                                channel=left_motor_channel,
                                alpha=left_motor_alpha)
        self.right_motor = Motor(self.motor_driver,
                                 channel=right_motor_channel,
                                 alpha=right_motor_alpha)

    def set_motors(self, left_speed, right_speed):
        self.left_motor.update_value(left_speed)
        self.right_motor.update_value(right_speed)

    def forward(self, speed=1.0, duration=None):
        self.left_motor.update_value(speed)
        self.right_motor.update_value(speed)

    def backward(self, speed=1.0):
        self.left_motor.update_value(-speed)
        self.right_motor.update_value(-speed)

    def left(self, speed=1.0):
        self.left_motor.update_value(-speed)
        self.right_motor.update_value(speed)

    def right(self, speed=1.0):
        self.left_motor.update_value(speed)
        self.right_motor.update_value(-speed)

    def stop(self):
        self.left_motor.update_value(0)
        self.right_motor.update_value(0)
