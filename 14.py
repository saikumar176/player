v=str(input())
a=v[::-1]
for i in a:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    continue
  else:
    print(i,end="")
