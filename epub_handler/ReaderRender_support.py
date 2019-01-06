from tkinter import *
from wordMeanings import wordUtils
import re

def calcLinePixels(num,cfont):
        spaces=''
        spaces += ' '*num
        line_len = cfont.measure(spaces)
        return line_len

def spacer(word,overflow):
    if overflow % 2==0:
        firstspace = int(overflow /2)
        lastspace = firstspace
    else:
        overflow-=1
        firstspace = int(overflow /2)
        lastspace = firstspace
        firstspace+=1
        
    spaced_word = (' '*firstspace) + word + (' '*lastspace)
    return spaced_word

def hardWordCallback(event):
    print('callback')
    index = event.widget.index("@%s,%s" % (event.x, event.y))
    tag_indices = list(event.widget.tag_ranges('hard'))
    
    hardword = ''
    
    # iterate them pairwise (start and end index)
    for start, end in zip(tag_indices[0::2], tag_indices[1::2]):
        # check if the tag matches the mouse click index
        if event.widget.compare(start, '<=', index) and event.widget.compare(index, '<', end):
            # return string between tag start and end
            print(event.x, event.y, event.widget.get(start, end))
            hardword+= event.widget.get(start, end)
            
    ClickableMeaningToolTip(event.widget,hardword,event.x, event.y)

def isblank(s):
    return not bool(not s or s.isspace())

def get_formatted_meaning(string):
    word=re.split('(\W+)', string, 1)[0]
    word=word.lower()
    return wordUtils.meaning_to_string(wordUtils.get_meaning(word))
    
    
class ClickableMeaningToolTip(object):

    def __init__(self, widget,hardword,pointx,pointy):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.hardword = hardword.strip()
        self.text = get_formatted_meaning(self.hardword)
        self.showtip(pointx,pointy)

    def showtip(self,pointx,pointy):
        if self.tipwindow or not self.hardword:
            return
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        off_x=-150
        off_y=-170
        tw.wm_geometry("+%d+%d" % (pointx-off_x,pointy-off_y))
        label = Label(tw, text='<'+self.hardword+'>\n'+self.text, justify=LEFT, background="#ffffe0", relief=RAISED, borderwidth=1,font=("tahoma", "8", "normal"))
        label.pack(ipadx=5)
        button = Button(tw, text="OK", command=self.hidetip)
        button.pack()
        tw.grab_set()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()