import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_audio_devices():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMute(), volume.GetMasterVolumeLevelScalar()


def set_audio_device(device_index):
    devices = AudioUtilities.GetSpeakers()
    device = devices[device_index]
    interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)
    volume.SetMasterVolumeLevelScalar(1, None)


def swap_audio_channel(device_index):
    # Get the current audio settings
    is_mute, volume_level = get_audio_devices()

    # Set the audio device to the desired channel
    set_audio_device(device_index)

    # Allow some time for the audio settings to apply
    time.sleep(1)

    # Restore the original audio settings
    set_audio_device(0)  # Assuming 0 is the index of the default audio device
    get_audio_devices()


if __name__ == "__main__":
    # Replace with the actual index of your desired audio device
    desired_device_index = 1

    # Swap audio channels when the specific audio device is connected
    while True:
        devices = AudioUtilities.GetSpeakers()
        connected_devices = [device.DeviceFriendlyName for device in devices]

        if "Your Desired Audio Device" in connected_devices:
            swap_audio_channel(desired_device_index)

        time.sleep(5)  # Check every 5 seconds

# script for global shortcut to swap audio channel, include discord and windows sound setting