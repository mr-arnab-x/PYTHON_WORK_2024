#--------------length of a list in function---------------------------

# def len_list(num=[12,13,14,5,78]):
#     print(len(num))   #--------type-----------> 1
     
# len_list()

# num=[12,13,14,5,78]
# def len_list(list):
#     print(len(list))   #------type----> 2
     
# len_list(num)


#--------print the list elemenents in a single line------------

# num=[12,13,14,5,78]
# def len_list(list):
#     print(list,end=" ")   #------type----> 1
     
# len_list(num)


# num=[12,13,14,5,78]
# def len_list(list):
#     for i in num:
#         print(i,end=" ")#------type----> 2
     
# len_list(num)

#---------------------------------factorial of n------------------------------


# def fact_n(n=int(input("enter the number : "))):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print ("the factorial value is:",fact)
        
# fact_n()


#---------------money converter (usd to inr )-----------------

# def conv_money(usd=int(input("enter the USD doller($): "))):
#     inr = usd*83.94
#     # print("INR ruppy is : ",inr)
#     return inr

# # conv_money()    
# inr_m = conv_money()
# print("INR ruppy is : ",inr_m)

#------------------------even - odd------------------------

def even_odd(n=int(input("enter the number : "))):
    if n%2==0:
        print("EVEN")
    else:
        print("ODD") #-type--> 1
        
    # return n
    
even_odd()


# def finder(n):
#     if(n%2==0):
#         print("even")       #-type--> 2
#     else:
#         print("odd")

# finder(int(input("enter the number : ")))



# n = int(input("enter your num:"))

# def odd_or_even(n):
#     if(n%2 == 0):
#         print("EVEN")      #-type--> 3
#     else:
#         print("ODD")
# odd_or_even(n)












