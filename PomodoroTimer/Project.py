from tkinter import Tk, Canvas, PhotoImage, Label
from tkinter import ttk
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF6B81"
RED = "#FF4D6D"
GREEN = "#3FA796"
YELLOW = "#FFF5E1"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 30 * 60
reps = 0
correct_sign = ""
tik_tok = None
current_count = 0
work_sessions = 0
ALARM_FILE = "alarm.mp3"


# ---------------------------- PLAY ALARAM ------------------------------- #
def play_alarm():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(ALARM_FILE)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing alarm: {e}")


# ---------------------------- UPDATE PROGRESS ------------------------------- #
def update_progress():
    # format checkmarks: 4 per line
    lines = []
    for i in range(0, len(correct_sign), 4):
        lines.append(correct_sign[i : i + 4])
    correct.config(text="\n".join(lines))

    # total time worked in minutes
    total_minutes = work_sessions * WORK_MIN / 60
    total_time_label.config(text=f"Total time worked: {total_minutes:.1f} min")


# ---------------------------- START TIME ------------------------------- #
def start_time():
    global reps, correct_sign, work_sessions
    # When starting: hide Start, show Reset and Pause
    button_start.grid_remove()
    button_reset.grid(row=3, column=2)
    button_pause.grid(row=3, column=0)

    reps += 1
    if reps % 8 == 0:
        correct_sign += "✔"
        work_sessions += 1
        update_progress()
        count_down(LONG_BREAK_MIN)
        timer.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN)
        timer.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        correct_sign += "✔"
        work_sessions += 1
        update_progress()
        count_down(SHORT_BREAK_MIN)
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    """canvas.create_text(100, 120, text=str(count-1), fill="white", font=(FONT_NAME, 35, "bold"))
    # using the previous line of code will create a text, each is above of the other one, not to do this -->
    ## you can change the value of the parameter text of the method (create_text)"""

    minutes = count // 60
    seconds = count % 60
    if count < 10:
        seconds = f"0{count}"
    if seconds == 0:
        seconds = "00"
    if count // 60 < 10:
        minutes = f"0{count//60}"
    global tik_tok, current_count
    if count > 0:
        current_count = count
        canvas.itemconfig(timer_down, text=f"{minutes}:{seconds}")  # note 8
        tik_tok = window.after(1000, count_down, count - 1)  # note 7
    else:
        current_count = 0
        canvas.itemconfig(timer_down, text="00:00")
        tik_tok = None
        play_alarm()
        # Timer finished: hide Pause, show Start again, keep Reset visible
        button_pause.grid_remove()
        button_start.grid(row=3, column=0)


# ---------------------------- RESET TIME ------------------------------- #
def reset_time():
    global reps, tik_tok, correct_sign, work_sessions
    if tik_tok is not None:
        window.after_cancel(tik_tok)
        tik_tok = None

    # stop alarm sound if it's playing
    try:
        pygame.mixer.music.stop()
    except:
        pass

    timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_down, text="00:00")
    correct_sign = ""
    work_sessions = 0
    correct.config(text="")
    total_time_label.config(text="Total time worked: 0.0 min")
    reps = 0

    # Show only the Start button again, hide Reset / Pause / Resume
    button_start.grid(row=3, column=0)
    button_reset.grid_remove()
    button_pause.grid_remove()
    button_resume.grid_remove()


def pause_time():
    global tik_tok
    if tik_tok is not None:
        window.after_cancel(tik_tok)
        tik_tok = None
        # Switch Pause -> Resume, keep Reset visible
        button_pause.grid_remove()
        button_resume.grid(row=3, column=0)


def resume_time():
    # Switch Resume -> Pause, keep Reset visible
    button_resume.grid_remove()
    button_pause.grid(row=3, column=0)
    # Continue counting down from the last stored value
    count_down(current_count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("740x500")
window.resizable(False, False)

canvas = Canvas(
    width=200, height=223, bg=YELLOW, highlightthickness=0
)  # note 1 & note 6
tomato = PhotoImage(file="tomato.png")
window.iconphoto(False, tomato)
canvas.create_image(
    100, 112, image=tomato
)  # this method needs three arguments (X, Y, image)  & # note 2
timer_down = canvas.create_text(
    100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(row=0, column=1)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Pomodoro.TButton",
    font=("Helvetica", 12, "bold"),
    foreground="#FFFFFF",
    background=GREEN,
    padding=(18, 10),
    borderwidth=0,
)
style.map(
    "Pomodoro.TButton",
    background=[
        ("active", PINK),
        ("pressed", RED),
        ("disabled", "#CCCCCC"),
    ],
    relief=[
        ("pressed", "sunken"),
        ("!pressed", "flat"),
    ],
)
button_start = ttk.Button(
    text="Start", command=start_time, style="Pomodoro.TButton", width=10
)
button_start.grid(row=3, column=0, pady=(20, 0))

button_reset = ttk.Button(
    text="Reset", command=reset_time, style="Pomodoro.TButton", width=10
)
button_pause = ttk.Button(
    text="Pause", command=pause_time, style="Pomodoro.TButton", width=10
)
button_resume = ttk.Button(
    text="Resume", command=resume_time, style="Pomodoro.TButton", width=10
)
button_reset.grid_remove()
button_pause.grid_remove()
button_resume.grid_remove()

correct = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
correct.grid(row=3, column=1, pady=(20, 0))

total_time_label = Label(
    text="Total time worked: 0.0 min",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 14, "bold"),
    highlightthickness=0,
)
total_time_label.grid(row=4, column=1, pady=(5, 0))

window.mainloop()
