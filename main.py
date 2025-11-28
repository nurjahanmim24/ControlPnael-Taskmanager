import tkinter as tk
from tkinter import ttk
from controllers import network, sound, battery, system_monitor, system_details, SystemSecurity

class PyOSManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Manager")
        self.root.geometry("800x600")
        self.root.configure(bg="#E0F7FA")  

        self.current_frame = None
        self.create_widgets()

    def create_widgets(self):
        # Title Label with color
        title_label = tk.Label(self.root, text="Control Panel", font=("Arial", 24, "bold"), bg="#E0F7FA", fg="black")
        title_label.grid(row=0, column=0, columnspan=6, pady=20, sticky="nsew")

        # Navigation Buttons Frame with background color
        button_frame = ttk.Frame(self.root, padding="10", style="TFrame")
        button_frame.grid(row=1, column=0, columnspan=6, pady=10, sticky="nsew")

        # Button Style (Green and Blue color scheme)
        button_style = ttk.Style()
        button_style.configure("TButton",
                               font=("Arial", 12),
                               padding=6,
                               relief="solid",
                               background="#388E3C",  
                               foreground="white",
                               width=15)
        button_style.map("TButton", background=[("active", "#1B5E20")])  
        # Navigation Buttons with styled color and font
        network_button = ttk.Button(button_frame, text="Network Settings", command=self.show_network_frame, style="TButton")
        network_button.grid(row=0, column=0, padx=5)

        sound_button = ttk.Button(button_frame, text="Management Bar", command=self.show_sound_frame, style="TButton")
        sound_button.grid(row=0, column=1, padx=5)

        battery_button = ttk.Button(button_frame, text="System Settings", command=self.show_battery_frame, style="TButton")
        battery_button.grid(row=0, column=2, padx=5)

        task_manager_button = ttk.Button(button_frame, text="Task Manager", command=self.show_task_manager_frame, style="TButton")
        task_manager_button.grid(row=0, column=3, padx=5)

        system_details_button = ttk.Button(button_frame, text="System Details", command=self.show_system_details_frame, style="TButton")
        system_details_button.grid(row=0, column=4, padx=5)

        system_security_button = ttk.Button(button_frame, text="System & Security", command=self.show_system_security_frame, style="TButton")
        system_security_button.grid(row=0, column=5, padx=5)

        # Content Frames with color customization
        self.network_frame = network.NetworkFrame(self.root)
        self.sound_frame = sound.SoundFrame(self.root)
        self.battery_frame = battery.BatteryFrame(self.root)
        self.task_manager_frame = system_monitor.TaskManagerFrame(self.root)
        self.system_details_frame = system_details.SystemDetailsFrame(self.root)
        self.system_security_frame = SystemSecurity.SystemSecurityFrame(self.root)

        # Configure grid weights to make frames responsive
        self.root.grid_rowconfigure(0, weight=0)  
        self.root.grid_rowconfigure(1, weight=0)  
        self.root.grid_rowconfigure(2, weight=1)  

        self.root.grid_columnconfigure(0, weight=1)  
        self.root.grid_columnconfigure(1, weight=1)  
        self.root.grid_columnconfigure(2, weight=1)  
        self.root.grid_columnconfigure(3, weight=1) 
        self.root.grid_columnconfigure(4, weight=1)  
        self.root.grid_columnconfigure(5, weight=1)  

        # Show the initial frame (Network Frame)
        self.show_network_frame()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.grid_forget()
        self.current_frame = frame
        self.current_frame.grid(row=2, column=0, columnspan=6, sticky="nsew")

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
