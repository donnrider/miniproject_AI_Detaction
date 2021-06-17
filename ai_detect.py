import cv2 , os
import numpy as np

cap = cv2.VideoCapture(0)
path = './images/'
b = c = l =  e = w =0

while True:
    check, frame = cap.read()
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('b'): b += 1; cv2.imwrite(path + 'bottle_' + str(b) + '.png', frame)
    if key == ord('c'): c += 1; cv2.imwrite(path + 'camera_' + str(c) + '.png', frame)
    if key == ord('l'): l += 1; cv2.imwrite(path + 'ligth_' + str(l) + '.png', frame)
    if key == ord('e'): e += 1; cv2.imwrite(path + 'else_' + str(e) + '.png', frame)
    if key == ord('w'): w += 1; cv2.imwrite(path + 'winai_' + str(w) + '.png', frame)
    if key == ord('q'): break
    y = [] ;  D = []

    for fname in os.listdir(path):
        if '.png' in fname:
            x = cv2.imread(path + fname)
            y.append(fname.split('_')[0])
            D.append(np.sum((x-frame)**2))  #ใช้ algorithm nearest neighbor หาเส้นจุด X , Y
            
    if len(D) > 0:
        ans = y[D.index(min(D))] #คำตอบคือ index ตัวแรกของตัวแปร D
        if ans != 'else' : cv2.putText(frame , ans , (400,450), cv2.FONT_HERSHEY_COMPLEX , 1, (255,0,0))

    cv2.imshow('frame',frame)
    