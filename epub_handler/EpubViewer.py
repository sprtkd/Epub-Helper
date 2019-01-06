import sys,os
from tkinter import *
import re
import tkinter.ttk as ttk
from tkinter import filedialog
py3 = True
from tkinter import messagebox
from EpubViewer_support import *
import epubHandler
import tkinter.scrolledtext as tkst
from ReaderRender import TextWithMeaningRender
from wordMeanings.wordUtils import MiniMeaningCache
from Account.AccountEditor_viewer import AccountEditor

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#d9d9d9' # X11 color: 'gray85' 
font10 = "-family {Yu Gothic UI} -size 12 -weight normal "  \
    "-slant roman -underline 0 -overstrike 0"
font11 = "-family {Gill Sans Ultra Bold} -size 12 -weight bold"  \
    " -slant roman -underline 0 -overstrike 0"
font12 = "-family {@Microsoft YaHei UI} -size 13 -weight bold "  \
    "-slant roman -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
    "roman -underline 0 -overstrike 0"
font14 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
    "roman -underline 0 -overstrike 0"
font15 = "-family {Trebuchet MS} -size 12 -weight normal "  \
    "-slant roman -underline 0 -overstrike 0"
font16 = "-family {Yu Gothic UI Semibold} -size 14 -weight "  \
    "normal -slant roman -underline 0 -overstrike 0"
font17 = "-family {Yu Gothic UI Semibold} -size 15 -weight "  \
    "normal -slant roman -underline 1 -overstrike 0"
font23 = "TkDefaultFont"
font9 = "-family {Yu Gothic Medium} -size 8 -weight normal "  \
    "-slant roman -underline 0 -overstrike 0"
        

    

class ePUBviewer:
    def __init__(self, top=None):
        self.epubFileName =None
        self.epubFile = None
        self.epubFileDetails=None
        self.currentPageNumber=0
        self.currentText=None
        self.MaxPageNumber=0
        self.currSelectedWord=None
        self.root=top
        top.resizable(False, False)
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x620+262+42")
        top.title("ePUBviewer")       
        top.configure(background="#d9d9d9")
        top.configure(height="56")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.maxTextPerLine = 87
        self.maxMeaningLen = 40
        self.MiniMeaningCache = MiniMeaningCache(self.maxMeaningLen)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.01, rely=0.02, height=40, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#eef285")
        self.Button1.configure(cursor="plus")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open''')
        self.Button1.configure(command=self.openEpubFile)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.14, rely=0.02, height=40, width=74)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#f4f4f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font14)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(relief=GROOVE)
        self.Label1.configure(text='''Page No:''')

        self.Spinbox1 = Spinbox(top, from_=0, to=1)
        self.Spinbox1.place(relx=0.23, rely=0.02, relheight=0.06, relwidth=0.11)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font=font14)
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(justify=CENTER)
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(state=DISABLED)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.41, rely=0.02, height=40, width=244)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font15)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief=RIDGE)
        self.Label2.configure(text='''Filename''')
        self.Label2.configure(anchor='e')
        
        createToolTip(self.Label2)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.34, rely=0.02, height=40, width=47)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#636363")
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''GO''')
        self.Button2.configure(command=self.gotoEpubPageNumber)
        

        self.Button3 = Button(top)
        self.Button3.place(relx=0.74, rely=0.02, height=40, width=117)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#00ffd4")
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font13)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Account''')
        self.Button3.configure(command=self.openAccount)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.9, rely=0.02, height=40, width=67)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#9cdb27")
        self.Button4.configure(cursor="hand2")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font12)
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Info''')
        self.Button4.configure(command=self.infoEpubReader)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.83, rely=0.89, height=44, width=57)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#a3a3a3")
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font11)
        self.Button5.configure(foreground="#ffffff")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''<<''')
        self.Button5.configure(command=self.gotoEpubPrevPage)

        self.Button6 = Button(top)
        self.Button6.place(relx=0.91, rely=0.89, height=44, width=57)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(background="#a3a3a3")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font11)
        self.Button6.configure(foreground="#ffffff")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''>>''')
        self.Button6.configure(command=self.gotoEpubNextPage)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.83, rely=0.84, height=28, width=124)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(relief=RIDGE)
        self.Label3.configure(text='''Page Scroll''')

        self.Button7 = Button(top)
        self.Button7.place(relx=0.01, rely=0.84, height=70, width=87)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#c2fff9")
        self.Button7.configure(cursor="hand2")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font14)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''See all
