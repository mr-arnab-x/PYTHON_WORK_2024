#print all numbers excpt multiple of 3

# i=0
# while i<=100:
#     if i%3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1


for i in range (1,101):
    if i%3==0:
        continue
    print(i)