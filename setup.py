import os
import subprocess

# Define project structure
PROJECT_DIR = "pyOS_Manager"
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
CONTROLLERS_DIR = os.path.join(PROJECT_DIR, "controllers")

# List of files to create
FILES = {
    "main.py": PROJECT_DIR,
    "assets/network.png": ASSETS_DIR,
    "assets/volume.png": ASSETS_DIR,
    "assets/shutdown.png": ASSETS_DIR,
    "controllers/network.py": CONTROLLERS_DIR,
    "controllers/sound.py": CONTROLLERS_DIR,
    "controllers/battery.py": CONTROLLERS_DIR,
    "controllers/system_monitor.py": CONTROLLERS_DIR,
}

# Create directories and files
for directory in [PROJECT_DIR, ASSETS_DIR, CONTROLLERS_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

for file_path, directory in FILES.items():
    full_path = os.path.join(directory, os.path.basename(file_path))
    if not os.path.exists(full_path):
        with open(full_path, 'w') as f:
            pass  # Create an empty file
        print(f"Created file: {full_path}")

# Create a virtual environment for the project
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
if not os.path.exists(VENV_DIR):
    subprocess.run(["python3", "-m", "venv", VENV_DIR])
    print(f"Virtual environment created at: {VENV_DIR}")

# Generate README file for documentation purposes
README_PATH = os.path.join(PROJECT_DIR, "README.md")
if not os.path.exists(README_PATH):
    with open(README_PATH, 'w') as readme:
        readme.write("# pyOS_Manager\n\n")
        readme.write("A control panel and task manager-like GUI for managing network, sound, battery, and system status, built in Python.\n")
        print(f"Created file: {README_PATH}")

print("Project setup complete.")
