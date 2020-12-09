import cv2
import numpy as np

def sketch(image):
    scale=0.40
    height=int(image.shape[0]*scale)
    width=int(image.shape[1]*scale)
    dim=(width,height)
    resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    sharp=cv2.filter2D(resize,-1,kernel)
    gray=cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)
    inv=255-gray
    #apply bluring
    blur=cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)
    #draw sketch
    s=cv2.divide(gray,255-blur,scale=256)
    return s

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    cv2.imshow('Live_Sketch_one',sketch(frame))
    # Key13==ENTER_KEY
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
