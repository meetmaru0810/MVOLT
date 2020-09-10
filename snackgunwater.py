import random

user_point=0
computer_point=0
chanceofservive=10
tie_point=0
list=["s","g","w"]

for i in range(1,11):
    computerinput=random.choice(list)
    userinput=input("snack for, gun for g, water for w:")

    if userinput=="s":
        if  computerinput=="s":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            tie_point+=1
            print("it is tie between com and user")
        elif computerinput=="g":
             chanceofservive-=1
             print("chance of servive",chanceofservive)
             print("computer has won") 
             computer_point += 1
        elif computerinput=="w":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            print("compter won")
            computer_point += 1


    elif userinput=="g":
        if  computerinput=="s":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            print("user won")
            user_point += 1
        elif computerinput=="g":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            tie_point+=1
            print("it is tie between com and user") 
        elif computerinput=="w":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            print("compter won")
            computer_point += 1

    elif userinput=="w":
        if  computerinput=="s":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            print("user won")
            user_point += 1 
        elif computerinput=="g":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            print("user won") 
            user_point += 1
        elif computerinput=="w":
            chanceofservive-=1
            print("chance of servive",chanceofservive)
            tie_point+=1
            print("it is tie between com and user")
            

print("computer system points:",computer_point)
print("user system points:",user_point)
print("tie points are:",tie_point)

if computer_point>user_point:
    print(computer_point)
    print("computer has won the game")
elif user_point>computer_point:
    print("user has won the game")
elif computer_point==user_point:
    print( "tio points are",tie_point)
    print("the match is tie")

    a=input()



        

