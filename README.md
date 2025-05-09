# Student_managment_system

A full-featured **Student Management System** built with Python and Tkinter that allows administrators to manage student data such as personal details, course information, and results efficiently.

---

## 🔧 Features

- **Student Registration**: Add and update student information including personal details and course enrollment.
- **Course Management**: Add and manage courses.
- **Result Management**: Add and view student results.
- **Search Functionality**: Search students by roll number.
- **Responsive Dashboard**: GUI built with Tkinter, providing a user-friendly interface.
- **Database Integration**: SQLite backend to store student and course data persistently.
- **Login/Register System**: User authentication for secure access.

---

## 🗂️ Project Structure

Result_Management_System-main/
├── images/ # Image assets used in GUI
├── course.py # Course management window
├── create_db.py # Script to create the database
├── dashboard.py # Main dashboard after login
├── login.py # Login window
├── register.py # Registration window
├── report.py # Student report generation
├── result.py # Result management
├── student.py # Student information management
├── rms.db # SQLite database file
└── README.md # Project description

---

## 🛠️ Tech Stack

- **Frontend**: Python Tkinter (GUI)
- **Backend**: SQLite (Database)
- **Language**: Python 3.x

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vaibhav725Sharma/Student_managment_system.git
   cd Student_Management_System-main
   ```
2. **Install Required Packages**

- Tkinter comes pre-installed with Python. If not:
  pip install tk

3. **Run the Application**

- python login.py
