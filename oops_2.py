# class car:
#     @staticmethod
#     def start():
#         print("start the car")
        
#     @staticmethod
#     def stop():
#         print("stop the car")
        
# class toyota_car(car):
#     def __init__(self,name):
#         self.name=name
        
# car1=toyota_car("honda")
# print(car1.name)
# car1.start()



#---------------------SUPER()------------------------------------------------------------



# class car:
#     def __init__(self,type):
#         self.type=type
        
#     @staticmethod
#     def start():
#         print("start the car")
        
#     @staticmethod
#     def stop():
#         print("stop the car")
        
# class toyota_car(car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)  #----THE USEGES OF SUPER()-------
#         # self.type=type
        
# car1=toyota_car("honda","electric")
# print(car1.name)
# car1.start()
# print(car1.type)   #----THE USEGES OF SUPER()-------


#-------------------------class method------------------------------------------------------------


# ##------------ 2 process to change the class attribute without using class_method-----------------------
# class person:
    
#     name="pro"
    
#     def __init__(self,name):
#         self.name=name
    
#     def __init__(self,name):    #-------------1st-process---
#         person.name=name
        
#     def __init__(self,name):    #-------------2nd-process---
#         self.__class__.name=name  #(__class__ -----> class name(person) = same)
        
# print(person.name)       
# p1=person("neha")
# print(p1.name)
# print(person.name)
# print(person.name)


#------------------------@classmethod---------------------------------------------



# class person:
    
#     name="pro"
    
#     @classmethod
#     def changename(new,name):   #--here "new" ( also we use "cls" like the video is same work ) is define the class -----> person
#         new.name=name
        
# p1=person()
# print(person.name)
# p1.changename("neha")
# print(person.name)
# print(p1.name)


#------------------------PROPERTY (@PROPERTY) DECORETOR----------------------------------------


#--------------------@property before use example--------------------------------------------

# class student:
#     def __init__(self,phy,chems,math):
#         self.phy=phy
#         self.chems=chems
#         self.math=math
#         self.persentage=str((self.phy+self.chems+self.math)/3) + "%"
        
#     def calculate_per(self):
#         self.persentage=str((self.phy+self.chems+self.math)/3) + "%"
        
# s1=student(98,99,97)
# print(s1.persentage)


# s1.phy=89
# print(s1.phy)
# s1.calculate_per()
# print(s1.persentage)


#-------------------------------------@PROPERTY----------------------------------------


# class student:
#     def __init__(self,phy,chems,math):
#         self.phy=phy
#         self.chems=chems
#         self.math=math
#         # self.persentage=str((self.phy+self.chems+self.math)/3) + "%"
        
#     # def calculate_per(self):
#     #     self.persentage=str((self.phy+self.chems+self.math)/3) + "%"
    
#     @property       # by using this we use this function as attribute
#     def persentage(self): 
#         return  str((self.phy+self.chems+self.math)/3) + "%"
        
# s1=student(98,99,97)
# print(s1.persentage)


# s1.phy=89
# # print(s1.phy)
# # s1.calculate_per()
# print(s1.persentage)



#---------------------polimorphism-------------------------------------------------------


## operator ( + ) work different according to the work(sitution)
## basic exampale of polimorphism

# print(1 + 2)
# print("Arnab" + " " + "Neha") #concatenate
# print([1,2,3] + [4,5,6]) #merge

## this is the basic example of polimorphysm


##----------------complex number with out using polymorphysm-------------------------

## add 2 complex numbers with out using polymorphysm


# class complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
        
#     def shownumber(self):
#         print(self.real,"i +",self.imag,"j")
        
#     def add(self,num2):
#         newreal = self.real + num2.real
#         newimag = self.imag + num2.imag
#         return complex(newreal,newimag)
        
        
# num1=complex(1,5)
# num1.shownumber()

# num2=complex(3,4)
# num2.shownumber()

# num3 = num1.add(num2)
# num3.shownumber()


##--------------------now we use dunder function of polymorohysm for this complex numbers------------------------------------



# class complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
        
#     def shownumber(self):
#         print(self.real,"i +",self.imag,"j")
        
#     def __add__(self,num2):     #here we use dunder function as addition
#         newreal = self.real + num2.real
#         newimag = self.imag + num2.imag
#         return complex(newreal,newimag)
        
#     def __sub__(self,num2):     #here we use dunder function as substraction
#         newreal = self.real - num2.real
#         newimag = self.imag - num2.imag
#         return complex(newreal,newimag)
    
#     ##---------divition , multiplaction ... etc. we have done anything using dunder function in polymorphysm   
        
# num1=complex(1,5)
# num1.shownumber()

# num2=complex(3,4)
# num2.shownumber()

# # num3 = num1.add(num2)
# # num3.shownumber()

# num3 = num1 + num2
# num3.shownumber()

# num3 = num1 - num2
# num3.shownumber()




##-------------------------practice questions-----------------------------------------------------


##------------------1st__Question-----------------------------------------------------------



# class circle:
#     def __init__(self,radious):
#         self.radious=radious
        
#     def area(self):
#         print ( "the area of the circle is is - ", (22/7)*self.radious**2)
        
#     def peremeter(self):
#         print ( "the peremeter of the circle is - ", 2*(22/7)*self.radious)
        
# c1=circle(21)
# print(c1.radious)
# c1.area()
# c1.peremeter()


##------------------2nd__Question-----------------------------------------------------------

# class employee:
    
#     def __init__(self,dept,salary):
#         self.dept=dept
#         self.salary=salary
        
#     def show_ditels(self):
#         print(f"Depertment of the employee is - ",self.dept)
#         print("Salary of the employee is - ",self.salary)
        
# class engineer(employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Editor",20000)
    
    
    
# # e1=employee("Design",15000)
# e1=engineer("Arnab",22)
# print(e1.name)
# print(e1.age)
# # print(e1.dept)
# # print(e1.salary)
# e1.show_ditels()


##------------------3rd__Question-----------------------------------------------------------


class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    # def show_final(self):
    #     print(f"your item is {self.item} and your total item price is {self.price}. Thankyou")
        
    # def __gt__(self,ord2):
    #     if ord1.price>ord2.price:
    #         return ord1.order
    #     else:
    #         return ord2.order
    
    def __gt__(self,ord2):
        return self.price > ord2.price
        
        
ord1=order("chicken",150)
ord2=order("bread",50)

print(ord1 > ord2) # True------> Yes ,,,, False--------> No









































































































