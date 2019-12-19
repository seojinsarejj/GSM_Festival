import cv2
import dlib
from math import hypot

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
    
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        left_point = (landmarks.part(36).x, landmarks.part(36).y)
        left_top = (landmarks.part(37).x, landmarks.part(37).y)
        right_top = (landmarks.part(38).x, landmarks.part(38).y)
        right_point = (landmarks.part(39).x, landmarks.part(39).y)
        right_bottom = (landmarks.part(40).x, landmarks.part(40).y)
        left_bottom = (landmarks.part(41).x, landmarks.part(41).y)
        left_point_to_left_top = midpoint(landmarks.part(36), landmarks.part(37))
        left_top_to_right_top = midpoint(landmarks.part(37), landmarks.part(38))
        right_top_to_right_point = midpoint(landmarks.part(38), landmarks.part(39))
        right_point_to_right_bottom = midpoint(landmarks.part(39), landmarks.part(40))
        right_bottom_to_left_bottom = midpoint(landmarks.part(40), landmarks.part(41))
        left_bottom_to_left_point = midpoint(landmarks.part(41), landmarks.part(36))


        left_point1 = (landmarks.part(42).x, landmarks.part(42).y)
        left_top1 = (landmarks.part(43).x, landmarks.part(43).y)
        right_top1 = (landmarks.part(44).x, landmarks.part(44).y)
        right_point1 = (landmarks.part(45).x, landmarks.part(45).y)
        right_bottom1 = (landmarks.part(46).x, landmarks.part(46).y)
        left_bottom1 = (landmarks.part(47).x, landmarks.part(47).y)
        left_point_to_left_top1 = midpoint(landmarks.part(42), landmarks.part(43))
        left_top_to_right_top1 = midpoint(landmarks.part(43), landmarks.part(44))
        right_top_to_right_point1 = midpoint(landmarks.part(44), landmarks.part(45))
        right_point_to_right_bottom1 = midpoint(landmarks.part(45), landmarks.part(46))
        right_bottom_to_left_bottom1 = midpoint(landmarks.part(46), landmarks.part(47))
        left_bottom_to_left_point1 = midpoint(landmarks.part(47), landmarks.part(42))

        line1 = cv2.line(frame, left_point, left_point_to_left_top, (0, 255, 0), 2)
        line2 = cv2.line(frame, left_point_to_left_top, left_top, (0, 255, 0), 2)
        line3 = cv2.line(frame, left_top, left_top_to_right_top, (0, 255, 0), 2)
        line4 = cv2.line(frame, left_top_to_right_top, right_top, (0, 255, 0), 2)
        line5 = cv2.line(frame, right_top, right_top_to_right_point, (0, 255, 0), 2)
        line6 = cv2.line(frame, right_top_to_right_point, right_point, (0, 255, 0), 2)
        line7 = cv2.line(frame, right_point, right_point_to_right_bottom, (0, 255, 0), 2)
        line8 = cv2.line(frame, right_point_to_right_bottom, right_bottom, (0, 255, 0), 2)
        line9 = cv2.line(frame, right_bottom, right_bottom_to_left_bottom, (0, 255, 0), 2)
        line10 = cv2.line(frame, right_bottom_to_left_bottom, left_bottom_to_left_point, (0, 255, 0), 2)
        line11 = cv2.line(frame, left_bottom,left_bottom_to_left_point, (0, 255, 0), 2)
        line12 = cv2.line(frame, left_bottom_to_left_point, left_point, (0, 255, 0), 2)
        
        
        
        lline1 = cv2.line(frame, left_point1, left_point_to_left_top1, (0, 255, 0), 2)
        lline2 = cv2.line(frame, left_point_to_left_top1, left_top1, (0, 255, 0), 2)
        lline3 = cv2.line(frame, left_top1, left_top_to_right_top1, (0, 255, 0), 2)
        lline4 = cv2.line(frame, left_top_to_right_top1, right_top1, (0, 255, 0), 2)
        lline5 = cv2.line(frame, right_top1, right_top_to_right_point1, (0, 255, 0), 2)
        lline6 = cv2.line(frame, right_top_to_right_point1, right_point1, (0, 255, 0), 2)
        lline7 = cv2.line(frame, right_point1, right_point_to_right_bottom1, (0, 255, 0), 2)
        lline8 = cv2.line(frame, right_point_to_right_bottom1, right_bottom1, (0, 255, 0), 2)
        lline9 = cv2.line(frame, right_bottom1, right_bottom_to_left_bottom1, (0, 255, 0), 2)
        lline10 = cv2.line(frame, right_bottom_to_left_bottom1, left_bottom_to_left_point1, (0, 255, 0), 2)
        lline11 = cv2.line(frame, left_bottom1,left_bottom_to_left_point1, (0, 255, 0), 2)
        lline12 = cv2.line(frame, left_bottom_to_left_point1, left_point1, (0, 255, 0), 2)
        



        cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
