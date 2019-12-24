from jetbot import Motor
import random


class TestMotor:
    def test_motion(self):
        """Test left/right motor's motion."""
        try:
            from Adafruit_MotorHAT import Adafruit_MotorHAT
            channel = 1
            driver = Adafruit_MotorHAT(i2c=1)
            motor = Motor(driver, channel=channel, alpha=1.0)
            # value in [-1, 1]
            for value in ((2 * random.random() - 1) for _ in range(5)):
                motor.update_value(value)
        except Exception as e:
            print(f'Test failed:\n {e}')
    
    def test_release(self):
        """Test motor's release function."""
        try:
            from Adafruit_MotorHAT import Adafruit_MotorHAT
            channel = 1
            driver = Adafruit_MotorHAT(i2c=1)
            motor = Motor(driver, channel=channel, alpha=1.0)
            motor._release()
        except Exception as e:
            print(f'Test failed:\n {e}')
            
