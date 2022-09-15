import cv2
from GazeTracking import gaze_tracking
import time

gaze = gaze_tracking.GazeTracking()
start = time.time()

data = {"distracted":0,"None":0}

webcam = cv2.VideoCapture(0)
total_distracted_time = 0
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    start_time = time.time()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    status = ""
    instant_distracted_time = 0
    if gaze.is_blinking():
        status = "Blinking"
    elif gaze.is_right():
        status = "distracted"
        instant_distracted_time = time.time() -  start_time
    elif gaze.is_left():
        status = "distracted"
        instant_distracted_time = time.time() -  start_time
    elif gaze.is_center():
        status = "Looking center"
    if status == "distracted":
        total_distracted_time += instant_distracted_time 
    cv2.imshow("Attention seeker", frame)

    if cv2.waitKey(1) == 27:
        end = time.time()
        break
webcam.release()
cv2.destroyAllWindows()
total_time = end - start # time(in secs) the program ran for 
print(" total time : ",total_time)
print(" total time you were distracted : ",total_distracted_time)

