##-----------------------------------------HERE WE GENERATE RANDOM PASSWORDS WITH LENGTH OF 12------------------------------------------


# import random
# import string

# def password_generator():
    
#     ##-----LET CREAT A VARIABLE TO COLLECT ALL THE {UPPERCASE,LOWERCASE,DIGITS,SPECIAL_CHARACTERS} IN IT-------------------------------------

#     all_val = string.ascii_letters + string.digits + string.punctuation

#     pass_len = 12   #----------IT SETS THE PASSWORD LENGTH - 12 ----------------

#     password = " "      #---------AT THE STARTING PASSWORD IS BLANK------------

#     for i in range(pass_len):

#         ##print(random.choice(all_val))

#         password += random.choice(all_val) 

#     print(f"YOUR PASSWORD IS - {password} ")

#     ##print("YOUR PASSWORD IS - ",password)



# if __name__ == "__main__":
#     password_generator()



##-------------------IN ANOTHER PROCESS -- LIST COMPREHENSION------------------------------------



import random
import string

def password_generator():
    
    ##-----LET CREAT A VARIABLE TO COLLECT ALL THE {UPPERCASE,LOWERCASE,DIGITS,SPECIAL_CHARACTERS} IN IT-------------------------------------

    all_val = string.ascii_letters + string.digits + string.punctuation

    pass_len = 12   #----------IT SETS THE PASSWORD LENGTH - 12 ----------------

    ##------LIST COMPREHENTION [ function_name  for i in range (n)]--------------------------------


    FINAL_RESULT = [ random.choice(all_val) for i in range(pass_len) ]

    """ IF WE WANT ALL OF THE LIST VALUES JOIN TOGETHER , MEANS OUTPUT IS IN NORMAL FORM NOT IN A LIST FORM
     FOR THIS WE USE ( A EMPTY STRING WITH DOT JOIN METHOD ) ----------->  [ " ".join ] LIKE THIS """
    
    ##FINAL_RESULT =" ".join( [ random.choice(all_val) for i in range(pass_len) ])

    """ here we write anything inside the empty string and result is different for this because the empty space is now fill with (A) """

    ##FINAL_RESULT =" A ".join( [ random.choice(all_val) for i in range(pass_len) ])

    ##print("YOUR PASSWORD IS  : ",FINAL_RESULT)

    print(f"YOUR PASSWORD IS  : {FINAL_RESULT}")


if __name__ == "__main__":
    password_generator()



