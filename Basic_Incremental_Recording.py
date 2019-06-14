import time
import picamera

for x in range(1):
    print('Start Recording ' + (time.strftime('%c').replace(" " , "_").replace(":","-")))
    with picamera.PiCamera() as camera:
        camera.framerate = (10)
        camera.resolution = (640, 480)
        #camera.start_preview()
        camera.start_recording('Camera/' + (time.strftime('%c').replace(" " , "_") + '.h264'))
        time.sleep(10)
        camera.stop_recording()
    print('Written: ' + time.strftime('%c'))
