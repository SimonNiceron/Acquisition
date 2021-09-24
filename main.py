import numpy as np
import cv2
from matplotlib import pyplot as plt


img_counter = 0

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read() #1 frame acquise à chaque iteration
    cv2.imshow('Capture_Video', frame) #affichage

    key = cv2.waitKey(1) #on évalue la touche pressée
    if key & 0xFF == ord('q'): #si appui sur 'q'
        break #sortie de la boucle while
    
    elif key%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        hist = cv2.calcHist(frame, [0,1,2], None, [32,32,32], [0,255])
        #plt.plot(hist) #où hist est la sortie de cv2.calcHist
        #plt.title('Histogramme')
        #plt.draw() #execute l'affichage
    
cap.release()
cv2.destroyAllWindows()