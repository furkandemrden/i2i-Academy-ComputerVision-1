import cv2

# Open webcam capture
cap = cv2.getTickCount() # ya da cv2.VideoCapture(0) kodun hangisiyse
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.imshow("Webcam Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()