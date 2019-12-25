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
    
    def test_forward(self):
        robot = Robot()
        for speed in (random() for _ in range(5)):
            robot.forward(speed)
            left_val = robot.left_motor.value
            right_val = robot.right_motor.value
            assert left_val == right_val

    def test_backward(self):
        robot = Robot()
        for speed in (random() for _ in range(5)):
            robot.backward(speed)
            left_val = robot.left_motor.value
            right_val = robot.right_motor.value
            assert left_val == right_val
            assert left_val == -speed
    
    def test_left(self):
        robot = Robot()
        for speed in (random() for _ in range(5)):
            robot.left(speed)
            left_val = robot.left_motor.value
            right_val = robot.right_motor.value
            assert left_val == -right_val
    
    def test_right(self):
        robot = Robot()
        for speed in (random() for _ in range(5)):
            robot.right(speed)
            left_val = robot.left_motor.value
            right_val = robot.right_motor.value
            assert left_val == -right_val
    
    def test_stop(self):
        robot = Robot()
        robot.stop()
        left_val = robot.left_motor.value
        right_val = robot.right_motor.value
        assert left_val == right_val == 0 