import tkinter as tk
import psutil
import os

class BatteryFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Set a pastel background color for the entire frame
        self.configure(bg="#E0F7FA")  # Light Sky Blue background

        # Label for Battery Status with customized color
        self.status_label = tk.Label(self, text="Fetching battery status...", font=("Arial", 14), bg="#E0F7FA", fg="#01579B")  # Blue text, SkyBlue background
        self.status_label.pack(pady=20)

        # Shutdown Button with customized color
        shutdown_button = tk.Button(self, text="Shutdown", command=self.shutdown, font=("Arial", 12, "bold"), bg="#D32F2F", fg="white", relief="solid")
        shutdown_button.pack(pady=10)

        # Restart Button with customized color
        restart_button = tk.Button(self, text="Restart", command=self.restart, font=("Arial", 12, "bold"), bg="#388E3C", fg="white", relief="solid")
        restart_button.pack(pady=10)

        # Call the update_battery_info function every 1000ms (1 second)
        self.update_battery_info()

    def update_battery_info(self):
        # Retrieve battery information using psutil
        battery = psutil.sensors_battery()

        # Debug: Check battery info
        print("Battery Info:", battery)

        if battery:
            # Convert the battery percentage to an integer
            percent = int(battery.percent)
            charging = battery.power_plugged
            status_text = f"Battery Percentage: {percent}%"
            
            if charging:
                status_text += " (Charging)"
                self.status_label.config(fg="#388E3C")  # Green text for charging
            else:
                status_text += " (Not Charging)"
                self.status_label.config(fg="#B71C1C")  # Red text for not charging
                
            self.status_label.config(text=status_text)
        else:
            self.status_label.config(text="Battery information not available.", fg="#757575")  # Gray text if no info available

        # Refresh the battery status every 1 second (1000ms)
        self.after(1000, self.update_battery_info)

    def shutdown(self):
        # Shutdown the system
        os.system("shutdown now")

    def restart(self):
        # Restart the system
        os.system("reboot")

# Example to test the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BatteryFrame(root)
    app.pack(padx=20, pady=20)
    root.mainloop()
