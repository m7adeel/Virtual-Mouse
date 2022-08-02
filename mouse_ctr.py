import cv2
import mediapipe
import pyautogui as pt

cap = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(max_num_hands=2,min_tracking_confidence=0.9,min_detection_confidence=0.5)
mpdraw = mediapipe.solutions.drawing_utils

click = "none"

while True:
    success ,img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    cv2.rectangle(img, (100,100), (400,400), (255,0,0),2)
    
    cv2.rectangle(img,(200,100),(300,400),(255,0,0),2)  
    cv2.rectangle(img,(100,200),(400,300),(255,0,0),2)   
    
    # cv2.circle(img,(570,200),30,(0,0,255),cv2.FILLED) 
    # cv2.circle(img,(500,200),30,(0,255,0),cv2.FILLED) 
    
    cv2.rectangle(img,(570,200),(525,230),(0,255,0),cv2.FILLED)
    cv2.rectangle(img,(525,200),(480,230),(255,0,0),cv2.FILLED)
    

    if results.multi_hand_landmarks:
        for handLns in results.multi_hand_landmarks:
            # mpdraw.draw_landmarks(img, handLns, mpHands.HAND_CONNECTIONS)
            #print(handLns.landmark[8])
            
            h,w,c = img.shape
            
            cx,cy = int(handLns.landmark[8].x * w),int(handLns.landmark[8].y * h)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            
            if cx > 400 or cx < 100 or cy > 400 or cy < 100:
                pass
            else:
                if cx < 200 and cy < 200:
                    # top right
                    pt.moveRel(15,-15,duration=0.01)
                elif cx < 200 and cy < 300 and cy > 200:
                    # right
                    pt.moveRel(15,0,duration=0.01)
                elif cx < 200 and cy < 400 and cy > 300:
                    # bottom right
                    pt.moveRel(15,15,duration=0.01)
                elif cx < 300 and cy < 200 and cx > 200:
                    # top
                    pt.moveRel(0,-15,duration=0.01)
                elif cx < 300 and cy < 300 and cx > 200 and cy > 200:
                    # center 
                    pass
                elif cx < 300 and cy < 400 and cx > 200 and cy > 300:
                    # down
                    pt.moveRel(0,15,duration=0.01)
                elif cx < 400 and cy < 200 and cx > 300:
                    # top left
                    pt.moveRel(-15,-15,duration=0.01)
                elif cx < 400 and cy < 300 and cx > 300 and cy > 200:
                    # left
                    pt.moveRel(-15,0,duration=0.01)
                elif cx < 400 and cy < 400 and cx > 300 and cy > 300:
                    # bottom left
                    pt.moveRel(-15,15,duration=0.01)
                    
            if cx > 480 and cx < 525 and cy > 200 and cy < 230:
                pt.rightClick()
            elif cx > 525 and cx < 570 and cy > 200 and cy < 230:
                if click == "left":
                    pt.mouseDown()
                else:
                    pt.leftClick()
                click = "left"
            else:
                click = "none"
                pt.mouseUp()
                    
                
            
            
                    
            
    
    cv2.imshow("Results",cv2.flip(img,1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
    

