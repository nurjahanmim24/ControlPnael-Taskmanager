import tkinter as tk
import os
from tkinter import ttk

class SystemSecurityFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.update_firewall_status()
        self.update_ssh_status()

    def create_widgets(self):
        self.configure(bg="#E0F7FA")

        # Title Label
        title_label = tk.Label(self, text="System & Security", font=("Arial", 18, "bold"), fg="black", bg="#E0F7FA")
        title_label.pack(pady=20)

        # Firewall Status Label
        self.firewall_label = tk.Label(self, text="Firewall Status: Checking...", font=("Arial", 12), fg="black", bg="#E0F7FA")
        self.firewall_label.pack(pady=10)

        # SSH Toggle Button
        self.ssh_button = tk.Button(self, text="Checking SSH...", command=self.toggle_ssh, font=("Arial", 12, "bold"), bg="#388E3C", fg="white", relief="solid")
        self.ssh_button.pack(pady=5)

        # Antivirus Status Label
        self.antivirus_label = tk.Label(self, text="Antivirus Status: Checking...", font=("Arial", 12), fg="black", bg="#E0F7FA")
        self.antivirus_label.pack(pady=10)

        # Security Log Button
        self.security_log_button = tk.Button(self, text="View Security Logs", command=self.view_security_logs, font=("Arial", 12, "bold"), bg="#D32F2F", fg="white", relief="solid")
        self.security_log_button.pack(pady=10)

    def update_firewall_status(self):
        """ Updates the firewall status dynamically every few seconds. """
        status = self.get_firewall_status()
        self.firewall_label.config(text=f"Firewall Status: {status}")
        # Update the status every 5000 milliseconds (5 seconds)
        self.after(5000, self.update_firewall_status)

    def get_firewall_status(self):
        """ Checks the status of the firewall (assuming UFW is installed). """
        try:
            # Use sudo to check firewall status and ensure it's captured correctly
            result = os.popen('sudo ufw status | grep "Status:"').read()
            print("Firewall check output:", result)  # Debugging line to check the result

            if "Status: active" in result:
                return "Active"
            else:
                return "Inactive"
        except Exception as e:
            return f"Error: {str(e)}"

    def update_ssh_status(self):
        """ Updates the SSH status dynamically. """
        if os.system("systemctl is-active --quiet ssh") == 0:
            self.ssh_button.config(text="Disable SSH", bg="#D32F2F")  # Red for disabling
        else:
            self.ssh_button.config(text="Enable SSH", bg="#388E3C")  # Green for enabling

    def toggle_ssh(self):
        """ Toggles the SSH service status and updates the button. """
        if os.system("systemctl is-active --quiet ssh") == 0:
            # Disable SSH
            os.system("sudo systemctl stop ssh")
            os.system("sudo systemctl disable ssh")
        else:
            # Enable SSH
            os.system("sudo systemctl enable ssh")
            os.system("sudo systemctl start ssh")
        # Update the SSH status after toggling
        self.update_ssh_status()

    def view_security_logs(self):
        """ Displays the security logs in a new window. """
        log_window = tk.Toplevel(self)
        log_window.title("Security Logs")
        log_window.geometry("600x400")

        # Read logs from auth.log (or similar)
        try:
            with open('/var/log/auth.log', 'r') as f:
                logs = f.readlines()
            log_text = "\n".join(logs[-100:])  # Display last 100 lines
        except Exception as e:
            log_text = f"Error: {str(e)}"
        
        log_label = tk.Label(log_window, text=log_text, font=("Courier", 10), anchor="w", justify="left")
        log_label.pack(padx=10, pady=10, expand=True, fill="both")

class PyOSManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Manager")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        self.current_frame = None
        self.create_widgets()

    def create_widgets(self):
        # Title Label for the Control Panel
        title_label = tk.Label(self.root, text="Control Panel", font=("Arial", 24, "bold"), bg="#388E3C", fg="white")
        title_label.pack(pady=20)

        # Navigation Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(side="top", fill="x", pady=10)

        button_style = ttk.Style()
        button_style.configure("TButton", font=("Arial", 12), padding=6, relief="solid", width=15)
        button_style.map("TButton", background=[("active", "#1B5E20")])

        network_button = ttk.Button(button_frame, text="Network Settings", command=self.show_network_frame, style="TButton")
        network_button.grid(row=0, column=0, padx=5)

        sound_button = ttk.Button(button_frame, text="Sound Settings", command=self.show_sound_frame, style="TButton")
        sound_button.grid(row=0, column=1, padx=5)

        battery_button = ttk.Button(button_frame, text="Battery Status", command=self.show_battery_frame, style="TButton")
        battery_button.grid(row=0, column=2, padx=5)

        task_manager_button = ttk.Button(button_frame, text="Task Manager", command=self.show_task_manager_frame, style="TButton")
        task_manager_button.grid(row=0, column=3, padx=5)

        system_details_button = ttk.Button(button_frame, text="System Details", command=self.show_system_details_frame, style="TButton")
        system_details_button.grid(row=0, column=4, padx=5)

        system_security_button = ttk.Button(button_frame, text="System & Security", command=self.show_system_security_frame, style="TButton")
        system_security_button.grid(row=0, column=5, padx=5)

        # Content Frames
        self.network_frame = tk.Frame(self.root)
        self.sound_frame = tk.Frame(self.root)
        self.battery_frame = tk.Frame(self.root)
        self.task_manager_frame = tk.Frame(self.root)
        self.system_details_frame = tk.Frame(self.root)
        self.system_security_frame = SystemSecurityFrame(self.root)

        # Show the initial frame (e.g., Network Frame)
        self.show_network_frame()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(expand=True, fill="both")

    def show_network_frame(self):
        self.show_frame(self.network_frame)

    def show_sound_frame(self):
        self.show_frame(self.sound_frame)

    def show_battery_frame(self):
        self.show_frame(self.battery_frame)

    def show_task_manager_frame(self):
        self.show_frame(self.task_manager_frame)

    def show_system_details_frame(self):
        self.show_frame(self.system_details_frame)

    def show_system_security_frame(self):
        self.show_frame(self.system_security_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = PyOSManagerApp(root)
    root.mainloop()
