import cv2
from cvzone.HandTrackingModule import HandDetector
import random
import time
import pyttsx3
cap = cv2.VideoCapture(0)  
detector = HandDetector()
sp = pyttsx3.init()
gestures = ["rock", "paper", "scissors"]
def detect_user_gesture(img):
    img1 = detector.findHands(img, draw = False)
   
    if img1:
        lmlist = img1[0]
        handphoto = detector.fingersUp(lmlist)
        return img, handphoto
    else:
        return None, None    
def get_computer_gesture():
    return random.choice(gestures)
def get_winner(user_gesture, computer_gesture):
    
    if user_gesture == computer_gesture:
        sp.say("its a tie")
        sp.runAndWait()
        return "It's a tie!"
    
    elif (user_gesture == "rock" and computer_gesture == "scissors") or \
         (user_gesture == "paper" and computer_gesture == "rock") or \
         (user_gesture == "scissors" and computer_gesture == "paper"):
        sp.say("You Win")
        sp.runAndWait()
        
        return "You win!"
    
    else:
        sp.say("Computer Wins")
        sp.runAndWait()
        
        return "Computer wins!"
def findGestures(lm, img):
    if lm == [0,0,0,0,0]:
        sp.say("Rock")
        sp.runAndWait()
        return "rock"
    elif lm == [1,1,1,1,1]:
        sp.say("Paper")
        sp.runAndWait()
        return "paper"
    elif lm == [0, 1, 1, 0, 0]:
        sp.say("scissor")
        sp.runAndWait()
        return 'scissors'
    else:
        return None
while True:
    status , img = cap.read()
    
    cv2.imshow("myphoto",img)
    user_img, user_lmList = detect_user_gesture(img)
    
    computer_gesture = get_computer_gesture()

    user_gesture = findGestures(user_lmList, img)
    if  user_gesture!=None:
        print(user_gesture, computer_gesture.capitalize())
        winner = get_winner(user_gesture, computer_gesture)
        print(user_img, winner)
        time.sleep(2)
   
    
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
