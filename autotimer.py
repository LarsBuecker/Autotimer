import win32gui
import time

active_window_name = ""

while True:
    new_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    
    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
    
    time.sleep(2)