
import math
import keyword
import random
from typing import MutableSequence

# Public key is <G,q,g,h>
# Private Key is <G,q,g,x>

def HCF(num1,num2):
    if num1<num2:
        return HCF(num2,num1)
    elif num1 % num2 == 0:
        return num2
    else:
        return HCF(num2,num1%num2)
def coprime(num1,num2):
    return HCF(num1,num2)==1

def EulerGroup(x):
    phiGroup=[]
    if x == 1:
        return 1
    else:
        for a in range(1,x):
            if coprime(x,a):
                phiGroup.append(a)
    print (phiGroup)
    return phiGroup


def numInGroup(x): # function to define the elements in quadratic group
    GList=[]
    for i in range (1,x):
        res = pow(i,2) % x
        GList.append(res)
    GList.sort()
    #print(GList)
    newGlist= list((dict.fromkeys(GList))) # To remove duplplicates from the list
    #print (newGlist)
    return newGlist

#def publicKey(): # generating Public Key



def message(modValue):
    #obj= elGamal()
    print("Please Enter the vale for M as an integer")
    m = int(input())
    m+=1

    mStar = pow(m,2)% modValue
    print(mStar)
    return mStar
        
   
    
def encryption(encValue,encOption):
        
    val = random.choice(encOption)
    print(val)

    

def main():
    print("*************************** Simple Program for EL-GAMAL Algorithm ***************************")
    print("Enter the value for q :")
    q = int(input())
    #print("You have chosen "+str(q))
    
    p = (2*q) + 1

    print("The value of P is "+ str(p)) 
    encList = numInGroup(p) # To chose a randome y from the list
    print(encList)
    encVal=message(p)
    print("Lets Encrypt a the message")
    encryption(encVal,encList)
    
    if __name__ == '__main__':
        main()





        








