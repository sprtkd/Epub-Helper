import pickle

class ReaderAccount:
    def __init__(self):
        try:
            with open('account.pkl', 'rb') as handle:
                self.accName,self.accAge ,self.accInterests = pickle.load(handle)
        except:
            print('No existing Account!')
            self.accName=None
            self.accAge = None
            self.accInterests=None
        self.initDictInterest()
            
     
    def changeAccount(self,name=None,age=None):
        if(name!=None):
            fname = ''.join(x for x in name if x.isalpha())
            self.accName=fname
            
        if(age!=None):
            self.accAge = age
            
    def setInterest(self,classname, boolval):
        if classname in self.accInterests and type(boolval)==bool:
            self.accInterests[classname]=boolval
            
   
    
    def returnAccountDetails(self):
        return self.accName, self.accAge, self.accInterests
    
    def saveAccount(self):
        if self.accName==None or self.accAge == None or self.accInterests==None:
            print("Cannot save, account empty!")
            return
        else:
            with open('account.pkl', 'wb') as handle:
                pickle.dump(self.returnAccountDetails(), handle, protocol=pickle.HIGHEST_PROTOCOL)
            print('account saved')
            
    def returnInterestList(self):
        intList = ['Literature','Science','Arts','Technology','Biology','Astronomy','Basic']
        return intList
            
    def initDictInterest(self):
        #if none, reset
        listIntClasses = self.returnInterestList()
        if self.accInterests==None:
            tempdict={}
            for classInt in listIntClasses:
                tempdict[classInt]=False
            self.accInterests=tempdict
        else:
            flag=False
            #if non empty, check if matches with current set, otherwise build a new one
            if len(self.accInterests)!=len(listIntClasses):
                flag=True
            else:
                for key1 in listIntClasses:
                    if not key1 in self.accInterests:
                        flag=True
                        break
                    
            if flag:
                tempdict={}
                for classInt in listIntClasses:
                    tempdict[classInt]=False
                
                
                for key in self.accInterests:
                    if key in tempdict:
                        tempdict[key] = self.accInterests[key]
                    
                self.accInterests=tempdict
                


#example
                
                
                
account = ReaderAccount()
#account.changeAccount('Suprotik',22)
#account.setInterest('Literature', True)
#account.saveAccount()
print(account.returnAccountDetails())