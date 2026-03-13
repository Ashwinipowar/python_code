m=5
for i in range(0,2*m-2):
  print("*" , end="")
print("\n")
for i in range(1, m-1):
  for j in range(0, m-i-1):
    print("*",end="")
  for k in range(1,2*m-1):
     print("0",end="")
      
  print("\n")