import pandas as pd
import pickle

def load_raw():
    df_actual = pd.read_csv('AoA.csv',encoding = "ISO-8859-1")
    new_df =df_actual.drop(['Alternative.spelling','Dom_PoS_SUBTLEX','Nletters','Nphon','Lemma_highest_PoS','AoA_Kup','Perc_known',
                 'Perc_known_lem','AoA_Bird_lem','AoA_Bristol_lem','AoA_Cort_lem','AoA_Schock'],axis=1)
    new_df.fillna({'AoA_Kup_lem': 30,'Freq_pm':0}, inplace=True)
    #print("nan",new_df[new_df.isnull().any(axis=1)])
    print('Data loaded')
    new_df.dropna(inplace=True)
    return new_df

#scaler
val=10

def capAtOne(a):
    if(a>val):
        return val
    return a

def ret_scores(row):
    SyllScore = capAtOne(row['Nsyll'] / 15)
    AoA =  val-capAtOne(10/row['AoA_Kup_lem'])
    
    FrequencyScore= val-capAtOne(row['Freq_pm'] / 50000)
    
    score = capAtOne((0.2*SyllScore) + (0.4*AoA) + (0.4*FrequencyScore))
    
    return row['Word'].lower(),score

def process_data():
    new_df = load_raw()
    df_final = pd.DataFrame({'Word':[],'Score':[]})
    print('Processing')
    for index, row in new_df.iterrows():
        w,grpscore = ret_scores(row)
        df_final=df_final.append({'Word':w,'Score':grpscore}, ignore_index=True)
        if(index%1000==0):
            print(index)
            
    return df_final

def save_as_dict(df_actual):
    print('dicting')
    final_dict={}
    for index, row in df_actual.iterrows():
        w = row['Word']
        sc = row['Score']
        if w not in final_dict:
            final_dict[w]=sc
        if(index%1000==0):
            print(index)            
    with open('data.pickle', 'wb') as handle:
        pickle.dump(final_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
pddata = process_data()
save_as_dict(pddata)     