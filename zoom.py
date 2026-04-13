import pyautogui
import time
import sys
import subprocess

#macos gelpers
def get_output():
    result = subprocess.run(['SwitchAudioSource', '-c'], capture_output=True, text=True)
    return result.stdout.strip()

def get_input():
    result = subprocess.run(['SwitchAudioSource', '-c', '-t', 'input'], capture_output=True, text=True)
    return result.stdout.strip()

def set_input(device):
    subprocess.run(['SwitchAudioSource', '-s', device, '-t', 'input'], capture_output=True)

def set_output(device):
    subprocess.run(["SwitchAudioSource", '-s', device], capture_output=True)

def activate():
    for zoom in ["zoom.us", "Zoom"]:
        result = subprocess.run(
            ['osascript', '-e', f'tell application "{zoom}" to activate'],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            return True
        print(zoom, result.stderr.strip())
    return False
    
def focus(file):
    if not activate():
        print("zoom not runing, cannot activate")
        sys.exit(1)
    
    time.sleep(2)

    output = get_output()
    input = get_input()

    pyautogui.hotkey("shift", "command", "a")
    pyautogui.hotkey("shift", "command", "a")
    set_output("Zoom Output")
    set_input("Zoom Audio")
    time.sleep(1)
    subprocess.run(['afplay', file])
    set_output(output)
    set_input(input)
    pyautogui.hotkey("shift", "command", "a")

if __name__ == "__main__":
    focus("result.wav")