from jetbot import Motor


class TestMotor:
    def test_left_forward(self):
        """Test left motor's forward motion."""
        try:
            from Adafruit_MotorHAT import Adafruit_MotorHAT
            channel = 1
            driver = Adafruit_MotorHAT(i2c=1)
            motor = Motor(driver, channel=channel, alpha=1.0)
            value = -0.5  # value in [-1, 1]
            motor.update_value(value)
        except Exception as e:
            print(e)
            
