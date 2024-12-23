import cv2

for i in range(4):
    rasm = cv2.imread(f"{i}.jpg")
    oqqora = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite(f"{i}_oqqora.jpg", oqqora)