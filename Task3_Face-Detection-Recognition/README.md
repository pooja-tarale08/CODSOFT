# AI Face Recognition Attendance System

## Overview

This project is a real-time Face Detection and Face Recognition Attendance System developed using Python, OpenCV, and the face_recognition library.

The system detects faces through a webcam, recognizes known individuals, and automatically records attendance in a CSV file.

## Features

* Real-time face detection using webcam
* Face recognition using facial encodings
* Automatic attendance marking
* Attendance storage in CSV format
* Duplicate attendance prevention
* Face labeling with recognized person's name

## Technologies Used

* Python
* OpenCV
* face_recognition
* NumPy
* CSV
* Datetime

## Project Structure

Task3_Face-Detection-Recognition/

├── face_detection.py

├── recognition.py

├── requirements.txt

├── README.md

└── known_faces/

## How to Run

1. Clone the repository

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add images of known people inside the `known_faces` folder.

4. Run the recognition system

```bash
python recognition.py
```

5. Press `q` to quit the application.

## Output

* Detects faces in real time.
* Recognizes registered users.
* Records attendance in a CSV file.
* Displays the person's name above the detected face.

## Future Improvements

* Multiple user recognition
* Date-wise attendance tracking
* GUI-based interface
* Database integration
* Cloud-based attendance management

## Author

Pooja Tarale
