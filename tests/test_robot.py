from jetbot import Robot
from random import random


class TestRobot:
    def test_set_motors(self):
        robot = Robot()
        for speed in (random() for _ in range(5)):
            robot.set_motors(speed, speed)
            left_val = robot.left_motor.value
            right_val = robot.right_motor.value
            assert left_val == right_val