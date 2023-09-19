import os
import cv2

output_dir = '/home/shiv/Downloads/frames1/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
cap = cv2.VideoCapture('/home/shiv/Downloads/HandGuesture.mp4')
    
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()