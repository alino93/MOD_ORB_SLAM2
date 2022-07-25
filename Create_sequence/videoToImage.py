import cv2

cap = cv2.VideoCapture('RC5_OR_0002.mp4')
frame_exists, curr_frame = cap.read()
frame_exists, curr_frame = cap.read()
frame_exists, curr_frame = cap.read()   # dump a couple of frames
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS: ",fps)
timestamps = []

while (frame_exists):
    frame_exists, curr_frame = cap.read()
    image = cv2.rotate(curr_frame, cv2.ROTATE_180)
    if frame_exists:
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)/1000 + 1341841873
        timestamps.append(timestamp)
        cv2.imwrite('%10.6f.png' % timestamp, image)
    else:
        break

cap.release()

try:
    with open('rgb.txt', 'w') as f:
        f.write('# timestamp filename\n')
        for i, timestamp in enumerate(timestamps[:-14]):
            f.write('{timestamp1:10.6f} images/{timestamp2:10.6f}.png\n'.format(timestamp1=timestamp, timestamp2=timestamp))
            # print('Frame %d difference:'%i, abs(ts - cts))
except FileNotFoundError:
    print("The name already exists")






