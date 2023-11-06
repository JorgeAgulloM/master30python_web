### Frames ###
import tkinter as tk

window = tk.Tk()
window.title('Frames | Tkinter & Python')
window.geometry('400x400')

def frame_f(side, anchor):
    frame = tk.Frame(window, width=150, height=150)
    frame.config(bg='gray')
    frame.pack(side=side, anchor=anchor, fill='x', expand=True)
    return frame

def quad(frame, bg: str, side: str, anchor: str):
    frame = tk.Frame(frame, width=150, height=150)
    frame.config(
        bg=bg,
        bd=4,
        relief='raised'
    )
    frame.pack(side=side, anchor=anchor)
    frame.pack_propagate(False)

    text = tk.Label(frame, text=bg)
    text.config(bg=bg, font=('Consolas', 16))
    text.pack(expand=True)

frame_top = frame_f('top', 'n')
frame_bottom = frame_f('bottom', 's')

quad(frame_top, 'red', 'right', 'n')
quad(frame_top, 'green', 'left', 'n')
quad(frame_bottom, 'blue', 'right', 's')
quad(frame_bottom, 'yellow', 'left', 's')

window.mainloop()