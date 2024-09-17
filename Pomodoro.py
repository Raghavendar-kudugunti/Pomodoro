from tkinter import *
import math
from tkinter import font
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(str(timer))
  canvas.itemconfig(timer_text,text ="00:00")
  timer_label.config(text="Timer")
  tick_label.config()
  global reps
  reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
      count_down(long_break_sec)
      timer_label.config(text="Break",fg=RED)

    elif reps % 2 == 0:
      count_down(short_break_sec)
      timer_label.config(text="Break",fg=PINK)
    else:
      count_down(work_sec)
      timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
   count_min = math.floor(count / 60)
   count_sec = count % 60
   if count_sec < 10 :
     count_sec = f"0{count_sec}"

   canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
   if count > 0:
    global timer
    timer = window.after(1000,count_down,count - 1)
   else:
    start_timer()
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✔"
    tick_label.config(text=marks)

def button_click(count):
  global timer  
  if timer:  
      window.after_cancel(timer)  
  timer = window.after(1000, count_down, count - 1)  





# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
frame = Frame(window)
frame.grid(padx=10,pady=10)

# Canvas setup
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,113,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)


# Timer label
timer_label = Label(text="Timer",fg=GREEN,font=("Arial",30,"normal"),bg=YELLOW)
timer_label.grid(column=1,row=0)

# Tick label
tick_label = Label(fg=GREEN,font=("Arial",30,"bold"),bg=YELLOW)
tick_label.grid(column=1,row=3)

# Start button
start_button = Button(text="start",bg="white",font=FONT_NAME,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

# Reset button
reset_button = Button(text="reset",bg="white",font=FONT_NAME,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)



buttons = [
    ("1 min", 0, 0, 60),  
    ("2 min", 0, 1, 120), 
    ("3 min", 0, 2, 180), 
    ("5 min", 1, 0, 300), 
    ("10 min", 1, 1, 600),
    ("15 min", 1, 2, 900), 
]


for (text, row, col, count) in buttons:  # Add count to the loop
    button = Button(frame, text=text, command=lambda c=count: button_click(c))
    button.grid(row=row, column=col, padx=5, pady=5)




window.mainloop()

