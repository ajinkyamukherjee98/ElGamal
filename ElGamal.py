
import math
import keyword



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
        newGlist= list((dict.fromkeys(GList))) # To remove duplplicates from the list
        print (newGlist)
    
    def message():
        print("Please Enter the ")

        

    numInGroup(p)







