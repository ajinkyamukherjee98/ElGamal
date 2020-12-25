
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


# Function to Calculate Prime Factors of a number and store them in a list
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


# Function to define the elements in a quadratic group
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

def message(modValue):
    #obj= elGamal()
    print("Please Enter the vale for M as an integer")
    m = int(input())
    m+=1

    mStar = pow(m,2)% modValue
    print(mStar)
    return mStar
        
def yGenerator(q):#
    y = random.choice(EulerGroup(q)) # To get a random y from Z*q
    return y

def privateKey(q):
    x = random.choice(EulerGroup(q)) # To get a random x from Z*q
    return x
# Function to generate a Public Key <G,q,g,h>
def publicKey(p,q): # generating Public Key
    g = random.choice(numInGroup(p)) # To get a random g from G(p).
    power = privateKey(q) # Get the private key x to calculate H
    # calcuate h
    h = modExponent(g,power,p)

# Function to Generate Cipher Text 1
def cipherText1(g,y,p):
    CT1 = modExponent(g,y,p)
    #print("CipherText 1 is "+str(CT1))
    return CT1


# Function to Generate Cipher Text 2
def cipherText2(h,y,m,p):
    Pt1= modExponent(h,y,p)
    Pt2 = modExponent(m,1,p)
    CT2 = modExponent(Pt1*Pt2,1,p)
    #print("CipherText 2 is "+ str(CT2)) 
    return CT2

# Function to encrypt the message and display ciphertexts
def encryption(g,y,h,p):
    print("Genertating Cipher Text 1")
    c1= cipherText1(g,y,p)
    m=message(p)
    print("Genertating Cipher Text 2")
    c2 = cipherText2(h,y,m,p)

    print("Cipher Text 1 is: "+ str(c1))
    print("Cipher Text 2 is: "+ str(c2))
   
# Main Function which would act as the Driver Code
def main():
    print("*************************** Simple Program for EL-GAMAL Algorithm(Quadratic residue) ***************************")
    print("Enter the value for q :")
    q = int(input())
    #print("You have chosen "+str(q))
    p = (2*q) + 1
    
    
if __name__ == '__main__':
    main()





        








