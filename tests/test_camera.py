from jetbot import Camera, bgr8_to_jpeg
from random import random
import time


class TestCamera:
    def test_init_start_stop(self):
        """Test camera's thread init/start/stop methods."""
        camera = Camera()
        camera.start()
        time.sleep(1)
        image = bgr8_to_jpeg(camera.value)
        camera.stop()
        assert image == bgr8_to_jpeg(camera.value)
        
            
