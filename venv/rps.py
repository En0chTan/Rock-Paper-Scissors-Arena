import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

detector = HandDetector(maxHands=1)

while True:  # Allow return to home screen
    timer = 0
    stateResult = False
    startGame = False
    scores = [0, 0]  # [AI, Player]

    # Home Screen
    while True:
        homeScreen = cv2.imread("assets/home_screen.png")  # Create a home_screen.png image
        cv2.putText(homeScreen, "Press 'S' to Single Mode", (250, 400), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5) # Display instructions for Single Player
        cv2.putText(homeScreen, "Press 'V' to Versus Mode", (250, 500), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5) # Display instructions for Versus Player
        cv2.putText(homeScreen, "Press 'Q' to Quit Game", (250, 600), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5) # Display instructions for Quit
        cv2.imshow("RPS Arena Home", homeScreen)

        key = cv2.waitKey(1)
        if key == ord('s'): # Check for 's' key press
            gameMode = "rps_BG1"
            break
        elif key == ord('v'): # Check for 'v' key press
            gameMode = "Versus_Mode"
            break
        elif key == ord('q'): # Check for 'q' key press
            exit()

    cv2.destroyWindow("RPS Arena Home")  # Close the home screen window

    # rps_BG1 Game Loop
    if gameMode == "rps_BG1":
        while True:
            imgBG = cv2.imread("assets/rps_BG1.png") # Load background for Single Mode
            success, img = cap.read()

            imgScaled = cv2.resize(img, (0, 0), None, 0.688, 0.688)
            imgScaled = imgScaled[:, 30:480]

            # Find Hands
            hands, img = detector.findHands(imgScaled)  # with draw

            if startGame:

                if stateResult is False:
                    timer = time.time() - initialTime
                    cv2.putText(imgBG, str(int(timer)), (595, 490), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 10)

                    if timer > 3:
                        stateResult = True
                        timer = 0

                        if hands:
                            playerMove = None
                            hand = hands[0]
                            fingers = detector.fingersUp(hand)
                            print(fingers)
                            if fingers == [0, 0, 0, 0, 0]: # Rock 
                                playerMove = 1
                            if fingers == [1, 1, 1, 1, 1]: # Paper
                                playerMove = 2
                            if fingers == [0, 1, 1, 0, 0]: # Scissors
                                playerMove = 3

                            randomNumber = random.randint(1, 3)
                            imgAI = cv2.imread(f'assets/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                            # Player Scores
                            if (playerMove == 1 and randomNumber == 3) or \
                                    (playerMove == 2 and randomNumber == 1) or \
                                    (playerMove == 3 and randomNumber == 2):
                                scores[1] += 1

                            # AI Scores
                            if (playerMove == 3 and randomNumber == 1) or \
                                    (playerMove == 1 and randomNumber == 2) or \
                                    (playerMove == 2 and randomNumber == 3):
                                scores[0] += 1

            imgBG[341:671, 796:1206] = imgScaled

            if stateResult:
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (80, 310))

            cv2.putText(imgBG, str(int(scores[0])), (330, 320), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 10)
            cv2.putText(imgBG, str(int(scores[1])), (1050, 320), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 10)

            cv2.imshow("rps_BG", imgBG)

            key = cv2.waitKey(1)
            if key == ord('s'): # Check for 's' key press to start game
                startGame = True
                initialTime = time.time()
                stateResult = False
            elif key == ord('q'):  # Add quit functionality
                exit()
            elif key == ord('r'):  # Return to home screen
                break

    # Versus_Mode Game Loop
    elif gameMode == "Versus_Mode":
        detector = HandDetector(maxHands=2)  # Allow detection of two hands
        while True:
            imgBG = cv2.imread("assets/rps_BG2.png")  # Load the background for Versus Mode
            success, img = cap.read()

            # Create imgScaled for both players
            imgScaled = cv2.resize(img, (0, 0), None, 0.688, 0.688)
            imgScaled = imgScaled[:, 30:480]

            # Find Hands
            hands, img = detector.findHands(imgScaled)  # Detect hands

            if startGame:

                if stateResult is False:
                    timer = time.time() - initialTime
                    cv2.putText(imgBG, str(int(timer)), (595, 490), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 10)

                    if timer > 3:
                        stateResult = True
                        timer = 0

                        if hands and len(hands) == 2:  # Ensure two hands are detected
                            player1Move = None
                            player2Move = None

                            # Assign hands based on their x-coordinates
                            if hands[0]['center'][0] < hands[1]['center'][0]:
                                hand1 = hands[0]  # Left-hand player
                                hand2 = hands[1]  # Right-hand player
                            else:
                                hand1 = hands[1]  # Left-hand player
                                hand2 = hands[0]  # Right-hand player

                            # Player 1 (Left-hand player)
                            fingers1 = detector.fingersUp(hand1)
                            print("Player 1:", fingers1)
                            if fingers1 == [0, 0, 0, 0, 0]:
                                player1Move = 1  # Rock
                            if fingers1 == [1, 1, 1, 1, 1]:
                                player1Move = 2  # Paper
                            if fingers1 == [0, 1, 1, 0, 0]:
                                player1Move = 3  # Scissors

                            # Player 2 (Right-hand player)
                            fingers2 = detector.fingersUp(hand2)
                            print("Player 2:", fingers2)
                            if fingers2 == [0, 0, 0, 0, 0]:
                                player2Move = 1  # Rock
                            if fingers2 == [1, 1, 1, 1, 1]:
                                player2Move = 2  # Paper
                            if fingers2 == [0, 1, 1, 0, 0]:
                                player2Move = 3  # Scissors

                            # Determine Winner and Update Scores
                            if player1Move and player2Move:
                                if (player1Move == 1 and player2Move == 3) or \
                                   (player1Move == 2 and player2Move == 1) or \
                                   (player1Move == 3 and player2Move == 2):
                                    scores[1] += 1  # Player 1 wins
                                    print("Player 1 wins!")
                                elif (player2Move == 1 and player1Move == 3) or \
                                     (player2Move == 2 and player1Move == 1) or \
                                     (player2Move == 3 and player1Move == 2):
                                    scores[0] += 1  # Player 2 wins
                                    print("Player 2 wins!")

            # Overlay Player 1's scaled image on the left
            imgBG[341:671, 76:486] = imgScaled

            # Overlay Player 2's scaled image on the right
            imgBG[341:671, 796:1206] = imgScaled

            # Display Scores
            cv2.putText(imgBG, str(int(scores[1])), (1050, 320), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 10)  # Player 1 score
            cv2.putText(imgBG, str(int(scores[0])), (330, 320), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 10)  # Player 2 score

            cv2.imshow("Versus_Mode", imgBG)

            key = cv2.waitKey(1)
            if key == ord('s'):
                startGame = True
                initialTime = time.time()
                stateResult = False
            elif key == ord('q'):  # Add quit functionality
                cv2.destroyAllWindows()  # Close all windows before exiting
                exit()
            elif key == ord('r'):  # Return to home screen
                cv2.destroyAllWindows()  # Close the game window
                break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()