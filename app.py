import sys
import os.path
import tkinter as tk
import tkinter.ttk as ttk
import os
import csv

from tkinter import LEFT, StringVar
from PIL import ImageTk, Image


# sets variable

vid_queue = []
description_1 = "INSTRUCTIONS: \n \n 1. Enter your Student ID and choose \n your group \n 2. Watch short videos: \n" \
                "     - [SPACE] to pause video \n "\
                "    - [ESC] to quit "
description_2 = "\n \n 3. Rate each video base on your satisfaction " \
                "\n 4. Press [CONTINUE] to progress \n until done \n 5. Press [DONE] to finish "
step = 0
result = []
path = os.getcwd()

# creates window GUI
root = tk.Tk()
root.title("Video Quality Rating")
root.configure(bg="#000000")

choice = StringVar()

canvas = tk.Canvas(root, width=600, height=400, bg="#000000")
canvas.grid(column=2, row=4)


# layout
logo = Image.open(path + "/logo.jpg")
logo = logo.resize((350, 170), Image.ANTIALIAS)
title = ImageTk.PhotoImage(logo)
title_text = tk.Label(root, image=title, borderwidth=0)
title_text.image = title
title_text.place(x=130, y=5)

registration_text = tk.Label(root, text="Student ID: ", bg="#000000", fg="#ffffff", font=8)
registration_text.place(x=255, y=140)

registration_box = tk.Entry(root, width=15, bg="#564d4d", fg="#ffffff", font=8, borderwidth=0)
registration_box.place(x=225, y=165)

# sets buttons style
btn_style = ttk.Style()
btn_style.theme_use("alt")
btn_style.configure("TButton", background="#db0000", foreground="#000000", font=10, borderwidth=0)
btn_style.configure("TRadiobutton", background="#000000", foreground="#db0000", font=10)

play_btn = ttk.Button(root, text="WATCH", width=20, command=lambda: play_vid(step))

play_next_btn = ttk.Button(root, text="CONTINUE", width=20, command=lambda: play_next(step))

finish_btn = ttk.Button(root, text="DONE", width=20, command=lambda: finish_rating(True))

choice_1 = ttk.Radiobutton(root, text="BAD", variable=choice, value="BAD", style="TRadiobutton")
choice_2 = ttk.Radiobutton(root, text="MEH", variable=choice, value="MEH", style="TRadiobutton")
choice_3 = ttk.Radiobutton(root, text="OK", variable=choice, value="OK", style="TRadiobutton")
choice_4 = ttk.Radiobutton(root, text="NICE", variable=choice, value="NICE", style="TRadiobutton")
choice_5 = ttk.Radiobutton(root, text="GREAT", variable=choice, value="GREAT", style="TRadiobutton")
group_1 = ttk.Radiobutton(root, text="Monday Group", variable=choice, value="Monday Group", style="TRadiobutton")
group_2 = ttk.Radiobutton(root, text="Thursday Group", variable=choice, value="Thursday Group", style="TRadiobutton")
group_1.place(x=150, y=195)
group_2.place(x=320, y=195)


# finishes testing
def finish_rating(event):
    if event and (len(choice.get()) != 0):
        result.append(choice.get())
        print(result)
        os.chdir(os.path.dirname(os.getcwd()))
        f = open("result.csv", "a", newline="")
        writer = csv.writer(f)
        writer.writerow(result)
        f.close()
        sys.exit(0)


# shows play btn
def show_play_btn(event):
    if len(registration_box.get()) != 0 and len(choice.get()) != 0:
        if event:
            play_btn.place(x=210, y=240)
            result.append(registration_box.get())
            result.append(choice.get())
            registration_text.place_forget()
            registration_btn.place_forget()
            registration_box.place_forget()
            group_1.place_forget()
            group_2.place_forget()
            # changes curr dir
            if choice.get() == "Group 1":
                os.chdir("./Monday Group")
            else:
                os.chdir("./Thursday Group")
            choice.set("")
            # gets the video queue
            for file in os.listdir():
                if file.endswith(".mp4"):
                    vid_queue.append(file)


# plays chosen video
def play_vid(number):
    os.system("ffplay -fs -autoexit " + vid_queue[number])
    result.append(vid_queue[number])
    play_btn.place_forget()
    choice_1.place(x=70, y=140)
    choice_2.place(x=170, y=140)
    choice_3.place(x=270, y=140)
    choice_4.place(x=370, y=140)
    choice_5.place(x=470, y=140)
    play_next_btn.place(x=210, y=240)
    global step
    step += 1


def play_next(number):
    global step
    if len(choice.get()) != 0:
        os.system("ffplay -fs -autoexit " + vid_queue[number])
        result.append(choice.get())
        result.append(vid_queue[number])
        choice.set("")
        step += 1
        if step >= len(vid_queue):
            play_next_btn.place_forget()
            finish_btn.place(x=210, y=240)


registration_btn = ttk.Button(root, text="Register", command=lambda: show_play_btn(True))
registration_btn.place(x=242, y=240)

desc_text_1 = tk.Label(root, text=description_1, justify=LEFT, anchor="w", bg="#000000", fg="#ffffff")
desc_text_2 = tk.Label(root, text=description_2, justify=LEFT, anchor="w", bg="#000000", fg="#ffffff")
desc_text_1.place(x=40, y=280)
desc_text_2.place(x=280, y=280)


root.mainloop()
