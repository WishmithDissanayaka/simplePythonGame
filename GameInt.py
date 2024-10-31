#seperation line
sep=str("___________________________________________________________________________________________________________________________________________________")
#introduction and main interactive user interface
name=str(input("enter your name : "))
print(sep)
print("1.Start".center(125),"\n","2.End".center(122))
print("[TIP - Enter '0000' as an assumption in order to exit]")
UserAns=str(input("Enter '1' to start the game and '2' to exit:"))
if UserAns==("1"):
    print(sep)
    print("Numbers to guess=XXXX","Colour Mapping:".center(225),"\n","1-White,2-Blue,3-Red".center(250),"\n","      4-Yellow,5-Green,6-Purple".center(250))
    print("\n","                                               Hello",name,"Welcome to Gameint!")
    print(sep)

    
#generating random numbers
    import random
    r1=random.randint(1,6)
    r2=random.randint(1,6)
    r3=random.randint(1,6)
    r4=random.randint(1,6)
    RandList=[]
    RandList.append(r1)
    RandList.append(r2)
    RandList.append(r3)
    RandList.append(r4)
    #print(RandList)
#variables for the game's body
    count=1
    score=0
#loop
    while count==1:
        while count<=8:
            print("Attempt number:",count,"                                        Guess:                                                         Score:")
            GuessList = list(input(" Please enter your 4 digit assumption: "))
            while len(GuessList)!=4:
                print("Please enter a 4 digit number")
                GuessList = list(input(" Please enter your 4 digit assumption: "))
            UserList = [int(x) for x in GuessList]
            print("Your guess was:\t\t\t\t\t\t",UserList)
#main if statements
            if UserList[0]>6 and UserList[1]>6 and UserList[2]>6 and UserList[3]>6:
                print("invalid number, type a number in between 1 and 6")
            if len(UserList)!=4:
                print("please enter a 4 digit number")

            if UserList[0]==RandList[0]:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   1")
            elif (UserList[0] in RandList):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   0")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   .")
            if UserList[1]==RandList[1]:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   1")
            elif (UserList[1] in RandList):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   0")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   .")
            if UserList[2]==RandList[2]:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   1")
            elif (UserList[2] in RandList):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   0")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   .")
            if UserList[3]==RandList[3]:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   1")
            elif (UserList[3] in RandList):
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   0")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   .")
            count=count+1
            print(sep)

            if UserList[0]==RandList[0] and UserList[1]==RandList[1] and UserList[2]==RandList[2] and UserList[3]==RandList[3]:
                if count==2:
                    score=100
                elif count==3:
                    score=87
                elif count==4:
                    score=75
                elif count==5:
                    score=60
                elif count==6:
                    score=48
                elif count==7:
                    score=35
                elif count==8:
                    score=23
                elif count==9:
                    score=0
                print("you have won.")
                print("your final score is",score)
                    
                reply=str(input("Do you want to try again (y/n):"))
                if reply==("n"):
                    print("thank you for playing.")
                    quit()  
                else:
                    print(sep)
                    count=1
                    import random
                    r1=random.randint(1,6)
                    r2=random.randint(1,6)
                    r3=random.randint(1,6)
                    r4=random.randint(1,6)
                    RandList=[]
                    RandList.append(r1)
                    RandList.append(r2)
                    RandList.append(r3)
                    RandList.append(r4)
                    #print(RandList)
    
            if UserList[0]==0 and UserList[1]==0 and UserList[2]==0 and UserList[3]==0:
                quit()

            if count==9:
                print("you have run out of attempts")
                reply=str(input("Do you want to try again (y/n):"))
                if reply==("n"):
                    print("thank you for playing.")
                    quit()  
                else:
                    print(sep)
                    count=1
                    import random
                    r1=random.randint(1,6)
                    r2=random.randint(1,6)
                    r3=random.randint(1,6)
                    r4=random.randint(1,6)
                    RandList=[]
                    RandList.append(r1)
                    RandList.append(r2)
                    RandList.append(r3)
                    RandList.append(r4)
                    #print(RandList)
else:
    quit()
    
    
        
 
        
        
        

