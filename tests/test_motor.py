from jetbot import Motor
from random import random


class TestMotor:
    def test_motion(self):
        """Test left/right motor's motion."""
        from Adafruit_MotorHAT import Adafruit_MotorHAT
        channel = 1
        driver = Adafruit_MotorHAT(i2c_bus=1)
        motor = Motor(driver, channel=channel, alpha=1.0)
        # value in [-1, 1]
        for value in ((2 * random() - 1) for _ in range(5)):
            motor.update_value(value)
    
    def test_release(self):
        """Test motor's release function."""
        from Adafruit_MotorHAT import Adafruit_MotorHAT
        channel = 1
        driver = Adafruit_MotorHAT(i2c_bus=1)
        motor = Motor(driver, channel=channel, alpha=1.0)
        motor._release()
            
