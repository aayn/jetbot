import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT


class Motor(object):
    """Used to update speed of the Jetbot motors.
    
    Args:
        driver: An `Adafruit_MotorHAT` instance used to control the motor.
        channel: Motor channel. Left is channel 1 and right is channel 2.
        alpha: Motor configuration parameter.
        beta: Motor configuration parameter.
    """
    def __init__(self, driver, channel, alpha=1.0, beta=0.0, *args, **kwargs):
        self._driver = driver
        self._motor = self._driver.getMotor(channel)
        self.alpha = alpha
        self.beta = beta
        self.value = 0
        atexit.register(self._release)  # Release at exit

    def update_value(self, value):
        """Sets motor value between [-1, 1]."""
        self.value = value
        mapped_value = int(255.0 * (self.alpha * value + self.beta))
        speed = min(max(abs(mapped_value), 0), 255)
        self._motor.setSpeed(speed)
        if mapped_value < 0:
            self._motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            self._motor.run(Adafruit_MotorHAT.BACKWARD)

    def _release(self):
        """Stops motor by releasing control."""
        self._motor.run(Adafruit_MotorHAT.RELEASE)
        
        
