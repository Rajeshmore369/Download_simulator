import tkinter as tk
from tkinter import ttk
import time
import threading

def start_download():
    try:
        total_time = int(time_entry.get())
    except ValueError:
        status_label.config(text="Please enter a valid time (in seconds).")
        return
    
    def download():
        progress_bar['value'] = 0
        progress_bar['maximum'] = total_time
        status_label.config(text="Downloading...")
        for i in range(total_time + 1):
            time.sleep(1)
            progress_bar['value'] = i
            percent = int((i / total_time) * 100)
            progress_label.config(text=f"{percent}%")
            window.update_idletasks()
        status_label.config(text="Download Completed!")

    threading.Thread(target=download).start()

# Create main window
window = tk.Tk()
window.title("Download Progress")
window.geometry("400x250")
window.resizable(False, False)

# Title label
title_label = tk.Label(window, text="Download", font=("Arial", 16))
title_label.pack(pady=10)

# Time entry
time_label = tk.Label(window, text="Set  Time (in seconds):")
time_label.pack(pady=5)
time_entry = tk.Entry(window, width=10)
time_entry.pack()

# Progress bar
progress_bar = ttk.Progressbar(window, length=300)
progress_bar.pack(pady=20)

# Progress labels
progress_label = tk.Label(window, text="0%")
progress_label.pack()

# Status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start button
start_button = tk.Button(window, text="Start Download", command=start_download)
start_button.pack(pady=10)

# Run the window
window.mainloop()
