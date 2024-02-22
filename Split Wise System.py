#DESIGN SPLIT WISE with three USERS
class Users:
  def __init__(self,id,name,bal,u1owe,u2owe,u3owe):
    self.id=id;
    self.name=name
    self.bal=bal
    self.u1owe=u1owe
    self.u2owe=u2owe
    self.u3owe=u3owe
  def show_bal(self):
    return (self.name,self.id,self.bal)
  
  def exact(self,arr):
    cashSpent=arr[1]
    whoSpent=arr[0]
    amongHowMany=arr[2]
    amongusers=[]
    index=3
    for i in range(amongHowMany):
      amongusers.append(arr[index])
      index+=1
    # if user 1 paid and to check if previously user 1 owes any amount to any other user
    if "u1"==arr[0]: 
      if "u2" in amongusers and self.u1owe[1]>0:
        if self.u1owe[1]>arr[6]:
          self.u1owe[1]-=arr[6]
        else:
          rem=abs(arr[6]-self.u1owe[1])
          self.u1owe[1]=0
          self.u2owe[0]=rem
      elif "u2" in amongusers and self.u1owe[1]==0:
        self.u2owe[0]+=arr[6]
      
      if "u3" in amongusers and self.u2owe[1]>0:
        if self.u2owe[1]>arr[7]:
          self.u2owe[1]-=arr[7]
        else:
          rem=abs(arr[7]-self.u2owe[1])
          self.u2owe[1]=0
          self.u3owe[0]=rem
      elif "u3" in amongusers and self.u1owe[2]==0:
        self.u3owe[0]+=arr[7]
   # if user 2 paid and to check if previously user 2 owes any amount to any other user     
    if "u2"==arr[0]:
      if "u1" in amongusers and self.u2owe[0]>0:
        if self.u2owe[0]>arr[6]:
          self.u2owe[0]-=arr[6]
        else:
          rem=abs(arr[6]-self.u2owe[0])
          self.u2owe[0]=0
          self.u1owe[2]=rem
      elif "u1" in amongusers and self.u2owe[0]==0:
        self.u1owe[1]+=arr[6]
      
      if "u3" in amongusers and self.u2owe[2]>0:
        if self.u2owe[2]>arr[7]:
          self.u2owe[2]-=arr[7]
        else:
          rem=abs(arr[7]-self.u2owe[2])
          self.u2owe[2]=0
          self.u3owe[1]=rem
      elif "u3" in amongusers and self.u2owe[2]==0:
        self.u3owe[1]+=arr[7]  
    
     # if user 3 paid and to check if user 3 previously owes any amount to other users    
    if  "u3"==arr[0]:
      if "u1" in amongusers and self.u3owe[0]>0:
        if self.u3owe[0]>arr[6]:
          self.u3owe[0]-=arr[6]
        else:
          rem=abs(arr[6]-self.u3owe[0])
          self.u3owe[0]=0
          self.u1owe[2]=rem
      elif "u1" in amongusers and self.u3owe[0]==0:
        self.u1owe[2]+=arr[6]
      
      if "u2" in amongusers and self.u3owe[1]>0:
        if self.u3owe[1]>arr[7]:
          self.u3owe[1]-=arr[7]
        else:
          rem=abs(arr[7]-self.u3owe[1])
          self.u3owe[1]=0
          self.u2owe[2]=rem
      elif "u2" in amongusers and self.u3owe[1]==0:
        self.u2owe[2]+=arr[7]      
      
      
      
      
    
  def equal(self,arr):
    cashSpent=arr[1]
    whoSpent=arr[0]
    amongHowMany=arr[2]
    amongusers=[]
    index=3
    for i in range(amongHowMany):
      amongusers.append(arr[index])
      index+=1
    typePayment=arr[len(arr)-1]
    moneySpentperUser=cashSpent/amongHowMany
    # if user 1 paid and to check if previously user 1 owes any amount to any other user
    if "u1" in amongusers and "u1"==arr[0]:
      if "u2" in amongusers and self.u1owe[1]>0:
        if self.u1owe[1]>moneySpentperUser:
          self.u1owe[1]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u1owe[1])
          self.u1owe[1]=0
          self.u2owe[0]=rem
      elif "u2" in amongusers and self.u1owe[1]==0:
        self.u2owe[0]+=moneySpentperUser
      
      if "u3" in amongusers and self.u2owe[1]>0:
        if self.u2owe[1]>moneySpentperUser:
          self.u2owe[1]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u2owe[1])
          self.u2owe[1]=0
          self.u3owe[0]=rem
      elif "u3" in amongusers and self.u1owe[2]==0:
        self.u3owe[0]+=moneySpentperUser
    # if user 2 paid and to check if previously user 2 owes any amount to any other user  
    elif "u2" in amongusers and "u2"==arr[0]:
      if "u1" in amongusers and self.u2owe[0]>0:
        if self.u2owe[0]>moneySpentperUser:
          self.u2owe[0]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u2owe[0])
          self.u2owe[0]=0
          self.u1owe[1]=rem
      elif "u1" in amongusers and self.u2owe[0]==0:
        self.u1owe[1]+=moneySpentperUser
      
      if "u3" in amongusers and self.u2owe[2]>0:
        if self.u2owe[2]>moneySpentperUser:
          self.u2owe[2]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u2owe[2])
          self.u2owe[2]=0
          self.u3owe[1]=rem
      elif "u3" in amongusers and self.u2owe[2]==0:
        self.u3owe[1]+=moneySpentperUser
    # if user 3 paid and to check if user 3 previously owes any amount to other users    
    elif "u3" in amongusers and "u3"==arr[0]:
      if "u1" in amongusers and self.u3owe[0]>0:
        if self.u3owe[0]>moneySpentperUser:
          self.u3owe[0]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u3owe[0])
          self.u3owe[0]=0
          self.u1owe[2]=rem
      elif "u1" in amongusers and self.u3owe[0]==0:
        self.u1owe[2]+=moneySpentperUser
      
      if "u2" in amongusers and self.u3owe[1]>0:
        if self.u3owe[1]>moneySpentperUser:
          self.u3owe[1]-=moneySpentperUser
        else:
          rem=abs(moneySpentperUser-self.u3owe[1])
          self.u3owe[1]=0
          self.u2owe[2]=rem
      elif "u3" in amongusers and self.u3owe[1]==0:
        self.u2owe[2]+=moneySpentperUser    
    
  def showUserOwe(self,user):
      if(user=="u2"):
        print( self.name[1],"owes", self.name[0] ,self.u2owe[0])
        print(self.name[1],"owes",self.name[2],self.u2owe[2])
      elif(user=="u1"):
        print(self.name[0],"owes ",self.name[1],self.u1owe[1])
        print(self.name[0]," owes",self.name[2],self.u2owe[2])
      elif(user=="u3"):
        print(self.name[2],"owes ",self.name[0],self.u3owe[0])
        print(self.name[2]," owes ",self.name[1],self.u3owe[1])  
            
          
  
  
u1= Users([1000,1001,1002],["Steven","Davis","Devin"],[0,0,0],[0,0,0],[0,0,0],[0,0,0])

u1.equal(["u1",1000,3,"u1", "u2", "u3","EQUAL"])

u1.equal(["u1",1000,3,"u1", "u2", "u3","EQUAL"])

u1.equal(["u2",600,3,"u1", "u2", "u3","EQUAL"])

u1.equal(["u2",9999,3,"u1", "u2", "u3","EQUAL"])

u1.exact(["u1",100, 2, "u2", "u3","EXACT",40,60])
















