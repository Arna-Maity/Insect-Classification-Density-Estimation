import pickle
import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()

with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','rb') as f:
    i = pickle.load(f)

host = 'rpi3b'

camera.start_preview()
sleep(5)
camera.capture(os.environ['HOME'] + ('/Sync/image%s' % i) + '_' + host + '.jpg')
#camera.capture(('/home/pi/Sync/image%s.jpg' % i))

i = i+1
with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','wb') as f:
    pickle.dump(i,f)

camera.stop_preview()