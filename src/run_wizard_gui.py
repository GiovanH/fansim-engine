import tkinter as tk
from tkinter import ttk
import patcher as fse_patcher
import argparse
import _logging


def formatHelp(helpstr):
    return helpstr.replace(". ", ".\n")


class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            self.tw, text=self.text, justify='left',
            background='white', relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


class CheckboxArg(object):
    def __init__(self, master, dest, help):
        super(CheckboxArg, self).__init__()
        self.dest = dest
        self.help = help
        self.var = tk.BooleanVar(master, False)


class ValueArg(object):
    def __init__(self, master, dest, help, nargs):
        super(ValueArg, self).__init__()
        self.dest = dest
        self.help = help
        self.var = tk.StringVar(master, "")
        self.nargs = nargs


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        argparser = fse_patcher.makeArgParser()

        self.logger = _logging.getLogger(__name__)

        self.checkboxargs = []
        self.valueargs = []

        for action in argparser._actions:
            if isinstance(action, argparse._HelpAction):
                pass
            elif isinstance(action, argparse._StoreTrueAction):
                self.checkboxargs.append(CheckboxArg(self, action.dest, action.help))
            elif isinstance(action, argparse._StoreAction):
                self.valueargs.append(ValueArg(self, action.dest, action.help, action.nargs))
            else:
                self.logger.error("Unknown type", type(action))

        self.argstr_vis = tk.StringVar()
        self.argstr = []

        self.initwindow()

        self.mainloop()

    def initwindow(self):
        # self.geometry("950x800")
        self.infobox = tk.Label(self, text="FSE Wizard", font=("Default", 24))
        self.infobox.pack()

        row = 1

        argframe = tk.Frame(self)
        for arg in sorted(self.valueargs, key=lambda a: repr(a.nargs)):
            if arg.nargs == "+":
                helptip = tk.Label(argframe, text=" ?", justify="right")
                CreateToolTip(helptip, "Seperate multiple values with spaces")
                helptip.grid(column=1, row=row, sticky="nw")

            tk.Label(argframe, text=arg.dest, justify="left").grid(
                column=2, row=row, sticky="nw")

            c = tk.Entry(argframe, textvariable=arg.var)
            c.bind("<KeyRelease>", self.updateArgStr)
            c.grid(column=3, row=row, sticky="nw")

            tk.Label(argframe, text=formatHelp(arg.help), justify="left").grid(
                column=4, row=row, sticky="nw")
            row += 1

        for arg in self.checkboxargs:
            tk.Label(argframe, text=arg.dest).grid(
                column=2, row=row, sticky="nw")

            tk.Checkbutton(
                argframe, text="--" + arg.dest, variable=arg.var,
                command=self.updateArgStr).grid(
                column=3, row=row, sticky="nw")

            tk.Label(argframe, text=formatHelp(arg.help), justify="left").grid(
                column=4, row=row, sticky="nw")
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
        fse_patcher.main(self.argstr)
        self.logger.info("Done!")


if __name__ == "__main__":
    MainWindow()
