from datetime import datetime
import csv
import os
import face_recognition
import cv2

# Create attendance file
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Time"])

marked_attendance = set()

# Attendance function
def mark_attendance(name):
    if name != "Unknown" and name not in marked_attendance:
        now = datetime.now().strftime("%H:%M:%S")

        with open(attendance_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, now])

        marked_attendance.add(name)
        print(f"{name} marked present at {now}")

# Load known image
known_image = face_recognition.load_image_file(
    "known_faces/pooja.jpeg"
)

known_encoding = face_recognition.face_encodings(
    known_image
)[0]

known_faces = [known_encoding]
known_names = ["Pooja"]

# Start webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)

    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_faces,
            face_encoding
        )

        name = "Unknown"

        if True in matches:
            name = known_names[matches.index(True)]
            mark_attendance(name)

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Recognition Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()