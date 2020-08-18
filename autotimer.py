import win32gui
import time

active_window_name = ""

while True:
    new_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    
    if active_window_name != new_window_name:
        active_window_name = new_window_name
        appName = active_window_name.split()
        print(appName[-1]) #4 for Mail bei Browser
        #print(active_window_name)
        if appName[-1] == 'Firefox':
            tab = appName[-4]
            if tab == 'Gmail':
                print("You are in Gmail")

    
    time.sleep(2)