from tkinter import *
import tkinter.ttk as ttk

class AccountEditor:
    def __init__(self, top):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Arial Rounded MT Bold} -size 11 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
        font13 = "-family {Arial Rounded MT Bold} -size 16 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
            
            
            
        self.root=Toplevel(top)
        self.root.wm_overrideredirect(1)
        
        
        
        self.root.resizable(False, False)

        self.root.geometry("400x450+387+136")
        self.root.title("AccountEditor")
        self.root.configure(background="#d9d5d9")



        self.Label1 = Label(self.root)
        self.Label1.place(relx=0.05, rely=0.02, height=41, width=354)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#895f16")
        self.Label1.configure(relief=SUNKEN)
        self.Label1.configure(text='''Account Editor''')
        self.Label1.configure(width=354)

        self.Label2 = Label(self.root)
        self.Label2.place(relx=0.08, rely=0.13, height=41, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(relief=GROOVE)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=84)

        self.Entry1 = Entry(self.root)
        self.Entry1.place(relx=0.3, rely=0.13,height=40, relwidth=0.61)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=244)

        self.Label2_1 = Label(self.root)
        self.Label2_1.place(relx=0.08, rely=0.24, height=41, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(relief=GROOVE)
        self.Label2_1.configure(text='''Age''')
        self.Label2_1.configure(width=84)

        self.Spinbox1 = Spinbox(self.root, from_=1.0, to=200.0)
        self.Spinbox1.place(relx=0.3, rely=0.24, relheight=0.09, relwidth=0.21)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font=font11)
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="1.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(to="200.0")
        self.Spinbox1.configure(width=85)

        self.Label3 = Label(self.root)
        self.Label3.place(relx=0.08, rely=0.36, height=41, width=334)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(relief=GROOVE)
        self.Label3.configure(text='''Interests''')
        self.Label3.configure(width=334)

        self.Checkbutton1 = Checkbutton(self.root)
        self.Checkbutton1.place(relx=0.08, rely=0.47, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font=font12)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(relief=RIDGE)
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(width=211)

        self.Checkbutton1_5 = Checkbutton(self.root)
        self.Checkbutton1_5.place(relx=0.08, rely=0.53, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_5.configure(activebackground="#d9d9d9")
        self.Checkbutton1_5.configure(activeforeground="#000000")
        self.Checkbutton1_5.configure(background="#d9d9d9")
        self.Checkbutton1_5.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_5.configure(font=font12)
        self.Checkbutton1_5.configure(foreground="#000000")
        self.Checkbutton1_5.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_5.configure(highlightcolor="black")
        self.Checkbutton1_5.configure(justify=LEFT)
        self.Checkbutton1_5.configure(relief=RIDGE)
        self.Checkbutton1_5.configure(text='''Check''')

        self.Checkbutton1_6 = Checkbutton(self.root)
        self.Checkbutton1_6.place(relx=0.08, rely=0.6, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_6.configure(activebackground="#d9d9d9")
        self.Checkbutton1_6.configure(activeforeground="#000000")
        self.Checkbutton1_6.configure(background="#d9d9d9")
        self.Checkbutton1_6.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_6.configure(font=font12)
        self.Checkbutton1_6.configure(foreground="#000000")
        self.Checkbutton1_6.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_6.configure(highlightcolor="black")
        self.Checkbutton1_6.configure(justify=LEFT)
        self.Checkbutton1_6.configure(relief=RIDGE)
        self.Checkbutton1_6.configure(text='''Check''')

        self.Checkbutton1_7 = Checkbutton(self.root)
        self.Checkbutton1_7.place(relx=0.08, rely=0.67, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_7.configure(activebackground="#d9d9d9")
        self.Checkbutton1_7.configure(activeforeground="#000000")
        self.Checkbutton1_7.configure(background="#d9d9d9")
        self.Checkbutton1_7.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_7.configure(font=font12)
        self.Checkbutton1_7.configure(foreground="#000000")
        self.Checkbutton1_7.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_7.configure(highlightcolor="black")
        self.Checkbutton1_7.configure(justify=LEFT)
        self.Checkbutton1_7.configure(relief=RIDGE)
        self.Checkbutton1_7.configure(text='''Check''')

        self.Checkbutton1_8 = Checkbutton(self.root)
        self.Checkbutton1_8.place(relx=0.08, rely=0.73, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_8.configure(activebackground="#d9d9d9")
        self.Checkbutton1_8.configure(activeforeground="#000000")
        self.Checkbutton1_8.configure(background="#d9d9d9")
        self.Checkbutton1_8.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_8.configure(font=font12)
        self.Checkbutton1_8.configure(foreground="#000000")
        self.Checkbutton1_8.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_8.configure(highlightcolor="black")
        self.Checkbutton1_8.configure(justify=LEFT)
        self.Checkbutton1_8.configure(relief=RIDGE)
        self.Checkbutton1_8.configure(text='''Check''')

        self.Checkbutton1_9 = Checkbutton(self.root)
        self.Checkbutton1_9.place(relx=0.08, rely=0.8, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_9.configure(activebackground="#d9d9d9")
        self.Checkbutton1_9.configure(activeforeground="#000000")
        self.Checkbutton1_9.configure(background="#d9d9d9")
        self.Checkbutton1_9.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_9.configure(font=font12)
        self.Checkbutton1_9.configure(foreground="#000000")
        self.Checkbutton1_9.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_9.configure(highlightcolor="black")
        self.Checkbutton1_9.configure(justify=LEFT)
        self.Checkbutton1_9.configure(relief=RIDGE)
        self.Checkbutton1_9.configure(text='''Check''')

        self.Checkbutton1_10 = Checkbutton(self.root)
        self.Checkbutton1_10.place(relx=0.08, rely=0.87, relheight=0.06
                , relwidth=0.53)
        self.Checkbutton1_10.configure(activebackground="#d9d9d9")
        self.Checkbutton1_10.configure(activeforeground="#000000")
        self.Checkbutton1_10.configure(background="#d9d9d9")
        self.Checkbutton1_10.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_10.configure(font=font12)
        self.Checkbutton1_10.configure(foreground="#000000")
        self.Checkbutton1_10.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_10.configure(highlightcolor="black")
        self.Checkbutton1_10.configure(justify=LEFT)
        self.Checkbutton1_10.configure(relief=RIDGE)
        self.Checkbutton1_10.configure(text='''Check''')

        self.Button1 = Button(self.root)
        self.Button1.place(relx=0.7, rely=0.56, height=64, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#00e808")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''DONE''')
        self.Button1.configure(width=87)
        
        self.root.grab_set()










