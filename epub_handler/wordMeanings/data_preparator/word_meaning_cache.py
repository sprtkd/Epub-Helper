import pickle
import re
from PyDictionary import PyDictionary

def score_loader():
    with open('data.pickle', 'rb') as handle:
        score_dict = pickle.load(handle)
    return score_dict


dictionary=PyDictionary()

def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning

def meaning_cache_loader():
        with open('minimean.pickle', 'rb') as handle:
            miniMean_dict = pickle.load(handle)
        return miniMean_dict

def textclean(text):
    text = re.sub(' +', ' ',text)
    text = re.sub('\t', ' ',text)
    text = re.sub('\n', ' ',text)
    text=text.strip()
    return text
  

def minitiarize_meaning(text):
    text = re.sub(r'\ba\b', '', text)
    text = re.sub(r'\ban\b', '', text)
    text = re.sub(r'\bthe\b', '', text)
    text = re.sub(r' and ', ',', text)
    text = re.sub(r' or ', '/', text)
    text = text.split(';')[0]
    text = text.split('.')[0]
    text = textclean(text)
    return text
    

def mini_meaning(word):
    meaning=get_meaning(word)
    if meaning!=None:
        for pos,mvals in list(meaning.items()):
            for mval in mvals:
                string_list = minitiarize_meaning(mval)
                return string_list
    else:
        string_list='Unknown'
        return string_list



def build_cache():
    meaning_dict = meaning_cache_loader()
    score_dict = score_loader()
    i=1
    j=len(meaning_dict)-3
    for key in sorted(score_dict.keys()):
        if i>=j:
            meaning_dict[key]=mini_meaning(key)
            if j%10==0:
                print(j)
                with open('minimean.pickle', 'wb') as handle:
                    pickle.dump(meaning_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
            j+=1
        i+=1
    with open('minimean.pickle', 'wb') as handle:
        pickle.dump(meaning_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
build_cache()