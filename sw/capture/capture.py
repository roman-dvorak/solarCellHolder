import cv2
import time

cam = cv2.VideoCapture(1)

#help(cam)
#cam.set(cv2.CAP_FFMPEG,True)
#cam.set(cv2.CAP_PROP_FPS,25)
print(cam)
time.sleep(0.1)
while(True):
    time.sleep(0.1)
    ret,frame = cam.read()
    #print(frame)
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()