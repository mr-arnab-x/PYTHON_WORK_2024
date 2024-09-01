#--------------------IF----ELIF-----ELSE----------------------------
name=input("My name is: ")
age=int(input("My age is: "))

if(age==18):
    print(name,"is  able to vote.")
elif(age>18):
    print(name,"is able to vote.")
else:
    print(name,"is not able to vote.") 

#---------- TRY TO NOT USE IN CODE ---------------------

age=int(input("age : "))   

vote=("no","yes")[age>=18]   #--------TERNARY_OPERATORS---------------

print(vote)


#---------------------------------------------------------------------------------------------------------------------------------------------------

# age=int(input("enter your age : "))
 
# if age>=18:
#      if(age>80):
#           print("no need to go the vote camp , give online vote if you are not comfortable.")
#      else:
#         print("the person is able to vote")
            
# else :
#     print("the person is not able to vote")