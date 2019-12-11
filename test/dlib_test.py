# _*_ coding: utf-8 _*_
import cv2
import dlib
import numpy as np
import sys
import os
from math import *
def dlib_test_001():
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("../model/shape_predictor_68_face_landmarks.dat")

    #读取图片
    img = cv2.imread("../app/static/images/face.png")

    # 取灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 人脸数rects
    rects = detector(img_gray, 0)
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img,rects[i]).parts()])
        for idx, point in enumerate(landmarks):
            # 68点的坐标
            pos = (point[0, 0], point[0, 1])
            print(idx,pos)

            # 利用cv2.circle给每个特征点画一个圈，共68个
            cv2.circle(img, pos, 5, color=(0,255,0))
            # 利用cv2.putText输出1-68
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(idx+1), pos, font, 0.5, (0,0,255), 1,cv2.LINE_AA)

    cv2.namedWindow("img", 2)
    cv2.imshow("img", img)
    cv2.imwrite("../app/static/images/face_2.png",img)
    cv2.waitKey(0)

import face_recognition
from PIL import Image,ImageDraw
def face_recognition_test_001():
    image = face_recognition.load_image_file("../app/static/images/face.png")
    face_location = face_recognition.face_locations(image)
    print(face_location)

    face_landmarks_list = face_recognition.face_landmarks(image)
    print(face_landmarks_list)
    pil_image = Image.fromarray(image)
    for face_landmarks in face_landmarks_list:
        d = ImageDraw.Draw(pil_image, 'RGBA')

        # Make the eyebrows into a nightmare
        d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

        # Gloss the lips
        d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
        d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

        # Sparkle the eyes
        d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

        # Apply some eyeliner
        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

        pil_image.show()


if __name__ == "__main__":
    # face_recognition_test_001()
    dlib_test_001()