#"input no of person and check that whom is younger,adult,middel age,senior citizen and after that count how many no of all"


# p=int(input("input how many person:"))
# count1=0
# count2=0
# count3=0
# count4=0
# for i in range(1,p+1):
#     a=int(input("enter the age:"))
#     if a<18:
#         count1+=1
#         print("younger")

#     elif 18<=a<=25:
#         count2+=1
#         print("adult ")

#     elif 25<a<65:
#         count3+=1
#         print("middle age")
    
#     elif(a>=65):
#         count4+=1
#         print("senior citizen")
# print("younger=",count1)
# print("adult=",count2)
# print("middle age=",count3)
# print("senior citizen=",count4)
        

#find the even and odd and ask the user do you want to conti. yes or no

# count1=0
# count2=0
# count3=0
# v=True
# while v:
#     n=int(input("enter the no to find even or odd:"))
#     count1+=1
#     if n%2==0:
#         count2+=1
#         print("even")
#         s=str(input("Do you want to continue y or n:"))
#         if s=="y" or s=="Y":
#             v=True
#         elif s=="n" or s=="N":
#             v=False
#         else:
#             v=False
#     elif n%2==1:
#         count3+=1
#         print("odd")
#         s=input("Do you want to continue y or n:")
#         if s=="y" or s=="Y":
#             v=True
#         elif s=="n" or s=="N":
#             v=False
#         else:
#             v=False
# print("total no:",count1)
# print("even no:",count2)
# print("odd no:",count3)


#voting task
# count1=0
# count2=0
# p=int(input("enter the no of people:"))
# for i in range(1,p+1):
#     age=int(input("enter the age:"))
#     if age==0:
#         print("not valid choice of age")
#     elif age<18:
#         count1+=1
#         print("not eligible for voting")
#     elif age>=18:
#         count2+=1
#         print("eligible to voting")
# print("not eligible:",count1)
# print("eligible is:",count2)