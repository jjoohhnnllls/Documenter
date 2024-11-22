import cv2
import numpy as np
import pyautogui as pyag
import mss
import os
import time



def start_recording():
    ##take screenshots or frames
    #screenshot= pyag.screenshot()
    ##save screenshot to captures folder
    #save_path = os.path.join("captures", "screenshot.png")
    #screenshot.save(save_path)
    ##loop continuos screenshot until user stop says stop


    # Create or ensure 'captures' folder exists
    if not os.path.exists("captures"):
        os.makedirs("captures")

    try:
        count = 1
        #select display
        with mss.mss() as sct:
            #list available displays
            monitors = sct.monitors
            print("Available Displays: ")
            for i,monitor in enumerate(monitors):
                print(f"{i}: Monitor {i}. {monitor}")


            #select which monitor to use
            selected_monitor_input = input("\nEnter number of displays")
            






        while True:
            #take screenshots or frames
            screenshot = pyag.screenshot()
            #save screenshot to captures folder
            save_path = os.path.join("captures", f"SS_{count}.png")
            screenshot.save(save_path)

            print(f"Screenshot {count} taken and saved to folder")
            count += 1 

            #wait for 1 second (time interval )
            time.sleep(1)
         
    except KeyboardInterrupt:
        print("\nscreenshot capture stopped by user.")

    

def end_recording():
    ...

def extract_frames():
    ...


start_recording()