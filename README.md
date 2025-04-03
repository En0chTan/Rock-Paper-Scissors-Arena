# Introduction 

Rock-Paper-Scissors AI Game is a computer vision-based game that allows players to play Rock-Paper-Scissors using hand gestures. The game has two modes:

<ol>
  <li> Single Mode - Play against an AI opponent. </li>
  <li> Versus Mode - Two players can compete using hand detection. </li>
</ol>

This project utilizes OpenCV, cvzone, and HandTrackingModule to detect hand gestures and determine the winner.


## Features
<ul>
  <li> Hand Gesture Recognition using OpenCV & Mediapipe </li>
  <li> AI Opponent for Single Mode </li>
  <li> Two-Player Versus Mode using dual hand detection </li>
  <li> Real-time Video Processing with OpenCV </li>
  <li> Score Tracking System </li>
</ul>



## Installation & Setup
To run this project, install the required dependencies:

```bash
pip install opencv-python cvzone mediapipe
```

  Ensure your system has Python 3.8+ installed.



## How to Play

1. Run the game:
```bash
python rps.py
```

2. On the Home Screen, press:
<ul>
  <li> 'S' key for Single Mode </li>
  <li> 'V' key for Versus Mode</li>
  <li> 'Q' key to Quit </li>
</ul>

3. In-game controls:
<ul>
  <li> 'S' to Start the game </li>
  <li> 'R' to Return to the Home Screen </li>
  <li> 'Q' to Quit </li>
</ul>



## Hand Gestures
To install the required dependencies, run the following command:
Gesture

| Gesture | Move |
|----------|----------|
| ✊ (Fist) | Rock |
| 🖐️ (Open Hand) | Paper |
| ✌️ (Two Fingers) | Scissors |

## Reference Source
[Murtaza's Workshop - Robotics and AI YouTube Channel](https://youtu.be/k2EahPgl0ho?si=jNQq_B5y4yGd7Mvt)
