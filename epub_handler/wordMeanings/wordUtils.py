###Suprotik Dey @bluezeal

#dictionary
#normalized lemma of words
#validity of words
#word_context_classifier

from PyDictionary import PyDictionary
import pickle
import re

dictionary=PyDictionary()

#--------------meanings--------------
def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning
        

def meaning_to_string(meaning):
    string_list=''
    i=1
    if meaning!=None:
        for pos,mvals in list(meaning.items()):
            string_list = string_list + '(' + pos +'):\n'
            for mval in mvals:
                string_list = string_list + str(i) + ': ' + mval + '\n'
                i=i+1
    else:
        string_list='Unknown\n'
        
    return string_list

class MiniMeaningCache:
    def __init__(self,lengthstr):
        self.meaning_cache_loader()
        self.lengthstr=lengthstr
    def meaning_cache_loader(self):
        with open('minimean.pickle', 'rb') as handle:
            self.miniMean_dict = pickle.load(handle)
    def get_miniMeaning(self,word):
        if word in self.miniMean_dict:
            minimeanTemp = self.miniMean_dict[word]
            if minimeanTemp==None:
                minimean='Unknown'
            else:
                minimean = minimeanTemp[:self.lengthstr] + (minimeanTemp[self.lengthstr:] and '..')
        else:
            minimean='Unknown'
            
        return minimean
        
    

#--------------meanings--------------
            

def tokenize_text(txt):
    tok_text = re.split('(\W+)',txt)
    return tok_text

class WordProcesser:
    def __init__(self,text):
        self.this_page_text = tokenize_text(text)
        self.curr_word_number=0
        self.total=len(self.this_page_text)
    
    def get_next_word(self):
        while self.curr_word_number<self.total:
            curr_word = self.this_page_text[self.curr_word_number]
            self.curr_word_number=self.curr_word_number+1
            if curr_word=='':
                return '',False
            return curr_word, word_score_classifier(curr_word)
        
        return None,False
        
    
#---------------word checking and fetch------------------------
    

#----------------score classifier----------------------
    
def get_age_from_account():
    return 15

def score_loader():
    with open('data.pickle', 'rb') as handle:
        score_dict = pickle.load(handle)
    return score_dict
	
score_dict = score_loader()
class_dict_thresh = {'1to8':'uncle','9to16':'agreement','17to22':'acceleration','23toRest':'economics'}
curr_age = get_age_from_account()


def word_score_classifier(word):
    if curr_age <=8:
        thresh_score = score_dict[class_dict_thresh['1to8']]
    elif curr_age <=16:
        thresh_score = score_dict[class_dict_thresh['9to16']]
    elif curr_age <=22:
        thresh_score = score_dict[class_dict_thresh['17to22']]
    else:
        thresh_score = score_dict[class_dict_thresh['23toRest']]
    
    n_word = word.lower()
    if n_word in score_dict:
        if score_dict[n_word] > thresh_score:
            return True   
    return False
    
    
#----------------score classifier----------------------

#---------------word context---------------------

#TODO
def word_context_classify(word):
    pass
#---------------word context---------------------