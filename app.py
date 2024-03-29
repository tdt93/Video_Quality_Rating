import sys
import os.path
import tkinter as tk
import tkinter.ttk as ttk
import os
import csv
import webbrowser
import random
import pymysql
import time
import datetime

from tkinter import LEFT, StringVar
from PIL import ImageTk, Image


# sets variable
vid_queue = []
description_0 = "INSTRUCTIONS: "
description_1 = "Enter your Student ID and choose your group. \n \n" \
                "or press [ESC] to close the window"
description_2 = "Watch short videos: \n \n" \
                "    - [SPACE] to pause video \n"\
                "    - [ESC] to quit "
description_3 = "Rate each video base on your satisfaction \n \n" \
                "Press [CONTINUE] to progress \nuntil done"
description_4 = "Congrats, you are half way there! \n \n " \
                "         Rate and let's continue..."
description_5 = "Please finish rating and answer the questionnaires \n \n " \
                "           by pressing [QUESTIONNAIRE]"
progress = 1
step = 0
time_stamp = ""
result = []
path = os.getcwd()
url = "https://psychocracow.fra1.qualtrics.com/jfe/form/SV_5o4u1gnnML5umQC"

# connects to database
db = pymysql.connect(host="[MySQL_SERVER]", port=[PORT_NUMBER], user="[USERNAME]", passwd="[DB_PASS]", database="[DB_NAME]")
my_cursor = db.cursor()


# creates window GUI
root = tk.Tk()
root.title("Video Quality Rating")
root.configure(bg="#000000")
root.wm_attributes("-fullscreen", "true")
root.bind("<Escape>", lambda event: root.destroy())

choice = StringVar()

# shows logo
logo = Image.open(path + "/logo.jpg")
logo = logo.resize((800, 390), Image.ANTIALIAS)
title = ImageTk.PhotoImage(logo)
title_text = tk.Label(root, image=title, borderwidth=0)
title_text.image = title
title_text.place(relx=0.5, rely=0.1115, anchor="n")

counter = tk.Label(root, text="Progress: 0/2", bg="#000000", fg="#db0000", font=("Helvetica", 18))
counter.place(relx=0.485, rely=0.35, anchor="center")

registration_text = tk.Label(root, text="Student ID: ", bg="#000000", fg="#ffffff", font=("Helvetica", 18))
registration_text.place(relx=0.49, rely=0.5, anchor="center")

registration_box = tk.Entry(root, width=20, bg="#564d4d", fg="#ffffff", font=("Helvetica", 19), borderwidth=0)
registration_box.place(relx=0.486, rely=0.55, anchor="center")

# sets buttons style, creates buttons
btn_style = ttk.Style()
btn_style.theme_use("alt")
btn_style.configure("TButton", width=15, background="#db0000", foreground="#000000", font=("Helvetica", 19), borderwidth=0)
btn_style.configure("TRadiobutton", background="#000000", foreground="#db0000", font=("Helvetica", 18))

play_btn = ttk.Button(root, text="WATCH", width=20, command=lambda: play_vid(step))

play_next_btn = ttk.Button(root, text="CONTINUE", width=20, command=lambda: play_next(step))

finish_btn = ttk.Button(root, text="QUESTIONNAIRE", width=20, command=lambda: finish_rating(True))

registration_btn = ttk.Button(root, text="Register", command=lambda: show_play_btn(True))
registration_btn.place(relx=0.485, rely=0.7, anchor="center")

# shows instructions
desc_text_0 = tk.Label(root, text=description_0, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 14))
desc_text_1 = tk.Label(root, text=description_1, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 12))
desc_text_2 = tk.Label(root, text=description_2, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 12))
desc_text_3 = tk.Label(root, text=description_3, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 12))
desc_text_4 = tk.Label(root, text=description_4, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 16))
desc_text_5 = tk.Label(root, text=description_5, justify=LEFT, anchor="w", bg="#000000",
                       fg="#ffffff", font=("Helvetica", 16))

desc_text_0.place(relx=0.8, rely=0.3, anchor="center")
desc_text_1.place(relx=0.8, rely=0.38, anchor="center")

# creates radio-buttons
choice_1 = ttk.Radiobutton(root, text="BAD", variable=choice, value="BAD", style="TRadiobutton")
choice_2 = ttk.Radiobutton(root, text="POOR", variable=choice, value="POOR", style="TRadiobutton")
choice_3 = ttk.Radiobutton(root, text="FAIR", variable=choice, value="FAIR", style="TRadiobutton")
choice_4 = ttk.Radiobutton(root, text="GOOD", variable=choice, value="GOOD", style="TRadiobutton")
choice_5 = ttk.Radiobutton(root, text="EXCELLENT", variable=choice, value="EXCELLENT", style="TRadiobutton")
group_1 = ttk.Radiobutton(root, text="Monday Group", variable=choice, value="Monday Group", style="TRadiobutton")
group_2 = ttk.Radiobutton(root, text="Thursday Group", variable=choice, value="Thursday Group", style="TRadiobutton")
group_1.place(relx=0.41, rely=0.61, anchor="center")
group_2.place(relx=0.56, rely=0.61, anchor="center")


