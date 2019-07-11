import subprocess
import tkinter as tk
from tkinter import Button, Label, Text
import threading


class Application(tk.Frame):
    output: Text
    display: Label
    start_button: Button
    pull_button: Button

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pull_button = tk.Button(self)
        self.pull_button["text"] = "Pull"
        self.pull_button["command"] = self._pull
        self.pull_button.grid(column=1, row=1)
        self.start_button = tk.Button(self, text="Start server",
                                      command=self._start)
        self.start_button.grid(column=3, row=1)

        self.display = tk.Label(fg="red")
        self.display.pack()

        self.output = tk.Text()
        self.output.config(width=300, height=30)
        self.output.pack()

    def _start(self):
        s = threading.Thread(target=self.start)
        s.start()
        s2 = threading.Thread(target=self.start2)
        s2.start()

    def _pull(self):
        s = threading.Thread(target=self.pull)
        s.start()

    def start(self):
        self.display.config(text="Starting websocket server")
        with subprocess.Popen("yarn prod", shell=True, stdout=subprocess.PIPE, cwd="./websocket") as p:
            for line in p.stdout:
                self.output.insert(tk.END, line)

    def start2(self):
        self.display.config(text="Starting django server")
        with subprocess.Popen("python3 manage.py runserver 0.0.0.0:8080", shell=True, stdout=subprocess.PIPE,
                              cwd="./serverless") as p:
            for line in p.stdout:
                self.output.insert(tk.END, line)

    def pull(self):
        self.display.config(text="Starting git pull")
        with subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE) as p:
            for line in p.stdout:
                self.output.insert(tk.END, line)


root = tk.Tk()
root.geometry("400x500")
app = Application(master=root)
app.mainloop()