Meanings''')
        self.Button7.configure(command=self.seeAllMeanings)

        self.Text1 = Text(top)
        self.Text1.place(relx=0.24, rely=0.84, relheight=0.11, relwidth=0.41)
        self.Text1.configure(background="#e8e8e8")
        self.Text1.configure(font=font23)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(padx="4")
        self.Text1.configure(pady="4")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=324)
        self.Text1.configure(wrap=WORD)
        addNewText(self.Text1,"")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.14, rely=0.84, height=70, width=84)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#e8e8e8")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font14)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(relief=GROOVE)
        self.Label4.configure(text='''Meaning:''')

        self.Button8 = Button(top)
        self.Button8.place(relx=0.65, rely=0.84, height=70, width=77)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#ffe7a6")
        self.Button8.configure(cursor="hand2")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font10)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''See
in depth''')
        self.Button8.configure(command=self.seeInDepth)

        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.01, rely=0.1, relheight=0.73, relwidth=0.98)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font16)
        self.Scrolledtext1.configure(foreground="#686868")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(padx="20")
        self.Scrolledtext1.configure(pady="20")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap=WORD)
        TextWithMeaningRender(self.Scrolledtext1,'',font16,font17,font9,self.maxTextPerLine,self.MiniMeaningCache).renderPage()
        
        
        
        
    #functions
    def openEpubFile(self):
        self.epubFileName = filedialog.askopenfilename(filetypes=(("Epub files", "*.epub"),
                                           ("All files", "*.*") ))
        
        if(self.epubFileName==None):
            return
        
        try:
            self.epubFile,self.epubFileDetails,self.MaxPageNumber = epubHandler.load_files(self.epubFileName)
        except:
            messagebox.showerror("Open","Cannot open file!")
            return
        self.Spinbox1.configure(state=NORMAL)
        head, tail = os.path.split(self.epubFileName)
        temp_text=tail+' ('+str(self.MaxPageNumber)+' pgs )'
        self.Label2.configure(text=temp_text)
        self.currentPageNumber=1
        self.Spinbox1.configure(from_=1)
        self.Spinbox1.configure(to=self.MaxPageNumber)
        self.currentText,self.currentPageNumber=epubHandler.get_page_by_number(self.epubFile,1)
        spinSetval(self.Spinbox1,self.currentPageNumber)
        self.showPage()
        
    

    def getSelectedWord(self):
        ranges = self.Scrolledtext1.tag_ranges(SEL)
        if ranges:
            sentence = self.Scrolledtext1.get(*ranges)
            word = re.split('(\W+)', sentence, 1)[0]
            word=word.lower()
            if(self.currSelectedWord==None or self.currSelectedWord!=word):
                self.currSelectedWord=word
                addNewText(self.Text1,'<'+word +'>\n'+get_word_meaning(self.currSelectedWord))
        
        
    def infoEpubReader(self):
        if self.epubFileDetails!=None:
            text = ''.join('\n{}:{}'.format(key, val) for key, val in self.epubFileDetails.items())
            messagebox.showinfo("Info",text+'\n\n\nViewer by Suprotik Dey\nBluezeal Labs')
        
    def gotoEpubPageNumber(self):
        to_gotopage = int(self.Spinbox1.get())
        if to_gotopage>self.MaxPageNumber or self.epubFile==None or to_gotopage==self.currentPageNumber:
            return
        self.currentText,self.currentPageNumber=epubHandler.get_page_by_number(self.epubFile,to_gotopage)
        spinSetval(self.Spinbox1,self.currentPageNumber)
        self.showPage()
        
        
    def openAccount(self):
        AccountEditor(self.root)

    #TODO        
    def seeAllMeanings(self):
        pass
        
    def seeInDepth(self):
        text=self.Text1.get("1.0",END)
        messagebox.showinfo("Detailed Meaning",text)
        
        
    def gotoEpubPrevPage(self):
        if(self.epubFile==None or self.currentPageNumber==1):
            return
        self.currentText,self.currentPageNumber=epubHandler.get_prev_page(self.epubFile)
        spinSetval(self.Spinbox1,self.currentPageNumber)
        self.showPage()
        
    def gotoEpubNextPage(self):
        if(self.epubFile==None or self.currentPageNumber==self.MaxPageNumber):
            return
        self.currentText,self.currentPageNumber=epubHandler.get_next_page(self.epubFile)
        spinSetval(self.Spinbox1,self.currentPageNumber)
        self.showPage()
    
    def showPage(self):
        TextWithMeaningRender(self.Scrolledtext1,self.currentText,font16,font17,font9,self.maxTextPerLine,self.MiniMeaningCache).renderPage()
        
    def updateViewer(self):
        self.root.update()
        #self.getSelectedWord()
        
    
            




def start_epubReader():
    root = Tk()
    epObj = ePUBviewer (root)
    try:
        while True:
            epObj.updateViewer()
    except Exception as exceptionCode:
        print(exceptionCode)


#main
start_epubReader()

