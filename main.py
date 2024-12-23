import cv2

for i in range(5):
    rasm = cv2.imread(f"rasm{i}.jpg")
    oqqora = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite(f"rasm{i}_oqqora.jpg", oqqora)