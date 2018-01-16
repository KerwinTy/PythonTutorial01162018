#import numpy as np
#import cv2

# Load an color image in grayscale
#img = cv2.imread('dlsu.png', 0)

#print(img)
#print (img.shape)
#cv2.imshow('dlsu.png',img)
#cv2.imwrite('dlsu1.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import numpy as np
import cv2

#cap = cv2.VideoCapture("McDonalds 15-Second Commercial.mp4")

#while(True):
    # Capture frame-by-frame
    #ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    #if cv2.waitKey(25) & 0xFF == ord('q'):
        #break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#while(cap.isOpened()):
    #ret, frame = cap.read()
    #if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        #out.write(frame)

        #cv2.imshow('frame',frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
    #else:
        #break

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    out.write(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
