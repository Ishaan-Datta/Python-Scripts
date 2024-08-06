import tkinter as tk
from win10toast import ToastNotifier
import psutil
import ctypes
import os
import threading
import time


class HeadphoneBatteryWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Headphone Battery Widget")
        self.root.geometry("300x100")

        self.label = tk.Label(root, text="Battery Level: N/A", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.check_battery_thread = threading.Thread(
            target=self.check_battery_status, daemon=True
        )
        self.check_battery_thread.start()

    def check_battery_status(self):
        while True:
            battery_level = self.get_headphone_battery_level()
            if battery_level is not None:
                self.update_label(battery_level)
            time.sleep(60)  # Check every 1 minute

    def get_headphone_battery_level(self):
        # Replace 'Your Bluetooth Device Name' with the name of your Bluetooth headphones
        device_name = "Your Bluetooth Device Name"

        try:
            result = os.popen("powercfg /batteryreport").read()
            battery_report_path = result.split("Battery life report saved to file: ")[
                1
            ].strip()

            with open(battery_report_path, "r") as file:
                report_content = file.read()

            start_index = report_content.find(device_name)
            if start_index != -1:
                battery_info = report_content[start_index : start_index + 200]
                battery_level_index = battery_info.find("Battery Level")
                battery_level = battery_info[
                    battery_level_index + 14 : battery_level_index + 16
                ]
                return int(battery_level)
        except Exception as e:
            print(f"Error getting battery level: {e}")
        return None

    def update_label(self, battery_level):
        self.label.config(text=f"Battery Level: {battery_level}%")
        if battery_level < 20:
            self.show_low_battery_notification()

    def show_low_battery_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast(
            "Low Battery Warning",
            "Headphone battery is low. Charge your headphones!",
            duration=10,
        )


def is_windows_11():
    try:
        os_version = os.system("ver")
        return os_version.startswith(
            "Version 10.0.22000"
        )  # Check if running Windows 11
    except Exception:
        return False


if __name__ == "__main__":
    if is_windows_11():
        root = tk.Tk()
        app = HeadphoneBatteryWidget(root)
        root.mainloop()
    else:
        ctypes.windll.user32.MessageBoxW(
            0, "This script is intended for Windows 11 only.", "Unsupported OS", 1
        )
