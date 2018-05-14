import numpy as np
import cv2
import itertools
from matplotlib import pyplot as plt
import threading

def exitCam():
    global cap
    # 캠 리소스 해제
    cap.release()

# 캠 캡쳐 핸들 가져온다
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:/Users/KNOTE/AppData/Local/Programs/Python/Python36-32/Lib/site-packages\cv2/data/haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('C:/Users/KNOTE/AppData/Local/Programs/Python/Python36-32/Lib/site-packages\cv2/data/haarcascades/haarcascade_eye.xml')

#10초 타이머후 exitCam메소드 실행
# 루프문
while(True):
    # 캡쳐 Frame
    ret, frame = cap.read()
    ## 프레임 컬러 설정함
    #realFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    realFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    totalSize = realFrame.shape
    lengthX = totalSize[0]
    lengthY = totalSize[1]

    newFrame = np.zeros((lengthX, lengthY), np.uint8)

    #좌우반전!
    realFrame = cv2.flip(realFrame, 1)
    #realFrame = cv2.Laplacian(realFrame, cv2.CV_64F)



    range = 17
    rX = 0
    while lengthX > rX:
        rXEnd = rX+range
        rY = 0
        while lengthY > rY:
            rYEnd = rY+range
            transitionDiv = realFrame[rX:rXEnd,rY:rYEnd]
            tempDiv = newFrame[rX:rXEnd,rY:rYEnd]

            tempSum = transitionDiv.sum()
            tempAvg = tempSum/(range*range)
            tempArr = transitionDiv.tolist()
            tempRangeArr = tempArr
            tempArr = list(itertools.chain(*tempArr))
            #*자로 해당 라인의 평균 차이값을 구해야함 그값을 이미지에 적용해야함.
            newFrame[rX:rXEnd, rY:rYEnd]= cv2.line(tempDiv,(rX,rX),(rX+16,rX+16),(255,255,255),1)

            #총 16방향으로 해당라인의 밝기값일 구한다.


            #newFrame[rX:rXEnd, rY:rYEnd]= cv2.line(tempDiv,(minPositionX,minPositionY),(maxPositionX,maxPositionY),(tempAvg,tempAvg,tempAvg),1)

            rY += range
        rX += range
    #얼굴 프레임 가져오기
    #faces = face_cascade.detectMultiScale(realFrame, 1.1, 1, 0, (10, 10))


    #for (x,y,w,h) in faces:
        #실시간으로 가져오는 얼굴 프레임틀을 realFrame <- 프레임 이미지 에 적용
        #cv2.rectangle(realFrame,(x,y),(x+w,y+h),(0,255,0),1, 4, 0)

    ## 윈도우 프레레임에 보임
    cv2.imshow('frame', realFrame)

    ## 종료 실행
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# 윈도우즈 해제
cv2.destroyAllWindows()