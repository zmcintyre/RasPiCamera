import time
import picamera

for x in range(1):
    print('Camera/Camera-' + str(x) + time.strftime('%A_%B_%d_@_%H-%M') + '.h264')
    time.sleep(2)
    with picamera.PiCamera() as camera:
        camera.resolution = (1296, 972)
        #camera.resolution = (2592,1944)
        camera.framerate = (30)
        camera.start_preview()
        # Camera warm-up time
        camera.start_recording('Camera/Camera-' + str(x) + '_' + time.strftime('%A_%B_%d_@_%H-%M') + '.h264')
        time.sleep(5)
        camera.stop_recording()
