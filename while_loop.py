
#----------------1st_problem-----------------------

# i=1
# while i<=100:
#     print(i)
#     i+=1

#-----------------2nd--------------------

# i=100
# while i>=1:
#     print(i)
#     i-=1

#---------3rd-------------------------------

# n=int(input(" Enter the number : "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

#------------------4th------------------

# num=[1,4,9,16,25,36,49,64,81,100]#list starts with index 0.
# #here index wise 0 to 9 but length wise 1 to 10 , so, index = (length - 1)
# idx=0
# while idx<=len(num)-1: # we also use idx < len(num) ;
#     print(num[idx])
#     idx+=1

#---------------------5th--------------------

num=(1,4,9,16,25,36,49,64,81,100)  #tuple starts with index 0.

#here index(idx) wise 0 to 9 but length wise 1 to 10 , so, index = (length - 1)

x=int (input("enter the number you want to search : "))

idx=0
while idx<len(num):
    if num[idx]==x: # also I can use x==num[idx]
        print("found , exist at index",idx)
    else:
        print("not found at idx",idx)
        
    idx+=1


    








