#------------SUM OF FIRST n NATURAL NUMBERS (USING WHILE-LOOP)-----------

# n=int(input("Enter the number: "))
# sum=0
# i=0
# while i<=n:
#     sum+=i
#     i+=1
# print("SUM OF FIRST",n," NATURAL NUMBERS : ",sum)    

#------------factorial of first n numbers (using for loop)-----------------

n=int(input("enter the number: "))

fact=1
for i in range(1,n+1,1):
    fact*=i
print ("the factorial value is:",fact)

    
    


