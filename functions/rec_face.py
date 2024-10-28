import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
from cv2 import *
from PIL import Image




def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./data/faces"):
        for f in fnames:
            if f.endswith(".png") or f.endswith('.jpg'):
                face = fr.load_image_file("./data/faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("./data/faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    image = Image.open(im)
    image.thumbnail((400,400))
    image.save('./data/test/face_small.jpg')
    im = './data/test/face_small.jpg'
    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            face_names.append(name)

        
    if len(face_names) != 0:
        print(face_names)
        return True
    return False

def detectFace():

    cascPath = "./data/HaarCascade/haarcascade_frontalface_default.xml"
    # cascPath = "./data/HaarCascade/haarcascade_eye.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
#    log.basicConfig(filename='webcam.log',level=log.INFO)

    video_capture = cv2.VideoCapture(1)
    anterior = 0

    # while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

        # for (x,y,w,h) in faces:
        #     cv2.rectangle(frame, (x,y), (x+w,y+h), (225,225,225,2.5))
            
        # cv2.imshow('qwerty',frame)
        # if cv2.waitKey(1) == 13 or cv2.waitKey(10) == 'q':
        #     break


        # print(f'\n{faces}')
        # print(f'\n{len(faces)}')

    if len(faces) == 0:
        pass
    else:
        capture = cap()
        if capture:
            return True
            # break
        return False

def cap():
    
#     initialize the camera
    cam = cv2.VideoCapture(1)   # 0 -> index of camera
    s, img = cam.read()
    if s:
        cam.release()
        cv2.imwrite("./data/test/face.jpg",img) #save image
        return True
    return False
    
def Recognize():
    
#    if detectFace():
    if classify_face("./data/test/face.jpg"):
        os.system('del data\\test\\face_small.jpg')
        os.system('del data\\test\\face.jpg')
        return True
    return False
# detectFace()