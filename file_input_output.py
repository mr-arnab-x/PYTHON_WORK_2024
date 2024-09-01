
#---------------------for read only---------------

# file=open("demo.txt","r") #for 'file' you can use anything like ---> f, new , ect. anything.

# data=file.read()
# data=file.read(5)

# line1=file.readline()
# print(line1)

# line2=file.readline()
# print(line2)

# print(data)
# print(type(data))
# file.close()


#-------------------write------------------------------------
#--------w=overwrite------a=add at the end(append)-------------

#     #rule---> 1

# f=open("demo.txt","w")

# f.write("hiiii .I am Arnab")
# f.write("hiiii \n.I am Arnab") # /n ---> used for next line
# f.close()

#    #rule---> 2

# f=open("demo.txt","a")

# f.write("\nhiiii .I am Arnab")
# f.close()


#---------------------------------with syntax---------------------------------------------


# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)


#------------------------------------------------------------------------------------------

# with open("demo.txt","w") as f:
#     f.write("I am learning python from Apna college")
    


#----------------------------------deleting a file----------------------------------------------------------

# import os

# os.remove("sample.txt") #for delete "sample.txt" file.

#-------------------------------------------------------------------------------------------------





