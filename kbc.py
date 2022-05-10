print("welcome the game :kaun banega crorepati")
Q=[["How many Continents are there ?"],
    ["what is the capital of India ?"],
    ["what is course are you doing in NG"]]
opt=[["Seven","Eight","Four","Three"],
         ["Mumbai","Kolkatta","Delhi","Banglore"],
         ["Toriusm","Software Engineering","B.Tech","Agriculture"]]
Answers=["seven","Delhi","software engineering"]

i=0
c=0
while i<len(Q):
    print(Q[i])
    j=0
    while(c<len(opt)):
        while(j<=len(opt)):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    i+=1
    lifeline=input("Do u want lifeline")
    if(lifeline=="yes"):
        print("1 Seven"   "4  three" )
        print("select ur answer")
        options =input("if answer")
        if options =="1":
            print("ur answer is correct")
            print("Congralations")
            print("ur next questions is :")
        else :
                print("your answer is wrong")
        break
    else :
        print("select ur answer")
        options =input("if answer")
        if options =="1":
            print("ur answer is correct")
            print("Congralations")
            print("ur next questions is :")
        else :
            print("wrong answer")
        break
c=0
while i<len(Q):
    print(Q[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    i+=1
    lifeline=input("Do u want lifeline")
    if(lifeline=="yes"):
        print("1 Mumbai"  "3 Delhi" )
        print("select your options")
        ans=input("select opt")
        if ans=="3":
            print("ur answer is correct")
            print("congralations")
            print("ur next questions is :")
        else :
            print("wrong answer")
        break
    else :
        print("select ur answer")
        ans=input("select answer")
        if ans=="3":
            print("ur answer is correct")
            print("good")
            print("ur next questions is :")
        else :
                print("wrong answer")
    break
c=0
while i<len(Q):
    print(Q[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c+=1
            print(c,opt[i][j])
            j+=1
    i+=1
    lifeline=input("Do u want lifeline")
    if(lifeline=="yes"):
        print("2 software engineering " "4 Agriculture" )
        print("select ur answer")
        ans2=input("select answer")
        if ans2=="2":
            print("ur answer is correct")
            print("good")
            print("ur next questions is :")
        else  :
            print("wrong answer")
    else :
        print("select your options")
        option2=input("select opt")
        if option2=="2":
            print("ur answer is correct")
            print("good")
            print("ur next questions is :") 
        else :
            print("wrong answer")
            break
            

