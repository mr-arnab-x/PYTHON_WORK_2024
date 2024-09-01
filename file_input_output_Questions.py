# with open("practice.txt","w") as f:
#     f.write("hii everyone\nWe are learning file i/o \n")
#     f.write("using java \nI like programing in python")


# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)


# new_data=data.replace("java","python")
# print(new_data)

# with open ("practice.txt","w") as f:
#     f.write(new_data)

# word="python"
# with open ("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")


# word = "python"  # Define the word to search for

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if word in data:
#         print("found")
#     else:
#         print("not found")

# def check_for_word():     #as a function represent.
#     word = input("enter the word you want to search : ")  # Define the word to search for
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if word in data:
#             print("found")
#         else:
#             print("not found")

# check_for_word()


# def check_for_line():     #as a function represent.
#     word = input("enter the word you want to search : ")  # Define the word to search for
#     line_no = 1
#     data=True
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1    

# print(check_for_line())



# def num_file():
#     with open("num.txt","r") as f:
#         data=f.read()
#         print(data)         # first type ---->

#         num_n=""
#         for i in range(len(data)):
#             if(data[i] == ","):
#                 print(int(num_n))
#                 num_n=""
#             else:
#                 num_n += data[i]

# num_file()


def num_file():
    count = 0
    with open("num.txt","r") as f:
        data=f.read()
        print(data)         # secoend type ---->

        num_n = data.split(",")
        print(num_n)

        for val in num_n:
            if int(val) % 2 == 0 :
                count += 1
    print(count)

num_file()
































