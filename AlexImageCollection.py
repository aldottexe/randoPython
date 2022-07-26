import cv2
import time
import threading
import os
import uuid

def timing(labels, imgCount):
    global topic
    global imgText

    for label in labels:
        topic = label
        for i in range(imgCount):
            imgText = f"{label} {i+1}"
            time.sleep(3)
    imgText = "done!"
    time.sleep(1)

def runCam():
    currentImgText = imgText
    currentTopic = topic

    while timingThread.is_alive():
        ret, img = cam.read()
        img = cv2.putText(img,currentImgText, textOffset, cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255,0),2)
        cv2.imshow('my webcam', img)

        if imgText != currentImgText:
            imgname = os.path.join(IMAGES_PATH,currentTopic,currentTopic+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imgname, img)
            
            currentImgText = imgText
            currentTopic = topic

        if cv2.waitKey(1) == 27:
            break

if __name__ == "__main__":

    IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
    labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
    number_imgs = 5
    textOffset = (50,50)
    img = 0
    cam = cv2.VideoCapture(0)

    if not os.path.exists(IMAGES_PATH):
            os.system(f"mkdir -p {IMAGES_PATH}")
    for label in labels:
        path = os.path.join(IMAGES_PATH, label)
        if not os.path.exists(path):
            os.system(f"mkdir {path}")

    timingThread = threading.Thread(target=timing, args=[labels, number_imgs], daemon=True)
    timingThread.start()
    
    runCam()

    cv2.destroyAllWindows()
