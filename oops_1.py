# class student:
#     name="arnab"
   
# s1=student()
# print(s1.name)


#--------------------------------------------------------------------------------------


# class student:
#     def __init__(self):
#         print(self)
#         print("Arnab is my name ......... ")
        
# acc1=student()



#------------------------------------------------------------------------------------

# class student:
#     @staticmethod       #STATIC_METHOD
#     def college():
#         print("future")
        
# acc1=student()
# acc1.college()


#--------------------------------------------------------------------------------------



# class student:
#     name_college="Future" #class attribute
#     def __init__(self,name):
#         self.nam=name     #object attribute
   
# s1=student("Arnab")
# print(s1.nam)


#-------------------------------------------------------------------------------------



# class student:
#     def __init__(self,name,marks):
#             self.name= name
#             self.marks=marks
            
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hii" ,self.name,"your avg score is - ",sum/3)
           
   
# s1=student("arnab",[88,98,90])
# print(s1.name)
# print(s1.marks)
# s1.get_avg()


#---------------------------------------------------------------------------------------------



class account:
    def __init__(self,bal,acc):#attribute
        self.balance=bal
        self.account_no=acc
    
    #debit method
    def debit(self,ammount):
      self.balance -= ammount
      print("Rs." , ammount," was debited" )
      print("total ballance = ",self.get_balance() )#acc1.balance
       
    #cradit method
    def cradit(self,ammount):
      self.balance += ammount
      print("Rs." , ammount," was cradited" )
      print("total ballance = ", acc1.balance)#self.get_balance()
       
       
     #printing method  
    def get_balance(self):
        return self.balance
       
        
acc1=account(10000,12345)
print("your account number is - ",acc1.account_no)
acc1.debit(100)  
acc1.cradit(101)
# print("your current balance is - ",acc1.balance)


#--------------------------------------------------------------------------------------





















