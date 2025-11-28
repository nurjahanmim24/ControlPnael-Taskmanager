import tkinter as tk
import alsaaudio
import subprocess
import os

class SoundFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.mixer = alsaaudio.Mixer()
        self.create_widgets()
        self.is_night_light = False  # Track if night light is active
        self.is_dark_theme = False  # Track if dark theme is active

    def create_widgets(self):
        # Set a soft sky blue background for the entire frame
        self.configure(bg="#E1F5FE")  # Soft Sky Blue background

        # Volume Control Section
        volume_label = tk.Label(self, text="Volume:", font=("Arial", 14, "bold"), bg="#E1F5FE", fg="#1E3A8A")  # Dark blue text
        volume_label.pack(pady=10)

        self.volume_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, 
                                      bg="#ECEFF1", fg="black", troughcolor="#B0BEC5", sliderlength=25, width=25)
        self.volume_slider.set(self.mixer.getvolume()[0])  # Set the initial volume
        self.volume_slider.pack(pady=15)

        # Brightness Control Section
        brightness_label = tk.Label(self, text="Brightness:", font=("Arial", 14, "bold"), bg="#E1F5FE", fg="#1E3A8A")  # Dark blue text
        brightness_label.pack(pady=10)

        self.brightness_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_brightness, 
                                          bg="#ECEFF1", fg="black", troughcolor="#B0BEC5", sliderlength=25, width=25)
        self.brightness_slider.set(self.get_brightness())  # Set initial brightness value
        self.brightness_slider.pack(pady=15)

        # Power Mode Button
        self.power_mode_button = tk.Button(self, text="Toggle Power Mode", command=self.toggle_power_mode, font=("Arial", 12, "bold"), relief="solid")
        self.apply_gradient(self.power_mode_button, '#B2DFDB', '#81D4FA')  # Gradient from paste to sky blue
        self.power_mode_button.pack(pady=20)

        # Night Light Button
        self.night_light_button = tk.Button(self, text="Toggle Night Light", command=self.toggle_night_light, font=("Arial", 12, "bold"), relief="solid")
        self.apply_gradient(self.night_light_button, '#B2DFDB', '#81D4FA')  # Gradient from paste to sky blue
        self.night_light_button.pack(pady=20)

        # Dark/Light Theme Toggle Button
        self.theme_button = tk.Button(self, text="Toggle Dark/Light Theme", command=self.toggle_theme, font=("Arial", 12, "bold"), relief="solid")
        self.apply_gradient(self.theme_button, '#B2DFDB', '#81D4FA')  # Gradient from paste to sky blue
        self.theme_button.pack(pady=20)

        # Reset to Default Button
        reset_button = tk.Button(self, text="Reset to Default", command=self.reset_defaults, font=("Arial", 12, "bold"), relief="solid")
        self.apply_gradient(reset_button, '#B2DFDB', '#81D4FA')  # Gradient from paste to sky blue
        reset_button.pack(pady=20)

    def apply_gradient(self, button, color1, color2):
        """ Function to apply gradient to buttons """
        button.config(bg=color1, fg="white")
        button.bind("<Enter>", lambda e: button.config(bg=color2))  # Change color on hover
        button.bind("<Leave>", lambda e: button.config(bg=color1))  # Revert color on leave

    def set_volume(self, vol):
        """ Set the system volume using alsaaudio """
        self.mixer.setvolume(int(vol))

    def set_brightness(self, brightness):
        """ Set the system brightness in real-time using xrandr """
        brightness = int(brightness) / 100  # Convert the slider value (0-100) to a float value (0-1)
        display_name = self.get_display_name()  # Get the display name dynamically
        if display_name:
            try:
                subprocess.run(f"xrandr --output {display_name} --brightness {brightness}", shell=True, check=True)
                print(f"Setting brightness to {brightness * 100}% for display {display_name}")  # Debug message
            except subprocess.CalledProcessError as e:
                print(f"Failed to set brightness: {e}")
        else:
            print("No display found to adjust brightness.")

    def get_brightness(self):
        """ Get the current brightness level using xrandr (Linux) """
        display_name = self.get_display_name()  # Get the display name dynamically
        try:
            if display_name:
                result = subprocess.run(["xrandr", "--verbose"], capture_output=True, text=True)
                for line in result.stdout.splitlines():
                    if display_name in line and "Brightness" in line:
                        brightness = float(line.split(":")[1].strip()) * 100  # Return as percentage
                        return round(brightness)  # Return brightness as an integer
        except Exception as e:
            print(f"Failed to get brightness: {e}")
        return 50  # Default value if there's an error or no display found

    def get_display_name(self):
        """ Get the name of the primary display output """
        try:
            result = subprocess.run(["xrandr"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if " connected" in line:  # Check for connected displays
                    return line.split()[0]  # Return the first part, which is the display name (e.g., eDP-1, HDMI-1)
        except Exception as e:
            print(f"Failed to get display name: {e}")
        return None  # Return None if no connected displays are found

    def toggle_power_mode(self):
        """ Toggle between power mode and performance mode """
        if self.is_night_light:
            self.set_brightness(30)  # Lower brightness for power-saving mode
        else:
            self.set_brightness(80)  # Higher brightness for performance mode
        print("Power mode toggled")

    def toggle_night_light(self):
        """ Toggle night light mode (reducing blue light by lowering brightness) """
        self.is_night_light = not self.is_night_light
        if self.is_night_light:
            self.set_brightness(40)  # Set low brightness for night mode
            print("Night Light Mode Activated")
        else:
            self.set_brightness(self.brightness_slider.get())  # Reset to current slider value
            print("Night Light Mode Deactivated")

    def toggle_theme(self):
        """ Toggle between dark and light theme for the GUI """
        self.is_dark_theme = not self.is_dark_theme
        if self.is_dark_theme:
            self.configure(bg="#303030")  # Dark background
            self.volume_slider.configure(bg="#424242", fg="white", troughcolor="#B0BEC5")
            self.brightness_slider.configure(bg="#424242", fg="white", troughcolor="#B0BEC5")
        else:
            self.configure(bg="#E1F5FE")  # Light background
            self.volume_slider.configure(bg="#ECEFF1", fg="black", troughcolor="#B0BEC5")
            self.brightness_slider.configure(bg="#ECEFF1", fg="black", troughcolor="#B0BEC5")
        print("Theme toggled")

    def reset_defaults(self):
        """ Reset the volume and brightness to default values """
        self.volume_slider.set(50)
        self.brightness_slider.set(50)
        self.set_volume(50)  # Set volume to 50
        self.set_brightness(50)  # Set brightness to 50

# Example to test the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SoundFrame(root)
    app.pack(padx=20, pady=20)
    root.mainloop()
