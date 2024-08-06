from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time

from comtypes import CLSCTX_ALL

def get_current_application_volumes():
    application_volumes = {"chrome.exe": 0.2, "firefox.exe": 0.1, "spotify.exe": 0.2}
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        if session.Process and session.Process.name() is not None:
            volume = round(float(interface.GetMasterVolume()), 2)
            name = session.Process.name()
            if name in application_volumes.keys():
                interface.SetMasterVolume(application_volumes[name], None)
            if volume == 1.0:
                interface.SetMute(1, None)
                interface.SetMasterVolume(0, None)
            print(f"Application: {name} Volume: {volume}")

def set_main_device_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(0.6, None)
    

starttime = time.monotonic()
while True:
    print("tick")
    get_current_application_volumes()
    set_main_device_volume()
    time.sleep(0.25 - ((time.monotonic() - starttime) % 0.25))
