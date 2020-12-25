
import math
import keyword
import random

#from typing import MutableSequence

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

def EulerGroup(x): # TO get a list of numbers in Z*q
    phiGroup=[]
    if x == 1:
        return 1
    else:
        for a in range(1,x):
            if coprime(x,a):
                phiGroup.append(a)
    #print (phiGroup)
    return phiGroup
def EulerTot(num):
    return len(EulerGroup(num))

def primefactor(n):
    factorlist=[]
    while(n%2)==0:
        factorlist.append(2)
        n=n/2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            factorlist.append(i)
            n=n/i

    if n>2:
        factorlist.append(n)

    return factorlist


# Function to do Modulo arithmetic as per the cryptographic rules
# Modulo Exponnentitaion 
def modExponent(num1,num2,num3): 
    # we know that Eulers Totient is always even
    # we also know the group proeprty using Chinese remainder Theorem that any number raised to the number of objects in the group
    # will give us 1.
    val = num2 - EulerTot(num3)
    
    #result = 0
    if val > 0:
        for i in range(0,len(primefactor(num2))):
            power = primefactor(val)
            num1= pow(num1,power[i]) % num3
    else:
        for y in range(0,len(primefactor(num2))):
            power = primefactor(num2)
            num1 = pow(num1,power[y]) % num3
    return num1


        
    


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

def publicKey(p,q): # generating Public Key
    g = random.choice(numInGroup(p)) # To get a random g from G(p).
    x = random.choice(EulerGroup(q)) # To get a random x from Z*q

    # calcuate h





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
    print("*************************** Simple Program for EL-GAMAL Algorithm(Quadratic residue) ***************************")
    print("Enter the value for q :")
    q = int(input())
    #print("You have chosen "+str(q))
    
    p = (2*q) + 1
    ans = modExponent(4,55,167)
    print(ans)
    
if __name__ == '__main__':
    main()





        








