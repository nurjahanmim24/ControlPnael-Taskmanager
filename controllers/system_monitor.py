import tkinter as tk
from tkinter import ttk
import psutil

class TaskManagerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#E0F7FA")  # Light Sky Blue background
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        # Header for the Task Manager
        header = tk.Label(self, text="Task Manager", font=("Arial", 24, "bold"), fg="#01579B", bg="#E0F7FA")
        header.pack(pady=20)

        # Frame for System Information (CPU, Memory, Disk)
        sys_info_frame = tk.Frame(self, bg="#E0F7FA")
        sys_info_frame.pack(padx=20, pady=10, fill="x")

        # CPU Usage
        self.cpu_label = tk.Label(sys_info_frame, text="CPU Usage: ", font=("Arial", 14), fg="#01579B", bg="#E0F7FA")
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.cpu_progress = ttk.Progressbar(sys_info_frame, orient="horizontal", length=250, mode="determinate", maximum=100)
        self.cpu_progress.grid(row=0, column=1, padx=10, pady=10)

        # Memory Usage
        self.memory_label = tk.Label(sys_info_frame, text="Memory Usage: ", font=("Arial", 14), fg="#388E3C", bg="#E0F7FA")
        self.memory_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.memory_progress = ttk.Progressbar(sys_info_frame, orient="horizontal", length=250, mode="determinate", maximum=100)
        self.memory_progress.grid(row=1, column=1, padx=10, pady=10)

        # Disk Usage
        self.disk_label = tk.Label(sys_info_frame, text="Disk Usage: ", font=("Arial", 14), fg="#388E3C", bg="#E0F7FA")
        self.disk_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.disk_progress = ttk.Progressbar(sys_info_frame, orient="horizontal", length=250, mode="determinate", maximum=100)
        self.disk_progress.grid(row=2, column=1, padx=10, pady=10)

        # Network Usage
        self.network_label = tk.Label(sys_info_frame, text="Network Usage: ", font=("Arial", 14), fg="#01579B", bg="#E0F7FA")
        self.network_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.network_usage_label = tk.Label(sys_info_frame, text="Waiting...", font=("Arial", 12), fg="#01579B", bg="#E0F7FA")
        self.network_usage_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Frame for Process List
        process_frame = tk.Frame(self, bg="#E0F7FA")
        process_frame.pack(padx=20, pady=10, fill="x")

        # Process List - Treeview (PID, Application Name, Status)
        self.process_tree = ttk.Treeview(process_frame, columns=("PID", "Application Name", "Status"), show="headings", height=10)
        self.process_tree.heading("PID", text="PID")
        self.process_tree.heading("Application Name", text="Application Name")
        self.process_tree.heading("Status", text="Status")
        self.process_tree.pack(padx=10, pady=10)

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(process_frame, orient="vertical", command=self.process_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.process_tree.configure(yscrollcommand=scrollbar.set)

        # Refresh Button
        refresh_button = tk.Button(self, text="Refresh", command=self.update_status, font=("Arial", 12, "bold"), bg="#388E3C", fg="white", relief="solid")
        refresh_button.pack(pady=20)

    def update_status(self):
        # Get and update CPU usage
        cpu_usage = psutil.cpu_percent()
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.cpu_progress['value'] = cpu_usage

        # Get and update Memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
        self.memory_progress['value'] = memory_usage

        # Get and update Disk usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        self.disk_label.config(text=f"Disk Usage: {disk_usage}%")
        self.disk_progress['value'] = disk_usage

        # Get and update Network usage
        net_io = psutil.net_io_counters()
        network_usage = f"Sent: {net_io.bytes_sent / (1024 * 1024):.2f} MB | Recv: {net_io.bytes_recv / (1024 * 1024):.2f} MB"
        self.network_usage_label.config(text=f"Network Usage: {network_usage}")

        # Update Process List
        self.update_process_list()

        # Update the status every second
        self.after(1000, self.update_status)

    def update_process_list(self):
        # Clear the existing process list
        for row in self.process_tree.get_children():
            self.process_tree.delete(row)

        # Get the list of processes
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                # Attempt to get the application name (the executable name)
                app_name = proc.info['name']
                if hasattr(proc, 'exe') and proc.exe():
                    app_name = proc.exe()  # Get the full executable path
                self.process_tree.insert("", "end", values=(proc.info['pid'], app_name, proc.info['status']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

# Example to test the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerFrame(root)
    app.pack(padx=20, pady=20)
    root.mainloop()
