import tkinter as tk
from tkinter import ttk
import patcher as pqms_patcher
import argparse


class CheckboxArg(object):
    def __init__(self, master, dest, help):
        super(CheckboxArg, self).__init__()
        self.dest = dest
        self.help = help
        self.var = tk.BooleanVar(master, False)


class ValueArg(object):
    def __init__(self, master, dest, help):
        super(ValueArg, self).__init__()
        self.dest = dest
        self.help = help
        self.var = tk.StringVar(master, "")


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        argparser = pqms_patcher.makeArgParser()

        self.checkboxargs = []
        self.valueargs = []

        for action in argparser._actions:
            if isinstance(action, argparse._HelpAction):
                pass
            elif isinstance(action, argparse._StoreTrueAction):
                self.checkboxargs.append(CheckboxArg(self, action.dest, action.help))
            elif isinstance(action, argparse._StoreAction):
                self.valueargs.append(ValueArg(self, action.dest, action.help))
            else:
                print("Unknown type", type(action))

        self.argstr_vis = tk.StringVar()
        self.argstr = []

        self.initwindow()

        self.mainloop()

    def initwindow(self):
        # self.geometry("950x800")
        self.infobox = tk.Label(self, text="PQMS Wizard", font=("Default", 24))
        self.infobox.pack()

        row = 1

        argframe = tk.Frame(self)
        for arg in self.valueargs:
            tk.Label(argframe, text=arg.dest).grid(column=0, row=row, sticky="w")
            c = tk.Entry(argframe, textvariable=arg.var)
            c.bind("<KeyRelease>", self.updateArgStr)
            c.grid(column=1, row=row, sticky="w")
            tk.Label(argframe, text=arg.help).grid(column=2, row=row, sticky="w")
            row += 1

        for arg in self.checkboxargs:
            tk.Label(argframe, text=arg.dest).grid(column=0, row=row, sticky="w")
            c = tk.Checkbutton(
                argframe, text="--" + arg.dest, variable=arg.var, command=self.updateArgStr)
            c.grid(column=1, row=row, sticky="w")
            tk.Label(argframe, text=arg.help).grid(column=2, row=row, sticky="w")
            row += 1
        argframe.pack()

        tk.Label(self, textvariable=self.argstr_vis, bg="black", fg="white", font=("Courier", 12)).pack(fill="x")

        self.btn_go = ttk.Button(self, text="Go!", command=self.run)
        self.btn_go.pack()

        self.updateArgStr()

    def updateArgStr(self, event=None):
        self.argstr = []
        for arg in self.checkboxargs:
            if arg.var.get():
                self.argstr.append("--" + arg.dest)
        for arg in self.valueargs:
            if arg.var.get():
                self.argstr.append("--" + arg.dest)
                for string in arg.var.get().split(" "):
                    self.argstr.append(string)
        self.argstr_vis.set("python run_wizard.py " + " ".join(self.argstr))

    def run(self):
        pqms_patcher.main(self.argstr)


if __name__ == "__main__":
    MainWindow()
