# ATTENDANCE_SYSTEM
**🧠 Face Recognition Attendance System
**
This project uses Python, OpenCV, and face_recognition to automatically mark attendance by detecting and recognizing faces through a webcam. It saves recognized names and timestamps in a CSV file.
**
📸 Features**

✅ Detects and recognizes faces in real time
✅ Marks attendance automatically in attendance.csv
✅ Prevents duplicate attendance entries
✅ Easy to customize and extend
✅ Lightweight and fast using face_recognition library (built on dlib)

**🧩 Technologies Used**

Python 3.8+
OpenCV (cv2)
NumPy
face_recognition
datetime
os

**🗂️ Project Structure**
Face-Recognition-Attendance/
│
├── image attendance/           # Folder containing known face images
│   ├── Prem.jpg
│   ├── Rahul.jpg
│   └── ...
│
├── attendance.csv              # File where attendance will be stored (auto-created)
│
├── main.py                     # Main Python script (your provided code)
│
└── README.md                   # Project documentation (this file)

**⚙️ Setup Instructions**

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/Face-Recognition-Attendance.git
cd Face-Recognition-Attendance

2️⃣ Install Dependencies

Make sure you have Python installed. Then run:
pip install numpy opencv-python face_recognition
Note: Installing face_recognition may require dlib. On Windows, install precompiled wheels if needed.

3️⃣ Add Training Images

Create a folder named image attendance (already present in the repo).
Add images of people you want to recognize.
Rename each image with the person’s name (e.g., Prem.jpg).

4️⃣ Run the Script
python main.py

5️⃣ How It Works
The webcam opens and scans faces.
If a face matches one from the image attendance folder, it:
Displays a rectangle and name.
Saves the name and current time in attendance.csv.

**📄 Output Example**

attendance.csv

Name,Time
PREM,10:15:22
RAHUL,10:20:41

**🧠 Code Explanation**
🔹 findEncodings(images)

Encodes all faces in the known image folder and returns a list of face encodings.

🔹 markAttendance(name)

Writes the recognized person’s name and timestamp to attendance.csv if not already recorded.

🔹 Main Loop

Captures webcam feed.

Detects and encodes faces.

Compares with known encodings.

Displays the recognized name and marks attendance.

🚀 Future Improvements

Add GUI for user-friendly interaction

Integrate with database instead of CSV

Add multiple camera support

Improve recognition under low light
**🪪 License**
This project is licensed under the MIT License — feel free to use and modify it for educational purposes.
