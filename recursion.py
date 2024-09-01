# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
    
# show(int(input("enter the number : ")))

#--------------------------fact of n--------------------------------------

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1)*n
    
# # fact(int(input("enter the number : ")))
# print(fact(int(input("enter the number : "))))

#-----------------sum of first n natural numbers---------------------

# def calc_sum(n):
#     if(n==0):
#         return 0
#     else:
#         return n+calc_sum(n-1)
   
# print(calc_sum(5))

#------------------print all elements in a list----------------------

name=["arnab","neha","sayan","anirban","surajit"]
def li_st(list,idx=0):
    if idx==len(list):
        return 
    print(list[idx])
    li_st(list,idx+1)
li_st(name)