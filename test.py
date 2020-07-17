import cv2, dlib
import numpy as np
from imutils import face_utils
from keras.models import load_model
import time
import serial

a = 1
port = 'COM5'
camera = 1
img_w = 640
img_h = 480
bpp = 3
sec = 0
open_eye = 0
pointer = 0


center_x = int(img_w/2.0)
center_y = int(img_h/2.0)
location1 = (center_x-150,center_y-120)
location2 = (center_x+150,center_y-120)
location3 = (center_x,center_y-120)

cnt = 0
IMG_SIZE = (34, 26)


arduino = serial.Serial(port, 9600)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

model = load_model('models/2018_12_17_22_58_35.h5')
model.summary()

def crop_eye(img, eye_points): 
  x1, y1 = np.amin(eye_points, axis=0)
  x2, y2 = np.amax(eye_points, axis=0)
  cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

  w = (x2 - x1) * 1.2
  h = w * IMG_SIZE[1] / IMG_SIZE[0]

  margin_x, margin_y = w / 2, h / 2

  min_x, min_y = int(cx - margin_x), int(cy - margin_y)
  max_x, max_y = int(cx + margin_x), int(cy + margin_y)

  eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)

  eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]

  return eye_img, eye_rect

# main
cap = cv2.VideoCapture(camera)

while cap.isOpened():
  ret, img_ori = cap.read()

  if not ret:
    break

  img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=1.2, fy=1.2)

  img = img_ori.copy()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


  faces = detector(gray)

  try:
    
  
    for face in faces:
      if len(faces)==1 :
        shapes = predictor(gray, face)
        shapes = face_utils.shape_to_np(shapes)

        eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
        eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])

        eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
        eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
        try:
          eye_img_r = cv2.flip(eye_img_r, flipCode=1)
        except:
          pass


        eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
        eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

        pred_l = model.predict(eye_input_l)
        pred_r = model.predict(eye_input_r)

    # visualize
        state_l = 'O' if pred_l > 0.1 else '-'
        state_r = 'O' if pred_r > 0.1 else '-'

        state_l = state_l % pred_l
        state_r = state_r % pred_r

        if state_l == 'O':
          cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(255,0,0), thickness=2)
        else :
          cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(0,0,255), thickness=2)


        if state_r == 'O':
          cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,0,0), thickness=2)
        else :
          cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(0,0,255), thickness=2)
            
      
        if state_r == '-' and state_l =='-' :
          sec+=1
          if sec >= 10:
            open_eye=0

        else :
          sec = 0
          open_eye+=1
      

        if sec >= 30 :    
          cnt +=1
        
          if cnt == 1 :
              arduino.write('1'.encode('utf-8'))
              print(1)
          elif cnt == 2:
              arduino.write('2'.encode('utf-8'))
              print(2)
          elif cnt >= 3:
              arduino.write('3'.encode('utf-8'))
              print(3)
              cnt = 0
              arduino.write('0'.encode('utf-8'))

          sec=0
          open_eye = 0

        if open_eye == 100:
          arduino.write('0'.encode('utf-8'))
          cnt = 0
          open_eye = 0


      cv2.putText(img, str(sec/10), location1, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255),2)
      cv2.putText(img, str(cnt), location2, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255),2)
      cv2.putText(img, str(open_eye/10), location3, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0),2)
  
  except:
    pass

  cv2.namedWindow("result", cv2.WND_PROP_FULLSCREEN) 
  cv2.setWindowProperty("result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN) 

   
  cv2.imshow('result', img)
  if cv2.waitKey(1) == ord('q'):
    break


