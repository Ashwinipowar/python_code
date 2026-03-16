# tup=(1)
# print(type(tup), tup) # now here it showing the this is integer but actul its tuple 
# so for only one element use the coma after that element


 
# tup=(1,)
# print(type(tup), tup) # now it showing this is a tuple



# error
# tup=(1,2,4,55,77,8)
# tup[0] = 40
# print(type(tup), tup) # throw an error bcz we cant change the tuple



# now we make it as list by the giving the bracket
# tup = [1,2,4,55,77,8]
# tup[0] = 40
# print(type(tup), tup)
# we use tuple where we wanna it for the important project and noone can change it by mistake for that we use tuple


# we can aad another data type also
tup = (1,2,4,55,77,8,"sitara","True")
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
#print(tup[5])
#print(tup[6])

if 77 in tup :
    print("yes we have this number")
tup2 = tup[1:4]   
print(tup2)