from tkinter import *


class TypingProgram:
    def __init__(self):
        self.has_written = False
        # Set timer choice to however long you want in seconds
        self.timer_choice = 10
        self.timer = self.timer_choice
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.title("Disappearing Text Program")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(3, weight=1)
        self.text = Text(wrap=WORD)
        self.text.grid(row=0, column=1, pady=(25, 10), padx=25)
        self.counter_label = Label(text=self.timer, relief=RAISED)
        self.counter_label.grid(row=1, column=1, pady=(0, 10))
        # self.set_timer_entry = Entry()
        # self.set_timer_entry.grid(row=2, column=1, pady=(0, 10))
        # self.set_timer_entry.bind("<Return>", self.set_timer)
        self.text.bind("<Key>", self.typing_starts)
        mainloop()

    # def set_timer(self, event):
    #     try:
    #         choice = int(self.set_timer_entry.get())
    #         self.set_timer_entry.delete(0, END)
    #         self.timer_choice = choice
    #         print(self.timer_choice)
    #     except ValueError:
    #         self.set_timer_entry.delete(0, END)

    def countdown(self):
        if self.has_written:
            self.timer -= 1
            if self.timer == 0:
                self.delete_and_reset()
            self.window.after(1000, self.countdown)
            if self.timer != self.timer_choice:
                self.counter_label.config(text=self.timer)
            else:
                self.counter_label.config(text=0)

    def delete_and_reset(self):
        self.text.delete(1.0, "end")
        self.has_written = False
        self.timer = self.timer_choice

    def reset_timer(self):
        self.timer = self.timer_choice

    # When user begins typing, the countdown function begins. As this function continues to run, any additional
    # key presses will reset the timer.
    def typing_starts(self, event):
        if self.has_written:
            self.reset_timer()
        else:
            self.has_written = True
            self.countdown()


if __name__ == "__main__":
    TypingProgram()