# shows play btn
def show_play_btn(event):
    if len(registration_box.get()) != 0 and len(choice.get()) != 0:
        if event:
            play_btn.place(relx=0.485, rely=0.7, anchor="center")
            desc_text_2.place(relx=0.8, rely=0.38, anchor="center")
            result.append(registration_box.get())
            result.append(choice.get())
            result.append("Test_01")
            desc_text_1.place_forget()
            registration_text.place_forget()
            registration_btn.place_forget()
            registration_box.place_forget()
            group_1.place_forget()
            group_2.place_forget()
            counter.config(text="Progress: 1/2")
            # changes curr dir
            if choice.get() == "Monday Group":
                new_path = os.path.join(path, "Monday_Group")
                os.chdir(new_path)
            else:
                new_path = os.path.join(path, "Thursday_Group")
                os.chdir(new_path)
            # gets the video queue
            for file in os.listdir():
                if file.endswith(".mp4"):
                    vid_queue.append(file)
            # generates repetitive video sequence :
            if choice.get() == "Thursday Group":
                tmp = vid_queue.copy()
                tmp.extend(tmp)
                vid_queue.extend(tmp)
            # saves id to database
            try:
                my_cursor.execute("insert into students(student_id, groups)"
                                  " values('%s', '%s')" % (registration_box.get(), choice.get()))
                db.commit()
                print("updated database successful")
            except Exception as e:
                db.rollback()
                print("Exception occurred: ", e)


# plays the 1st video
def play_vid(number):
    if len(choice.get()) != 0:
        if progress == 2:
            get_curr_time()
            result.append(choice.get())
            result.append(time_stamp)
            save_result(vid_queue[-1], choice.get(), time_stamp)
        # generates random video sequence:
        random.shuffle(vid_queue)
        choice.set("")
        os.system("ffplay -fs -autoexit -fast " + vid_queue[number])
        result.append(vid_queue[number])
        play_btn.place_forget()
        desc_text_2.place_forget()
        desc_text_4.place_forget()
        desc_text_3.place(relx=0.8, rely=0.38, anchor="center")
        choice_1.place(relx=0.3, rely=0.54, anchor="center")
        choice_2.place(relx=0.4, rely=0.54, anchor="center")
        choice_3.place(relx=0.5, rely=0.54, anchor="center")
        choice_4.place(relx=0.6, rely=0.54, anchor="center")
        choice_5.place(relx=0.7, rely=0.54, anchor="center")
        play_next_btn.place(relx=0.485, rely=0.7, anchor="center")
        global step
        step += 1


# plays the next video in the sequence
def play_next(number):
    global step, progress
    if len(choice.get()) != 0:
        os.system("ffplay -fs -autoexit " + vid_queue[number])
        get_curr_time()
        result.append(choice.get())
        result.append(time_stamp)
        result.append(vid_queue[number])
        save_result(vid_queue[number-1], choice.get(), time_stamp)
        choice.set("")
        step += 1
        if step >= len(vid_queue):
            play_next_btn.place_forget()
            if progress == 1:
                step = 0
                progress = 2
                counter.config(text="Progress: 2/2")
                desc_text_4.place(relx=0.485, rely=0.45, anchor="center")
                play_btn.place(relx=0.485, rely=0.7, anchor="center")
                result.append("Test_02")
            else:
                desc_text_5.place(relx=0.485, rely=0.45, anchor="center")
                finish_btn.place(relx=0.485, rely=0.7, anchor="center")


# finishes testing
def finish_rating(event):
    if event and (len(choice.get()) != 0):
        get_curr_time()
        result.append(choice.get())
        result.append(time_stamp)
        save_result(vid_queue[step - 1], choice.get(), time_stamp)
        os.chdir(os.path.dirname(os.getcwd()))
        f = open("result.csv", "a", newline="")
        writer = csv.writer(f)
        writer.writerow(result)
        f.close()
        db.close()
        # opens questionnaire link
        webbrowser.open(url, new=0, autoraise=True)
        sys.exit(0)


# gets time stamp
def get_curr_time():
    global time_stamp
    time_temp = time.time()
    time_stamp = datetime.datetime.fromtimestamp(time_temp).strftime('%Y-%m-%d %H:%M:%S')


# saves result to database
def save_result(vid_id, rate, time_temp):
    try:
        my_cursor.execute("insert into expEvaluation(student_id, video_id, evaluation, time_stamp)"
                          " values('%s', '%s', '%s', '%s')" % (registration_box.get(), vid_id, rate, time_temp))
        db.commit()
        print("updated database successful")
    except Exception as e:
        db.rollback()
        print("Exception occurred: ", e)


root.mainloop()
