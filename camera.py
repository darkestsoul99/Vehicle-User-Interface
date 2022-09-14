from picamera import PiCamera
import time

class piCamera(): 
    def __init__(self, parent=None):
        self.camera = PiCamera()
        self.camera.start_preview()
        time.sleep(5)


