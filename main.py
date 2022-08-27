from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
LITE_YELLOW = "#FCF8E8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeations = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_update, text="00:00")
    timer_label.config(text="Timer")
    done_button.config(text="")
    global repeations
    repeations = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global repeations
    repeations += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repeations % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif repeations % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    elif count_minutes == 0:
        count_minutes = "00"

    canvas.itemconfig(timer_update, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marked = " "
        work_sessions = math.floor(repeations/2)
        for _ in range(work_sessions):
            marked += "✔"
            done_button.config(text=marked)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=LITE_YELLOW)

canvas= Canvas(width=200, height=224, bg=LITE_YELLOW, highlightthickness=0)
pomidor = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomidor)
timer_update = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=LITE_YELLOW, font=(FONT_NAME, 32, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

done_button = Label(fg=GREEN, bg=LITE_YELLOW, font=(32))
done_button.grid(column=1, row=3)




window.mainloop()