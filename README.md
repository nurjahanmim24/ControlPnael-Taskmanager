
# 🖥️ Control Panel Task Manager

A Python-based desktop application that emulates a simplified version of the Windows Task Manager. It provides real-time monitoring of system processes, CPU usage, and memory consumption, allowing users to manage and terminate processes efficiently.

## 📁 Project Structure

```

Control\_panel\_Task\_manager/
├── controllers/               # Contains modules for process management
├── myenv/                     # Virtual environment directory
├── get-pip.py                 # Script to install pip
├── main.py                    # Main application script
├── os diagram.drawio          # System architecture diagram
├── requirements.txt           # List of project dependencies
└── setup.py                   # Setup script for packaging

````

## 🛠️ Features

- **Process Monitoring**: View active processes with details like PID, name, CPU, and memory usage.
- **Process Management**: Terminate unresponsive or unwanted processes directly from the interface.
- **Resource Visualization**: Real-time graphs displaying CPU and memory usage.
- **User-Friendly Interface**: Intuitive GUI for easy navigation and control.

## 🧰 Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## 🚀 Installation & Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/0xzahed/Control_panel_Task_manager.git
   cd Control_panel_Task_manager
````

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python main.py
   ```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📚 Other Projects

### Course Management System
**[Live Link](https://your-live-link.com) | [Github](https://github.com/nurjahanmim24/course-management-system)**

A full-stack learning management system for managing courses, assignments, exams, and student enrollments with real-time notifications and cloud storage.

- Multi-role authentication (Admin, Teacher, Student), profile management, and protected routes
- Course creation, assignment & exam management, automatic grading, and file submissions
- Google Drive integration, email notifications, and student progress tracking
- Responsive UI with Tailwind CSS, toast notifications, and interactive dashboards

**Technologies Used:** Laravel, PHP, Tailwind CSS, JavaScript, SQLite, Google Drive API, TinyMCE

---
