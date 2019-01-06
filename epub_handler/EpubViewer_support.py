from tkinter import *
import tkinter.ttk as ttk
py3 = True
from wordMeanings import wordUtils
from wordMeanings.wordUtils import WordProcesser, MiniMeaningCache

def spinSetval(sb,val):
    sb.delete(0,"end")
    sb.insert(0,val)

def addNewText(textbox,text):
    textbox.config(state=NORMAL)
    textbox.delete('1.0', END)
    textbox.insert(END, text, "bold")
    textbox.config(state=DISABLED)
    

def get_word_meaning(word):
    return wordUtils.meaning_to_string(wordUtils.get_meaning(word))

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self):
        "Display text in tooltip window"
        self.text = self.widget['text']
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip()
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)