from jetbot import Camera, bgr8_to_jpeg
from random import random
import time


class TestCamera:
    def test_init(self):
        """Test if camera instance is initialzed."""
        camera = Camera()
    
    
    def test_start_stop(self):
        """Test camera's thread start/stop methods."""
        camera = Camera()
        camera.start()
        time.sleep(1)
        image = bgr8_to_jpeg(camera.value)
        camera.stop()
        assert image == bgr8_to_jpeg(camera.value)
        
            
