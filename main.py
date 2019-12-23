import cv2
import dlib

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade =  cv2.CascadeClassifier('haarcascade_eye.xml')

eye_detect = False

while True:
    ret, frame = capture.read()

    if ret:

        if eye_detect:
            info = "Eye Detection ON"
        else:
            info = "Eye detection OFF"


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)



        print(len(faces))

        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            if eye_detect:
                roi_gray= gray[y:y+h, x:x+w]
                roi_color=frame[y:y+h,x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
            
        k=cv2.waitKey(30)

        if k == ord('i'):
            eye_detect= not eye_detect

        if k==27:
            break
        

        cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

capture.release()
cv2.destroyAllWindows()