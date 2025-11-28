import tkinter as tk
from tkinter import ttk
import subprocess
import psutil

class NetworkFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Create tabs for different types of network settings
        tab_control = ttk.Notebook(self)  # Use ttk.Notebook instead of tk.Notebook
        tab_control.pack(fill="both", expand=True)

        # WiFi Settings Tab
        self.wifi_frame = tk.Frame(tab_control, bg="#E1F5FE")  # Light SkyBlue background
        tab_control.add(self.wifi_frame, text="WiFi")
        self.create_wifi_widgets()

        # Ethernet Settings Tab
        self.ethernet_frame = tk.Frame(tab_control, bg="#C8E6C9")  # Light Pastel Green
        tab_control.add(self.ethernet_frame, text="Ethernet")
        self.create_ethernet_widgets()

        # Dial-Up Settings Tab
        self.dialup_frame = tk.Frame(tab_control, bg="#E8EAF6")  # Light Blue background
        tab_control.add(self.dialup_frame, text="Dial-Up")
        self.create_dialup_widgets()

    def create_wifi_widgets(self):
        # Style for WiFi Section
        label_style = {'font': ("Arial", 12), 'bg': "#E1F5FE", 'fg': "#01579B"}  # Blue text, SkyBlue background
        button_style = {'font': ("Arial", 12, "bold"), 'bg': "#388E3C", 'fg': "white", 'relief': "solid"}

        # WiFi Widgets
        ssid_label = tk.Label(self.wifi_frame, text="SSID:", **label_style)
        ssid_label.pack(pady=5)
        self.ssid_entry = tk.Entry(self.wifi_frame, font=("Arial", 12))
        self.ssid_entry.pack(pady=5)

        password_label = tk.Label(self.wifi_frame, text="Password:", **label_style)
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.wifi_frame, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        connect_button = tk.Button(self.wifi_frame, text="Connect WiFi", command=self.connect_wifi, **button_style)
        connect_button.pack(pady=10)

        disconnect_button = tk.Button(self.wifi_frame, text="Disconnect WiFi", command=self.disconnect_wifi, **button_style)
        disconnect_button.pack(pady=10)

    def create_ethernet_widgets(self):
        # Style for Ethernet Section
        label_style = {'font': ("Arial", 12), 'bg': "#C8E6C9", 'fg': "#2E7D32"}  # Green text, Pastel Green background
        button_style = {'font': ("Arial", 12, "bold"), 'bg': "#388E3C", 'fg': "white", 'relief': "solid"}

        # Ethernet Widgets
        ethernet_status_label = tk.Label(self.ethernet_frame, text="Ethernet Connection Status:", **label_style)
        ethernet_status_label.pack(pady=5)

        self.ethernet_status = tk.Label(self.ethernet_frame, text="Checking...", font=("Arial", 12), bg="#C8E6C9", fg="#388E3C")
        self.ethernet_status.pack(pady=5)
        self.update_ethernet_status()

        enable_button = tk.Button(self.ethernet_frame, text="Enable Ethernet", command=self.enable_ethernet, **button_style)
        enable_button.pack(pady=5)

        disable_button = tk.Button(self.ethernet_frame, text="Disable Ethernet", command=self.disable_ethernet, **button_style)
        disable_button.pack(pady=5)

    def create_dialup_widgets(self):
        # Style for Dial-Up Section
        label_style = {'font': ("Arial", 12), 'bg': "#E8EAF6", 'fg': "#1A237E"}  # Dark Blue text, Light Blue background
        button_style = {'font': ("Arial", 12, "bold"), 'bg': "#388E3C", 'fg': "white", 'relief': "solid"}

        # Dial-Up Widgets
        username_label = tk.Label(self.dialup_frame, text="Username:", **label_style)
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.dialup_frame, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.dialup_frame, text="Password:", **label_style)
        password_label.pack(pady=5)
        self.dialup_password_entry = tk.Entry(self.dialup_frame, show="*", font=("Arial", 12))
        self.dialup_password_entry.pack(pady=5)

        connect_button = tk.Button(self.dialup_frame, text="Connect Dial-Up", command=self.connect_dialup, **button_style)
        connect_button.pack(pady=10)

        disconnect_button = tk.Button(self.dialup_frame, text="Disconnect Dial-Up", command=self.disconnect_dialup, **button_style)
        disconnect_button.pack(pady=10)

    # WiFi Methods
    def connect_wifi(self):
        ssid = self.ssid_entry.get()
        password = self.password_entry.get()
        command = f"nmcli dev wifi connect '{ssid}' password '{password}'"
        subprocess.run(command, shell=True)

    def disconnect_wifi(self):
        command = "nmcli dev disconnect wlan0"
        subprocess.run(command, shell=True)

    # Ethernet Methods
    def update_ethernet_status(self):
        ethernet_connected = False
        for iface, addrs in psutil.net_if_addrs().items():
            if iface.startswith("en") or iface.startswith("eth"):
                ethernet_connected = True
                break

        if ethernet_connected:
            self.ethernet_status.config(text="Connected")
        else:
            self.ethernet_status.config(text="Disconnected")

        self.after(5000, self.update_ethernet_status)  # Update every 5 seconds

    def enable_ethernet(self):
        command = "nmcli dev set eth0 managed yes"
        subprocess.run(command, shell=True)

    def disable_ethernet(self):
        command = "nmcli dev disconnect eth0"
        subprocess.run(command, shell=True)

    # Dial-Up Methods
    def connect_dialup(self):
        phone = self.phone_entry.get()
        username = self.username_entry.get()
        password = self.dialup_password_entry.get()
        command = f"wvdial --phone {phone} --username {username} --password {password}"
        subprocess.run(command, shell=True)

    def disconnect_dialup(self):
        command = "pkill pppd"
        subprocess.run(command, shell=True)
