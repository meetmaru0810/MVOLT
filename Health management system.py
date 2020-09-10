import datetime
def gettime():
    return datetime.datetime.now()

def log(k):
    c=int(input("1.exercise and 2.food:"))
    if c==1:
        if k==1:
            value=str(input("enter the value:"))
            with open("meet_logex.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
                print("written successful")
        elif k==2:
            value = str(input("enter the value:"))
            with open("zenith_logex.txt","a") as f:
                f.write(str(gettime())+ ":"+ value+"\n")
                print("written successful")

        elif k== 3:
            value=str(input("enter the value"))
            with open("prince_logex.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
                print("written successful")
    elif c==2:
        if k==1:
            value=str(input("enter the value:"))
            with open("meet_logfood.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
                print("written successful")
        elif k==2:
            value = str(input("enter the value:"))
            with open("zenith_logfood.txt","a") as f:
                f.write(str(gettime())+ ":"+ value+"\n")
                print("written successful")

        elif k== 3:
            value=str(input("enter the value"))
            with open("prince_logfood.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
                print("written successful")


def retrive(k):
    c = int(input("1.exercise and 2.food:"))
    if c==1:
        if k == 1:
            f = open("meet_logex.txt")
            b = f.read()
            print(b)
        elif k == 2:
            f = open("zenith_logex.txt")
            b = f.read()
            print(b)
        elif k == 3:
            f = open("prince_logex.txt")
            b = f.read()
            print(b)
    elif c==2:
        if k == 1:
            f = open("meet_logfood.txt")
            b = f.read()
            print(b)
        elif k == 2:
            f = open("zenith_logfood.txt")
            b = f.read()
            print(b)
        elif k == 3:
            f = open("prince_logfood.txt")
            b = f.read()
            print(b)







n=int(input("1 meet 2 zenith 3 prince:"))
a=int(input("enter 1 log 2 retrive:"))

if a==1:
    log(n)
elif a==2:
    retrive(n)