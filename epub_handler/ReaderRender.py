from tkinter.font import Font
from tkinter import *
from wordMeanings.wordUtils import WordProcesser
from ReaderRender_support import *


class TextWithMeaningRender:
    def __init__(self,textbox,paragraph,defaultFont,hardFont,meaningFont,maxChars,miniMeaningCache):
        self.paragraph=paragraph
        self.miniMeaningCache=miniMeaningCache
        self.textbox=textbox
        self.defaultFont = Font(self.textbox,defaultFont)
        self.meaningFont= Font(self.textbox,meaningFont)
        self.hardFont= Font(self.textbox,hardFont)
        self.textbox.configure(font=self.defaultFont)
        self.textbox.tag_config("meaning", font=self.meaningFont)
        self.textbox.tag_config("hard", font=self.hardFont)
        self.textbox.tag_bind("hard", "<Button-1>", hardWordCallback)
        self.maxTextPixels=calcLinePixels(maxChars,self.defaultFont)
        self.parseTextToMeanings()
        self.finalOrder=None
        self.calcPageLayout()
        
    def parseTextToMeanings(self):
        text_words = WordProcesser(self.paragraph)
        self.parsedParagraph=[]
        self.parsedMeanings=[]
        while True:
            word,isHard = text_words.get_next_word()
            if word==None:
                break
            self.parsedParagraph.append(word.replace('\n',' '))
            if isHard:
                mm=self.miniMeaningCache.get_miniMeaning(word.lower())
                self.parsedMeanings.append(mm+'  ')
            else:
                self.parsedMeanings.append('')
                
                
    def renderLine(self,starti,endi):
        meaning_segment = ''.join( self.parsedMeanings[starti:endi] )
        self.textbox.insert(END, meaning_segment+'\n',"meaning")
        for itera in range(starti,endi):
            if isblank(self.parsedMeanings[itera]):
                self.textbox.insert(END, self.parsedParagraph[itera],"hard")
            else:
                self.textbox.insert(END, self.parsedParagraph[itera])
        self.textbox.insert(END, '\n')
    
    def renderPage(self):
        self.textbox.config(state=NORMAL)
        self.textbox.delete('1.0', END)
        if self.finalOrder==None:
            print('Page Not Ready')
            return
        for i in range(len(self.finalOrder)-1):
            self.renderLine(self.finalOrder[i],self.finalOrder[i+1])
        self.textbox.config(state=DISABLED)
        
    def calcPageLayout(self):
        segment_len = 0
        if(len(self.parsedParagraph)!=len(self.parsedMeanings)):
            raise Exception("Parse mismatch!")
        line_start = [0, len(self.parsedParagraph)]       
        for i in range(len(self.parsedParagraph)):
            m_len = self.meaningFont.measure(self.parsedMeanings[i])
            t_len = self.defaultFont.measure(self.parsedParagraph[i])
        
            if m_len > t_len:
                self.parsedParagraph[i] = spacer(self.parsedParagraph[i],int(round((m_len - t_len)/self.defaultFont.measure(' '))))
            elif m_len < t_len:
                self.parsedMeanings[i] = spacer(self.parsedMeanings[i],int(round((t_len - m_len)/self.meaningFont.measure(' '))))
            segment_len += max(t_len, m_len) 
            if segment_len> self.maxTextPixels:
                segment_len = 0
                line_start.insert(-1,i)
            
        self.finalOrder = line_start

