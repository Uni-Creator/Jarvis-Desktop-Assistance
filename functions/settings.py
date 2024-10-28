# importing the required packages
# import pyautogui as pya
# from cv2 import VideoCapture,VideoWriter,VideoWriter_fourcc,namedWindow,resizeWindow,\
#     WINDOW_NORMAL,cvtColor,COLOR_BGR2RGB,waitKey,destroyAllWindows,imshow,imread,imwrite
    
import cv2
# import numpy as np
import time
# import screen_brightness_control as sbc
from winshell import recycle_bin
import ctypes
from ctypes import wintypes
# import subprocess as sp
import os
# import sounddevice as sd
# # from scipy.io.wavfile import write
# import wavio as wv
from threading import Thread
# from win10toast import ToastNotifier
from PIL import ImageGrab

def rawScreenshot():
    im = ImageGrab.grab()
    data = im.load()
    # print(type(data))
    mouse = mousePosition()
    # print(mouse[0],mouse[1])
    mouse = (mouse[0]-10,mouse[1]-10) if mouse[0]<1900 and mouse[1]<1060 else mouse
    for i in range(mouse[0],mouse[0]+10):
        for j in range(mouse[1],mouse[1]+10):
            data[i, j] = 225,225,225
    return im

def mousePosition():
    # cursor = ctypes.wintypes.POINT()
    cursor = wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)

def record_screen(Time=None,fps=30,resolution=(1920, 1080),micph=False):
    import numpy as np

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    dateTime = time.strftime("%Y%m%d_%H_%M_%S")
    # Specify name of Output file
    filename = f"./data/files/Recordings/ScreenRecording_{dateTime}.avi"

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Recording *", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Recording *", 480, 10)
    start = time.perf_counter()
    Time = time.perf_counter() if Time is None else Time 
    # a,end = 0,0
    # while end - start <= Time:
    if micph and Time:
        m = Thread(target=mic,args=[Time,'micRec'])
        m.start()
        # m.join()
    # output = ()
    while time.perf_counter() - start <= Time:

        # Take screenshot using PyAutoGUI
        img = rawScreenshot()
        frame = np.asarray(img)
        # # Convert it from BGR(Blue, Green, Red) to
        # # RGB(Red, Green, Blue)[]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # # Write it to the output file
        out.write(frame)
        
        if cv2.waitKey(1) == ord('q'):
            # end = time.perf_counter()
            break
            
        # del frame
        # a+=1
        # end = time.perf_counter()
    # Destroy all windows
    cv2.destroyAllWindows()

    # Release the Video writer
    out.release()

    # print(a,end-start,a/(end-start))

    print('File saved successfully:',filename)
    return True

def brightness(input):
    import screen_brightness_control as sbc

    currentBrightness = sbc.get_brightness()

    if 'increase' in input:
        func = 'Increased'
        sbc.set_brightness(currentBrightness+5)
    if 'decrease' in input:
        func = 'Decreased'
        sbc.set_brightness(currentBrightness-5)
    if 'max' in input:
        func = 'Maxed'
        sbc.fade_brightness(100)
    if 'min' in input:
        func = 'Minimized'
        sbc.fade_brightness(25)
    if 'fade' in input:
        func = 'Faded'
        sbc.fade_brightness(0, increment=5,start=100)
        sbc.fade_brightness(100, increment = 5)
        sbc.fade_brightness(currentBrightness, increment = 5)

    print("Last brightness: ", currentBrightness)
    print("Current brightness: ", sbc.get_brightness())
    return func + ' to ' + str(sbc.get_brightness())

def volume(volume):
    from pyautogui import press

    if 'up' in volume or 'increase' in volume:
        press('volumeup')
        return "Volume Increased"

    elif 'down' in volume or 'decrease' in volume:
        press('volumedown')
        return 'Volume Decreased'

    elif 'mute' in volume:
        press('volumemute')
        return 'Volume Muted'

    else:
        return "Unable to change volume state"

def mic(duration,filename=None,freq = 50000):

    from sounddevice import rec,wait
    # from scipy.io.wavfile import write
    from wavio import write
    # Recording duration -> duration

    # keyboard = Controller()
    # start  = time.perf_counter()

    # Start recorder with the given values
    # of duration and sample frequency
    recording = rec(int(duration *freq),
                    samplerate=freq, channels=2)

    wait()

    # print(sd.get_stream())
    # sd.stop()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency

    # write("./data/files/Recordings/recording0.wav", freq, recording)

    # Convert the NumPy array to audio file
    dateTime = time.strftime("%Y%m%d_%H_%M_%S")
    path='text.wav'
    # path = f"./data/files/Recordings/recording_{dateTime}.mp3" if filename is None else f"./data/files/Recordings/{filename}.mp3"
    write(path, recording, freq, sampwidth=2)
    return path

def recycled(func='empty'):
    
    if func == 'empty':
        recycle_bin().empty(show_progress=True, sound=True)
        return "Recycle bin emptied."
    
    if func == 'restore':
        restored_files = []
        for item in recycle_bin():
            item.undelete()
            restored_files.append(item.original_filename())
        return restored_files

def power(input):
    from subprocess import call

    if 'shutdown' in input:
        call('shutdown /sg', timeout=20)
    elif 'lock' in input:
        ctypes.windll.user32.LockWorkStation()
    elif 'restart' in input:
        call(["shutdown", "/g"], timeout=20)
    elif 'hibernate' in input:
        call("shutdown /h", timeout=20)
    elif 'log out' in input:
        call(["shutdown", "/l"], timeout=10)

def camera():
    try:
        # os.system("start shell:appsfolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App")
        # os.system("start microsoft.windows.camera:")
        os.startfile('microsoft.windows.camera:')
        return True
    except:
        return

def changeBackground():
    import wallpaper
    wallpaper.run()

def takeScreenshot():
    '''"printscreen",
    "prntscrn",
    "prtsc",
    "prtscr"'''
    from pyautogui import hotkey
    hotkey('win','prtsc')
    return True

# def notification(msg,type='simple',duration=5):
    
    # toast = ToastNotifier()
    # if type is 'simple':
        # icon_path = "data/files/ico/bell.ico"
    # toast.show_toast("Jarvis",msg,duration,icon_path)

# record_screen(10,micph=True)
# mic(5)
# volume('up')
# takeScreenshot()
# rawScreenshot().show()
# changeBackground()
# recycled('restore')