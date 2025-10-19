import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime

path = "image attendance"
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)

# Load all images and names
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    else:
        print(f"Warning: Unable to load image {cl}")

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_encodings(img)
        if len(faces) > 0:
            encodeList.append(faces[0])
        else:
            print("No face found in one of the images.")
    return encodeList

def markAttendance(name):
    # Create file if it doesn't exist
    if not os.path.exists('attendance.csv'):
        with open('attendance.csv', 'w') as f:
            f.write('Name,Time\n')

    # Open in append + read mode
    with open('attendance.csv', 'a+') as f:
        f.seek(0)
        mydatalist = f.readlines()
        nameList = [line.strip().split(',')[0] for line in mydatalist]

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.write(f'{name},{dtString}\n')
            print(f"✅ Attendance marked for {name}")

encodelistknown = findEncodings(images)
print(f'Total encodings found: {len(encodelistknown)}')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facecurframe = face_recognition.face_locations(imgs)
    encodecurframe = face_recognition.face_encodings(imgs, facecurframe)

    for encodeFace, faceloc in zip(encodecurframe, facecurframe):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        facedis = face_recognition.face_distance(encodelistknown, encodeFace)
        match_index = np.argmin(facedis)

        if matches[match_index]:
            name = classNames[match_index].upper()
            print(name)
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, name, (x1+8, y2-8), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Video', img)
    cv2.waitKey(1)
