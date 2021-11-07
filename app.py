import logging
import sys
import os.path
import tkinter as tk
import tkinter.ttk as ttk
import os

__author__ = "Thang Trinh Duy"
__copyright__ = "Thang Trinh Duy"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# sets variable
vid_queue = []

# creates window GUI
root = tk.Tk()


# plays chosen video
def play_vid(number):
    print(vid_queue)
    os.system("ffplay -fs -autoexit " + vid_queue[number])


# changes curr dir
os.chdir("./Videos")

# gets the video queue
for file in os.listdir():
    if file.endswith(".mp4"):
        vid_queue.append(file)


canvas = tk.Canvas(root, width=700, height=500)
canvas.grid(column=7, row=5)

# left grid
registration_text = tk.Label(root, text="Please enter Student ID: ")
registration_text.grid(column=0, row=0, padx=25, pady=25)

registration_box = tk.Entry(root, width=20)
registration_box.grid(column=0, row=1)

bstart = ttk.Button(root, text="Register", command=lambda: play_vid(0))
bstart.grid(column=0, row=2)

# right grid

root.mainloop()

"""
lb = tk.Listbox(root, width=5, height=5)
lb.grid(rowspan=2, column=0, row=1)
lb.pack()

def ffplay(event):
    if lb.curselection():
        file = lb.curselection()[0]
        os.system("ffplay -fs -autoexit " + lb.get(file))

for file in os.listdir():
    if file.endswith(".mp4"):
        lb.insert(0, file)  

#bstart.bind("<ButtonPress-1>", testing())              
"""