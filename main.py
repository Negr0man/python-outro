import base64, time, wave, random, pyaudio, keyboard, os, threading
from tokenize import Ignore
i = 10
p = pyaudio.PyAudio()  
launch_code = random.randint(100000, 999999)

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def BSOD():
    os.system('cls')
    os.system('color 1F')
    print('A problem has been detected and Windows has been shut down to prevent damage to your computer.')
    print("\nIf this is the first time you've seen this stop error screen, restart your computer. if this screen appears again, follow these steps:")
    print('\nCheck to make sure any new hardware or software is properly installed. I this is a new installation, ask your hardware or software manufacturer for and Windows updates you might need')
    print('\nIf problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.')
    print('\nTechnical information:')
    print('\nSTOP: 0x000000FE (0x00000008, 0x000000006, 0x00000009, 0x847075cc)')

def terminateSong():
    stream.stop_stream()  
    stream.close()  
    p.terminate() 

def playSong():
    try:
        data = f.readframes(chunk)
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)
        stream.stop_stream()  
        stream.close()  
        p.terminate()
    except Exception:
        try:
            stream.stop_stream()  
            stream.close()  
            p.terminate()
        except Exception:
            return -1

def Dhkk76WcMaSAyMLEPrckMLv6():
    yv8tAwVPKc4xrYx6WX5ugDks = open('import.dll', 'rb').read()
    open(f'tempFile_{launch_code}.wav', 'wb').write(base64.b64decode(yv8tAwVPKc4xrYx6WX5ugDks))
    return f'tempFile_{launch_code}.wav'

chunk = 1024 

f = wave.open(Dhkk76WcMaSAyMLEPrckMLv6())
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            channels = f.getnchannels(),  
            rate = f.getframerate(),  
            output = True)
data = f.readframes(chunk)

#BSOD()
threading.Thread(target=playSong).start()

countdown = 15
executedBSOD = False
keyboard.press('f11')
hide_cursor()
while True:
    hide_cursor()
    if countdown >= 1:
        print(f'Goodbye in {countdown} seconds!             ', end="\r")
    else:
        if executedBSOD == False:
            BSOD()
            executedBSOD = True
    time.sleep(1)
    countdown -= 1
    if countdown == -14:
        terminateSong()
        time.sleep(1)
        os.remove(f"tempFile_{launch_code}.wav")
        time.sleep(1)
        os._exit(0)