
import math
import keyword
import random
from typing import MutableSequence



class elGamal():

    print("*************************** Simple Program for EL-GAMAL Algorithm ***************************")
    print("Enter the value for q :")
    q = int(input())
    #print("You have chosen "+str(q))
    
    p = (2*q) + 1

    print("The value of P is "+ str(p))
    
    
    def numInGroup(x):
        GList=[]
        for i in range (1,x):
            res = pow(i,2) % x
            GList.append(res)
        GList.sort()
        #print(GList)
        newGlist= list((dict.fromkeys(GList))) # To remove duplplicates from the list
        #print (newGlist)
        return newGlist

    encList = numInGroup(p) # To chose a randome y from the list
    print(encList)
    def message(modValue):
        #obj= elGamal()
        print("Please Enter the vale for M as an integer")
        m = int(input())
        m+=1

        mStar = pow(m,2)% modValue
        print(mStar)
        return mStar
    encVal=message(p)
    
    def encryption(encValue,encOption):
        
        val = random.choice(encOption)
        print(val)

    print("Lets Encrypt a the message")
    encryption(encVal,encList)
        





        








