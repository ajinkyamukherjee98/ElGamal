
import math
import keyword
import random
from types import *
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

# Function to check if number is coPrime or not
def coprime(num1,num2):
    return HCF(num1,num2)==1

# Function to check if a given number is a natural number or not
def natural(num):
    if num>0 and type(num) == int:
        return 1
    else:
        return 0
    
# Function to get a list of number in Z*q
def EulerGroup(x):
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
    if val >= 0:
        for i in range(0,len(primefactor(num2))):
            power = primefactor(val)
            num1= pow(num1,power[i]) % num3
    else:
        for y in range(0,len(primefactor(num2))):
            power = primefactor(num2)
            num1 = pow(num1,power[y]) % num3
            #print(power)
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

# Function to generate Multiplicative Modulo inverse of a number
# num1 * itr = 1 mod num2
# Return Itr which is multiplicative Inverse of num1 while dividing with num2 resulting in 1 as reminader
def multInverse(num1,num2):
    for itr in range(1,num2):
        if((num1*itr)%num2) == 1:
            return itr
        else:
            continue

# Function to convert Original Message from M to M*
def message(modValue):
    #obj= elGamal()
    print("Please Enter the vale for M as an integer")
    m = int(input())
    m+=1

    mStar = pow(m,2)% modValue
    print("The vaue for m* is: ")
    print(mStar)
    return mStar

# Function to choose y at random       
def yGenerator(q):#
    y = random.choice(EulerGroup(q)) # To get a random y from Z*q
    print("Y chosen is: "+str(y))
    return y

# Function to choose randome Key x  
def privateKey(q):
    x = random.choice(EulerGroup(q)) # To get a random x from Z*q
    print("X chosen is: ",str(x))
    return x

# Function to choose g 
def gGenerator(p):
    g = random.choice(numInGroup(p)) # To get a random g from G(p).
    print("The g chosen is: "+str(g))
    return g
# Function to generate a Public Key <G,q,g,h>

# Function to generate h
def publicKey(p,q,power,g): # generating Public Key
    # calcuate h
    h = modExponent(g,power,p)
    print("The value of h is: "+str(h))
    return h 

# Function to Generate Cipher Text 1
def cipherText1(g,y,p):
    # Cipher Text 1 is g**y mod p
    CT1 = modExponent(g,y,p)

    #print("CipherText 1 is "+str(CT1))
    return CT1


# Function to Generate Cipher Text 2
def cipherText2(h,y,m,p):
    # Cipher Text 2 is (h**y *mStar)mod p
    # I have split the Cipher Text Calculations into two parts
    # Part 1 is calcuting h**y mod p
    Pt1= modExponent(h,y,p)
    
    #Part 2 is mstar % p
    Pt2 = m % p
    
    # Finally I calculate  the entire thing properly
    CT2 = (Pt1*Pt2)%p
    #CT2 = modExponent(Pt1*Pt2,1,p)
    #print("CipherText 2 is "+ str(CT2)) 
    return CT2

# Function to encrypt the message and display ciphertexts
def encryption(g,y,h,p,m,x):

    print("Genertating Cipher Text 1")
    #Calculate C1
    c1= cipherText1(g,y,p)
    print("Cipher Text 1 is: "+str(c1))

    # Calculate C2
    c2 = cipherText2(h,y,m,p)

    print("Cipher Text 2 is: "+ str(c2))

    print("Decrypting the Message")
    decryption(c1,c2,x,p)


# Function to Decrypt the cipher texts to give us 
def decryption(c1,c2,x,p):

    # To decrypt the cipher text to get the original message is 
    # c2/c1**x = h**y.m/g**xy => g**xy*m/g**xy = m
    # denom = c1**x mod p
    # numerator * Inverse(denmo) = decryoted message

    denom = modExponent(c1,x,p)
    print("C1**x is: "+str(denom))
    
    # Calculating Inverse of Denominator
    # Inverse of Denominator is denmo * inverse of Denmo = 1 mod p
    invDenmo  = multInverse(denom,p)
    print("Inverse of C1**x is: "+str(invDenmo))
    prod = c2*invDenmo
    mStar = prod % p
    print("Hence mStar is: "+str(mStar))

    
        
  
# Main Function which would act as the Driver Code
def main():
    print("*************************** Simple Program for EL-GAMAL Algorithm(Quadratic residue) ***************************")
    print("Enter the value for q :")
    q = int(input())
    #print("You have chosen "+str(q))
    p = (2*q) + 1
    # Step 1 input the message
    m = message(p)
    #cprint(m)
    # Value of G 
    g= gGenerator(p)
    # value of y is 
    y = yGenerator(q)
    # x generator is 
    x = privateKey(q)
    # calculating h
    h = publicKey(p,q,x,g)

    
    encryption(g,y,h,p,m,x)
       
if __name__ == '__main__':
    main()





        








